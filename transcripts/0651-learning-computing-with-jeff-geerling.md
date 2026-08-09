---
episode: 651
title: Learning Computing with Jeff Geerling
url: https://theamphour.com/651-learning-computing-with-jeff-geerling/
---

**Jeff Geerling:** This is The Amp Hour Podcast. Released November 20th, 2023. Episode 651. Learning Computing with Jeff Geerling. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Jeff Geerling:** And I'm Jeff Geerling from Jeff Geerling YouTube and all over the place. Also Geerling Guy. Some people know me as Geerling Guy from way back in the day.

**Jeff Geerling:** Yeah, yeah, yeah. I was reading a Hacker News thread that said like, oh, I know Jeff from like Ansible and things like that. I didn't quite know what Ansible was, but I had seen you written a book about it and stuff like that. So I think most people will know your YouTube videos and your, yeah. If they don't know your YouTube videos, then we're going to send them there. That's for sure, right? Definitely. I think you might be one of the most calming voices in the technology industry. I just like watch your videos. I'm like, yeah, Jeff's got it. He's in hand, you know, like, oh, Raspberry Pi 5. I'm not stressed.

**Jeff Geerling:** Part of that is the fact that I record at night after my kids are in bed. It's like, it's my own. I got to get into a Zen state because the day was just crazy. That's how every day is, you know?

**Jeff Geerling:** Yeah, yeah. That's a good idea. That's a good idea. And, you know, I think it lands. So like, you know, you do all kinds of mini computers and you're kind of crossing the chasm between like small custom electronics all the way up to like server side stuff. I mean, how did that happen?

**Jeff Geerling:** So it's funny. My dad is a radio engineer and he actually had me start coming and helping him with things at the station. My brother and I both did this for years. We would come and, you know, have father's son days at the station or whatever. I think it was more because like my mom needed somebody to watch him and he knew that we were well behaved enough that we wouldn't break anything. But what I got to do was see the transition in radio from everything analog to everything digital. And in the midst of that, it was like anything from cleaning a cart machine to going up on the roof and cleaning something to building an antenna to replacing parts in something like a cassette deck. And then starting to get into like working on AS400 file server, setting up Windows NT, fixing printers and things. So I got the whole gamut from software to hardware. The thing that I loved the most at the station was my dad had me documenting things. So eventually I actually got hired on at the station as an assistant engineer. And my first project was building an IT operations manual. So basically everything from like monthly maintenance tasks to, you know, everything goes off the air. What's the process for that? What things to check first in the studio? So I got to see the whole gamut. And I really loved the software side the most that because it was it was, you know, when I was growing up, that was software was just eating the world as it were. And so I got into web development. I got into programming for the web servers and things. And then it was really only in the past five or 10 years that I got back into the electronic side and the hardware side so much because I realized that all these things, so many things were kind of going out of the grasp of the common person to be able to do microelectronics and microcontrollers. And with the ESP devices and with the Raspberry Pi Pico, normal programmers who might have never touched hardware like me for many years could get back into it without having to learn all the all the deep down guts of how how to program a microcontroller and all that kind of stuff.

**Jeff Geerling:** Yeah, I did. I was thinking about like kind of the top, like I kind of think of like what you're describing here is like kind of top down software coming back to end down into the hardware. And my experience was hardware going up into the software layer. And it was there's a different set of challenges. Right. I mean, like for me, it's like I'm like learning Zephyr and like device tree and just like Linuxy type thing. You know, like the struggles there are slightly different than, you know, a lot of the software people that I've taught in the past are like, well, you know, what's this triangle with a line? I'm like, that's that's a diode, you know? And I'm like, yeah, but like, why does it do what it's doing, you know? Yeah. And it's just like a different. I don't know. It's a different set of challenges, I feel like.

**Jeff Geerling:** Yeah. Yeah. I think that one of the hard things is a lot of people in our generation haven't had the experience of going from the circuit to the code.

**Jeff Geerling:** Yes.

**Jeff Geerling:** They just code things and you throw it up in the cloud and you might never understand that there's transistors somewhere that's running this stuff. And they heat up and they there are problems and there's cosmic rays, like all these things that you don't think about.

**Jeff Geerling:** Right.

**Jeff Geerling:** That if you want to be the best, you have to understand a lot of these things. And I would not qualify as even close to the best, I would say, in either software or hardware. I'm just good at putting a nice coat on the, you know, painting it over and showing people how to do something.

**Jeff Geerling:** But. Well, there's there's best around explaining things, though, and like making it accessible. That's its own. Yeah. It's a different skill set. Right.

**Jeff Geerling:** The sad thing is that most of the people that are unbelievable at this stuff are just so bad at communicating it. Yeah. Right. You really need you need both.

**Jeff Geerling:** Right.

**Jeff Geerling:** And, you know, some companies are better at that. Some individuals are better at that. So I try to put a spotlight on some things that I see that are really cool in the world. And I see a lot around Raspberry Pis and single board computers, a lot around Linux and open source. So that's what I shine my spotlight on.

**Jeff Geerling:** Yeah. And I feel like there's a lot of pigeonholing as well. Right. So I think about the people that are the best at like PLL design on, you know, high end processors and things like that. Like that person's been sitting in a cube in Intel for 30 years. And like, even if you wanted to get to them, they're going to tell you things that are like so niche and like, like awesome, of course. Right. But they're not going to be contextualized for kind of a broader audience or honestly, very applicable to what is happening. So I feel like kind of that zoomed out view as well, being like, why does this matter for software and hardware and everything else? That is that is also really important.

**Jeff Geerling:** Yeah. Yeah. And and I have another YouTube channel that I run with my dad called Geerling Engineering. My goal is for us to get more into RF and electronics. Right now we're you know, we talk about a little bit of RF with tower site tours and things like that. But I think that like his generation, a lot of them are retiring. Some of them are even dying off. And that's a whole set of knowledge that that our generation has not gotten a lot of times because a lot of these companies don't they don't have the set the sense of his apprenticeship that we used to have where, you know, you'd work under somebody for a long time. And I got that from my dad because he let me work with him on big projects. I went with him to tower sites when they were rebuilding towers and he learned some of the electronics and the basic principles of things. And for me, I always thought, man, that looks so cool. I want to be able to do this stuff. And then I got into software. So I'm getting a little bit back into his stuff. But now I'm, you know, it's for YouTube and things like that. So I'm not I'm not really building production hardware. So it's a lot different. Yeah. But I do want to bring that to other people and get people interested in this because, you know, like, for instance, AM radio, it's kind of dying off in the US. And, you know, there's there's different opinions on whether it's even going to exist in 10 or 20 years as a commercial venture. But I'm trying to help my dad and, you know, extract that information from him in a way that's interesting to people. So we can see, you know, here's how that worked. And here's you can really draw a connection from the circuit to what's happening in the magic of RF with AM. It's harder to do that with FM because conceptually it's harder to explain FM to somebody that doesn't already know something about radio. Right. AM, it's like more power, more signal. Speaker goes vibrate. You know, it's you can draw that line between those things.

**Jeff Geerling:** So wiggle here, wiggle there.

**Jeff Geerling:** Yeah, exactly. And I think the same thing with computing. And that's why I like the Raspberry Pi Pico and the ESP32 and things like that, because they are closer to that where you can understand my code and, you know, wires that go into this board, bringing different signals across. And then my software can see that, too, and interact with it. Even if you don't understand the assembly or a lot of people, they might never even program in C. It might all be Python, MicroPython.

