---
episode: 295
title: An Interview with Omer Kilic
url: https://theamphour.com/295-an-interview-with-omer-kilic/
---

**Omer Kilic:** This is The Amp Hour Podcast, recorded April 20th, 2016. Episode 295, an interview with Omer Kilic. Welcome to The Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Omer Kilic:** And I'm Omer Kilic from Den Automation.

**Omer Kilic:** Welcome. And we're actually in the Den Automation office.

**Omer Kilic:** Welcome to Brick Lane.

**Omer Kilic:** Yeah. Yeah, so we're in London. Oh, yeah. I was like, oh, yeah. We were here last night, right? We were hanging out here last night. But where are we in London in relative terms?

**Omer Kilic:** So you're in the world-famous Brick Lane, where we have a lot of carry houses and a lot of hip bars.

**Omer Kilic:** And the bagel shop.

**Omer Kilic:** Oh, the bagel shops are the greatest.

**Omer Kilic:** Right. So last night we were at a meetup. There's like 25 people there or so.

**Omer Kilic:** Yeah, good turnout.

**Omer Kilic:** A couple beers, another place, a couple more beers. And then the bagel shop was the place we had to hit. And I will say that was the right place to go.

**Omer Kilic:** Well, we're glad you liked this. Yeah, right. I approve of London. We need to take care of you. I mean, you're a guest, right? Oh, yeah.

**Omer Kilic:** Right, right, right. So that's good. So you are... How long has Den Automation been here?

**Omer Kilic:** So we moved in around October time. This was an empty room. I mean, of course, this is a podcast and not many people are seeing it. But there's things everywhere now and we kind of need to find a bigger office. Yeah.

**Omer Kilic:** It looks like maybe... Well, I don't know how many people are here every day. But you have a little lab space. You have to ask stuff like that.

**Omer Kilic:** Yeah. But it's been fun. I mean, in traditional startup style, we built everything from scratch. Like, went to Ikea, loaded up like a small truck, load of things. And now we're kind of developing some cool stuff here.

**Omer Kilic:** And we will get to that in a second. Before that, let's get some of your background. So you've done other startups. You've done electronics. Obviously, we've followed each other on Twitter a long time. Yeah, we're Twitter buddies. Yeah, Twitter buddies.

**Omer Kilic:** So I started at uni doing computer systems engineering, which is kind of a... It overlaps the software engineering and electronics engineering practices. And I kind of focused on more of the digital microelectronics, FPGAs, microcontrollers, and PCB design, that kind of stuff. And then I liked academia so much, naive of me, that I stayed on to do a PhD. And the topics I looked at, I started with, were partial dynamic reconfiguration on FPGAs.

**Omer Kilic:** Oh, so like the thing where you load a bit file, and then part of that bit file acts as a bootloader for the next bit file.

**Omer Kilic:** Yeah, and you can basically reconfigure parts of your system while the other parts are still running.

**Omer Kilic:** It's the dream of an FPGA, which actually isn't used that often, right?

**Omer Kilic:** No. I mean, the beauty of it is that it's really interesting. Mm-hmm. And it's... There have been very many different ways of doing it. Mm-hmm. Even so... Even, you know, things that were not officially supported by Xilinx, but people kind of abusing, you know, the standard configuration facilities to do like a hacky, kind of hack together reconfiguration stuff. Right.

**Omer Kilic:** It's not like they're like encouraging you to do it because people think that's the right idea, but usually it's not.

**Omer Kilic:** Yeah, true. And Xilinx added support for this in... I can't remember the ISE version.

**Omer Kilic:** Wait, was it the one with tons and tons and tons of disks and gigabytes of files?

**Omer Kilic:** Oh, the full installation was something like 12, 13 gigabytes. Yeah, yeah. I mean, ask SAR about this. Oh, yeah. Right. We were hanging out with the last night as well. So that was fun. But then I kind of realized... The particular application area I was looking at was image processing, StereoVision. Image processing on FPG is fun, right? Yeah, it's great.

**Omer Kilic:** It's a great application for it.

**Omer Kilic:** But then I realized I kind of had... I was more interested in system-level problems. So the tools and methodologies I was developing for the reconfiguration of FPGAs, I started applying them to a wider embedded systems kind of system approach.

**Omer Kilic:** So like loading firmware remote type stuff?

**Omer Kilic:** Remotely, kind of like a distribute... It turned my... The thesis title ended up being something along the lines of a dynamically reconfigurable framework for distributed embedded systems. So...

**Omer Kilic:** Perfect. Which is practical, actually. Like that's the kind of stuff that my old company used to do all the time, where you get to push updates to the field. And it's a huge... I'm sure Alicia and Chris, if they're listening, would be like, yeah!

**Omer Kilic:** So what inspired me was looking at all my lab buddies struggling with all these sorts of different types of systems they were inheriting from other students and spending a lot of their time on the configuration, management, distribution, communication side of things. And I tried to kind of apply certain principles that I learned along the way, talking to my buddies in CS doing concurrency parallelism and other group of friends doing distributed computing and stuff and applying it to an embedded kind of domain. It was fun. Submitted, defended, I still need to submit corrections. It's not done yet, but hopefully it will be out of the way after that. Towards the tail end of that, I kind of wanted to explore a bit more of the software engineering side of things. The internet, the cloud, these distributed services and so on. So I joined the company to do distributed Erlang. Erlang is a...

**Omer Kilic:** That sounds familiar. It's a programming language.

**Omer Kilic:** It's a programming language that was originally designed for embedded systems at Ericsson years and years ago. It ran...

**Omer Kilic:** Ericsson, whatever happened to those guys? They used to make phones, right? They did, yes.

**Omer Kilic:** Funny enough, we were talking about with our industrial designer in the office a couple of days ago about how awesome some of the old Ericsson designs were. Yeah, particularly the T28, the GSM ones. I don't know if you got them in the US.

**Omer Kilic:** Yeah, I never really paid attention to the GSM stuff because I was always on Verizon.

**Omer Kilic:** The T28 had this asymmetric antenna on it. That was so cool.

**Omer Kilic:** I always wanted one, but... Yeah?

**Omer Kilic:** And it was terrible now that we have these amazingly beautiful smartphones and stuff. Right, right.

**Omer Kilic:** But yeah, at the time... Actually, I was just... So on your recommendation and a bunch of other people's recommendation, I was at the London Science Museum today. It's so good. It was amazing. It was amazing. But they had a whole section on communication stuff. And then you get to the end and it's like, oh, this is like a wall of cell phones. And so I saw a bunch of designs as well. It was interesting. I also saw the big brick phones and stuff.

**Omer Kilic:** Beautiful stuff. I loved it.

**Omer Kilic:** Actually, they were doing a little... Sorry, don't mean to step on your toes here. No, that's right. They were doing a little demo. They actually had phones and stuff out. And I walked up to them and I'm like, how many kids know what these things are? He's like, do you know what these are? I'm like, yes, I know what they are. I'm like, I used to have a rotary phone. Come on, man. Everybody... Yeah. But it's...

**Omer Kilic:** Well, they don't make them like they used to. Thank God for that. Yeah. Well, arguably, yes. Actually, yes. What am I talking about? So I kind of looked at how we can play with Erlang and embedded systems because Erlang employs this model of concurrency called actor model where things are abstracted into their own individual units. Think of it as processes, but without the horrible kind of how do I get things communicating approach because actors have mailboxes. They can send messages to each other.

**Omer Kilic:** Oh, so kind of like when you're doing like... Shoot, what's that called? Mailboxes are like for our tosses, right? Yeah, yeah.

**Omer Kilic:** You can think about it the same way. At the moment, I mean, the lineage of Erlang is again, telephone switches, data exchanges, that kind of deal. But now it powers a lot of messaging systems. You must have heard of WhatsApp, the messaging app. That's powered by Erlang and stuff. I thought that was J2ME. Well, I think one of their clients is J2ME. I'm talking about the backend side of things. Oh, okay, okay. But I kind of took a different approach and said, can you actually run this on the device? And we actually put out a framework for Raspberry Pi where you could abstract all the hardware concepts or map them into actors and have messages passed amongst themselves and so on. Interesting. We had concurrent blinking lights and all that stuff. It was fun. I think it's still living in some shape and form.

**Omer Kilic:** Is Erlang hard to program? I've never even...

