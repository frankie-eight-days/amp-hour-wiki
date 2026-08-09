---
episode: 661
title: Blogging Electronics with Pallav Aggarwal
url: https://theamphour.com/661-blogging-electronics-with-pallav-aggarwal/
---

**Pallav Aggarwal:** This is The Amp Hour Podcast. Released March 10th, 2024. Episode 661. Blogging Electronics with Pahlav Agarwal.

**Chris Gammell:** Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Pallav Aggarwal:** Hi, my name is Pahlav Agarwal. I am from Kappa Fembedit, Bangalore, India.

**Chris Gammell:** Hey, Pahlav. Yeah, good to meet you. I've been a fan of your blog and your stuff online for a long time, so I'm really glad to be chatting with you.

**Pallav Aggarwal:** Yeah, hi, Chris. Great. Thank you so much for having me.

**Chris Gammell:** Yeah, my pleasure. My pleasure. We are going to be talking, you know, so I've been posting some of your stuff to our subreddit and talking about it on the show once in a while, but I'd love to just get to know you, get to know the stuff that you like working on. The thing that caught my eye when I first started kind of noticing your blog was your series on the CH32 V003, and you kind of go through a lot of the different functions, you get some of the test code up and running, and so that was, you know, one of my big interests in your stuff, and then I just kept seeing all the other stuff you do. You've been pulling cans off of stuff lately, a lot of, like, cell modules, and I'm like, yes, that's me too. I like that stuff. Yeah.

**Pallav Aggarwal:** Yeah, that was very, very old.

**Chris Gammell:** Yeah. How did you get started with the CH32 V003?

**Pallav Aggarwal:** So I think I was looking at CH32 V003 since a couple of months, and then during August timeframe in 2023, I got some time free for a couple of weeks, and then I thought, okay, this is an interesting platform for ultra low-cost, you know, products, and I was already doing teardowns, you know, to figure out how the whole consumer electronic works, and, you know, that really matches my interest, and, you know, I started learning, and then I realized, okay, I'm learning, and I'm keeping the whole learning in my head. What is the point? Right. So let me take some notes and put it on my blog because I don't have a physical notebook. Yeah. My notebook is my blog, so I keep everything over there, and maybe while I'm learning, trying to, you know, keep things simple so that people will also be able to follow, right? Because whenever you are working on a new MCU, it takes a lot of time. It takes a couple of weeks, you know, to, you know, smoothly go from one interface to other, understand the internals, and understand the limitations, et cetera. So, yeah, I did that for various interfaces and, you know, wrote a few blogs and posted them, and I hope it is useful to a few people.

**Chris Gammell:** Yeah. I mean, great for me. I don't care about other people. I just care about me.

**Pallav Aggarwal:** So nice to hear that it is useful for you at least. Yeah.

**Chris Gammell:** Yeah, exactly. Yeah. I did note, so like you actually were going through the IDE as well, the Moon River, Mound River, Moon River, however you say the, that was like the official supported IDE. I ended up doing the CH32V003 fun library, the CN lore we had on the show. Have you had a chance to try out that fun library or are you just sticking in the IDE?

**Pallav Aggarwal:** I did try for a couple of days, but then I went through the, you know, the usual way of engineers to work. You can use the fun library, but the problem is not many people will be able to understand that, right? If you go to bare metal way of working, it's not that easy, right? So I thought, okay, let me take the HAL layer and on top of HAL layer, how we can, let me show how different interfaces can be used with the help of, you know, standard company provided HAL layer. So that was the idea.

**Chris Gammell:** That makes sense. Yeah. And I have seen some stuff, like one thing that is the HAL and the examples from Moon River and just, I think from the WCH as well. I think there's more overall details, but I think they're very specific to the chip versus, I think the fun library also has like external stuff. So I've been playing around with that, the NRF24 interface, which I, that's like a little bit different, but it's, I think it's probably all of the above, right? Then you could see how someone implemented a HAL. You could always write your own HAL if you wanted to, but honestly, I'm just trying to use someone else's work in all the cases. I don't want to do, I don't want to be twiddling bits on the registers. And so I just take advantage of who's.

**Pallav Aggarwal:** I think fun library is really good and highly optimized. And several people are already using that. But I thought, okay, going via HAL would be much better. Maybe in the future, I will also try fun library for some of the projects, right? Because anyway, you have this low cost platform where resources are constrained. You have 16 kilobyte of flash and two kilobyte of RAM. So eventually when you go for, you know, commercial products, then you might need to, you know, optimize.

**Chris Gammell:** Yeah, totally. Totally.

**Pallav Aggarwal:** And I've seen, I've seen HAL is not very optimized and a lot of bugs are also there.

**Chris Gammell:** Got it. Got it. And so in your work, so you have, you know, you do a lot of publishing, you do experimentation on your blog, stuff like that. You're also a consulting engineer. You also do designs for other people or are they mostly for yourself?

**Pallav Aggarwal:** Yeah. So mainly I have a consulting firm, as I mentioned, Capoff Embedded. And we do hardware, custom hardware development, firmware development for any MCU microprocessor on system or system on module. And then we also help companies in design optimization for power consumption, cost, and, you know, mass manufacturing. And we also help companies in test, test automation. So they want to go from prototype to high volume manufacturing. They need to really make sure product is compatible with, you know, high, high volume manufacturing setup, right? You can't have a prototype level board to be manufactured in very high volume setup. So you need to have some prerequisites for that, right? So we try, we try to help companies in test automation, building test automation solution.

**Chris Gammell:** That's great. That's great. And so you're experimenting with the CH32 V003, but you also, you said you do pretty much any chip, but do you have like a kind of a go-to off the shelf in a, in a normal, a normal use case?

**Pallav Aggarwal:** So most of the time we are, you know, driven by what customers have already used or they prefer to, but in several cases, we get a chance to choose which platform we want to. For example, we have used Apollo three microcontroller from a big micro, which is lowest power, lowest power, you know, consuming microcontroller, Apollo three, very Bluetooth,

**Chris Gammell:** Bluetooth chipper, right?

**Pallav Aggarwal:** Exactly.

**Chris Gammell:** Yep.

**Pallav Aggarwal:** Exactly. They have, they have non Bluetooth, you know, NCO also.

**Chris Gammell:** Oh, I didn't know that. Okay. I've always seen it. I know SparkFun uses them for, they had like a SparkFun module that was based on that. Module. Exactly. Right. Right. Okay.

**Pallav Aggarwal:** And now, now they have Apollo four. Oh, interesting. Which is, yeah, which is consuming for microampere per megahertz. Very, very low. It's like 10, it's like 10 times than any other competitor.

**Chris Gammell:** Yeah. That's great. Yeah. It is interesting that they really play in that space. I, I had a friend back in Chicago who was using Ambik stuff and he said, yeah, you know, you're going to pick it as a hardware engineer, but then when the firmware stuff, he was a little underwhelmed by the firmware, like IDE and stuff like that. Was that, is that your experience or is it decent on the website?

**Pallav Aggarwal:** Yeah, exactly. Exactly. I had a very difficult situation because I picked up projects based on Apollo. And then when I started, it was very difficult. And then I figured out, okay, one of their distributors, they were willing to help me. And then, you know, they, you know, I was trying to help, take help from them, how to use different drivers, et cetera. Otherwise it would have been very difficult because support from company is not there, which I understand they can't do, you know, support, you know, low volume customers. But I think till now they were focusing on very high volume, very low number of customers. But I think eventually if they want to grow and they want to, you know, be seen in many more devices than just very high volume products, like variables, they have to, you know, start providing more content, more tutorials, more videos. Yeah.