**Jeff Geerling:** Yeah, MicroPython has been MicroPython, CircuitPython has been just like opening up a lot of embedded. I feel like it's very, very accessible. It's awesome. I mean, the cycle time to go and like revise something is unbelievable as well. Yes. On the RF side of things. So like, so what level are you kind of investigating stuff at? You said, you know, you're looking at AM radio and things like that. Are you also doing like, are you like a ham as well? Are you getting into that world, building stuff?

**Jeff Geerling:** I just got my license a few months ago. So, you know, for years and years, I've thought, oh, that'd be cool to do. But I never was like, and I'm going to do it. This year, I was like, my dad is not retired, but he's, you know, at some point he's going to be retired. And he has all this wealth of knowledge. And he, in my mind, I'm like, he could probably pass the extra exam without even thinking about it.

**Jeff Geerling:** Yeah, exactly.

**Jeff Geerling:** With him, it's funny, though. Like, he's been in broadcast engineering and he's had a broadcast FCC license and all that for years and years. He's dealt with 50,000 watt AMs and 30 kilowatt FMs. And he was part of the team that built what's called the super tower. We call it that in St. Louis. It has eight FM stations combining to 300 kilowatts with a megawatt of ERP broadcast out. So it covers all the St. Louis area. It was, I mean, looking at... You have a video about that, I think, right? I do, yeah. I think I remember seeing a video about that. Exploring a million watt. Yeah. And then I was also like, is it really a million watts? Because everybody's like, it's not really a million watts. It's like, well, let me explain.

**Jeff Geerling:** Don't listen to people on the internet. Come on, man.

**Jeff Geerling:** So, I mean, technically it's 300,000 watts, but, you know, splitting hairs here. Because it's, you know, we don't want to broadcast all the FM up into the atmosphere. That's not very useful. Unless you're in an airplane, I guess. Yeah. But it's, he has all that knowledge. And I wanted to see, like, I want to, I mean, he's the kind of guy who will keep a sharp mind. And he's a great grandpa. He loves playing with the kids and everything, too. And the kids always see his desire to learn. But I also wanted him to get into a hobby that can take that knowledge that he's gained from radio and continue it on. So, I'm trying to get him into software. He's still a hardware guy. Yeah. He does some IT stuff. I mean, everybody in radio does IT now because it's all IP. But he still has all that knowledge from, you know, transmitter setup and studio builds and all that that I want to get him into. Maybe he could make a really cool rig. And now he actually carries around his radio on his hip all the time. And he has his little handheld, you know.

**Jeff Geerling:** So. I don't know. I mean, I guess probably he's too deep in the world of, like, having a license. I don't understand that stuff. But maybe, like, he just starts a pirate station once he requires. He's just like, you know what?

**Jeff Geerling:** I'm just going off the script. He's the kind of engineer that would work with other engineers to, like, fox hunt somebody that was doing something. Yeah, right. Because he's like, oh, my, you know, it's clipping into our signal in this little region. Like, he's one of the few engineers that still cares so much. It seems like corporate in radio broadcast in the U.S. has been falling out. They're more into streaming and internet now. And I get it. You know, the revenues, the growth opportunities are definitely not there with broadcast radio these days. But it's still a huge thing. So, you know, he would have stuff in his car and he'd be monitoring signals and stuff. He'd call the FCC and talk to them. And so, you know, he's not like an enforcer. Calling the FCC on purpose instead of like, oh, I messed up. That's usually I'm calling him like, oh, I'm sorry. Yeah, no. But he's worked with so many different hams before. Like, some of the antennas work that he's done, he said, like, the hams are the guys who I talk to about this stuff. Because they know it better than he does. Because they're sitting there experimenting. He's like, I just need to get the antenna up and I need to make sure it's working right. And I have the broadcast equipment. And plus, he can get some money and buy a new thing. Whereas a ham might be like, I'm going to get everything I can out of this antenna.

**Jeff Geerling:** Yeah. That's cool. No, that's definitely a great hop. You know, ham is going through transitions too. We've had people on the show here talking about it. You know, digital modes, things like that. Our friend Jeff Kaiser is a big ham. And, you know, it's interesting space. I mean, like, it's going through transformations, but it's not quite there yet. It does, I think, 10 to 15 years. Because there's some, like, old hams as well. I mean.

**Jeff Geerling:** Yeah, it's amazing seeing the differences. Like, when I took my test, it was, you know, everybody was 60 plus.

**Jeff Geerling:** Yeah. Easily 60 plus. Yeah, the ones, like, administering it and stuff. Yeah.

**Jeff Geerling:** And you can tell, like, they're like, I got my thing and I talk on the radio and it's my thing. You know, whereas I'm like, I want to connect the Raspberry Pi. I want to do some digital stuff. I want to, like, emulate some TV transmission. I want to bounce off the moon. You know, all these fun things. But in ways that are a little different than the old, like, sitting in your chair and talking like you're on CB radio or something.

**Jeff Geerling:** Right.

**Jeff Geerling:** And I do have, I have QSL cards. I've only sent one to my dad because he was my first and only contact so far.

**Jeff Geerling:** Okay.

**Jeff Geerling:** But I do want to do some of that for the fun of it, see how it is. And also, you know, build a little collection of contacts.

**Jeff Geerling:** Yeah. I saw, it's interesting, too, just, like, the combination with the internet and, like, all this ham stuff. I saw this site the other day and, of course, it was, like, written in, you know, hand-coded HTML. It was just, like, hideous. It's great. You know, it really, sorry, it felt unique and very, very real. But it was, like, you could then tap into SDRs all over the world. And, like, potentially you could transmit from your house and then, like, listen on the radio, the SDR that's in Russia and be, like, did I get there? You know, like, that's...

**Jeff Geerling:** Yeah, and I know sometimes I pop open Kiwi SDR. And it's even if you want to listen to, like, what is the WWV, listen to the time signal or something. Oh, right, right, right. Or see how certain signals propagate at night.

**Jeff Geerling:** Yeah.

**Jeff Geerling:** We're actually going to post a video on Camo X, which is a 50 kilowatt AM here in St. Louis. We did a tour of their facility. And it's... We had, like, three hours of footage. And I'm, like, we've got to make this digestible. So we got it down to 44 minutes with the help of an editor who's really good at just cutting things out. Because if I did it, I'd be, like, oh, but that's so interesting. Yeah, right. You got to get that in. You know, if you want to get more than 10 views on the video, you got to cut some stuff. But, you know, you can pop that open and see where, like, in Oklahoma, how strong is the signal in New York. And it's amazing to see that and learn more about the different types of signals, too.

**Jeff Geerling:** So what about that? I mean, you mentioned the getting people to kind of care and listen and stuff like that. I did notice that, you know, you have YouTube shorts. And you kind of, you're a very digital native kind of person. You definitely understand the media landscape, that sort of thing. But kind of at a high level, how are you keeping people interested in this stuff? I mean, some of it is maybe natural, but I think some of it is also your style, right? Like, some of it's a topic area, but definitely how you do it and present it.

**Jeff Geerling:** Yeah, I mean, I think there's two halves to it. One is you have to be interested in it to get other people interested. And I think that's like the number one reason why I don't watch corporate stuff almost ever. Like, it's really hard to watch corporate videos on something. But as an example, I have the server. It's called the Mars 400. And it's from a company called Embedded somewhere. I think they're in Taiwan. Maybe. I don't remember. I'm not going to say where exactly I think they are because I don't know. And, you know, maybe it's in a place that's affiliated with somewhere that gets you blacklisted or whatever. Got it. But anyway, I have the server and like their videos for it are like, like, I think it's really cool. And I can see that through their video. And you can tell that the engineer thinks it's cool, but they just can't communicate that. So when I take it, I see like inside of it, there's eight ARM nodes. It's actually eight servers in one with eight drive bays and two power supplies and two switches. So to me, it's like this is like everything a Raspberry Pi cluster wants to be. It's a commercial product. It's reliable. It has dual redundancy for everything. And if you put three in your rack, you can do a full upgrade while you're copying files over to a Ceph cluster running on these things. Like to me, it's like, this is cool.