**Omer Kilic:** So the problem with Erlang is it's actually a very simple language. It's very concise. But the syntax is compared to, say, C or, I'm going to use the J word, JavaScript. We'll be talking more about that. Oh, yeah. I'm looking forward to it. I love JavaScript. So Erlang is different. It has a very different syntax. And the problem with... This is not an Erlang thing. But the problem with most people is that they actually are very... They don't really look at their... What's the problem with people? I don't know. I don't know, Chris. The problem is people get stuck with simple concepts like syntax. Come on. Spend like two days and syntax becomes a secondary factor, right?

**Omer Kilic:** I suppose, yeah. I mean, any language has its... Of course.

**Omer Kilic:** And especially when you're dealing with things like... So Erlang has this feature. A little quick plug for Erlang. Erlang has this feature where you can match patterns on the messages that you're receiving very easily. And the bit syntaxes and doing protocol level stuff in Erlang is beautiful, right? Because you're just defining grammars. They're actually part of the function body. Let's just call them function bodies, function bodies. And then you can match on the incoming messages and so on. You don't have to do horrible reg X structures and stuff. Right, right, right, right. So it's a... I mean, for me, it's still a very interesting language. And I still prototype quick and dirty things using our old framework sometimes. But yeah, I guess that was a long-winded way of saying it's not that difficult. It's just that you need to look past the syntax. You just don't get stuck on the syntax. Okay, cool.

**Omer Kilic:** Cool. So you took... You're still defending, you said, on the PhD side?

**Omer Kilic:** Yeah, I defended. Oh, you defended. I got the list of corrections. I just need to find the time to, you know... Yes.

**Omer Kilic:** Well, that could last another 10 years. We'll see, yeah. Yeah, I think I need to do that in the next six months or so. But we'll see. Yeah.

**Omer Kilic:** I mean, I'm not going to let it go after this point. Yeah, yeah. I've lost enough hair over it. Yeah, right.

**Omer Kilic:** Yeah. So you've taken that and you've parlayed it now. You said you've done a couple other startups as well. Oh.

**Omer Kilic:** Actually, no. This is my first startup. After the Erlang stuff, I joined a hardware company. Oh, okay.

**Omer Kilic:** Like an established one.

**Omer Kilic:** It was an establishment. It is still an establishment, actually. It's still there. And this was more of a kind of a much bigger scale and actual hardware as opposed to software. Oh, okay. Because I decided that while I enjoyed Erlang and distributed systems and stuff, I kind of enjoyed doing PCBs and electronics and embedded Linux board bring up drivers getting lost in data sheets and cursing it.

**Omer Kilic:** Well, having both of those domain expertise is super important, too. Being able to write the drivers, you need to know the hardware, right? Yeah. I mean, that's super important.

**Omer Kilic:** To me, it's always about problem solving, right? I'm more interested in the system level problem that needs to be solved. Right. I mean, if that requires me to dive into the kernel, I'm not claiming I'm like an expert kernel hacker or whatever, but I like getting lost and learning something new out of it as well. Yeah.

**Omer Kilic:** You will definitely, if you plumb those depths, you will find a monster or two, right? Oh, absolutely.

**Omer Kilic:** And, of course, dealing with, you know, big semi and, you know, vendor SDKs and vendor drivers. Oh, here, have this, like, kernel 2.6 driver that kind of works. Right. But you're on kernel.

**Omer Kilic:** You can just troubleshoot the rest of it. Exactly. Just tell us about all the errata. We'll put it back into the, you know, you'll solve someone else's problem, too. It doesn't that feel good?

**Omer Kilic:** It feels amazing. So, yeah, I did a lot of prototyping, kind of everything from board that we'll bring up to even towards the end of my tenure there, doing factory testing. Oh, nice, yeah. It was nice because I got to see, like, it's not every day that you get to interface with big, you know, factories and stuff in, you know, Far East and all that stuff. Right, right. Yeah, it's like an eye-opener, right? It is.

**Omer Kilic:** For how things are really done. Absolutely. I think we talked to Jeff about, Jeff Kaiser, about that a bunch. I mean, not a bunch of people, but, yeah, like the, you know, the boots on the ground.

**Omer Kilic:** Yep.

**Omer Kilic:** Oh, oh, that's what they're doing. Oh, my God.

**Omer Kilic:** One thing I'm not missing out is, I mean, I was based in London. I traveled a fair amount, but I don't miss my 3 a.m. San Jose, London, Suzhou, China, you know, meetups.

**Omer Kilic:** Wait, so when you fly, do you fly that way? Do you fly through, like, Dubai or something to get to China?

**Omer Kilic:** You could, if you really try to, yeah. Or you could just, I mean, when I go to Shenzhen, I just go to Hong Kong and then just go somewhere. Oh, you can go here to Hong Kong. Oh, I didn't know. Okay, okay. I mean, London to Hong Kong is a fairly established. But you're going east either way. Yeah, exactly. So, interesting. But, yeah, that was an eye-opener. That was an education. But after that, I realized I wanted to do a bit more of a concrete, you know, get hands dirty, work with smaller teams.

**Omer Kilic:** Right. Smaller teams, you work on more of the system, right?

**Omer Kilic:** Also, I was getting a little tired of traveling and living out of hotel rooms. It's not as glamorous as people think it is.

**Omer Kilic:** It isn't. I mean, it's nice at first.

**Omer Kilic:** At first, but then...

**Omer Kilic:** But also, Suzhou or wherever you end up going. I mean, like, it can be the expat thing. Yeah. Not expat, but, like, being in a rather foreign environment gets... Yeah. It wears on you.

**Omer Kilic:** I mean, I was very lucky. I had a very nice support system. All the people I work with were amazing. Amazingly, like, the hospitality they provide was amazing. And I enjoyed it. I learned a lot of things. But at the same time, I wanted to be, you know, I didn't want to travel that much. And I wanted to just be in London for a while. Right.

**Omer Kilic:** Well, and having that knowledge is super important, too. Knowing how to navigate the markets and knowing manufacturing stuff.

**Omer Kilic:** Well, the way I look at it is, everything is a learning experience, right? And if you can make it fun, you can keep going at it.

**Omer Kilic:** Right.

**Omer Kilic:** Because, like, think about the startup environment. The reason I joined the startup environment is because, A, it was actually quite an interesting project. And we'll get to it later. But, B, there's a lot of things to be learned. And it's an opportunity to, A, improve yourself and, at the same time, do something that potentially can be, you know, big and, you know, nice.

**Omer Kilic:** Right. And I think it's much like travel that eventually you might, if you went from startup to startup to startup always with, like, a couple people. Yeah. You always run into the same kind of frustrations.

**Omer Kilic:** The ultimate goal is to become a farmer and, like, start producing cheese anyway. Right?

**Omer Kilic:** Is that your goal? I mean, if you talk to anyone... We were talking about cheese before, and I am thinking about cheese.

**Omer Kilic:** The cheese mountain. Yeah, the cheese mountain. Jokes aside, like, if you talk to anyone in the UK tech circles, like, becoming a farmer and, like, start producing cheese and beer is the ultimate goal. Really? I'm not talking about the next two, but, like, the ultimate goal.

**Omer Kilic:** You just mean, like, simplicity and, like, kind of a... Yeah, yeah. Yeah.

**Omer Kilic:** Because, like, you can only deal with so many kernel, like, oddities until, like, you just want to do something with your hands, right? Yeah. I mean, I took a carpentry... That's when you start machining. Come on, man. Yeah. I actually had a carpentry course I attended last year. Oh, nice. Yeah. That's super stressful. But I had to cut it short because I had to go to California. Right. I mean, damn those sunny weather having days.

**Omer Kilic:** Yeah, yeah. You got to hate being in Palo Alto on a nice day.

**Omer Kilic:** It's the worst. Yeah. Yeah.

**Omer Kilic:** So, okay. So, how is it? I mean, we talk about... Me and Dave talk about startups. You know, we've had other guests on who are startups. But, you know, I guess... Well, I mean, we've had some startups, but maybe more kind of a big mix. This is a legit hardware startup. Yeah.

**Omer Kilic:** We're doing a lot of hardware.

**Omer Kilic:** Yeah. Which is good. But I think there's interesting problems with that. Money, obviously, is always going to be a problem. But... And one I always point out to people, I'm like, you know, like software companies, they raise a bunch of money and their costs are like nice chairs, good computers, and people. Snacks. Yeah, snacks. Oh, of course. Right. But then a hardware startup has to be like, oh, and also $100,000 in molds or something, you know, or... Yeah, yeah, yeah. ...you know, a $10,000 prototype board that I got overnight. Right? Sure. It's just like, oh, shit, you know? Exactly.