**Chris Gammell:** Yeah. And I think, I think that's a lot of the big vendors too. Like they're traditionally, they're like very top down push. So like, you know, they'll go into like a wearable, you know, they'll go into like a wearable manufacturer and like sell it at like CTO level. And then they push it down the chain. But these days it feels like so many people are like reading blogs like yours or going to a spark fund or similar, you know, and going bottom up. And if you don't have that, then they're like, well, where are all these new people? Where, how do we get in to the opportunities for the new projects? So I think they're finally wising up to it, but I'm not sure. Yeah. I mean, I don't think they've realized how expensive it can be. Like the software is so expensive to like do good software and projects, you know, it's really tough. I mean,

**Pallav Aggarwal:** at time I was also very frustrated and I was thinking like, you know, did I take a good decision? And, you know, I have created a small article. I mean, a couple of articles on Apollo because I, I thought, okay, there is nothing available online. So let me, let me try to, you know, publish whatever I have learned so far so that, you know, other people can save hundreds of hours.

**Chris Gammell:** Exactly. Yeah. It's like empathy to yourself, your past self, but you're also helping new people too. Right. It's just like, Oh, I wish I would have had this, you know,

**Pallav Aggarwal:** the only reason I'm publishing is because I know hardware development on hardware is very, very hard. And, you know, you can't find these things in books. That's right. Right.

**Chris Gammell:** And if it is, it's like, it's like 6502. It's just stuff that, it's, you know, books are just so old for that kind of thing. So you gotta be on the way.

**Pallav Aggarwal:** Exactly. And not many people are sharing things, right. Very few people are sharing, right. That is also a problem, right. We are, you know, people who are, the number of people who are consuming are, you know, such a large number that we need at least 10 X more people publishing.

**Chris Gammell:** Yeah. I agree. Yeah. And I think the, the incentive isn't there for like a lot of the companies. So like you said with like Ambix or similar, like we're picking on them, but it's not, it's not just them, right. It's like any large, ship company that's selling into, you know, commercial space. It's like the company that's doing that. They're not incentivized to publish about their stuff. Cause it's basically, if not trade secret, it's, you know, just, it might actually be patented or similar, right. Just like on the firmware side, I guess patented is open, but, but like, it's just, there's no incentive to share the guts because that's how they get a competitive advantage over their customers. So then it's like,

**Pallav Aggarwal:** not really. I would say, I would say, uh, if you have a microcontroller, how to use your microcontroller is your responsibility, right? Otherwise how people will be able to use your microcontroller. Sure.

**Chris Gammell:** Oh, Oh, you're saying from the, the chip vendors perspective, but I'm saying like, like if Garmin, right, Garmin isn't like incentivized to publish about how they might use the Ambit or some other part in their product. Right. And that would actually be useful for people like you and me, right? We were like, Oh, Garmin uses it. And also look how they use it. And like, that would be good for the chip maker, but Garmin's not. Yeah.

**Pallav Aggarwal:** I don't think Garmin or any company who is like a product manufacturer will get into, you know, doing such stuff because it doesn't align, align with their work.

**Chris Gammell:** Right. You know where the money is. Content Creation. Yes.

**Pallav Aggarwal:** Yeah.

**Chris Gammell:** People can't see, uh, Pallav's video right now, but he's draped in gold and, uh, you know, he's just looking very fancy right now. No, hardware and firmware engineers. We're known for being very fancy. Yeah. Maybe. Yeah.

**Pallav Aggarwal:** Gold is, uh, nothing but PCBs. New stuff. Yeah, exactly. Yeah. Yeah. Yeah.

**Chris Gammell:** Yeah. Great. So I saw you, you also, so you not only make this content, you're also selling stuff for yourself. And you saw it. I saw, uh, I hadn't seen the site where you're selling stuff before. What was it? Evelta? Evelta.com? That's like where you're selling? Yeah. Yeah.

**Pallav Aggarwal:** So we, yeah, we have, we have created a few products, small, uh, you know, evaluation boards or USB PD, uh, you know, uh, USB PD board, and then ESP 32 programmer. So the reason we created, because we face some problem and then we created these products for our use and then realize that everyone is facing problem. So why can't we have this online available and, you know, sell it to people. Also, this helps us showcase the kind of workmanship we do, right? Otherwise we can't show our customers projects, right? Got it. So we are trying to create some products which are useful for embedded community, which will help embedded community, you know, build products easier and faster. And at the same time, we are also able to showcase our engineering skills and workmanship. Yeah. Right.

**Chris Gammell:** Totally. Yeah. So I noted on the site as well, that the prices are listed in rupees. Are those, these are all like locally produced, locally sold as well.

**Pallav Aggarwal:** Yeah, exactly. So we are manufacturing in India. We are taking help from PCB, manufacturer and assembler in India. And we are trying to do as much as in India. And, you know,

**Chris Gammell:** yeah. Yeah, that's great. I had, I had been working with someone who was in India and I, I was trying to send them a board and they're like, like sometimes like the import duties were tough too. So I feel like having like locally made stuff as well also benefits just from like keeping costs down. Like, you know, you're targeting the CH 32V, right? Which is a low cost line, but then it's like even better for like having locally produced. Cause then it cuts down on imports and stuff like that as well.

**Pallav Aggarwal:** Yeah. For buyer, it is very, you know, convenient because they don't need to go through the custom process, which is very, very painful and unpredictable many times. Right. Because we are doing it, we are buying components, we are buying, you know, a lot of evaluation boards, et cetera. And we face that every now and then. And it's random. Sometimes we are able to get our shipments cleared in seven days. Sometimes it takes seven weeks. Yeah. Right. Right. So yeah, it's,

**Chris Gammell:** as an individual, you might be okay, but it's like, as a business, you're like, I can't, I can't tell my customers that. Right.

**Pallav Aggarwal:** Exactly. Exactly. So we have to be ready once when we are, you know, in a advanced stage of closing a proposal, we just buy some critical stuff. Right. So that's how we, we handle things.

**Chris Gammell:** I think we haven't had a guest on from India, at least in a while. I'm trying to think the last time we did, but can you tell me more about just like the ecosystem there? And like, you know, I, like I said, I've worked with some firmware engineers based out of there before, but they were, they were more on the firmware side, right? They weren't building their own hardware and stuff like that. So what about the hardware building ecosystem where you are?

**Pallav Aggarwal:** So I think a hardware ecosystem is there, but we have some challenges. For example, not many companies are providing all online setups. So you have to send them Gerber files or email and talk and, you know, exceptions will be there. And, you know, sometimes follow-up will be required. So all those kinds of stuff is there. Right. Yeah. But a few companies are there in India as well, where you can just go online on their portal. You can put your Gerber files and you will get a, you know, quote instantly. You can pay and then, you know, process starts. Yeah. So, yeah,

**Chris Gammell:** I mean, ecosystem in that way is like pretty, pretty, pretty dependent on zip files. So like there's some, you know, more modern ones, but I like, I feel like most of them are still like mom and pop shops that have been like, yeah, we've been building boards for 50 years and, you know, there's still like, there's still hand popping a lot of stuff and making boards for some military contractor for like, you know, the past 30 years or something crazy like that. So, yeah. Exactly.

**Pallav Aggarwal:** Exactly. It is, it is little difficult for people who are prototyping, but yeah, you know, we have more than a hundred, for example, manufacturers, PCB manufacturers.

**Chris Gammell:** Oh,

**Pallav Aggarwal:** great. Oh, nice. And a lot of assemblers, but you need to really figure out which, which one is going to work for you from location point of view, from the kind of technology you want to build, all those things. Right.

**Chris Gammell:** Got it. Got it. And then are you sourcing most of your, most of your clients and like the people you're building electronics for, are they mostly India based as well?