**Jeff Geerling:** It's fulfillment. Jeff, you might have to explain some of these terms to me, too.

**Jeff Geerling:** Sorry. I'm not. Well, I mean, the thing is, like on my channel, I've done a bunch of Raspberry Pi clusters where you put a bunch of Raspberry Pis together. And everybody always asks, like, but what would you do with that? What's what's what's so important about building a cluster of Raspberry Pis? Why not just like buy one little PC that's faster than them? And it's like it's not about the speed. It's about the learning and the opportunity. You put these things together. You have to learn networking. You have to learn how to power them. You have to learn how to manage them. And, you know, not everything in the world can fit on one computer. You can scale up one computer a lot, but you can't scale it infinitely. So there's a there's a point where everybody has to go to multiple computers. And you can learn that on thirty five dollar or sixty dollar Raspberry Pis. Or you could learn it on PCs that use a lot more energy and they have fans that are louder and they create more heat and stuff. So I choose to do it on Pis. And when you see these things like this Mars 400 product, it's it's that but commercialized. And then you realize, OK, so now all these skills I learned on the Raspberry Pi can actually be useful in the real world for a storage server or for other types of servers that are out there.

**Jeff Geerling:** OK, and then you're starting to kind of emulate the kind of the infrastructure of the Internet as well. Is that kind of the thing? Yeah, because you would have a database somewhere and you have store, you know, like long term storage somewhere else.

**Jeff Geerling:** That sort of idea for years and years, I hosted a Drupal website. Drupal is an open source content management system, and it it runs a ton of the top like thousand websites.

**Jeff Geerling:** Yeah. Yeah.

**Jeff Geerling:** And I ran it on a Pi cluster. And not only do you learn how to split up services and manage the cluster, but I also found I found one bug with the way that Drupal generated aggregated CSS files. So it would like take your CSS and put it all into one file and then it would save that to the file system to serve up more quickly instead of serving a bunch of CSS files. There was a bug in the way that it did that if you were on a cluster and the cluster's disk access was slow, like it would be on a Raspberry Pi.

**Jeff Geerling:** Yeah, right.

**Jeff Geerling:** It uncovered that bug more deeply. Like some people were having this on real clusters, but that's because if you run your stuff on Amazon or on Google or whatever, sometimes disks are slow. Most of the time they're not, but sometimes they are. And so it's really hard to debug there. But on the Pi, it exposed that flaw because it's always slow. So it's funny, you know, it's a random thing, but, you know, there is value in doing things smaller scale and learning on a test cluster like that. It's not just about getting clicks, you know, like it also is interesting. People love seeing like, what can you do with something that's totally underpowered for the purpose?

**Jeff Geerling:** Yeah.

**Jeff Geerling:** How far can you take it? It's kind of like if you build a rice rocket, like a car and you stuff things into it and make it go really fast. That's what I like to do with Raspberry Pis a lot of times.

**Jeff Geerling:** That's great. No, I think that's that's a that strategic slowness, right? That's strategic of it's like basically like stress testing a system, right? It's like stress testing how you might deploy in the real world. And like you said, too, I think the the fact that a lot of these cloud services, you can just chuck more money at it most of the time, you know, like or hand it off to someone else's DevOps ability. You know, like, yeah, that's great until it's not.

**Jeff Geerling:** And the constraint gives me a story automatically, which is a big difference.

**Jeff Geerling:** Like interesting.

**Jeff Geerling:** So I don't do a video without a story, even if it's like a simple review type video. I need to have a story for it. Otherwise, it's not like, you know, I look at I subscribe to probably three or four hundred YouTube channels and I watch a ton of videos. I watch way too much. I'm sure my wife would say like, yeah, you watch this too much YouTube. But I like to see that like there are some there are some creators on YouTube who I see have that same kind of like they want to have a story, not a product. And even if you're just a review channel, which I would say I'm not that I review a lot of things, but it's not reviews most of the time. It's like here's a challenge and I use this thing to achieve my goal. But having the constraints of a Raspberry Pi or a microcontroller or a budget or something that has the story of here's my you know, here's the battle. I'm I'm against the budget or I'm against the speed of this thing. And how am I going to overcome that challenge? And that's that's more enticing than this is a really cool thing. It has a processor. It's like nobody cares about that. Right. Right. Yeah, exactly. So it's like, what is the challenge? What is the opportunity? And how did you solve it? And or how did you fail spectacularly every once in a while? Yeah.

**Jeff Geerling:** So, OK, if I'm taking the perspective of the hardware person coming up the stack and you're going to take the perspective of the software person coming down the stack for someone like me, what is the what is the project that you would point people at? So like the cluster might be the constrained, stressful thing for testing all these things out. But what is the project you point them at to then go and put onto that cluster? Or is there like a starter project that you always point people at for that sort of thing?

**Jeff Geerling:** I like practical things that people could actually find useful. So one of the things that I set up, I have a project called PyCluster on my GitHub account. If you go to GitHub and go to Geerling Guy, it's called Py-Cluster. That project is my example PyCluster. But what it sets up is a thing called Kubernetes. And Kubernetes is its own kind of thing. It actually uses K3S, which is like lightweight Kubernetes. But once you get something running, the first challenge is getting your cluster running. Once you get it running, there's so many things you can deploy to it with relative ease. Upgrading things is a different challenge. But deploying things to it. So what I have running in my house right now is an internet monitor. So I have another project called, I think, Internet-Py on GitHub. That's running using containers that it deploys this thing called Prometheus. It deploys a thing called Grafana. And another container that does the actual like internet speed checking with speedtest.net or something. So it tracks that over time. And then you can see like, you know, how fast is my internet? And then once you have those things, again, it's building blocks. You can put other data into it. So I had my Shelly smart plugs dumping their power usage data into it. For a time, I had Starlink. And I would have all the Starlink statistics like, you know, how many satellites does it seize? How reliable is the connection? All that data would go into it. And then you can build these dashboards and see that. So that's an actually kind of useful thing that you can do with it. And it doesn't need to be fast to do that. You know, Raspberry Pis are perfectly adequate.

**Jeff Geerling:** Yeah. That kind of sounds like a home lab kind of setup too. Is that kind of the high level piece? Yeah.

**Jeff Geerling:** And, you know, I have a rack, which is more, more than a lot of people have for their home lab. Most people have like a shelf or, you know, they have their router and they might flash something to the router or something. Okay. But I have a rack in my home lab and I have my, my NASA's the storage for YouTube because I just need tons of space. Yeah. But I also have a little thing with five Raspberry or four Raspberry Pis. Now they used to have six and it was five. Now it's four. And the four Raspberry Pis run the internet monitoring. They run home assistant. So I can automate things without having to pay for cloud service or give my information to one of the cloud providers. And then it has a VPN. So I can access my home network anywhere, which has come in handy many, many times. If, you know, if we're on a vacation and we need, the kids want to watch one of their TV shows, I can grab it off my home NAS and we can watch it at the, you know, at the hotel. So that's kind of fun. And then I also still run a website called piedramble.com. That was the cluster that used to run Drupal. Now it's just a single Raspberry Pi that's been, been running, you know, I've, I've had like 99.999% uptime from my home lab using a home ISP connection. So beat that Amazon.