**Omer Kilic:** Yeah. Regulatory approvals. Oh, yeah.

**Omer Kilic:** We'll talk about that too, yeah. So, what's it like for you? I mean, what's the experience?

**Omer Kilic:** So, my role in this company at Den Automation, I'm the chief hacker slash CTO, so... Chief hacker. I am.

**Omer Kilic:** Is it on business cards?

**Omer Kilic:** It is on business cards. But the funny story is, especially when you're dealing with manufacturing folks, they don't get it. No. Because it's kind of a more mature industry. Right. They don't think it's funny. They actually have two business cards. One of them just says chief technology officer and one of them is just chief hacker.

**Omer Kilic:** Well, because they're also looking for people that are decision... I mean, you're a decision maker as well. Yeah. And that's what they're really looking for.

**Omer Kilic:** But then, here's the thing. In a six, seven person startup, right? Right. Your title doesn't really mean anything.

**Omer Kilic:** Totally agree. But, yeah.

**Omer Kilic:** But at the same time, yeah.

**Omer Kilic:** I've struggled with that too, where it's like, okay, there's three people in a company. Why are you the chief this, chief that? Some of it is actually from a corporation standpoint, I know. Yeah. Yeah. And then the rest, I think, is just because you need to be the decision guy.

**Omer Kilic:** True. And I do end up having to decide on all the technological elements of our products. But the experience has been great so far, and I'm really looking forward to the months ahead. Because we're currently at a stage where we have done quick and dirty prototypes with lots of wires coming out of it. Nice. We are prototyping our ID and started receiving beautifully machined parts. Oh, yeah. It's all happening. But it's hard work. It's not standard.

**Speaker ?:** Long hours.

**Omer Kilic:** It's not a nine-to-five job. Don't let anyone tell you.

**Omer Kilic:** I don't think anyone listening would really expect that. Yeah.

**Omer Kilic:** But as I've mentioned, it's all, like, you learn a lot of different things. And one of the important things in a startup, and we've kind of been working with this kind of attitude since the beginning, is understanding and accepting your weaknesses and seeking for help or external, you know, sort of sourcing different projects to subcontractors or agencies. Yeah, right. And design agencies, engineering companies, it's very important. Because if you try to, I'm not saying you can't do it, but if you try to solve problems that are best solved by, you know, domain experts, even though it might cost you a bit more, it's going to make your life so much easier.

**Omer Kilic:** Right. Well, yeah, it's a kind of balance of, like, because you talked about wanting to learn, right? So, like, say that you had to go send out an email to, like, your campaign backers or something like that, and you want to do that perfectly. Yeah. Yeah, you might learn that stuff, but it's probably not, if you've got other stuff to do, you have to actually focus on the important things.

**Omer Kilic:** It's, yeah, I completely agree. So, we've been very lucky to have partnered up with some really, you know, great companies and organizations, and development is, you know, full steam ahead, happening full steam ahead. Awesome. Awesome. It's also, it's nice to be able to iterate on ideas very quickly. That's one of the things I love about a startup. It also means, it's a curse and a blessing, right? So, if you think about a standard or, like, a well-established engineering company with lots and lots of divisions, offices spread around the world, you need a lot of documentation. You need a lot of spec work. And, you know, you need a lot of everything before anything can start. By anything, I mean mostly development work. Right.

**Omer Kilic:** Versus sitting next to someone and turning them and going, let's try this.

**Omer Kilic:** So, in a hardware startup, distributed teams are very, very, very difficult to pull off. Yeah. Especially, like, I'm a strong believer that the firmware engineer should sit right next to the hardware engineer. Yeah. In their lap almost. Yeah, exactly. So, we've been... Yeah, no, that's, especially during, like, board bring-up. Like, so important. Yeah, yeah. So, on more than one occasion, we were able to come up with an idea on Monday morning, you know, quickly research what's available, design a quick test board, Monday, Tuesday, send off for a PCB fab. At the same time, ID gets done. We have a quick resin printer in the office, which we love. Oh, yeah. Yeah. And by Friday, we've kind of iterated on the concept with physical hardware in our hands already.

**Omer Kilic:** That's a great turnaround, yeah.

**Omer Kilic:** I mean, it's... Think about it this way, right? Quick prototyping is amazing these days, especially when it comes to PCBs. Oh, yeah, yeah. Yeah. 3D printers, I'm not a big believer in filament-based ones. I mean, they do work... I mean, it's rough stuff.

**Omer Kilic:** It depends how much finish you need on your stuff, so...

**Omer Kilic:** I have one at home. I kind of... I use it for printing lots of, like, L brackets, fixtures... Yeah, yeah, yeah. You know, quick things. It's great for that. I love it.

**Omer Kilic:** Like jigs and test holders and stuff like that.

**Omer Kilic:** But when you're trying to print kind of like a device prototype that you're developing, you kind of need a bit more resolution. And we actually have been very happy with our resin printer. Yeah. Not naming any names. Uh-huh.

**Omer Kilic:** But it's great. It's on your Twitter account, I think, so... Is it? Yeah, we'll let people go for it. Exactly. Okay, that's fine.

**Omer Kilic:** But we found that, like, if you actually spend a tiny bit of time with, you know, some wet and dry and actually prime it... Oh, yeah. It looks amazing. It looks amazing. I'll show you some samples later. And that kind of quick iteration cycles are what I am really, really happy about. Yeah. Sometimes we don't even need to do custom hardware. You can just store the development kits because development kits are almost free these days. People are dying to give you their development kits. It's also very funny how... Should I tell? Sure. Right. I don't know. Big semi trying to enter the whole development market. Oh, yeah. Right. We're targeting pro makers or maker pros. It's so funny.

**Omer Kilic:** It's... Yeah. You mean everybody having Arduino pinouts on their thing and chasing... Yeah.

**Omer Kilic:** Not just that, but, like, the whole market... Like, the mindset. Yeah. Yeah, I don't know.

**Omer Kilic:** It's weird. Uh...

**Omer Kilic:** Uh... Uh...

**Omer Kilic:** Uh...

**Omer Kilic:** certain point not you but like the people that they're selling you're just going to stop and be like can i buy more chips from you can i talk to your fae so they can design in parts for every

**Omer Kilic:** other socket on the board i have a great story about this so uh a couple of weeks ago i i was in shenzhen i still don't know if i'm pronouncing it correctly i think it's i said shenzhen yeah i don't know if that's right either so who cares we'll go with shenzhen so i was in shenzhen and i um yeah not naming names big semi um they're in pretty much every kind of wireless access point device oh yeah um just before i left i you know just for a laugh i gave them a call i said i'm interested in this part i'd like to talk to an fae i'd like to create an account or open an account and they said the first sentence was um unless you can commit to 250 000 units per year um per parts or per product category or whatever i can't remember uh we won't be able to provide assistance i was like okay thank you very much so that's what i expected this is the thing right in in my previous life i was able to get access to these things very easily with just one email um being a startup you don't really get the luxury of you know emailing faes directly right startup email account but right

**Omer Kilic:** so but they still say they want to talk to you of course oh absolutely they want they want the

**Omer Kilic:** marketing side of it they'll sell you uh maker pro development boards and stuff but try buying

**Omer Kilic:** their chips so you just jump from one to 250 250 000 you're good of course yeah that's easy yeah you

**Omer Kilic:** don't need to go a million you can only you can do 250 only 250 000 per quarter per quarter right luckily they said per year okay i mean that's the saving grace of the whole i forget who was talking

**Omer Kilic:** about that they said they said yeah we do 10 000 and they called them back the next month so when

**Omer Kilic:** you want your next 10 000 so it's a completely different mindset and like they're not really interested in small fish they are they're in for the big hitters and you can't blame them because if you think about the competition and the way they operate for that right but this is not me like actually um you know bad mouthing them or anything it's just the way the market works right but anyway so arrive in shenzhen um i go to one of the many beautiful markets in find the first stall um through google translate um asked to buy four of these chips and i'll actually give you a picture so you can link to it yeah um and like 15 minutes later and i think i paid 15 quark per chip or something something like that um 15 15 r&b um so yeah wow so it's like two and a half bucks yeah something like that um i got four beautiful chips taped to a piece of cardboard with like packing tape