**Pallav Aggarwal:** So my clients are mainly from us and Europe mostly.

**Chris Gammell:** Okay.

**Pallav Aggarwal:** And then a couple of them are from India as well.

**Chris Gammell:** Okay. What is, I, again, like, I don't even know, like, so industries in India, what are, what are they often targeting? Is it just like automotive, industrial, similar kind of stuff as here?

**Pallav Aggarwal:** So in India, a lot of, I mean, India is a big country. You have a lot of, a lot of, you know, industries, for example, especially in Bangalore, you know, military segment is big. Defense and military is big. And then automotive is big in Bangalore and Pune region. Right. And then a lot of industrial stuff is going on. So, yeah, I mean, you can think of anything and that is happening in India. Yeah. A lot of, a lot of consumer electronics is happening now. You know, people used to buy everything from outside and, you know, bring it and just, you know, sell it or trade it. But now they have started doing partial, let's say manufacturing or to start with assembly and then getting into, you know, what they can manufacture. Right. Yeah. So trying to do as much as possible in India so that we can, you know, improve the ecosystem.

**Chris Gammell:** Yeah, no, that's, that's the best thing. And one thing I have noticed, I was just looking on the, the Zephyr meetups the other day and there was like a couple of Zephyr meetups and they're just like super well attended and like, seems like just vibrant ecosystem as well for like firmware, hardware, that stuff kind of stuff. So that's, that's really reassuring. Yeah. Growth of growth of the ecosystem. That's what we want to see more of, you know?

**Pallav Aggarwal:** Exactly. I mean, a lot of incubators are there and then makerspaces are there in India where, you know, a lot of help is available. So I think we are growing and, you know, our ecosystem is becoming more strong. So I think next 20, 30 years, we are going to be, as a country, we are going to be spending more of our power and energy into manufacturing.

**Chris Gammell:** Yeah. That's great. Yeah. I mean, like just, you think about all the, all the industries that are moving aside from stupid AI, that seems to be hitting the headlines all the time, you know, aside from like, you know, just pure compute type stuff, like all the, all the climate change type activities and new automotive, new industrial type stuff. Just, yeah, a lot of it requires a lot of, a lot more atoms than bits, you know? And so that's where folks like you and I come in, hopefully. Yep. Yeah. That's great. That's great.

**Pallav Aggarwal:** Yeah.

**Chris Gammell:** Yeah. So I did notice as well, like I said, I noticed your, your cellular stuff, like how you're kind of digging under the cans and, and photographing and things like that. I thought that was really interesting. What is the, what's the cellular like IOT ecosystem like, like in India?

**Pallav Aggarwal:** So if you're talking about cellular, inter, uh, cellular connectivity, I think very popular are Simcom, Quictel. Okay. They are very popular. Yep. Right. Okay. And then, uh, other platforms are also there. For example, now Kevly is coming. Uh, and then, I don't know that one. What's that one? Kevly wireless.

**Chris Gammell:** Kevly wireless. They are,

**Pallav Aggarwal:** C-A-V-L-I. Yeah. They are basically manufacturing in India, their modules. Okay. And then a lot of other companies are also there. For example, NeoWay is there. And then, you know, other, uh, Chinese companies are there. For example, Tellit is there, right? Yeah. Yeah. Yeah. But most popular ones are Simcom and Quictel. Then when you need performance, Ublox comes into the picture.

**Chris Gammell:** Okay. Yeah. Once you're ready to pay through the nose. Exactly. Yeah. Those are not, those are not cheap. Those are my, I have a bunch of those like laying around from an old build and I'm like, I should sell these on the secondary market, but I don't know how to sell them. You know, they're like, and they're pretty old. They've not been very well taken care of in my, you know, in a bucket in my shelf. Uh, but I know that they were like worth a lot, you know? Yeah, exactly.

**Pallav Aggarwal:** Exactly. I have used Ublox in a couple of projects where, you know, performance was the only criteria, you know, for example, I did, uh, you know, uh, personal tracker where the, the, the ask was single charge six months. It should work. Okay. Right. Nice. With, within a, you know, constrained. Reasonable size battery as well. Not like a, not like a car battery or something like that. Exactly. It's a pendant pendant, like a system. Okay.

**Chris Gammell:** So like a life alert stuff, I guess I just say like life, life alert, you know, that reference, that was always a thing in the, in the U S yeah,

**Pallav Aggarwal:** it was like,

**Chris Gammell:** uh, there was a commercial in the U S where it was like an older lady. And, uh, and then she had a life alert pendant on, which would like call, this is like way before cellular stuff was more ubiquitous as well. So it was like, it was like a radio technology, but the thing was like, I fallen and I can't get up. So it was like lamb, like it was always like, lampooned in different like contexts, you know, like I fallen and I can't get up. You know, it was just always like used in other jokes and stuff like that. Even though it was a very serious service.

**Pallav Aggarwal:** I thought you have to press every five minutes to tell that I'm alive. I'm alive. Yeah,

**Chris Gammell:** there you go. Yeah, exactly. Yeah. The keep a life signal. Yeah. That's usually more of an electronics thing, I guess. Right. Yeah.

**Pallav Aggarwal:** Yeah. So you blocks is also, yeah, one of the platforms people are using, but I think as per my experience and understanding, quick tell and simcom are the ones which are getting used to most, most of the projects. That's great. That's great.

**Chris Gammell:** So you, you had mentioned, you know, you kept saying we for cap of is how big, how big is your consulting group? Is it like, just you and then you kind of subcontract or is it a set group of people?

**Pallav Aggarwal:** So we have a few people on board and then, you know, we work as a team. We have more than five people now. And we also hire people on contract based on, you know, if we are missing on some skillset, some gap is there for a project, right. Then we hire people on contract as well.

**Chris Gammell:** Yeah. That's great for being able to scale up. And yeah, I mean like you just never know how jobs come in. Are you, are you seeking out the new business or are you, are you more leading the teams and stuff like that?

**Pallav Aggarwal:** Yeah. Yeah, exactly. So we are, we are expanding our team. We are hiring more people. And then we are also looking for more customers where we can, you know, work on pipeline of project, right. So we currently, our association is with the companies who have, you know, project one after the other so that we are involved, you know, in a long-term way rather than just one off project. That is also our focus. We want to associate with companies who want to, you know, work on long-term, right. Who will see us as.

**Chris Gammell:** Recurring business, lots of boards, that sort of thing. Like team extension, that kind of thing. Exactly.

**Pallav Aggarwal:** Exactly. We become their extended R and D team members and we work, you know, strategically with them. We help them, you know, generate ideas, right. You know, a lot of, a lot of times you need people from outside industry to help you give, you know, out of the box solutions, right. Because you are biased because you have spent 20 years in the industry. Exactly.

**Chris Gammell:** Yeah. It is interesting when people come from like a non, maybe a technical space, but maybe even like someone who's like a mechanical engineer, but then they're like, well, I need to, you know, I'm making this e-bike or something like that. And I want to just see where it's going throughout town or something like that. They're focused on the mechanics and the building of the bikes and maybe there's electric system, but then they want to like really ramp it up and make it like a smart system or add new capabilities to it. And then you can kind of add, Hey, I know about electronics, but then you know about the space. Exactly. Exactly.

**Pallav Aggarwal:** That's great.

**Chris Gammell:** That's great. How, how are people often finding you content or some other way?

**Pallav Aggarwal:** So basically we have done previous work in past years, so they are able to find via references. So most of the projects are coming via references or sometimes via content.

**Chris Gammell:** That's great. Yeah. That kind of thing is, it's nice to have people find you while they're, while you're sleeping, right? It's just like,