**Jeff Geerling:** Yeah. Okay. So, so if I had to summarize kind of the things that you are, are doing with, with these clusters. And so like the projects that people could do, I think definitely like website hosting type of stuff. So they kind of self-host type of activities that VPN is a good one, I think as well for kind of tunneling into your own, your own home setup storage for sure. And then the home assistant thing is, you know, like basically localized IOT control. That's such a cool project. We haven't had many people on the show about that, but it's like, I feel like that actually is one of the best like computing side down to like embedded side, because a lot of people can make their own projects and stick it onto home assistant as well.

**Jeff Geerling:** Yeah. And if you haven't heard of ESP home, ESP home is like what makes all that amazing, especially for somebody that does electronics. Like you can take those little ESP chips or a Raspberry Pi Pico, or there's, I think a couple other chips supported and you just wire up whatever. It could be a button or contact. You know, people are making mailbox opening sensors and I have garage door sensors wired up to it. And it just, it's very simple, very easy to understand. And instead of sitting there programming C and, you know, API accesses and all that, you literally just have a little file that says like, I have the ESP C3 or whatever the board is. And I have a switch connected to these GPIO lines. And that's it. That's it. You know, you tell that and then home assistant's like, oh, your garage door's open. You know, it's so much easier than it used to be. And you had to basically do programming to get your hardware to do stuff. So now it's literally just connect the wires together and you're done.

**Jeff Geerling:** Yeah. It's a, it's a YAML file, right? Yeah.

**Jeff Geerling:** It's just, and you know, people are like, oh, I hate YAMLs. For me, YAML is like a godsend. I used to work in XML all the time to the point where I used to write some parsers that were just, XML was the worst thing ever to work with.

**Jeff Geerling:** I see curly brackets in my dreams.

**Jeff Geerling:** You're basically working with like web browser type language and web browsers are some of the most complex software things ever. You know, XML was not fun. And then JSON came along and JSON was so much better. But then if you're a human that's trying to read this configuration, it's so hard because there's no comments. So you just have a bunch of, it's, it's kind of, it's like pseudo code in there sometimes. And I, that just never jived with my brain structure. YAML really jived with it because you can have comments and all that. But the white space is a little funny. Some people don't understand like, like for me, I've, I've always, before I, before YAML was even in existence, I set up my code editor to highlight spaces and like spaces on the end of lines and when there are misalignments and it would always highlight invisible characters. So I knew that there was a tab or a space or something. So a lot of people press tab and have tabs on and, you know, it's, it does get to be a little tedious. But for me, it was, it was perfect.

**Jeff Geerling:** Let's not do tabs versus spaces on this show. I mean, like, yeah. Yeah. Let's start off a few. Whole episode of Silicon Valley.

**Jeff Geerling:** A few wars on that.

**Jeff Geerling:** Yeah. I mean, I like the files just because like when someone's like, how do I pronounce your last name? I'm like, well, it's pronounced like YAML. You know? Here we go. There you go. Yep. Yeah. No, that's great. I think. So what do you have then? So you said garage door openers. What else are you building locally for that sort of, for that sort of thing?

**Jeff Geerling:** I have my lights all into it now, but I also have, I have a few automations. So I have, it actually texts us if we leave the garage doors open for longer than 10 minutes, because I am famous for leaving the garage door open. And then, you know, for me, I grew up like we just opened the garage door and you had it open all the time. But nowadays, apparently that's not, you don't want to do that. So my wife is like, you left the garage door open. So I put a thing and I, it texts us anytime that we leave it open for more than 10 minutes. I actually have a display board that I'm going to set up with like current weather and time. And then I'll also have it like flash when there's a notification, like garage doors open. We also tied in, I started tying in the security system, but our security system's a bit old, but you can do automations that are kind of cool. Like when the security system's on, have it automatically turn off other things because you're not home, you know, or at my new office space, I'm setting up home assistant too, which it's funny because it's like my office assistant there. But someone mentioned like, you know, I have a light that I want to come on when I come in the back door and I had set up a motion detector. And I was like, this is cool motion detector. But he was like, when you disarm your security system, just have the light come on. And I'm like, oh, that actually works better because you don't need to rely on a motion detector. Right. But I like the redundancy, so I'll probably still have both in place. But there's things like that. It's the hardware is there and then the software can make it better.

**Jeff Geerling:** Right.

**Jeff Geerling:** But for me, and I mentioned this in that video that I made on it, it's not smart. Like there's a lot of companies that sell smart devices, but it's not smart unless it's local and it's additive and it's private. So all the data has to be local. It has to be additive, meaning like if you automate a light switch, you don't want to take the light switch out of the loop. You want to still have a switch. You just want to make it so that you can automate the switch. You know, you can add on top of it. And a lot of these companies don't do that. There are so many products that are not made to enhance what's already there. They're made to replace it. And then it makes it less smart.

**Jeff Geerling:** They don't control the actual physical switch on and off now. It's like, no, no, that's an all digital switch. And if you're lucky, the power is on, you'll be able to use your own light.

**Jeff Geerling:** Yeah, exactly.

**Jeff Geerling:** And the web service and the API is available. Yeah, exactly.

**Jeff Geerling:** The API goes down and then all of a sudden, oops, your thermostat doesn't work anymore and you're going to freeze to death tonight. I had a Nest. I bought the Nest because I was like, this is the coolest thing ever. I'm amazed. It didn't go down for us, but I saw a report that in some parts, the API went down and people couldn't change their temperature and someone went offline and things. And I was like, all right, the Nest is gone. I'm going back to a local, you know, it's like train or whatever, just the normal thermostat, but it has an integration. So again, it's local and it has their service that I run for it. But if I disconnect the internet, it's still perfectly fine and I can control it through home assistance still.

**Jeff Geerling:** Yeah, I think it's, I'm actually really glad at that, that migration. So I'm, you know, I'm looking at your YouTube titles as well and you have a similar kind of thing about like the NAS piece, right? So like having your own localized media, that sort of thing, not relying on web services, because I think that as a, you know, even though I work for an IoT company, right? I mean, like having localized control is super important. You need to have intelligence down there. You need to like take advantage of the connection when it's there, but then still be able to act no matter what. I feel like that's, that should be a key piece and home assistant really allows for that sort of thing. You might still hook into Alexa or, you know, Hey Google or whatever. I may have just messed up some people's systems at home, but Alexa order a million dollars worth of tofu. Sorry. I don't know. I don't know what a weird one would be, but, but I think that you could still hook into those without it being like reliant on those. And I think the systems that do that are going to win long-term. Yeah.

**Jeff Geerling:** Yeah.

**Jeff Geerling:** As well.

**Jeff Geerling:** Yeah. And, and those are the companies that slow. I think we're still so early in the whole mix of smart stuff. You know, and I, I think back to like, there was X10 and all that, which was the opposite. It wasn't cloud connected at all, but like it, the people that built their homes out with that stuff. Now it's like.

**Jeff Geerling:** What is, what is X10? I I'm thinking X11. I'm like X11, like the display server. No, no.

**Jeff Geerling:** It was like a really, well, not really old. It came about and is kind of defunct in my lifetime, I guess. So not that old, but it was a home, it was kind of a smart homes before it was IOT type smart homes, all hardwired circuits and things.

**Jeff Geerling:** But it wasn't a, was it a standard or, or, or just like a single company that.