**Omer Kilic:** and in like clear just slowly to untape these yeah yeah um it was glorious i mean of course i didn't do

**Omer Kilic:** anything with those chips yeah in fact i think oh yeah i did i did these solder like on one of the

**Omer Kilic:** development boards you say you should frame them you should frame those four if you still have

**Omer Kilic:** i gave one to aaron actually um from umlaut uh we happen to be in shenzhen at the same time so um anyway funny story so the the the moral of the or like the point of the story is that um it's not a level playing field right right the access to these kind of things for western engineer is very very very limited so when you're designing with that those kind of devices it forces you to um until you reach a very very good volume um use modules which is a cost adder you don't have the flexibility you have right um on this subject last month uh ivan our firmware engineer and i gave a talk at the open source hardware user group oh yeah um and it was all about discussing um how you can actually start developing with these classes of like the wireless soc class devices um because these devices are great for two and a half bucks you get pc express usb like a linux capable processor you just take a bit of ram and some spi flash and you're good to run all your javascript applications right so chris is

**Omer Kilic:** smirking yes yeah anyways keep going yeah anyway but i agree that the the access to just the feature

**Omer Kilic:** set is amazing right yeah um so where people are trying to push 32-bit microcontrollers into all these you know applications that arguably require a bit more horsepower um it's it's yeah you can see yourself using these classes of devices of course the problem is they're much higher power than their microcontroller counterparts right um when i say microcontroller counterparts i'm talking about things that don't necessarily run a full operating system full stack memory management and rf very very limited memory and this actually especially in the iot results in uh potentially weaker crypto um slightly more convoluted ways of dealing with things and so on and so forth right so um anyway i like wireless socs ysocs they're great but um but there's trade-offs there are trade-offs it's engineering

**Omer Kilic:** yeah welcome to the world of engineering yes engineering still valid of course okay so let's talk about den i mean so uh you had told me a little bit about this and i got to see a demo today um actually no before we talk well should we talk about den first or should we complain

**Omer Kilic:** about iot first i'm not a marketing person so i'll give you a like a two minute overview of what

**Omer Kilic:** we're doing okay that's a good idea um i think we definitely need to complain about iot in general

**Omer Kilic:** oh we can we can talk about that how long do you have until your flight tomorrow we're close to bagels and indo so it's true we can just survive here for a while here okay so then automation uh we're reinventing the the light switch and the plug sockets reinventing yeah you guys aren't though i mean you guys are enhancing we're enhancing it okay so that was that's the usual like one line it up you use but what we're doing is we're working in the home automation fee or subsection of the iot domain um and we're kind of taking a look at all the products that are out in the market and saying hang on a second like shall we do like a bit more kind of user experience research shall we actually figure out what people need right and most importantly shall we just not introduce goofy user interfaces i'm talking about hardware interfaces to people so

**Omer Kilic:** and i i will point out as well that you guys are basically listening to me uh we were talking about this i think it was i forget what show it was a couple shows ago where i was just complaining about i want a switch i want a switch to be a switch and dave talks about the same thing and surprisingly that's what you guys are doing yeah we're big fans oh yeah that's why yeah no no i mean i think it's a natural thing though it's like we were talking about natural user interfaces we i mean especially because when you're trying to sell a high-end higher-end product not high-end but higher-end product you're going to be selling to people that are mature have money yeah probably not 20 year olds are going to be 50 year olds that are used to that grew up with switches well the uk

**Omer Kilic:** housing market at the moment is ridiculous young people simply do not have the money to buy houses

**Omer Kilic:** right point right yeah right so yeah so that's about knowing what your user actually is exactly but

**Omer Kilic:** that's not the main point the main point is we're designing devices that um when fitted into or retrofitted into an existing house right won't look alien right they will look exactly like they're non-smart counterparts um but we'll have a whole bunch of smarts inside right and the kind of mobile and web app approach we're taking is we have our in-house design team we're doing all these ux studies our entire office is covered in you know ux studies at the moment um and really we want to design stuff that we want to use as engineers right and people may be scoffing but i think that actually

**Omer Kilic:** is more important obviously i'm more on the website now too i understand a little bit more about it it's more important than people actually give it credit for yeah and especially when you start talking about consumer level stuff because this is what it's ultimately going for yeah i i kind of

**Omer Kilic:** there was a bit of a snuff earlier with my statement when i said we as engineers want to use these things that we we want to we don't want you know engineers to look at it and say oh i can do all these different things with it that's not our primary selling point our main selling point is that we're designing basic user interfaces uh with very advanced tech behind it and creating beautiful relationships between different devices intuitive stuff right intuitive is the word we're looking for i guess so if you look at the ideal iot environment everything should blend in right the whole ubiquitous yeah yeah computer whatever so and the most important thing of course is that um your plug sockets or socket outlets um should be able to talk in a meaningful context with your say fire alarm or your light switches should be able to detect that something's going on in your house and perhaps turn things on right so that you don't stumble and hit your toes and yeah right intelligent devices because that's probably a better term for i guess anyways right i guess the the underlying point is that interoperability is very very important right and in in the iot world that's one thing that we are doing a terrible

**Omer Kilic:** job as as as an industry right because everything kind of goes for flash and like oh look at this whiz bang one thing yeah and and i blame marketing folks for this because i think it's the case that

**Omer Kilic:** engineers want things to talk to each other and it's not it's not really a technical challenge most of the time right of course there are different communication standards different wireless standards and all that stuff but you know if and we also like it's just a battle of hubs in houses these days yeah so like you have zigbee hub you have a wi-fi hub you have like some weird 433 or 844 i can't remember the u.s frequency like ism frequency um so yes that is a problem but at the same time it's more of a the larger problem that we need to solve is the companies should stop saying okay like we'll just create another walled garden or yeah we'll just create another alliance with you know all these big names and the problem is there's a beautiful xkcd about this right if you have like 16 standards and if you kind of try to solve this whole problem by setting another standard now we have 17 standards right

**Omer Kilic:** right so um and they're all it's almost like a it's like a pissing contest too where it's like no no me me me my standard and then the hope is just they'll get big enough that then it does become the standard which historically has worked like spi was a motorola thing and then eventually it just

**Omer Kilic:** became a thing you know but at the moment it's it's a case of um a lot of these um sizable companies saying come integrate with us no one's having the okay what can we do to integrate with others conversation right the actual internet there are only a couple of there and as a small startup right obviously we don't we're not the big names that establish these you know alliances you know these grand your names that actually don't mean anything um there are only a handful of sensible partnership programs out there um right uh but at the end of the day apple will do their own thing google nest will do their own thing and so on so right um the interoperability and the integration between different ecosystems is the biggest challenge in iot um and it's it's tough especially for a company of our size um we going forward we're probably going to have to dedicate serious resources or even a dedicated team of people to handle all the integration scenarios yeah it's like a business development

**Omer Kilic:** type thing where you like you have to go and talk to google and it's a matter of it's not again it's

**Omer Kilic:** not a technical challenge right you could put enough manpower to write adapters and all that stuff but at the same time which alliance should you be you know joining which which faction should you be right it's it's like your side it's it's it's painful but it's the biggest challenge at the moment i mean there's i'm going to give a talk about this uh at nmi and at an nmi meeting in the next couple of months there's this is the nmi a national microelectronics institute it's uh it's it's a joint event by british computing society open source hardware user group and the national microelectronics institute and and and the and the theme of the of the talk is open source is great i i'm a true believer in open source and i can't wait to open source some of the stuff that we are developing here once we actually get to the point that we're happy with them and also we clear all legal stuff etc um but at the same time open source is a is a is potentially a poison as well so open source is a great enabler for iot greatness and mediocrity right so there's this so okay here's the thing there's there's a there's a wrong kind of openness that these whole align let's set up a new alliance kind of you know uh approach is creating so what they're saying is okay we're going to be open we're going to you know give you access to our protocols and specifications and stuff which is great but at the same time you really should have used some other open source or open protocol or open you know approach to the problem rather than inventing your own right um and this is not a very popular i've had very many discussions about this not people so some people actually think that this is a dumb argument but i i'm i strongly believe that there's like a right kind of openness to approaching a problem and the you know the wrong kind of open sure yeah um but this is this is a bit like the previous discussion we were having right for for i'm going to name it up for qualcomm to join like you know some other ecosystem that doesn't make business sense for them right right they need to provide the whole thing as a solution to sell to their folks and what is this driven by their marketing team so while the engineers at heart they might want to be open and like you know have this amazing you know idealistic view of iot where everything is talking to each other it's a marketing decision to brand and try and sell that as a solution right yep so it's a big challenge iot is for it to make sense we're gonna have to work a lot harder in the integration standpoint