**Pallav Aggarwal:** you have not yet started outbound.

**Chris Gammell:** Okay. Yeah. Yeah. I mean, that's its own thing too. I feel like that's, that's mostly just handing Google your wallet and being like, uh, try and find me anyone. And it doesn't always work out super great.

**Pallav Aggarwal:** Yeah. I think, uh, that way I'm quite lucky that people are able to find me. And, you know, they are able to contact.

**Chris Gammell:** And I think that that is the investment of content though. Right. I just think exactly. You know, I have people that have talked to me about like, you know, like, Hey, I'm a new, I'm a new consulting engineer. I want to like find some work, whatever. Like, should I make content? And my thing is like, yeah, you should, but also like, don't expect it to work for six months. Right. You have to just keep doing it without the promise of it. Like, it's not like one blog post leads to one client, unfortunately. Exactly. So when,

**Pallav Aggarwal:** yeah, exactly. When I started in 2017, I started, you know, blogging in 2017 when I started writing, it was medium, not even my website.

**Pallav Aggarwal:** Right. Yeah. Yeah.

**Pallav Aggarwal:** And for two years, not many people were, you know, reading my blogs and I knew that it will take time. And, you know, even if 10 people are reading, I was like, okay, it's worth it. Let's do it.

**Chris Gammell:** That's basically the, the thing that's keeping the power going. Like one person contacts me and they're like, reach out and like, Hey, I listened to the show. I'm like, yes, keep going. Exactly. I'll have another five years. There we go. It feels great also,

**Pallav Aggarwal:** you know, when people contact you and, you know, appreciate the content we are generating. It's great to hear from other people, you know, they are able to get some help and, you know, from the content I'm producing. Yeah.

**Chris Gammell:** Yeah. That's, it's a, it's a warm fuzzy, but it's, it's harder. I feel like when people are like, you know, like I started content, I need a job right now. I was like, Oh, okay. Well, it's like, you got to keep going because of the warm fuzzies. Right. That's what it comes down to.

**Pallav Aggarwal:** Yeah, exactly. You can't write a blog at 10 a.m. and 4 p.m. You expect the contract.

**Chris Gammell:** Yeah. Right. Right. And 5 p.m. You'd get the money from it, you know, like prepayment, you know, a hundred percent.

**Pallav Aggarwal:** A hundred percent advance. And maybe for the next five years, you are, you are, you are now, you know, well, well said.

**Chris Gammell:** Yeah.

**Pallav Aggarwal:** You have no worries. Now focus on the work.

**Chris Gammell:** Yeah. So I noticed as well that on your YouTube as well, like you, so you do a lot of teardowns now as well. Are you, do you find that that obviously would no, no strangers to teardowns here at the Amp Hour. Dave, my co-host says a lot of teardowns and obviously a lot of people in the ecosystem do that as well. But do you find that that helps your design sensibilities? What, what made you start doing that? And like, what are you, what are you learning from it on a personal basis?

**Pallav Aggarwal:** So I think everything I am doing on content is basically out of curiosity, whatever I want to learn, I am trying to do those experiments and learning. And, and then out of that learning, I create articles so that I can also reuse that. And also sharing because, you know, not many people will have access to that information and it will be useful for other people. So it's basically curiosity. So one, around one year back, I thought how people are able to make, you know, wearable, for example, watches within let's say 10, $12. I mean, this is crazy. You can't even get, you know, AMOLED LCD in that price. Come on. Yeah. How can you do a strap and then electronics with, you know, most advanced SOC, low power battery.

**Chris Gammell:** and there's margin in there somewhere too, right? It's like, if you and I are paying 10 or $12, someone's getting 40% of that as a retailer. Exactly.

**Pallav Aggarwal:** So how, how they are able to do it. I was like, you know, I need to do something to learn that. Right. So I started doing, and then after doing a couple of them, I was like, okay, I'm enjoying it. So I should keep doing it. Tear it all down. Yeah, exactly. Whatever comes at my home or office, first thing I, first question comes to my mind is, can I open it? Right.

**Chris Gammell:** Can I see what you're doing? Good for the business, bad for family members, you know, like did someone, did, why is, why are there marks all over this plastic?

**Pallav Aggarwal:** Yeah,

**Chris Gammell:** exactly. That's great. That's great. So, and have you been able to extract, you know, some design lessons from it as well? Like have you, have you figured out the secrets of the 10 to $12 watch or what, what have you pulled out of that? Are you like, do you pull part numbers as well?

**Pallav Aggarwal:** Yeah. Yeah. So I have a full, you know, I have a non-published blog where I have written, you know, hundreds of part numbers, which are like, you know, ultra low cost ADCs, ultra low cost MCUs and, you know, things like you, you have never heard of.

**Pallav Aggarwal:** Got it.

**Pallav Aggarwal:** So those are like, yeah, I mean, that's the summary of whatever I've done so far in teardowns. And I mean, in general, it is all about optimizing your design, and simplifying your design, right. Don't make it complex. As soon as you start making things complex, you know, you know, at every stage, right. You're designing, you're manufacturing, you're testing, right. You're packaging, everything becomes complex. So the biggest lesson is make it simple, right.

**Chris Gammell:** Yeah.

**Pallav Aggarwal:** Think about what is really necessary.

**Chris Gammell:** I was on a project once where I had access to a, a low cost catalog of vendor chips, like, and it was a lot of fun to play around with it just to see how low the prices could go. But like you're saying, it was like, I added all this complexity. Cause I'm just like, Ooh, it was like being in a toy store with like a free coupon, you know, I'm being like, Ooh, I want one of these. And one of these, I bet I could use one of these, you know, I'm just like, like, and the board got bigger and it was just like, and it ended up all coming off in rev B, but for rev A, I was just going nuts with it. And it, it introduced way more complexity than was needed.

**Pallav Aggarwal:** Exactly. So we, we have consulted, uh, some of the customers where they came in and asked for, you know, can you review our designs? And a couple of times we ended up telling them, okay, 40% of your design is not really required. You have to just remove it from power. Wow. Yeah. If you, and from cost point of view. Right. So I was asking them, okay, why do you need this? And they were like, there is no answer.

**Chris Gammell:** I saw, I saw it in a catalog. I saw it at a, I saw it on a blog. At one time they're going to be like, I saw it on your blog. And then you're going to be, you know, then you're going to be in a real tough spot.

**Pallav Aggarwal:** So a lot of good to have were there. So, yeah.

**Chris Gammell:** Yeah. Right.

**Pallav Aggarwal:** Right.

**Chris Gammell:** Yeah. The, uh, I might need it someday kind of thing, you know, it is that's like fighting that instinct.

**Pallav Aggarwal:** Yeah, exactly. I mean, for example, in my, you know, design optimization consulting for low power, I see, you know, tens of LEDs and LDOs everywhere. Right. So, and then they say, okay, I'm struggling to optimize. And I was like, okay, everything is in front of you.

**Chris Gammell:** Yeah. Get out the thermal camera being like spot, spot, spot. These are all linear regulators. These are all your LEDs, right? Exactly. Yeah. LEDs is one where I, I've gotten sucked in, you know, I'm like, you know, too many times when I've been like troubleshooting, I'm like, Oh, one more LED, you know? Yeah. Yeah. How we will,

**Pallav Aggarwal:** how we will know that our device is working.

**Chris Gammell:** Right? Right. Exactly. We couldn't possibly tell any other way unless it blinks. It has to blink. It's a sign of life.

**Pallav Aggarwal:** Yeah, exactly. Or some five minutes.

**Chris Gammell:** It says I'm alive.

**Pallav Aggarwal:** Something like an audio message that, okay. Yeah.