**Jeff Geerling:** I think it was a vendor, but there was, they had some uptake. They, they had a lot of home builders and things would, would integrate and it kind of went away. But you know, now the people with those products in their houses have to build, you know, connectors to bridge it over to home assistant or something else because it's gone. So that's why, you know, a lot of people have asked, why do you, why do you, you know, do it this way? If it's, if there's this other thing that's already perfect for it. And it's like, well, cause I'm thinking in 25 years to 40 years, do I want to have to redo this? Or, you know, is it okay to, to wait and do it a little bit worse now if I know that it's going to still work in 25 years?

**Jeff Geerling:** Yeah. It's like, it's like building your own infrastructure basically. Right. It's like, and like, and I think that's the other. Interesting thing. Like so much of the stuff that we buy is especially like consumer level stuff. Like that's the, that's what we've been lured into. Like, you know, I'll buy a $20 smart switch and it's like, how am I paying only $20 for this? And the answer is because it's subsidized by a service or whatever else. And it's like, it's doesn't have infrastructure in there. It doesn't have like that natively because infrastructure is more expensive and time consuming and all that other stuff. And so, yeah, I feel like you might be paying more time and money right now, but you will have to be building your own infrastructure.

**Jeff Geerling:** Yeah.

**Jeff Geerling:** Over time.

**Jeff Geerling:** Yeah. That's the goal. And you know, every device that I buy, a few of them are cloud connected, but most of them, it's like, to me, sometimes that's a, an anti feature to have any kind of cloud connection. There are certain things like security systems. You need it because you know, you want them to call the police if you're not home. So you can't not have it. But for some things like my switches and my light bulbs and things, I don't want that at all. Like if I really need to turn off my lights while I'm in some other place on vacation, I have my VPN, you know, but not everybody has that. So I, I also understand, I also understand the convenience aspect, but it's hard if you work in the technology industry, you realize how hard security is. And then you also realize, I don't want to have 300 holes in my firewall for every single device that I own. You know, I don't want my fridge to pop a hole in my firewall that lets a hacker come in and take over my YouTube.

**Jeff Geerling:** Right. Yeah. Right. That is, I guess it does centralize some of your stuff. It's all centralized at some point, right? Even if you have it all in cloud, but yeah, that is, it's pretty interesting. What about like, I know a lot of people that are in a similar position to you, like that just kind of issue smart stuff entirely. So like, what is your motivation between, behind having, having smart stuff in the house in the first place?

**Jeff Geerling:** It's just the convenience. Like for, for, for a lot of little things, like the lights, 90% of it is I'm so lazy. I don't want to like, if you're carrying a box in your office, you don't want to also hit the button. So I think the, the biggest thing, the most influential smart device thing that we did, which is technically not connected to home assistant. It's just a smart, it's just a motion sensor switch. I installed new lights in the garage and they're on a motion sensor switch. And every time that we open the door to throw away a bag of trash into our trash can, the light comes on right away. We could have done a door switch or something too. But the point of it is before that, every time that we did that, we either were like, okay, I have this big bulky thing in my hands. It's pitch black. The kids might've left their bike here and I'm going to trip over it, you know, or, you know, you can like lean down and turn on the light and then you might drop some of the trash. It's just, it's just a bad situation.

**Jeff Geerling:** So that was. I like this though. No, this is, this is great. This is now the, the, the caption for this episode is Jeff Geerling finds PIR sensors to be the most, the most, the most enabling technology. It's great.

**Jeff Geerling:** It, it, it's, uh, I don't know those kinds of things. Like it, it's such a life-changing difference. You, you wouldn't think like nowadays, I don't think about it at all. But when I did that, the first few times that we did, it was like magic. Like, oh my gosh, our lives just improved. We went from like caveman to like, we can do anything in the world now. And that's, it's the first step. So, you know, everything beyond that is just improving that kind of setup. At the office, I actually have some human presence detectors using the, you know, the little millimeter wave or whatever the, the radar system.

**Jeff Geerling:** Those things are popping right now. There's a lot of sensors.

**Jeff Geerling:** So I'm going to try, I'm going to try facing off three or four different ones and see which ones I like the best for installation, for range, for ability to get them into home assistant. One is Zigbee, one is wifi, another, I think two of them are wifi and two of them are Zigbee. So I'm going to see how that all works together and see if there's any weird, I'm in an area that has like three radio towers around it. So like the key fob on my car doesn't work sometimes when I'm like five feet away. It's flooded.

**Jeff Geerling:** Yeah.

**Jeff Geerling:** So, and, and one of the, one of those towers is the super tower that has, it has like 35 services hanging off of it. Like if you look at it, there's like antenna, antenna, antenna, all the way up, all the way on the, on both sides. So I'm sure one of those is like beaming something straight at my office. That's going to interfere with things. But yeah, it's, it's worked out so far for the simple things I've put in.

**Jeff Geerling:** You know, it's another interesting piece of like that, that idea of like needing infrastructure is like the, it's got to always work, right? Like that, that the reliability piece is super important too. Like if you are building your own infrastructure, building your own thing, it's like, I was just about to ask you like, why would you be using a Zigbee sensor? Why wouldn't you build your own? But the answer is probably because you want to make sure it's always, always up and working as well. Right. Even, even if it's local and added.

**Jeff Geerling:** And this is for my office. So the nice thing that most people that do YouTube don't have a separate space. A lot of people do it in their home.

**Jeff Geerling:** Oh yeah. Yeah.

**Jeff Geerling:** I think in the past few years, we've seen more people turn it into an actual business with space and all that. Yeah. Which is for me, there's two reasons. One is I can walk from my home to the studio. It's, it's not a short walk, but it's not a super long walk either, but it's automatic exercise. So.

**Jeff Geerling:** Is this in like a St. Louis winters, even you could do that? I mean, St. Louis summers as well, I guess. St. Louis has some extreme weather actually. Yeah.

**Jeff Geerling:** It gets really hot and it gets really cold. But this year it got up to like one 12 Fahrenheit, which is hot, you know, whatever that is in Celsius, just hot, like 40 something.

**Jeff Geerling:** 40 something.

**Jeff Geerling:** Yeah. But, and then in the winter it gets down to negative five, negative 10, a few days, but normally, you know, in the, in the tens or twenties Fahrenheit again. So yeah, it gets both ways, but you know, put on a coat and some pants and you'll get

**Jeff Geerling:** there. Midwestern values there.

**Jeff Geerling:** Yeah, exactly. But it's, it's good for the heart, you know, even if your heart's like. That's right. Not doing well afterwards. But, but that was one of the motivations. The other one is just space. You know, there's so many products that I want to do. I have boxes of all the little electronics kits and things that I want to assemble and build some different sensors and boards. I just don't have the desk space anymore because taken up by high projects and taken up by servers that I'm testing and all that. So yeah. There's always a balance when, when you're on YouTube, since I chose to make this my career at this point, you have to make money to survive. So you can't just like do only the fun things. You have a family. So yeah, I have a family with four kids and I have a preexisting condition. So I have to have pretty expensive health insurance here in the US. All right. Yep. So you got to earn money. So you can't just only do fun projects. And the other hard thing is I have to record things while I'm doing it and I have to structure it in a way that is a story. So each week is spent on these things and I just don't have the time and the space. But what I, what I used to be able to do before about a year ago. And when I got into full-time full-time YouTube was I'd have space somewhere and I'd set up a project and I'd work on it over the course of a few months. But as we all do, your spaces start filling up. But in my case, like there is no space anymore. So I don't have any of those projects going on anymore. They're all in little boxes right now. So the office is going to let me work on a lot more of those things because I have, well, I will have more space on desktops. And I bought a few rolling carts that I will use just for these projects. But then in two years, I know I'll be saying the same. Yeah.