**Omer Kilic:** interesting so how did this all start i mean what is what is the story behind the company too so obviously we're talking about some of the realities of pushing it forward but where did it start so

**Omer Kilic:** yasser our founder um had this brilliant idea when he was he was still a teenager he was at school um and he he put together this mock-up uh this proof of concept rig and with that he was able to raise a substantial amount of initial seed funding to put together the team um i know yasser through previous contacts previous connections and i um for me i've i've given presentations about how iot is great and how iot is terrible and i have a love and hate relationship with it right so i want it we all do i mean yeah i mean i want it to work but we really don't need any wine bottles with touchscreens on

**Omer Kilic:** them right so maybe we do is that the new one no no no i like that that exists no i know i i know what it is uh because that was a yc company wasn't it i wouldn't be surprised i think it was um okay so that

**Omer Kilic:** that was a direct attack i feel bad about it but let's let's let's look at another we can bleep it out

**Omer Kilic:** maybe you know i don't know let's keep it bad about the bleep with the touchscreen on it no i think you're right enough that yeah no i think you're right about that though the point is

**Omer Kilic:** there are some amazing applications of iot right especially if you look at the health care you know bringing services to um you know remote communities you know sensor networks these are great applications but at the same time you know is it a tumblr that let's put a chip in it is it i don't know yeah there's there's a beautiful blog okay like let's put a chip basically yeah it's something along the lines of that and there's also a beautiful twitter account called internet of leaps yeah yeah you can say it can we okay internet of shit it's great whoever's running it oh yeah my house that was the

**Omer Kilic:** one that you did today that there was no no no no no no no no no no no no no no no is that is that is that coming next yeah we can get that next yeah so that was in reference to uh 94 percent of developers 94 98 something like that said that they would be using javascript as their main programming language for iot devices let me finish the den story and we'll get to

**Omer Kilic:** javascript so yeah he also had this brilliant idea uh he put together the initial team and even our initial hiring process was all you know let's hire a ui ux person to be in-house first you know let let them drive the whole application design as opposed to just engineers putting together this

**Omer Kilic:** kind of tech demo looking thing yeah thinking about it holistically so you're having other pieces yeah so

**Omer Kilic:** i mean i absolutely love what some other engineers have done in this field and you know i'm not dissing the technology one bit but you know we decided to approach it from a different perspective and um now we have um firmware in-house industrial design in-house mobile slash cloud um we interface with a partner for our cloud services um but you know we do the modeling etc on their systems uh we have our ui ux person in-house and for a short amount of time we actually have an rf designer rf engineer a buddy of mine who had recently finished his phd um joined us to help us with some um antenna issues because as a digital engineer i do not understand antenna design i don't either

**Omer Kilic:** i think that's its own yeah antennas are i won't say black magic but they are definitely their own thing and like we talked about like when you're starting to do regulation type stuff too that's super

**Omer Kilic:** important to make sure you get it right the first time yeah and also we're designing in-wall devices right so um it's it's it's a nightmare yeah i'm not it's not it's not a nightmare it's perfectly doable and we will do it but it's a it's not an easy sort of design challenge it is a design challenge and you can appreciate there's a lot of stuff in it so we should have a lot of metal behind an antenna yeah guess what happens it's like a ground plane exactly so um that's why we have uh someone helping us and this this goes with the previous point i was making right as a start as a hardware startup especially just like identify and accept your weaknesses and get help yeah speaking of

**Omer Kilic:** weaknesses i have done a bad job as a uh as a podcaster here what are you guys making we haven't so we're now 40 ish minutes in what are we oh wow so what what is the actual device that you're

**Omer Kilic:** started out as we're we're starting off with uh plug sockets for our us listeners and socket outlets for our uk listeners um devices that you plug appliances into right um and uh light switches okay but we also identified that just having a light switch and a plug socket is not going to be enough so we're experimenting with a remote um we envisage most of the interaction going to mobile apps because everything does these days and everyone has mobile phones but for certain cases where for instance one use case will be extending you know uh an on and off switch on a lamp for

**Omer Kilic:** a less abled person oh sure you kind of put like a touch pad on a chair we're very against touch pads

**Omer Kilic:** we like tactile tactile feedback and tactile buttons that's why we reinvented the whole mechanism in which

**Omer Kilic:** we can uh actuate things but so we should also mention too with so with the uk sockets or whatever

**Omer Kilic:** you call them so one thing that's different between uk and us sockets is that in uk all of our uh socket outlets are actually our plex sockets are switched right so we have you can individually turn off so

**Omer Kilic:** like you have your lamp plugged into the wall you could turn it off at the wall yeah so there's a

**Omer Kilic:** rocker switch in there that you can turn on and off which is great um us the us you have you basically

**Omer Kilic:** have to have it at each um usually in the wall junction yeah and so that can actually control

**Omer Kilic:** multiple multiple plugs in a room yeah um and our and our light switches look a little bit different than their us counterparts as well that's right yeah right um so we're starting with the uk market um that's where we are where we're based and um soon after in the very in the very near future we'll be starting our explorations into other markets us being the first one as well yeah but it's a challenge because it's a different paradigm um sure yeah so it's going to be a mainly a marketing challenge and after that a massive engineering challenge because the way the us sockets are made the back boxes and the modular plugs etc it's very different so right i'm really looking forward to it yeah that's

**Omer Kilic:** going to be well i think yeah for me from a space concern so i i'm kind of been traveling around sampling all these different as in germany they have the the two-prong circular and all the yeah and uh everything just seems bigger here too right so the us one is definitely like a junction box in the us is pretty tight yeah so that's going to be a hell of a challenge yeah we have an entire box of

**Omer Kilic:** uh us products that we brought along many trips um nice and it's it's a it's definitely a challenge but

**Omer Kilic:** you do like challenges yeah so uh okay so that's going to be good uh so then that's connected so each one's individual so the one thing i like about the uk stuff is that because you have the safety turn off at each switch yeah that means you can basically individually control each each plug yeah which is

**Omer Kilic:** great so in terms of smartness um we're adding power consumption monitoring per appliance or per socket outlet and also plug identification as well so one approach to identification is um just labeling things but people unplug things and plug them elsewhere and what you labeled your hair dryer now becomes an iphone charger right so we have we're working on a bit more uh we're working on a technology that's a bit more smarter than that so um and it's and to support all this we're exploring other sensors that we can integrate with our ecosystem um and yeah that's that's pretty much it um that's good so then does that so you

**Omer Kilic:** mentioned that it talks to apps and stuff like that um is it just our straight rf or is it like a why each one's wi-fi connected um details tbd gotcha okay so some kind of communication mechanism but not necessarily we can't talk about where it's connecting right now yeah we're kind of in the middle of a kind

**Omer Kilic:** of a marketing launch for a new website and stuff we'll be announcing this very soon on our website okay that's fine but one thing that's extremely crucial for us and i think this deserves to be mentioned is that um we'll ensure that even if the internet's offline you can turn on your light

**Omer Kilic:** switches right right well that's and that's ultimately what it comes down to right so like all of these things it's like so we're talking about natural stuff i don't want to have to find my remote i don't have to find my smartphone yeah i don't want to have to do anything different than the

**Omer Kilic:** normal go up and push a button and it turns on so that's what we're aiming for i mean i really want to believe in iot i think i mean it's it's somewhat clear now that i i want to believe well you're

**Omer Kilic:** working in a company that's in the space and we're making it uh we're making it better and we truly

**Omer Kilic:** believe that and this is not my marketing side speaking this is like pure engineering joy when we receive prototypes and they kind of reflect the ideas that we had i mean you don't do hardware you know this feeling right yeah when you receive prototypes and everything fits together and it works exactly and you can appreciate like in a in a like a wall socket there are a lot of components of course so

**Omer Kilic:** um we should mention that too so that's another interesting thing is that um a lot of people go external from this because uh basically you guys are recreating a wall yeah uh socket these are in world devices um right so you're not using existing hardware like i think a lot of people would say oh well i'll put a relay in line with the power or something like that you guys are rebuilding the