**Chris Gammell:** I'm cool. Exactly. Yeah. Yeah. It would be nice to almost have like a, like a standardized interface, like almost like, so like using like a CH32V as like a interface, like an I2C device where you could like, assuming it always worked perfectly, right? Cause then you don't want to have to troubleshoot your troubleshooting device, but assuming it ever always worked perfectly, being able to like hook that onto the bus, during troubleshooting. And then you have all these lights to light up, right? During troubleshooting. And then later you just pull it off. You know, it's like a product test, test only, not in production sort of thing, you know, having standardized debugs like that. Some people just use debugger, but, but I like the blinkies, you know,

**Pallav Aggarwal:** I have seen, uh, RP 2040 getting used in some of the, you know, debuggers. Yeah. And, Oh really? Yeah. And then when these USB to UART bridges, right, they were very difficult to, you know, buy during COVID people started using the RP 2040. Yeah.

**Chris Gammell:** Yep. As a, as a,

**Pallav Aggarwal:** as a bridge.

**Chris Gammell:** Anything that was available during the, uh, yeah, exactly. Sure. I mean,

**Pallav Aggarwal:** I remember strategizing that, okay, let's buy everything we need for first and second level of prototype development, and then finalize our schematic and PCB design.

**Chris Gammell:** Yeah. Yeah. Yeah. Push the, kick that can down the road. Exactly.

**Pallav Aggarwal:** Yeah. COVID was a crazy time.

**Chris Gammell:** How, how much, uh, how much of the, your business is that, is that optimization? Cause I feel like that is a, a useful thing, but it's often, you know, as a consultant, it's not the most, um, like ongoing, it's like kind of almost like one time thing, you know?

**Pallav Aggarwal:** Yeah. It's like 15, 20% of, uh,

**Chris Gammell:** okay.

**Pallav Aggarwal:** Yeah. It goes, uh, you know, sometimes it is high. Sometimes it is low depending on, you know, who is facing what kind of problem. Right.

**Chris Gammell:** Yeah. I feel like it would be for the listeners of this show would be interesting because a lot of them are like, Whoa, I'd love to have someone like make my design more efficient. You know, that kind of thing is like, it is for the target audience. Like, like we have here listening, they'd probably be very interested. Uh, but I think more, you know, like the customers you're usually interacting with, they're probably like, well, just make it good. Right. They'd probably like more like just make it a good product and then it's on you to.

**Pallav Aggarwal:** Yeah, exactly. So every time it, it starts like you cannot, you have to make it functional and then we go for, you know, further optimization. Right. Um, very few companies I have seen that, okay, this is, you know, my performance criteria and let us start considering from day one, what we are going to do. Right. If it is not performing in first proto, second proto, it is fine, but still this is our, you know, top most criteria we should consider. Right. Exactly.

**Chris Gammell:** Yeah. I've been guilty of, uh, over optimizing on that first rev for sure. And it's like, sometimes it is good to have a little bit of inefficiency on the first couple of revs, just to make sure, like you said, function is there or whatever. Yeah. Like I remember, um, past guests of the show, uh, Sean, uh, cross, he had like a really, really big FPGA board with like all these breakouts. It was just like way bigger than it needed to be. Yeah. And I was like, yes, that is what I, that's what I need to do more often where I, I always think about the, the, the more form and fit instead of the, the, yeah, just the function at the beginning. You know, the function is the most important thing on the rev a, I feel like.

**Pallav Aggarwal:** Exactly. And I think, uh, in, uh, rev one, what you need to focus on is how your rev one is going to help you in debug because first revision is going to be more of debugging than, you know, performance, right? Because a lot of things will not work, right? You have to understand.

**Chris Gammell:** Oh yeah, I know that one.

**Pallav Aggarwal:** Right? Because data sheet had something and you understood in a different way, right? A lot of times, right? And then you missed something, right? Uh, because there are 3000 parameters you are juggling with.

**Chris Gammell:** Exactly. Exactly. Yeah. I can't. Yeah. Yeah. Yeah. And it's like, and then they buried, they buried some like, you know, caveat and a footnote somewhere. And it's like, Oh, Oh yeah. Yeah. That is there. But it's not useful chip company.

**Pallav Aggarwal:** Six size, six font, uh, yeah, exactly. In the data sheet.

**Chris Gammell:** Any, uh, any good, uh, good stories about that? Any, any, uh, any problems that you've had in that, in that space?

**Pallav Aggarwal:** I have recently saw an I2C device where such note was mentioned with, uh, you know, very small size font. I was like, wow, what an innovation in the data sheet.

**Chris Gammell:** Yeah. Right. Right. Right. Yeah. They really should put it on page one, but they put it on like page 30, right? It's exactly.

**Pallav Aggarwal:** And, and many companies are expert in spreading their single topic to every page they know of. Right. For example, if they're talking about I2C, they have to talk about I2C every second page instead of, you know, grouping everything together and make, make life easy. So they, they want us to work more and be alive.

**Chris Gammell:** Right. Yeah. Yeah. Yeah. Yeah. I guess, I guess it does require a rev B. So, and that does mean we get more work, but it's not what we actually want to deliver to client. Like we want the rev A to be the best, right? Like that is the best case scenario. So yeah.

**Pallav Aggarwal:** Yeah, exactly. Everyone is looking for a first time right design, but that's a myth. Yeah. That's always a myth.

**Chris Gammell:** Yeah.

**Pallav Aggarwal:** Whoever says first time right design, they have done more work towards, you know, reviews and, you know, evaluation. If you spend like two months in evaluation, for sure, you are going to get, you know, rev one, or if you're doing a Delta revision, then yes, you can get the first time right design, but otherwise it's very challenging. It's very, very challenging. And it needs a lot of attention and reviews in order to achieve first time right design.

**Chris Gammell:** Yeah. Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** Yeah. And it might end up costing more in that way anyways. Right. So like, again, from like delivering to a customer, it feels like that, that is not necessarily.

**Pallav Aggarwal:** Yeah. I think, I think we should, we should aim for that, but we should not, you know, think too much that, you know, my first revision has to work. Obviously everyone is aiming for first time right design and they don't want, you know, silly mistakes, but still in general, even if there are no mistakes, you will find from DFM point of view or from, you know, the accessibility of some parts of your product, you would like to, you know, optimize, for example, some connectors should be placed differently, right? Because now you are, you started thinking from user point of view, right? And application point of view or deployment point of view. Right. Right. Right. Yeah.

**Chris Gammell:** Totally.

**Pallav Aggarwal:** Totally. I remember we did one project for variables and we have done 10 times the size of the variable first revision because we can't use zero, you know, zero four zero zero two components and the smallest chips available and then make our life hell during debugging. Right. Totally. Because we want to make sure our concept is functional and working and then we can very easily. So moving from zero six zero three to zero four zero two doesn't make, you know, I mean, doesn't take much effort. We can very easily do it, but we should know that whatever you have drawn is going to work. Right. Yeah.

**Chris Gammell:** I agree. So,

**Pallav Aggarwal:** yeah. So we, yeah, that,

**Chris Gammell:** that, that shrinking stage is definitely like planning for that in this, in the upfront with the customer or, you know, internal teams or whatever you're doing. Right. It just, it does make sense because yeah, that's a great point about the debugging and, and just like the being able to get at all the signals that you need to and whatever. That's exactly, like I said, that's definitely one of the mistakes I've made many times before.

**Pallav Aggarwal:** Yeah. I mean, assembly options, right. You, if you are unsure of something, give assembly options. So that you, you know, three things I can try. Right.

**Chris Gammell:** Yeah. Right. Right.

**Pallav Aggarwal:** And then,