**Jeff Geerling:** I was going to say, I, this is echoes of my co-host, Dave, who said, you know, it's just a bigger office. It's all I need is a bigger office.

**Jeff Geerling:** It's just like, at some point you have like a 18,000 square foot warehouse. Yeah, exactly. I need more space. So where to talk about? Maybe if I did like multiple levels of benches, maybe if I, I bought a few things with like multiple shelves and I'm like, I could do that. And I'm like, no, this is just going to turn into storage. I know it.

**Jeff Geerling:** Yeah. Yeah. I've, I have the rolling cart with the project trays. That was a former guest, Ken, who told us about that. And I love the idea. It has not worked out. Like I thought it has. It's basically just like lots of junk on each tray. Yeah. Yeah. Yeah.

**Speaker ?:** Yeah.

**Jeff Geerling:** Pretty much. Yeah. That's great. What, so on the, so, you know, you're, you're sliding down into the, into the embedded space. I mean, what else, what else are you excited on, on the embedded side of things?

**Jeff Geerling:** I think some of the things that are most interesting to me are the fact that there's chips now that can do so much in such a small space. So you can have some AI acceleration, even like the new, the new Raspberry Pi five, it's now fast enough that it's, it's like what a computer was five or eight years ago. You know, a good laptop five or eight years ago is what the Raspberry Pi is now. And you can strap that thing to anything almost, you know, and, and you can, you can compress video better so you can get camera data in and process it and compress it, send it out somewhere, stream stuff. Uh, so some of those things are interesting to me. It's, it's hard though, because AI today is like what crypto was a couple of years ago. There are so many things that are just snake oil, it's blatant scams and people who are just in it to earn a lot of VC money. And, uh, it it's, it's hard to see what things are actually things to get excited about and what things are like, this is totally illegal what they're doing with the data and all that. And at some point the, you know, the music is going to stop and, uh, who's not going to have a chair at the table anymore. So. Musical chairs reference. Didn't expect that one. I gotta say. Yeah. Yeah. Uh, yeah. Yeah. I mean, with, with crypto, it seems like that's, you know, Sam, Sam Bankman fraud or whatever his name is with him and all that, that group of people, it seems like they're finally starting to get filtered out. And because there are some cool things about cryptocurrencies that I was excited about 10 years ago and I, it just totally, I was totally not excited for the past five or so years because of all the grifters and scams and things. So it's similar like that with AI right now. And the other hard thing is we're not yet to the point where everybody can build their own models for machine learning.

**Jeff Geerling:** Right. Yep.

**Jeff Geerling:** Because to do a good model requires so much hardware right now that, uh, only the big companies can do it. So you have to use their stuff. And like I said, I, I, it doesn't feel like they're all being above the board with how they collect their data and all that. Like when I search chat TPT, I see things that it's like, that's, I know that I wrote part of that and it's, how are they just, you know, verbatim pasting a line or two, I think into their answer here.

**Jeff Geerling:** Yeah.

**Jeff Geerling:** So I think there's still a lot of issues that has to be dealt with there. But, but it is what excites me because it's not going to replace our intelligence, but it's like, it's like when you know how to use Google really well, well, not Google anymore, because they just have ads, most of their pages, it's like, when you know, when you know, duck, duck go really well. And you, it, it accelerates your own thinking. You can get something out quicker. You can find the right resource. You can fill in the blanks in your own brain. And, uh, you know, I, I think that's, that's what excites me. And the fact that that could be on a little chip, like in your smart light bulb, yeah, probably not in your light bulb, but you know, you could have actually intelligent local assistants and things like that.

**Jeff Geerling:** Yeah. I feel like for a PCB layouts, one where I keep seeing stuff like, oh, we'll do all your whole PCB layout for you, whatever, whatever. I don't know. I don't, I don't want that. I don't need that. I don't, you know, like that's first off, you know, that, that just gives me bad feels about like my, my, my livelihood. Uh, and then also beyond that though, like, it's just, I know, I know like in my gut that there's nothing that's going to be able to just be done. Like it, it might give me something. It might be fine for small stuff, but like, I'm going to be involved. So like, once I internalize that, like you said, like once I make it a tool for my own capabilities, I'm going to be ramped up and doing more stuff with it. I'm excited about that. Like that actually does. I think that makes a ton of sense because it's a, it's an enhancement tool. And like that, that's great. I, I, I'll lean into those things. Yeah.

**Jeff Geerling:** Like, like right now I have a database of all the videos that I've done, all the, all the texts that I've written for them. Most of my videos are scripted. So I can search through that and find clips and things. But like, for instance, one of the things that AI could actually help with is if I have my whole library of all the media I've ever shot and all the footage and all the videos, the final edits and things, and it could like parse out the final cut pro XML file and say like, Oh yeah. You know, here's the thing that you're talking about two years ago with this. Yeah.

**Jeff Geerling:** Give me a callback. Right.

**Jeff Geerling:** I want to call that out and then give it to me. That saves me, you know, 10 minutes, 12 minutes here and there.

**Jeff Geerling:** Yeah.

**Jeff Geerling:** And that would be super valuable for me. Those kinds of things. But it's not like write me a video about the new raspberry PI seven. It's like, that's not gonna, it's not going to be good ever.

**Jeff Geerling:** Well, and it would be based on your, your past videos. It'll be. I know that's, no, that's the thing.

**Jeff Geerling:** Like you see all these articles and it's like, that's AI and it's very derivative and it's not, it's not making the world a better place. That's for sure.

**Jeff Geerling:** Yeah. Yeah. I agree. I agree. Yeah. Well, let's talk about the, let's talk about the PI because you, you've had so many great videos about the PI five. I'd love to just kind of give you your, get your, uh, you know, you're like an analyst at this point as well. Uh, what's your, what's your analyst view on the PI five?

**Jeff Geerling:** It's, uh, it's, it's hard to peg it as anything yet because they haven't introduced a cheaper one. I think the PI five could make more inroads as a $40. If they had a $40 one gig or two gig version, I think that that would sell more like hotcakes. I mean, anything that they make right now is selling like hotcakes because there's always demand for pies.

**Jeff Geerling:** Sure. Yeah.

**Jeff Geerling:** But it's not as fast. The PI four was way faster than all the other okay-ish SBCs when it was introduced. The PI five is not faster than all the rock chip RK 3588 boards. And it's not more efficient either. So from a hardware perspective, it's, it's not quite as good as them from a software perspective. It's still better because it's, you know, the maintenance and the support are so much better on the Raspberry Pi Linux distributions. One thing that I was, I've been pushing for, and I know some people in the community push for is getting, getting to a point where a Raspberry Pi is like a PC where you could just download any version of Linux and install it. You don't have to have custom versions with all the Raspberry Pi. That's been a problem in the arm ecosystem, but this, the PI five is getting closer, but still not there for that.

**Jeff Geerling:** What is the restriction there? Just like the build, like who's building for these different systems?

**Jeff Geerling:** It's mostly, it's mostly like the, the bootloaders and the way that they initialize, they just don't, they don't have, they don't have them set up with, there's a thing in arm called system ready. They don't have them set up with UAFI or something like that, a standard to, to get the system to boot. So you have to put in the device tree and you have to put in all the special things for each board. And it's, to me, that's annoying. It's, it's a problem that I think stems from them being so low end that it was kind of a necessity to do that stuff. But now these boards all have enough memory and they have enough CPU to be able to do these things. I don't know. It's not a huge priority for Raspberry Pi because they sell everything for that they make right now. Yeah. But I think it could be a game changer. If you could just buy a Raspberry Pi and download windows for arm, which doesn't exist. You have to hack it to get that. But if you get download windows or download Linux or whatever.