**Omer Kilic:** actual thing if you go to shenzhen you can just buy um a plug-in adapter with wi-fi and a relay built in for not a lot of money and a lot of products that are you know effectively plug-in devices are derivations of that you know design i mean we could have gone for the easy option and just rebadged or re-id the entire thing and then just do the software layer yeah but if you think about it you know it has its users i have used them in the past um in fact i still have one turning things on and off um at my parents place but i mean it does look goofy if you if you were to retrofit your entire house with all these things that are just sticking out of the wall they get knocked off um and really again the software becomes a burden because again the nature of rebadging something you just take their software and reskin it right right and it's it's a real problem it's right so if you have you're thinking of that from the user level that's not quite great we're not going for the easiest option we're definitely going for the hardest option but we believe that it is necessary um we're of course you know standing on the shoulders of giants right we're not reinventing the wheel we're using open source technologies um you know some of the designs um when we actually publish more information you know you you'll be able to guess what technologies we use and kind of stuff and we buy when we just tear it apart too yeah that also works um i'll put a little easter egg in there for you cool little shout out okay yeah that's good

**Omer Kilic:** can you make it so that when when i open it up and there's like a pcb in there it says

**Omer Kilic:** this pcb made with chip runner or something like that well here's the thing as as a hacker myself i i thoroughly want this to be very open but it's very difficult for a mass market product to have um you know to be like to to have like to please the hackers yeah and be a viable consumer product at the same time right so an example right i i would like to open up the api to the devices on the device level and give everyone access to everything but guess what you know a couple of people will do it a couple of people will enjoy using it but most people will brick it right potentially right right and the six person team can't support that exactly and building the support network and the rma process for in wall you know live devices yeah yeah it's it's kind of difficult so um so i break my device and

**Omer Kilic:** then i destroyed my wall trying to get it out of there so can you think about a scenario where if you

**Omer Kilic:** were to like allow access to all the facilities of the device a malicious competitor let's say let's make it more sinister release the dodgy firmware update that bricked all our devices yeah yeah i mean that that would be am i being too paranoid but you see the point that's pretty paranoid but i

**Omer Kilic:** think it's uh if if it got big enough i mean there there are stakes i guess yeah so let's like discount

**Omer Kilic:** the whole you know competition being sinister fact but it's a very real risk that if you allow people to tinker with things they can get the devices to do things that are potentially dangerous right well

**Omer Kilic:** especially because it's playing with power right that's another thing so you guys i mean that that is a big accepting factor is that you are designing devices that can literally kill someone that's why you have to go through approvals and all that other stuff and yeah i mean that's stressful what we're

**Omer Kilic:** developing right now is surely not going to be what we're producing when we get to volume stage it's going to have to go through several external design reviews and then ultimately go through all the regulatory approvals and that's when we'll be happy and what is regulatory here in uk what's that like uh we have a body growing body called uh british standards um and there's a whole bunch of different standards that we'll have to get through i'll send you a list if you're interested sure yeah um so again to the point while i want this whole system to be very hackable uh and you know interoperability being one of the key selling points that we will use we still need to maintain a certain level of control um and simply for the safety of the devices and safety of the people more importantly right

**Omer Kilic:** right so yeah i think that especially like a consumer level device like this it's in the name right it's going to be mostly consumers yeah and and then even the people that are that decide to dig into it will

**Omer Kilic:** probably be from the the developer side the details are being ironed out and worked on at the moment but we'll definitely have a way where people can integrate with our devices details of which i don't know to be perfectly honest but again we we we're not just using interoperability as a buzzword we'd like this to work yeah and i i wish i truly wish that more you know people had this kind of mindset or this approach because then the lives of you know smaller companies like us will be much easier right because like how many ecosystems can you realistically partner up with right you need to you know and at launch especially like you're not going to have the resources to do everything and you know the devices you're developing you need to kind of decide on you know one standard to use and if that aligns with most of the standards that's great but it doesn't most of the time so anyway interoperability is a major major problem and i think this is like the sixth or seventh time that i've like touched on this on this podcast but

**Omer Kilic:** it's in three right no no i agree i mean i think that's the problem is that like that's the reason that it's been such a big deal so far anyways is that it's so such a vertical process where you need the mechanical you need it to be safe you need it to be you know rf connected you need it to have the firmware you need it to have the software you need to have the cloud level stuff like that is the problem yep and now you guys are trying to do with a small team so well we like hard challenges so yeah well good because you sure as hell signed up for one uh okay so uh so you said there's uh you'll send me the standards um that kind of stuff let's talk about the the that internet of shit tweet that we were so so right now if someone wanted to write um an app level stuff for your for your thing how did how would that even go i mean obviously it's not it's not there yet but

**Omer Kilic:** uh you mean if someone wants to integrate with our stuff yeah i mean well like it will be think about all the other kind of respectable ecosystems it will be on an api level right okay um so it whether it happens on the local network level or cloud level we ideally want it to happen on the local level but then there are challenges associated with that so that we're working on that but i i'm not gonna i'm not just gonna give people a c++ sdk and let them write code it's gonna be a process where they can pick whatever language they want and they use so the the whole javascript thing i i'm i'm i'm perfectly okay with javascript but i do i do get a kick out of people talking about embedded javascript running on microcontrollers and those things being deployed in commercial applications right i don't think that is the right approach to you know developing products because in especially not because it's javascript any dynamic language anything that runs in a vm it's ultimately going to be more difficult to prove and like test and yeah you know i'm sure i'm going to get a lot of hate for this and people are going to point me at all the like testing unit testing toolkits and frameworks and stuff but i i strongly think that

**Omer Kilic:** like i mean even from a responsiveness uh a responsiveness standpoint well the vm folks have it easy

**Omer Kilic:** we're getting faster and faster processes right um so um but i don't know i think firmware should be but and also i'm i'm not of this school but there's a school of thought that you know it goes by the belief that like maybe we should let embedded engineers write embedded code and you know it's it's kind of a i don't really want to be sided with that but that's that's that's that has been mentioned once or twice in hardware circles as well but then again most hardware people can be quite

**Omer Kilic:** bitter about things so yes i do uh well i think the only the only argument i would say for you guys is that uh the only the only advantage you have in this situation is that you're at a power source right and uh most devices don't have that if they're battery powered then these kind of high-level languages are just not the right answer because of the amount of battery they take true but that's

**Omer Kilic:** you know not what the belief that most people have with the whole javascript argument which is crazy

**Omer Kilic:** well that's fine but batteries are not cheap and i don't like i don't like lugging around my extra

**Omer Kilic:** battery you know yeah i mean what use the tool that's best suited for the job right right and to

**Omer Kilic:** me at least stated on this program once before yeah to me at least javascript for battery powered

**Omer Kilic:** devices is not the right answer yeah don't get me wrong i i prototype with a lot of like lua vms and you know python and stuff i love that because it allows me to really quickly churn out prototypes and proof of concept and stuff but when when i for product that i am designing and ultimately will be producing more than five off i i would like to do it a bit more properly gotcha so you guys are going to be

**Omer Kilic:** you'll have an api level thing but um so basically i mean it's going to be the same kind of thing that your your your app developers are working with is that the idea um maybe not necessarily the same

**Omer Kilic:** thing uh it probably there will be a huge overlap between those things um but things like the firmware upgrades i mentioned it might be we probably won't allow people to put arbitrary firmware in our devices which is a totally justified view right if you want to if you want to avoid the warranty and do your own thing you're on your own you probably can stick you know whatever debug interface we end up using on our boards and just desolder the spi flash and put your own stuff in there yeah and i'm perfectly happy with that but again you know then it it's not in our control what people do with the devices right

**Omer Kilic:** again because from a safety perspective you have to kind of yeah it will be there will be loads of

**Omer Kilic:** disclaimers about it warning signs stickers you know embossed casing you know markings and all that stuff because we have to it's it's safety of our users is of paramount importance right so and it actually scares me because these are once again you know it sounds like your name is on the uh

**Omer Kilic:** the the the corporation paperwork too so that means at a certain point you're actually liable right uh

**Omer Kilic:** yeah so this is why you know we're definitely going through external design review and very rigid like process of um you know compliance testing and regulatory approvals and stuff so in that vein um we've been recently uh starting to you know set up our product life cycle management and associated with our quality management um you know these are the sort of things that most startups really don't need or have to deal with don't think about in general right yeah so but because of the um kind of oh you