**Chris Gammell:** yeah, I mean, that's a lesson relearned during the pandemic as well. Right. Oh man. Having like multiple footprints being like, yeah, you know, zero home here, zero home there. We'll figure out. Exactly. I mean,

**Pallav Aggarwal:** I remember doing designs where multiple, you know, opems were used, multiple memory footprints were used in order to make sure that whichever is going to be available, we are going to use it.

**Chris Gammell:** Yeah. Yeah. Yeah. It's when you start cursing the fact that people moved away from standard footprints, you'd be like, couldn't this just be the same, same stupid footprint. You're like, why do they need to use different packages everywhere? Yeah,

**Pallav Aggarwal:** exactly.

**Chris Gammell:** Yeah,

**Pallav Aggarwal:** exactly. Exactly. And you, you find out that, you know, after 20 years of experience, you only know half of the packages available in the world.

**Chris Gammell:** Totally. Yeah. You always find that one, you know, you never, you never discover that new footprint until you realize that you can't buy the, you can't buy the alternate for it. You know, you're like, why did TI, it's always TI too. I feel like TI is one of the worst defenders on this. They always want to make a new fancy footprint. I feel like they're using it as like trade secret light, you know, they're just,

**Pallav Aggarwal:** yeah,

**Chris Gammell:** come on TI. That's the IP. Yeah. Right. Yeah. So we've been talking troubleshooting here and you do do, you know, reviews on test equipment, stuff like that. What is your, what's your go-to setup? If you're, if you're just sitting down at the bench to go troubleshoot a customer project, what's, what's on your bench? What's your, what are your go-to tools?

**Pallav Aggarwal:** So let's, let's say if we are trying to troubleshoot power consumption, my go-to tool is going to be, for example, Juulscope, right? One of the best power optimization energy, you know, analyzer available in the market. And we hook it up. And see what's going on. And, you know, before starting to analyze anything, we need to also understand the hardware and the software flow, right? Because a lot of times, for example, I'll give you example. We, we have done a lot of optimization in software and people were like, you know, only hardware optimization is good enough. And we did more optimization in software. For example, in one project, we figured out that when you are not using UART, you are consuming, you know, 200, more than 200 microampere. So when you de-initialize UART and you don't use that block, you don't provide any power, you switch off that block, you are saving a lot of power. And for example, one company was sending 200 bytes to mobile phone using JSON packet, right? And then JSON was so heavy. We reduced that to 16 bytes. Yeah. Only 16 bytes. Back down. Yeah, right. 16 bytes. Yeah. And that has reduced their power consumption by, you know, hundreds of microamps. Right. Yeah.

**Chris Gammell:** I do like the readability of JSON, but it's, it is, it feels like it's like a software person's, you know, like, yeah, I mean, it is easy for mobile phone.

**Pallav Aggarwal:** It is easy for mobile phone, but then you don't talk about battery. Yeah, exactly. If you need battery life, you have to do the way it is really required. You are talking about 10 year life and you are talking about that, you know, I want to send via JSON and I want to write my name, full name and don't do like that. Right. Initials. And no punctuation. And then, and then Mr. Get it out there.

**Chris Gammell:** Yeah.

**Pallav Aggarwal:** Exactly. So you, you can't do like that. Right.

**Chris Gammell:** Got it. Yeah. Yeah. Yeah. Okay. So power optimist. That's great. That's great. What about other like troubleshooting types? I think I saw Celia on your.

**Pallav Aggarwal:** Yeah. Celia logic is a great tool for, you know, protocol analyzer. For example, we use a lot of times for I2C, can RS 45, basically Modbus. And then sometimes for SPI as well. So I have never used anything else than cell logic. It's the best tool available in the world from my personal opinion point of view.

**Chris Gammell:** Yeah.

**Pallav Aggarwal:** So I started. There you go.

**Chris Gammell:** Two recommendations. Yeah.

**Pallav Aggarwal:** I mean, everywhere I go, whoever asked me about logic analyzer, I say, yeah, this is the website and don't see anything else.

**Chris Gammell:** All right. Well, that's great. You know what? And if people want to contest that, they can make their own content about it. Darn it. You know, exactly. Exactly. Show me how it is better. Show me.

**Pallav Aggarwal:** Exactly. Exactly. Head to head. Let's do it. Exactly. Let's do it. Yeah. And then I'll show you how cell logic is better in most of the situations. For a very particular situation, for example, you are doing USB analysis, right? High speed USB or something. Obviously, cell logic is not the best tool, right? Right. I'm not talking about that. I'm talking about general electronics debugging, which is like 95% of your work. Cell logic is going to be the winner.

**Chris Gammell:** Yeah. That's great. That's good. And I think that's good too, to have the tools you reach to and go to, right? Like that just shortcuts that process. And then it's like, like you said with the microcontrollers too, like just the number of, the amount of time it takes to evaluate a new thing too, then you have to like, basically it's opportunity cost to go and evaluate the new tool. Exactly.

**Pallav Aggarwal:** I mean, initially I was not thinking about creating, you know, CS32 V003 development board, but then when I started doing evaluation, I had a MCU breakout board and there was nowhere I can hook up my oscilloscope and, you know, also connect my jumper. I was like, wow, what kind of evaluation platform we have? We need something else. So I created, I created one and then I thought, okay, this will be useful for others also, right? It will save time. Every time they are going to use or evaluate. Right.

**Chris Gammell:** Yeah, totally.

**Pallav Aggarwal:** Yeah.

**Chris Gammell:** Yeah. No, I think that, yeah, that kind of thing. And like, again, it's just something you reach for and you're able to just go and use for that sort of thing is awesome. Yeah. I mean, yeah,

**Pallav Aggarwal:** in troubleshooting, other than that,

**Pallav Aggarwal:** we also use static analyzers for, you know, analyzing codes. Right.

**Chris Gammell:** Okay. Yeah. Yeah. We do that. Just to see like where you're, where you're spending the most time and stuff like that. Exactly. I don't think I've ever used a static analyzer. What is that? What does that look like?

**Pallav Aggarwal:** So static analyzer will tell you, you know, how many functions you are using, how they are connected. It will give you high level flow chart. Right. It will tell you, you know, if you have used, uh, allocated a memory and, you know, you are, you are not freeing that memory, for example. So a lot of things you can even do compliance testing for Misra C. Right. So a lot of standards are there, right. You can, if you are following some standard for a project, then you can, you know, do static analysis. Yeah.

**Chris Gammell:** That's nice. Yeah. And so you just basically like put your code into there and it just kind of pops out like a, exactly equivalent of like a PDF report, something like it.

**Pallav Aggarwal:** Yeah. It's like a interactive report, interactive report inside the software. And then you go through all the points. And then at the end, you realize that, you know, your code is now much more modular, much more usable. Right. That's nice. For example, there is a saying, if your function is more than 200 lines, you have to better split that function. Right.

**Chris Gammell:** Yeah. Right. So then it's giving you some of those guidelines and it's almost like a, like a parser, but in like a very, very high level.

**Pallav Aggarwal:** Exactly. Exactly. If you're missing too many comments, for example, right. Then they will say, okay, it is hard to understand your code, right. If you don't have function headers, if you don't have file headers, right. So a lot of things, a lot of things.

**Chris Gammell:** And now. So what I'm, what I'm imagining is a countdown to some brilliant new startup doing this, but then calling it AI.

**Pallav Aggarwal:** Yeah. Yeah. Yeah, exactly. Embedded code AI. So as soon as, as soon as, you know, AI hype started, everyone started using AI based this AI based this, right.

**Chris Gammell:** Yeah.