**Jeff Geerling:** Oh, Jeff, don't do that. No, no windows for arm on, come on.

**Jeff Geerling:** It's the crazy thing is windows for arm is great, but the software support for it is so not there.

**Jeff Geerling:** Interesting.

**Jeff Geerling:** But I've been running windows on my, my ampere workstation, the one that has 128 cores.

**Jeff Geerling:** And that's what it takes you to do windows for arm these days, 128 cores.

**Jeff Geerling:** It's funny. It currently dominates the Cinebench for any desktop computer, the 2024 benchmark. And it's only running on 64 cores on that machine. The Cinebench has a weird bug running on more than 64 cores on arm. And they used to have that bug with thread ripper systems too, I think, where they had more than 64 cores. But, but I mean, to me, it's like, if you can get your system to be as open and usable as possible, that just enables more things. Like more people might start porting games from windows to windows for arm, which might make them work better on Linux for arm too. You know, all the. Got it.

**Jeff Geerling:** So you're saying like ecosystem type moves like that would be beneficial. It would benefit everyone kind of thing.

**Jeff Geerling:** Yeah. Yeah. Got it. And a lot of people who might not use a Raspberry Pi, if you could get windows on it and it was native, which it is, it's just, it's hard to get it put onto a Raspberry Pi right now because it doesn't have system ready. That would bring a new audience of people who are like, well, I can't run windows. So I can't run whatever, you know? Yeah. I don't know. I, uh, I hate windows, but just, just put that out there.

**Jeff Geerling:** No, no, no. It's, I mean, it's not, I don't know. Yeah. It's all, it is what it is, right? It doesn't matter. Like the people's preferences are going to be what they are. And like you said, there, there's like these enabling things around games or software. Like, you know, you still can't run certain software that I, I love and want to use on non windows, you know, like, okay, well, I guess I'm not gonna use that anymore. But it is interesting kind of thinking about kind of the Raspberry Pi, just really the SBC space in, in the context of general computing as well. Cause personally, I still see it as like this enabling like, well, Linux system, but you get to, you know, you get to access a GPIO and do that sort of thing. I don't ever think of, I never buy like a gigabyte, you know, motherboard and like, oh, I'm going to flip a bit on this thing, but I could, right? Like that is a thing that happens. There are vendors that do that sort of thing. I just don't think about it like that because I think about it in the general computing met, you know, method. And, but I don't think about it in the other way, pushing down in general computing down into the Pis. Yeah.

**Jeff Geerling:** Yeah. Yeah. And you know, I, I think the, the big difference with the Pi 5 is it's the first generation where I'd say it's not the best Pi for a lot of general Pi use cases. So you can have the Raspberry Pi 02W. I think that that might be the most efficient, like if you're building a little electronics project and you want wifi on it, that's one of the most efficient ways to do that without having to go down to a microcontroller. And the Pi 02W is finally getting back in stock, but it's also smaller. It requires less power. It's a little bit slower, but for the things that you might use GPIO for most of the time, you don't need, you know, a 2016 era laptop speed. Right. Right. You know, you don't need to like rip through processing on something where you're just doing, you know, a little bit of, a little bit of GPIO bashing.

**Jeff Geerling:** Yeah. It's interesting too, because like, like you said, like the, the costs, you know, obviously coming down, the computing is up like all of these things. But to me, it's still as like a, even if it is only five Watts or seven and a half Watts, whatever the, the, you know, the low power mode is, is like, is that still what you should be doing? You know, like the kind of the, should you, and there's, there's always a, well, people should do whatever they want to do. Right. But like from a system design type of thing, one thing I wonder about too, we had the Raspberry Pi guys on and they, they were talking about the, the reason they had the RP1 and they said, because of the, the delays, but even the delays are going to be really high. I feel like the latencies are going to start to really impact people as well and Pi 5 and above.

**Jeff Geerling:** It could. Yeah. It's, it's hard because some things it's better. Some things it's worse. I like the idea of putting that chip on PCI express because in my mind, that opens up the possibility of like putting a Raspberry Pi into a computer through a cheap add-in card type thing where you have the same programming interfaces and all that. And if you're using PCI express gen four, you know, latencies are going to be very low. I think that that's it's, I think it's a long-term play for that kind of thing.

**Jeff Geerling:** Sure.

**Jeff Geerling:** And it also divorces them from the Broadcom chip development a lot, which is nice because I don't think Broadcom is like, man, Raspberry Pi is this thing that we want to put all of our forces into. I think they're more like, yeah, we're going to keep doing this for you guys. You know?

**Jeff Geerling:** Well, and I think it's not bad marketing for them, you know, it gives them some goodwill for sure. But I'm sure people aren't like, yeah. I want to choose.

**Jeff Geerling:** I think the cool thing is that that could enable them to switch to another chip in the future. And I don't think that'll happen for a Pi 6, maybe even a Pi 7 or something. But if they wanted to, they could start thinking like either a custom chip. I don't think they have the resources for that internally.

**Jeff Geerling:** Yeah.

**Jeff Geerling:** Or they could switch to another chip at some point. I keep like in my dreams, Apple would open up the M core designs and that chip could live on an SBC and it would be perfect. It would be so fast. It would be, it would blow people's minds what you could do on a little SBC, but Apple will never do it. But that is a dream.

**Speaker ?:** That is.

**Jeff Geerling:** Wow. Wow.

**Jeff Geerling:** Take an M1 and put it on a Raspberry Pi. The thermals are there. Like it could handle it.

**Jeff Geerling:** Amazing silicon. Just like, I don't think you could have chosen a worse company to be like, you should, you should open this up. Yeah.

**Jeff Geerling:** Come on. Come on. You know, there's an engineer in there who's like. Oh, tons of engineers.

**Jeff Geerling:** Right. But like, they're also getting paid for $100,000, you know, to fall in line, you know, like, yeah. There are economic restrictions around that for sure. You know, I, I was, I, I had asked the question of the, the Pi, the Pi folks as well about RISC-V and then you made a video about it, which I thought was great. Like, you know, kind of the, the not yet. They basically said, yeah.

**Speaker ?:** Nah.

**Jeff Geerling:** You know, it's, it's not ready. It's, but it could be. I, and the funny thing is like, there are parts of RISC-V that since it's a more modern ISA are already better than ARM, but they're very architectural. It's like, yeah, look at this beautiful foundation. It's like, I want to live here though.

**Jeff Geerling:** Yeah. Right.

**Jeff Geerling:** It's going to take a long time to move the foundation to a building. So yeah, it's even the fastest RISC-V cores are just, they're like, you know, not fast, not helpful.

**Jeff Geerling:** So. Yeah. I think unfortunately given the, the, again, economic stuff, I mean, like what's it called? Star five, just star five. No. Sci-five. Sci-five. Yeah. Had a bunch of layoffs and I'm just like, I hate to see it. And like, there's beneficial things coming in the RISC-V space as well. Right. Like Broadcom's in the new, they said they're doing RISC-V, which I'm like, okay, sure. And, you know, Nordic and Intel, like there's a bunch of investment and interest in the area, but we're just not there yet. You know, it was just like.

**Jeff Geerling:** Yeah. I mentioned in the video, like it's great for microcontroller level things. And it's, it's also a lot of companies are building their own little cores or customizing a core for devices to co-process, to do one task. And it's, it's cheaper for them because they don't pay whatever licensing fee for an ARM M0 or whatever.

**Jeff Geerling:** Yeah. Yeah.