**Omer Kilic:** mean the documentation standpoint because when you get to yeah because regulation is such a super big

**Omer Kilic:** piece of documentation so you have to take these things very seriously um right how's that going is it okay these things are generally very expensive bits of software oh yeah well and i think that i mean ultimately it's uh yeah that's it's necessary evil i've accepted that and um it's it's unfortunately when you're running full steam ahead with prototyping and when you again have such a small team documentation and business process and you know documentation these these kind of things do take

**Omer Kilic:** a huge chunk of your right you know day um but you at least looked at the system and you said this is going it's either an annoyance and an issue now or a huge deal later right if we try to deal with this

**Omer Kilic:** right before we're about to press the button to order some units we're in trouble a that's not the right approach and b we're not going to be able to do that because the whole point of traceability and the whole point of the quality management and the product life cycle management is that you start at the beginning um this this goes to our kind of cad libraries ecad mcad libraries and all that stuff as well so um it's it's it's taking a lot of time i'm not gonna lie but if you're dealing with critical you know safety kind of constraints yeah i feel like we at least have the obligation to do so

**Omer Kilic:** well that's good i mean it's really i mean really it's really good that you're thinking about that stuff up front because um you know i i always wondered like because you know uh there was the wink stuff yeah um from quirky and like they were just churning stuff out yeah and that was the piece that i always wondered about because a lot of them were very power-based and stuff like that i'm just what how do you even do that you know like there's just so much overhead there it is um and there is

**Omer Kilic:** and so this goes back to what we're kind of quickly discussing in the pub last night right so becoming a pro maker versus going into the realms of like big boy manufacturing kind of thing right so this is not something you generally need to do um if you're producing like a battery powered you

**Omer Kilic:** know wireless remote or something right a sensor connected to a bluetooth module ideally you should

**Omer Kilic:** because ultimately it will make your life easy but like you don't have to but when you're dealing with like live power and people in sort of interacting with it um it's kind of a different story but then you know there's there has been a lot of um press and even books written about this whole pro maker thing right how do you go about prototyping to production and you're you're involved in this as well um but the whole i feel like there's always that step in the between though where it's like

**Omer Kilic:** well you do this and this and this and you need to raise this money and you need all this other stuff and then the unstated step is hire someone yeah you know um have someone redesign your product

**Omer Kilic:** not just that but if you think about the manufacturing side of things right sourcing components i'm very familiar with this yes yes um i was just using your tools today but that takes an incredible amount of time just on your part yeah in a previous life i had the luxury of you know pinging someone saying critical parameters d's can you give me a part and a couple of days later i had the cad libraries ready and everything right exactly but yeah i don't have that luxury now so right um step one become a big huge business yeah so no one really focuses on the uh there's a lot of like there's a lot of again you know books articles blog posts twitter streams you know about how you can launch a product on kickstarter how you can you know put together whatever but data packs um standardized bombs you know um what does actually a manufacturing team look like right what sort of resources you need what sort of steps you need to go through what sort of product development what are the standardized or accepted like product development categories and manufacturing and you know what are what are the etiquettes of dealing with you know cems and you know sems and all that kind of stuff it's it's folklore um you don't get taught this at school um it's a huge learning process and well i'm hoping that people have written the initial series of books will focus on that as

**Omer Kilic:** their next projects maybe yeah i think i mean there is some good stuff out i mean like the bolt folks and like you know the people that are honestly it's very china focused i think yeah and uh that's good and bad i think that the interesting thing is when people are like oh i don't or can't do that um yeah you know and it's like oh well that might not apply anymore then but there is some general stuff

**Omer Kilic:** no true and this is by no means again you know dissing the work the great work that people have put together in this field but um the whole china discussion is another interesting point right um people some people have the belief that oh like volume china volume equals china that that's not necessarily true um you know through our exploration we've actually identified great manufacturing partners in europe in western europe and yeah you know china means that you have like if you don't have a dedicated uh chinese speaking person on the ground on the ground this is very important yep um you're not going to be able to pull things off if you don't have like prior manufacturing experience even if you have prior manufacturing experience but like arguably if you don't have a man on the ground things are

**Omer Kilic:** going to be a mess yep so um well if it means if you don't have a person on the ground that you will

**Omer Kilic:** probably be that person as a hardware yeah exactly but then if you're also uh you know if you have other duties that you have to attend to it's things are going to take a beating you're going to take a beating ultimately right right right um and like time zone differences and you know 12 13 hour flights actually do matter when things are you know when um shit hits the fan for lack of a better word yeah

**Omer Kilic:** and i think the main point being that china isn't always the answer sometimes it is yeah absolutely and if you're with a partner that already works there that's great but it's just not always the answer and

**Omer Kilic:** also things work differently in china there's there's a different handshake in china um and you need to be aware of these things i mean part of my explorations into visiting china factories and talking to people that do things over there some very exciting things in fact is trying to understand you know the cultures the culture difference and you know how things are run there it's very different to you know a standard like western cem receiving data pack whatever right and unfortunately there's a there's a real risk of you know your ip being you know sure kind of leaked or whatever or you know literally taken to another factory and being produced side by side as well or in the same factory at night right that might that might happen too so um like if if i may you know to any young um budding hardware folks you know volume doesn't equal or manufacturing doesn't equal to china most of the time you know you are probably going to have a better luck uh with a local enough manufacturing partner that is willing to take on a small startup and hold your hand through the process because it's never just a case of uh yeah here's my board files yeah right um think about it right if you're prototyping an idea what you do you do you go to osh park um i'll very happily endorse osh park they're amazing um and uh you'll order some boards you know six boards multiples of three yes um and you'll order some parts from digi key funnel whatever you'll solder them together or you might even choose to use one of the like the quick prototyping services and have assembled boards yeah but then um when you're working with a cem you never just send them a gerber and just a like a half-assed list of components right right right whatever you have for a 10k yeah right yeah so that doesn't work like that but unfortunately again like you need to educate yourself before you reach that point or well the education is different depending on which cem you go to oh definitely um everyone has a different way of dealing with things this is another reason why we wanted to formalize our plm process right because if we can like have a repeatable data pack generation environment that's someone should trademark that you just did i don't want to um so anyway

**Omer Kilic:** the point you mean like a standardized output though exactly if you have a standardized output and if

**Omer Kilic:** you can manage our engineering correction notices in one place and everything is just in one place

**Omer Kilic:** it will make a life-easy you're front-loading all of the shitty stuff that you have to deal with

**Omer Kilic:** eventually yeah right um so what i'm trying to say is you might actually have better luck uh succeeding in whatever whatever you're trying to do with regards to manufacturing with a local partner because especially if you're producing you know a lot of something even logistics becomes an issue right you know what are you going to do with all the things yeah um fulfillment logistics uh and if you if you look at uh wired had a wired uk had an amazing um series of articles uh this month on china and the new generation of chinese companies like xiaomi um like dji um and dji is chinese i didn't know that the drone company yeah i think the the their offices there they have offices every round of round um one quote that stuck with me was when they interviewed xiaomi their model is no inventory like just produce everything ship everything as quickly as possible and maintain minimum minimum inventory right and super lean super lean and this is what you know they they sold a hundred thousand phones in like four

**Omer Kilic:** seconds in india or something like that just yeah it's crazy i think mine is actually uh is that no

**Omer Kilic:** no mine's a huawei i think right yeah um so anyway the point is you'll have much better luck especially if this is the first time you're doing this thing with a local partner then you know just dumping your files in china okay do i come off as really bitter i don't know i don't think so i

**Omer Kilic:** think i mean like i don't think you're saying that like it's a bad experience it's just that you need to measure no matter what you do you need to have your eyes open right i mean like and i think that people that aren't going to have their eyes open are going to screw from the beginning but like it's just a you need to be thoughtful about this stuff yeah and you guys are front-loading a lot of the the because you recognize the regulatory load that's really smart i think um does the regulatory stuff does that

**Omer Kilic:** impact the china decision at all or not not really because ultimately your quality management systems should flag up items that will cause problems in your you know regulatory um oh right okay um they should right yeah if material thicknesses are not what they should be or if the material you know

**Omer Kilic:** qualities are not what they should be are you already speccing a qc plan for all your of all your