**Pallav Aggarwal:** Yeah. Yeah. I mean, same thing happened with the IOT, right. 2013, 2012. Before that, I remember using cellular modem in 2006, 2007 for connectivity with server, right. At that time, there was no cloud. Everything, everything we were, everything we were calling it as server. Right. But then, you know, 2010 timeframe, everyone started like IOT. Wow. Right. Something new.

**Chris Gammell:** Right. And then everyone was doing. Same, same, same idea. Is that right? Yeah. Yeah.

**Pallav Aggarwal:** Exactly. So it's like hype.

**Chris Gammell:** Yeah. Well, I think, I think IOT is low on the hype cycle. I think hopefully it's in, it's in that final, that final reascent, but yeah, I think we're still, we're still cresting the curve on the AI stuff for sure. Exactly. We're in the middle of it.

**Pallav Aggarwal:** I should also start saying AI based, matured and successful designs. Yeah, exactly.

**Chris Gammell:** AI based teardowns. We could sell a lot of snake oil. That's what I'm saying. You know, like we could really, we could really make a market for it. Yeah,

**Pallav Aggarwal:** exactly. Exactly. A lot of people are doing automation and they are calling it as a AI.

**Chris Gammell:** Right. Exactly. Yeah. If then statements becomes AI. Exactly. That's great.

**Pallav Aggarwal:** Yeah. But I think a lot of good tools are coming. A lot of good companies are also there who are really trying to use AI as well. Not just automation. Yeah. It's interesting. A lot of companies have started doing, you know, a couple of things in PCB automation, for example, PCB design, you know, automation and creating schematics, reviewing schematics. A lot of things are happening. I have evaluated a couple of them and, you know, they are not yet mature, but it is very interesting to see these, you know, kind of tools coming and trying to change the way we work. Yeah.

**Chris Gammell:** Yeah. Yeah. I just, I was just looking through you. So you have a page on your website where you kind of keep track of all these too, huh? Yeah. That's a nice, nice page to just have their circuit mind JITX. Yeah. A lot of these ones that have seen flux. So yeah, that's a,

**Pallav Aggarwal:** yeah. One day I was trying to research on, you know, what is happening in AI for electronics and I found some companies and then I thought, okay, interesting. So let me create a page and put it on my website so that I can come back and see. And now I see, you know, very popular page for on my website. It's like most visited page since last one year.

**Chris Gammell:** Oh, really? Oh, really? Yeah.

**Pallav Aggarwal:** Yeah.

**Chris Gammell:** Yeah. Yeah. Exactly. Yeah. Yeah. It is. And it is good too, to have like, like you said, you're keeping track of this for yourself, but also other people can find it. Have you, have you actually adopted any of these in your like daily workflows or are they just more experiments so far?

**Pallav Aggarwal:** So far they are experiment, but I'm trying to see, you know, when these tools are ready, because there are, there are a lot of overheads involved when you are trying to use these tools because they are still beta. Right. And it is not going to work the way you want to work. Right. If you are in the middle of your project and you are trying to use these tools, that's the wrong way of using these tools. Right. You have to learn how it works in which situation, which design it will work. And then, you know, try to use that. You, you have to be mindful about what is available. What is ready. Right.

**Chris Gammell:** Yeah. I, the only one I don't see in your list is some, we had, we had quilter on here. There's one. Yeah. Yeah.

**Pallav Aggarwal:** Quilter is also there. I've not tried them yet. And I've, also not updated my blog post.

**Chris Gammell:** Yeah.

**Pallav Aggarwal:** Yeah. A couple of them are there. Yeah.

**Chris Gammell:** Yeah. Yeah. It's interesting. I, I don't know. I, I have no doubt that we're going, that I'm going to supplement my own work. I already do supplement my own work with AI, right? Like people who look at the blog post for the amp hour, right? I use, I don't care about what the image looks like when it's, when it's a Dave and show with me and Dave, it's just, it's just an AI generated image. That's just the silly title we came up with. Right. But like, I don't know. Like I, I feel like a little more resistant on this side of stuff, just because like you said, it's like the workflow and like, how do you know it's right? Like it ends up coming back to me to make sure it's right. So now I'm doing, you know, I'm either paying or giving my time and attention to something. It's like, there's no guarantee it's right. And so it's like, okay, well, why don't I just do it right the first time myself? You know?

**Pallav Aggarwal:** Yeah, exactly. So that's why I said that you need to figure out where it will help you. For example, if tool helps you figure out 10 options of doing cellular connectivity, that is good enough. You should understand that. Yeah. Right. Don't expect, you know, everything created, you know, product is created by AI tool. Don't expect that. Yeah. Expect, you know, bits and bytes now, and those bits and bytes will become blocks and maybe schematic. You know, that's how it will work. And if you don't, you know, get involved now, you are going to lose how things have involved, evolved.

**Chris Gammell:** That's true.

**Pallav Aggarwal:** And, you know, you will only know the last part of things.

**Chris Gammell:** Yeah. Yeah. I'm still referencing things from 10, 15 years ago personally. So you've got to keep up on things too, right? I mean, that's probably why it's such a popular page on your site.

**Pallav Aggarwal:** Yeah. I've, I've spoken to the founder of GTX and CLS and got the demo also in one-to-one meeting. It was very interesting to see what these guys are doing. And for some situation they have matured tool also, but yeah, yeah. Things, things are still evolving.

**Chris Gammell:** Yep. Yeah. So another, another page you have next to this is kind of the AI hardware platform. So like the Jetson and the.

**Pallav Aggarwal:** Yeah. That is also not updated. I have not updated. A couple of more platforms are available nowadays. Sure.

**Chris Gammell:** Yeah. I feel like that's just going to keep zooming higher and higher. But like, I am curious just in a, in a broad case, how you find yourself using these maybe in client work. So like, are people asking for like image processing at the edge for that sort of stuff? Or like, is this again, just eval just to keep on top of things or you actually have clients who are like, no, no, no. I need to do like, you know, photo detection at the edge sort of thing.

**Pallav Aggarwal:** So in two of our projects in hardware, we have added, you know, hardware accelerator.

**Chris Gammell:** Okay. Yep.

**Pallav Aggarwal:** Because a customer wanted to do a hardware accelerator for some of their image processing and audio processing work. And that was more like, you know, experimental for them that, okay, let us create a hardware. And if it works, we are going to use it. Otherwise we can just leave it. So, you know, a lot of companies will do like that, right? They want to try, right? Otherwise how you are going to try.

**Chris Gammell:** Right. Well, and I think a lot of that, like we talked about before with like the selling top down into companies, I feel like almost maybe not being sold, but definitely like CIOs at like big companies are like, Oh, I just heard about AI. And then they tell their employer, they tell their managers who tell the employees like, Hey, the big boss wants to try out AI so that they could put it into a presentation. And it's like, great. Maybe it works, but it's like still just like a banner level feature rather than like an actual need. I'm always curious about the actual needs for it. And it seems like those are a little light, at least ones that I've seen.

**Pallav Aggarwal:** I mean, a lot of interesting chipsets are there. I don't remember the name. One second. Let me just check. So there is one company in us, they are building accelerators for audio and you can do like, you know, understand what is happening in the background. So my, my, my input is going to that device and you can program it. And once you have, you know, programmed it using some model, you will be able to detect somebody's typing. Somebody's talking to people are talking. One person is shouting. Somebody has thrown plate or whatever. Right. So interesting stuff, interesting stuff.

**Chris Gammell:** You can see what is happening in your pre-qualified models and stuff like that. Sort of.

**Pallav Aggarwal:** Exactly. And it's very low power, micro ampere power. And, you know, they were showing stuff connected over as, you know, connected to STM 32. Very interesting stuff.

**Speaker ?:** Hmm.