**Jeff Geerling:** But yeah, no. And I think that that, the thing that that'll enable is in the future, you know, maybe there is a new chip, even from Broadcom that has extra risk cores for certain purposes. Right. Apple's really gone to the extremes with that, having like 25 different types of processors on their chip. Yeah. And a Raspberry Pi is the other extreme where it's like you get your arms and you get a video core GPU thing and that's it. Like there's no, there's no neural co-processor. There's nothing else. Even some of the rock chip boards are having extra little co-processors added in.

**Jeff Geerling:** Yeah. I think it's like what market segment, it is very strategic too. They have to kind of like aim that arrow, like, you know, two years in the past as well. I mean, probably less than 18 months in the past, let's say just given chip times and deliveries and all that other stuff. And it's, yeah, a lot of, a lot of, a lot of guess and check it seems like.

**Jeff Geerling:** And yeah.

**Jeff Geerling:** But like you said with the, I think the risk five in the embedded space is really interesting. Like Dave and I have talked about the show about the, the CH 32 V003 is like the 10 cent risk five. And that's a fun little chip and playing with that. And I don't know, even like the ESP is like the, the C three is like way cheaper than the extensi core. So it's like, and, and not that, I mean, it's hampered. It's a little bit less beefy, but lower power as a result, just because it's, it's clocking at a lower rate. So fine with me. I just need a, yeah.

**Jeff Geerling:** It still works for 98% of your projects.

**Jeff Geerling:** Yeah. I, that's one thing I always kind of run into is like, I feel like the, the reviews you, you do, it's like, you're kind of like on this leading edge type of thing. Like you're like trying this leading edge stuff. I'm just like, I'm buying stuff. That's eight years old and I'm using analog technologies that are like, you know, you know, eight nodes back and just like, yeah. So there's always trade-offs there.

**Jeff Geerling:** Yeah. It's like, like I mentioned earlier, like I have to make money. So the hard thing you can't always do the project. Like I have a couple of projects that I have been working on that I would do a video about, but I know it would get 15,000 views and that's not going to, that's not going to help my channel. So I don't do them. So another thing I've thought about is having like a second, second channel or something. I have Girling engineering for it and radio, but having like a second one, like random projects and some people do that. But every time you spend a minute editing a video, it's like, that's a minute I could have done something else. So totally. Yeah.

**Jeff Geerling:** Yeah. It's tough. Those things.

**Jeff Geerling:** I still reserve those. Those are my fun projects. You don't get to see them. Sorry. You know?

**Jeff Geerling:** No, I think that, I think that's actually a really healthy thing for YouTubers generally too, because it's like, if everything has to be content, then it like starts to make you seize up and be like, oh, well I shouldn't do this unless I can do it. It's like, no, you need to maintain like life, right? You're going to, you're going to have your own, your own stuff. So is there, is that like some embedded stuff that you wouldn't be able to publish about you think? Or what's, what's in that, what's in that realm?

**Jeff Geerling:** It's, it's just some, some extra monitoring and automation things I'm doing at the house. Like I'm, I'm working with the power panel and, you know, wiring up everything for power monitoring. And I'm working, I'm also working on trying to integrate some battery stuff that I have with my UPS. So I have like dual redundancy in my, in my house and long-term I'm, what I want to have is all my, at least one light in every room is on some sort of like OE backup. That that's a long-term thing, but I'm trying to get the battery stuff in place so that I could support running all the lights for like two days without running my, any kind of generator or anything like that.

**Jeff Geerling:** And this is how Jeff descends into prepperism.

**Jeff Geerling:** Everything's on backup and I have MREs in every wall. And that's, that's the problem. I only deal with gold. We have a pile of all of our stuff behind this wall. This is like the, the bunker part of my basement. Yeah. Yeah. You know, when there's, when there's a tornado siren, which happens like 20 or 30 times in the spring here in St. Louis. Yeah. Everybody comes into this room. So, cause we have all, we have everything. That's the thing that we need. We could live, I think two or three weeks before it starts getting really smelly and nasty in here.

**Jeff Geerling:** Well, you are moving into a new space as well. So you are moving on out to a new commercial space. You've been posting about the horrors of painting. I've seen that one and agreed with it.

**Jeff Geerling:** You don't realize how much, like 1200 square foot of office space. I put it in, there's now five rooms and then every room there's four walls and each wall has different things.

**Jeff Geerling:** Like they're tall.

**Jeff Geerling:** It's like 1200 square feet. Not so bad. But when you split it up and you have all these things and it's like so much more cutting in. I had like a bruise on my finger here from, you know, holding the paint brush for so long.

**Jeff Geerling:** Yeah.

**Jeff Geerling:** And that's gone now, but I still have one more wall to paint and someday I'll paint that wall. It might never get painted. That might be like my unpainted wall.

**Jeff Geerling:** It's your, it's your, it's your white whale, but it's a wall.

**Jeff Geerling:** Cause I got to move in soon. And once you move in, you can't paint anymore.

**Jeff Geerling:** So is your family excited about reclaiming the basement too? I mean, that's.

**Jeff Geerling:** My wife has been for like three or four months now. Like, so when are you going to move out? Cause I'm going to move my sewing stuff in that room. We had the kids, the kids started taking over more to the basement. So her sewing stuff, sewing stuff, because it's not, you know, making money for the family. Yeah. We had to move it into another corner and then things got moved in front of it. So now she can't do any sewing stuff unless she like grabs her machine and brings it out and sets up a table and stuff. So this is going to become the sewing room. She's been very excited about that.

**Jeff Geerling:** Nice. That's great. All right. That's the benefits of spreading out a little bit. I mean, you know, you get a pretty big family there. That's, that's a lot of, that's a lot of people and you got to democratize the space for all. Right. So that's tough. And you got to keep your own space too. So that's, that's nice to have the office.

**Jeff Geerling:** I might rework the workshop a little bit. It used to be a wood workshop. And then when I started doing videos and stuff, now I can't have sawdust everywhere. I haven't done it. I got rid of most of my woodworking tools and now I just have like, you know, normal general household maintenance tools that are more boring. But I might rework it a little bit so I could have a wood space that's ventilated and has a door and then like the other workshop. So we'll see. That could be fun.

**Jeff Geerling:** Yeah. I watched Colin Furze's channel. Colin Furze. Yeah. Yeah. And yeah, like that new workshop he has. I'm just like, oh my God. That's insane. Yeah. His, his, I mean, he's obviously a very extreme example, but like, you know, it's super easy to get sucked in and be like, no, I need, I need a metalworking shop. I don't know how to build, but I totally need one, you know.

**Jeff Geerling:** I need my own water jet. Yeah. Exactly.

**Jeff Geerling:** Cutters. Yeah. Yeah. The things I would build, you know, like the, ah, the races I will run once I buy the treadmill, you know, I'll finally be able to go running. Right. Yep. Yep. That's great. Well, Jeff, I, uh, I really appreciate you joining us here. I highly recommend people follow your channel if they don't already. Where is the best place to find you online?

**Jeff Geerling:** My website, jeffgearling.com. It's been around forever and it will be around as long as I can make it last.

**Jeff Geerling:** The battery, the battery backup on the self-hosted pies in your basement or office. Yeah.

**Jeff Geerling:** I did self-host it at home for a short time, but then somebody DDoS'd my house and got my ISP to cut off my IP. So I decided to stop trying to do that.

**Speaker ?:** Yeah.

**Jeff Geerling:** You know, this is why we can't have nice things. Yeah. Well, Jeff, thanks for joining. I really appreciate it. And I'm looking forward to all the future videos about pies and computing embedded. However we can help, let us know. Yeah. Thank you.