**Omer Kilic:** hardware uh we're starting it right now but it's so this is one of those things that we might have to bring someone in as well like qc experts yeah because that's another discipline we don't have a qc person on board yet um we're currently a quick plug and i'm terribly sorry about this like we're currently raising the next round of funds that we'll use to get to the pre-production stages right now right um so that part of that uh funding is going to go into setting up our manufacturing

**Omer Kilic:** efforts right i mean even just initial material cost stuff i mean like you gotta you gotta buy the stuff

**Omer Kilic:** right i mean for for for us uh we're not going to be able to get away with just producing like you know 3000 of one unit right um we have to go yeah we have to go big otherwise you know it's you can again appreciate the complexity of such a device with all these functions and it's it just doesn't make sense for us to be producing only a couple handful hundreds of those things right

**Omer Kilic:** um well and you said so you mentioned that it has like current monitoring inside too and it's like you know removing that doesn't really give you much either right there's so much in the mechanical pieces yeah it's mostly the mechanics yeah so like that's that's what's really interesting about

**Omer Kilic:** it so one thing that generally shocks people who are new to manufacturing is it's not the electronics cost boards are cheap right components are cheap tooling costs for casings right assembly costs testing costs you know testing is an interesting topic as well you know um what you do on your bench you know with your you know adafruit isp programmer does not necessarily you know and that's just at a board

**Omer Kilic:** level too you're now you're talking about assembly testing yeah and i mean probably even power testing right yeah so and you said that uh plugs are a fuse so that is a godsend i suppose well yeah

**Omer Kilic:** yeah that is that is one saving grace but then we need to ensure that an overload condition is not going to damage our power supply for instance so and these things are built into the wall so we need to ensure everything is yeah what's your lifetime you're going to spec on these things tbd but it's it should align well with you know uh what i mean i expect like 10 yearish yeah 10 yearish figure is is what

**Omer Kilic:** we're in that's a really interesting do you have to do uh like failure detection on the firmware side

**Omer Kilic:** too uh yeah there's there's a quite a serious amount of you know diagnostics real-time diagnostics happening in the firmware yeah monitoring things and i forget who's i saw some tweet the other day that

**Omer Kilic:** said i bought a smart light bulb that was specced for 20 years a smart led light bulb that was specced for 20 years but the rf failed after two which i expected so now i just have a i guess my 18 years are it's not a smart light bulb anymore you know and and that's kind of another thing where it's like that's some long that's some long timelines that a lot of people expect right we buy a house you expect the oopsie uh buy a house you expect to knock your beer over uh you buy a house uh you expect all the fixtures are going to work that they're easy yeah we're not designing things that you put in your wall

**Omer Kilic:** you know potentially spend a lot of money just installing them calling an electrician or something

**Omer Kilic:** and then they're dot devices after two years oh because here you actually have to have a electrician install stuff yeah i know dave's talked about that with 220 so like it's it's in the us i shock myself all the time i'm fine but your kettles take too long to boil water oh yeah there's there's the big trade-off that's

**Omer Kilic:** what we really need to be talking about as a kind of british person kettles are a big problem it is

**Omer Kilic:** faster here i will say oh yeah it's shockingly faster yeah uh scary as well yeah so yeah i mean it's qc and

**Omer Kilic:** reliability and these these are things that we take very seriously and you know ultimately we appreciate how difficult some of the things we're doing are um and it's it's only when you start thinking about you know the lifetime of a device that certain things become an issue like you were talking about radios for instance all these things it's just adds up right you know the list of things you need to ensure that like they're they're fine is it's quite long um yeah so yeah fun times at

**Omer Kilic:** then automation offices oh man you're gonna have a hell of a time are you guys uh currently so you

**Omer Kilic:** did a so that was already crowdfunded once is that right so our initial round a seed round was on kick uh on cedars uh our um platform for raising funds so you can't people can't buy these right now so if we

**Omer Kilic:** have uk listeners right now they couldn't go buy one or well yeah our crowdfunding second round of

**Omer Kilic:** crowdfunding campaign is now active we're actually actively raising funds now so uh okay it's a convertible round so um this is by no means a financial advice just go read the page that it's it's the description is there i i'm i'm an engineer i'm a lowly electronics engineer i'm not going to go into finances in this podcast yeah that's fine okay but if people want to get in on this they can yeah yeah yeah but ultimately you know just to recap our kind of um driving um kind of mantra it's just making things kind of beautiful functional and you know ultimately simple that can be integrated into

**Omer Kilic:** other ecosystems and all that stuff okay so now the real question because we were yeah we're hour 15 in um how soon am i going to find out how the little thing switches on or off so the demo i saw again now that we're this far in we should mention more about how the device works it's real it's a little cliffhanger here on the amp part this week uh so i could switch the light on and off right the socket on and off and then i can grab a uh some other device mobile app whatever yeah or remote hit a button mm-hmm and it physically switches yep and you're going to be able to talk about that soonish very soon okay um we have like a reminder on my phone maybe like a month from now i can bug you yeah um

**Omer Kilic:** we'll hack some of the 220 units to work on 110 and send some over your way oh that'd be fun yeah with a huge sheet of disclaimer yeah and a huge rcd stuck to it as well um so we've evaluated quite a few different technologies for the actuator mechanism and last week we uh signed off on the concept that we believe will make into production make it to production at the moment we're still in prototyping stages yeah well super snappy too i

**Omer Kilic:** mean like that yeah and everything looked really so like i said we've talked about it before everything

**Omer Kilic:** looked like i expected it to look after after we're done recording this um we'll give you a quick

**Omer Kilic:** response time demo as well ah good because that's another big piece too right yeah so we've like along the

**Omer Kilic:** way uh the all the um tools that we discussed uh rapid prototyping quick iterations prototypes all along the way uh we've been lucky enough to source all the beautiful development boards that we have these days put together test clusters um to test connectivity um response times range and all these things and um yeah we're we're we do a lot of test driven hardware developments in which we just breadboard everything you know solder up like quick prototypes and um it's it's it's great because you know verification in hardware along the way is um i'm more believer of that kind of concept than just writing a 60 page document right that mandates how things should work but then you know when you get to implementation you might find that actually you can't really do that so um okay nice we're lucky i mean as a hardware engineer i'm i feel blessed almost uh yeah to have access to all these quick prototyping services you know the machines this is the time man it is the time um so i'm very happy well except i'm not so well

**Omer Kilic:** you still have to make us things so the thing that's always stressful that yeah uh is there any last raging we should have about iot this is a term because i was thinking we're going to have some like raging uh we complained about iot i think i think that like we've done well this has been much more like a great discussion about manufacturing in reality yeah we've contained ourselves on that

**Omer Kilic:** iot rage concept i mean at the last open source hardware camp uh in beautiful hebden bridge in west europe last year i gave a talk about you know uh i think the title was iot the great iot hardware kerfuffle um you know people talking about uh you know making things connect to each other and platforms and again it's great to be able to have access to like a flurry of development boards and stuff but there's certain things that are better suited to you know limited range of applications so a battery powered raspberry pi probably not a great idea it can be done how big is the battery yeah exactly it depends on how that's a car battery yeah then you're fine yeah i take that argument back um so it was a it was a talk uh that i ranted quite heavily in the first couple of minutes on um the unnecessary iot applications yeah i believe the bluetooth toilet was mentioned okay yeah um my favorite was the bluetooth toothbrush that enabled a personal brushing journey aha at least two minutes right you could do that with a kitchen timer yes or yeah anyway um so in that in that presentation i did actually discuss like the different kinds of you know or different classes of hardware or processors that we have mainly focusing on the processors and you know what are the weaknesses strengths and you know um um yeah i i think again we've done a very good i think we got it out of our system last night in the pub when you know the discussion on it kind of yeah all great discussions happens in pubs and great product decisions of course yeah uh we've contained ourselves well for this podcast i feel okay

**Omer Kilic:** yeah well if we if we feel the uh the urge to to rant more let's let's take it to twitter like

**Omer Kilic:** let's take listener feedback on how great or how terrible i am am i doing this right i think so yeah

**Omer Kilic:** that's good that's very social of you yeah now now uh the den automation if you complain about iot

**Omer Kilic:** a light turns on somewhere yeah every time you complain about iot deity makes the kitten right

**Omer Kilic:** right right right awesome well hey thanks for being on the show uh thank you very much for having me yeah recommend people check out den automation i think it's going to be i think this is like i said i think this is the best may not be the final answer but it's definitely a step in my direction thank you that means a lot cool thanks for getting on the show awesome thanks for having me