**Pallav Aggarwal:** I was, I was even thinking that, okay, maybe we should create some boards and show people how to use it because it is very difficult. Meaning, meaning to add, to start using that part is difficult because they are making chips, but they are making it difficult. Checking their data sheet, getting access to their data sheet, getting access to getting started document, getting access to SDK, getting access to their boards. Everything is so difficult. Right.

**Chris Gammell:** That's a good point.

**Pallav Aggarwal:** If someone can write down, okay, this is how you have to do each stage, it is huge value. Right. And we were a couple of months back, we were thinking about doing that. Yeah.

**Chris Gammell:** As a service for the customer, for the client, for the chip companies rather, and the module makers.

**Pallav Aggarwal:** So more from building, you know, knowledge base for ourselves first, because once we know how it works, we can, you know, tell companies how they can benefit out of these technologies. Right. If we don't have experience, how can we help other people? Right.

**Chris Gammell:** Totally. So we have to, I just, I was just thinking that chip companies should hire someone like you to write their documentation for them as well, just because it's like, you know, the perspective of someone who wants to use it. You're basically talking about like a, what I would call like a developer relations type thing. That's what I do. Right. But like, it's almost like, because you, you are the user, you know how to like make something the users want. Right.

**Pallav Aggarwal:** Exactly. Exactly. I'll be very happy if someone contacts me and say, okay, can we collaborate and do some content, which will make their chip, you know, more usable, chip more usable. Right. Yeah. And more. Yeah.

**Chris Gammell:** It's almost like once a month, if you just go through the, go through the pain and the process of, of like trying to source it and trying to talk to it, like starting from scratch, like, exactly. Oh man, all this stuff pops out. Just like, Oh, this is broken. So this is broken. Still, this got better. This got worse. You know, exactly. Yeah,

**Pallav Aggarwal:** exactly. So I think those companies are still supporting their customers one-to-one. That is how it is working. For example, I told about Mbeck, right? It works very well with their customers. We are one-to-one relations there.

**Chris Gammell:** Right. Cause there's some technical expert inside of Mbeck. Who's like, well, I'll just get you started and they'll do it, but it's not like for the mass market. It's just for that.

**Pallav Aggarwal:** It's not publicly documentation is not publicly available in the form. It is very easy to use. Something is available, but it is, I mean, from my point of view, it is not very easy to understand and start using. Yeah. Right. Because, digestible and whatever. Yeah. New platform means new understanding, right? New APIs and how to use it. Yeah. A lot of things are there where you have questions. You have to have some way to ask questions, right? Where to, where do I ask if. Yeah. Right. Yeah. Is there a forum? Is there a support channel? Yeah. If forum is there, when I write, two years later, someone contacts me. What is the point?

**Chris Gammell:** Yeah. Right. Exactly. Exactly. Yeah. It's a, it is a tough problem and it's good. You're good. You're thinking about it. I hope the, I hope the chip comes, like I said, like I said earlier in the show, it is expensive, right? Having good software, having good docs, all that stuff is expensive. I feel like most of them don't price it in. And instead they say, well, we'll just pay for an FAA, pay for sales, push it down, you know, from the top. And it's like, okay, well, you know, that's the old way of doing it. So it works sometimes. Yeah.

**Pallav Aggarwal:** From that point of view, I think Nordic Semiconductor has done really good job. They have good documentation.

**Chris Gammell:** They're my go-to for a lot of examples.

**Pallav Aggarwal:** I really like Nordic Semiconductor company, how they provide support on their forum is very good. If you remove support, nobody will use that product.

**Chris Gammell:** Yeah.

**Pallav Aggarwal:** So a lot of support they are trying to provide. And then recently they have created this, you know, you know, power, power analyzer tool, low cost power analyzer tool.

**Chris Gammell:** Oh yeah. Also PPK2. Yeah.

**Pallav Aggarwal:** PPK2. I have used that for several projects, right? Where you don't want accuracy up to nano ampere level. It's good enough tool for many situations. And now they have created a tool for, you know, initialization of your initialization code. So it's really useful.

**Chris Gammell:** Which tool is that? That's like for the NDS code or something else?

**Pallav Aggarwal:** Or for PPK? Not for PPK. So if you are using Nordic Semiconductor chip and you want to initial, you want an initialization code, for example, STM32, you have STM32 cube ID where you can initialize your peripherals. Yeah. Right.

**Chris Gammell:** Yeah.

**Pallav Aggarwal:** So something similar they have created, which helps, you know, otherwise it was very difficult. Initial. I mean, we have used Nordic Semiconductor in some of our projects and it was difficult.

**Chris Gammell:** Yes. Right. Yeah. So like device tree and Zephyr type stuff.

**Pallav Aggarwal:** And now you have to configure SDK. Right. Yeah.

**Chris Gammell:** Yeah. Right. So now it's more like a graphical style, but it's making that device tree for you. That's right. Yeah. That is a lot better. That is. That's what I want as a hardware engineer. Usually.

**Pallav Aggarwal:** I mean, that's the best thing. I mean, STM32 has done the best thing by providing wizard, right? Wizard for your, all IOs.

**Chris Gammell:** Yeah. Yeah. I feel like the, the downside is always when you need to move a pin later. That's always the thing that scares me. When you have to move a pin later, we have to reconfigure. You're like, Oh, now I'm going to Rev B and I have to regenerate. stuff, you know, like the, maybe not.

**Pallav Aggarwal:** Maybe generating is not a big deal, but you have to follow some, you know, programming style. So they have provided sections where you can write your own code.

**Chris Gammell:** Yeah. That's right. Yep. Right.

**Pallav Aggarwal:** If you don't follow that, then you will mess up.

**Chris Gammell:** That's right. Yeah. That's, and that's exactly what I've said. I've definitely blown away code before. You always, you know, commit to, commit to your repo before you, before you regenerate.

**Pallav Aggarwal:** So that's where your GitHub helps you. Totally. Yes. Yes. Right. Even if you messed up, your last version is available to help you. Yeah, exactly.

**Chris Gammell:** That's great. Great. Well, Pallav, I really appreciate you telling me about all this stuff and please, please keep publishing all the great things you do. I, I have your feed coming directly into my Slack channels. Pro tip for people that don't know, if you do slash feed in Slack, you can add an RSS feed and it just pops up Pallav's blog or the amp hour feed. If you want to RSS is alive and well in Slack, apparently. And there's other ways to.

**Pallav Aggarwal:** Great. Thank you so much for sharing that. Yeah. Yeah.

**Chris Gammell:** So, yeah, please keep it up. And how can people find you and find cap of if they want to hire, hire your company?

**Pallav Aggarwal:** So they can visit our website. It is HTTPS forward slash cap of dot in. And then they can also reach out to me at info at the red cap of dot in. So cap of a C-A-P-U-F.

**Chris Gammell:** It's like a capacitor microfarad. Is that the origin of that name?

**Pallav Aggarwal:** Yeah. So the name is totally synthetic. And the reason behind synthetic name was, I wanted to create something unique.

**Chris Gammell:** Findable on Google and searchable and bring it on. Yeah.

**Pallav Aggarwal:** Yeah, exactly. So cap of embedded is all about unique embedded services. And that's how we work. When people work with us, they find us unique. That's great. That's great. Hopefully.

**Chris Gammell:** I'm sure. I mean, just from this conversation, it sounds like you are definitely have your clients best interest at heart and you're advocating for better chip companies, better stuff in the industry. So like minds here. I'm really glad you came and stopped by and told me all about it. Thanks for being here today.

**Pallav Aggarwal:** Thank you, Chris. Thank you. And it was nice talking to you. Thank you so much for having me. We'll be right back.
