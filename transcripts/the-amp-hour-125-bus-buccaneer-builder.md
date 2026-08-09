---
episode: 125
title: An Interview with Ian Lesnet - Bus Buccaneer Builder
url: https://theamphour.com/the-amp-hour-125-bus-buccaneer-builder/
---

**Chris Gammell:** This is the Amp Hour Podcast, recorded December 10th, 2012. Episode 125, with guest Ian of Dangerous Prototypes, bus, buccaneer, builder.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of ChipReportTV and Chris Gammell's Analog Life. And I'm Ian Lene from Dangerous Prototypes.

**SPEAKER_00:** Hey, Ian. Thanks for joining us. Oh, thank you so much for having me.

**Chris Gammell:** I did not realize your name was pronounced like that. I feel bad now. Yeah, so do I. I've been saying it wrong.

**SPEAKER_00:** Well, you'll never actually hear me use my last name. That's why in forums and even presentations at Maker Faire, I insist that they just put Ian. Really? Interesting.

**Dave Jones:** Okay.

**SPEAKER_00:** It's much easier for everyone that way, I think. Right. That is easier.

**Dave Jones:** All right. Cool. See, I'm exactly the opposite because David is so common and then David Jones is so common. I've had to put my middle initial when I used to publish stuff so that I didn't get confused with any other David Joneses. So I had to put David L. Jones just to differentiate myself from everyone else. Yes. You're going the celebrity one name route, huh?

**SPEAKER_00:** Well, I think the Dangerous Prototypes fills it in.

**Dave Jones:** Yeah, of course. Yep. So how's your into, you're an open hardware aficionado.

**SPEAKER_00:** Oh, yes. At Dangerous Prototypes, we try to make a new open source hardware project every month. Open hardware means, of course, that all the files, the documentation, the pictures, even the articles and things we write about our hardware, it's all licensed under an open license. So anyone can take it and use it just about however they want. The million-dollar question is what license do you prefer? Okay. Well, you know, in the past, we've done a lot of Creative Commons attribution share alike. So you have to share it as well and you have to put our name on it. But increasingly, we're doing public domain. Oh, interesting. Just do whatever you want with it. Right. You know, I come from this as a writer and a blogger and my first open hardware was published on Hackaday and other blogs. And really, the license is just a formality. Yep. I really want people to be able to do what they want with the work and have a good time with it. I really don't want them to worry about licensing restrictions or any of that kind of stuff. And I'm not into the philosophy of licensing. I know there's good reasons that people do all sorts of different license types. What I really want is the least amount of BS possible for the people using our stuff. And so, you know, public domain is the way to do that. We just claim all rights except our trademark on the name. And then people are able to use it however they want. And this started with development boards and breakout boards because you're making a board specifically for an engineer to use to build or learn a project. And why on earth would you lock that down? Yeah, I know. In my mind, that's like a textbook saying, well, every time you use this formula you found here, you have to attribute this textbook.

**Chris Gammell:** Mm-hmm.

**SPEAKER_00:** And that's not generally the way it works. I wouldn't put it past too many publishers, though.

**Chris Gammell:** I think some of them might go to that model eventually. Charge you 200 bucks and then, you know, 50 cents per equation.

**SPEAKER_00:** So I really, you know, I just want people to be able to use our stuff however they want, especially the development boards and the breakout boards, stuff that's intended for engineers to use it in their own projects and to quicken their development cycle. I just, we're putting all of that out under public domain now.

**Dave Jones:** Fantastic. Thumbs up. Definitely.

**SPEAKER_00:** Well, it hasn't hurt us any yet.

**Speaker ?:** Right.

**Dave Jones:** How did you get into all this? You started on Hackaday, but what about before that? If you always published stuff, worked on projects and stuff like that, tell us about your background.

**SPEAKER_00:** I saw on the Reddit there was a question about my education. Oh, okay. I did start as an engineer, but I wasn't very good at it, and I didn't like it very much. Oh. So in my master's degree, I moved to urban planning and regional development, and I also did a, I started a PhD in that as well. And when I did my PhD, I started writing a dissertation about using wireless sensors and wireless sensor networks to sort of learn things about cities and measure things in cities. And I worked with what was called the Berkeley SmartMote at the time based on the TinyOS operating system. And I got this equipment, and I tried to implement it, and it just didn't work very well. So, of course, after being frustrated with it for a while, I had to whip out my acid etch tank and start building QFN radio boards in my dormitory room on top of a hot plate. And that's really where I learned the nuts and bolts of electrical engineering, something aside from the theory. And that I found I liked quite a lot. Yeah, that's fun stuff, right? And so in the process of developing this wireless sensor network, which ultimately I always want to point out fails. It was just a disaster of a project.

**Chris Gammell:** Is that just like a general sweeping statement? Why?

**Dave Jones:** Please tell us. Let's get into the technical details. Why did this thing fail? Was it politics or was it engineering?

**SPEAKER_00:** Oh, no, it was engineering and my lack of ability to pull that off as my first major project. No question about it.

**Chris Gammell:** That was a big bite to take, I think, but yeah.

**SPEAKER_00:** Yes, yes. But along the way, I developed a number of tools and a number of scripts and a number of things that eventually became the bus pirate. I developed these tools for debugging problems I didn't understand, especially doing things very low cost because I was a starving grad student. And since I wasn't in a proper engineering department, I didn't have access to the tools you would have if you were in an electrical engineering department doing this instead of in an urban planning department.

**Dave Jones:** Right.

**SPEAKER_00:** So I developed all of these little tools and all these little helpers that eventually became things like the bus pirate. And so for a few years, I published the bus pirate on my private blog on my own website. And then eventually I went to write for Hackaday, the fairly well-known blog. And I wrote features for them. And I started writing a few features about the bus pirate and how it had developed over time. And people were actually quite interested in it. And it really surprised me. And after about a year of writing about it on Hackaday, Eric Pan from Seed Studio, a manufacturing company in China who does exclusively open hardware, approached me and said, Hey, you know, we've had some readers say they'd really like to buy some bus pirates. And we can make some. We can make as few as 20 and try to sell them. And I laughed. I said, There's no way in the world anybody wants to buy this. You're not going to sell 20 of them. You're going to have a warehouse.

**Dave Jones:** You'll be left holding a bag at 19, you know? Yeah, exactly.

**SPEAKER_00:** I figured there's going to be 20 widgets sitting there rotting in a warehouse in China. And, you know, I was still in the graduate student mentality. That was a lot of money to me.

**Chris Gammell:** You've got to take delivery. Those will be sitting in your dorm room under your bed.

**SPEAKER_00:** Yeah, exactly. Exactly. Oh, man. But we ran the bus pirate as a pre-sale, which I guess these days you do Kickstarter or Indiegogo. But we just did a pre-sale and pre-order with Seed Studio on their site. And we did it as a fundraiser for Hackaday. And, you know, in a week, I think we sold 1,000 of them. Holy crap. And I was really impressed and just couldn't believe it. So from there, I started Dangerous Prototypes to release my new open hardware projects.

**Dave Jones:** So how many of these things are you sold now? How many are out there in the world? Of bus pirates? I've certainly got one. And I think somebody sent me another one.

**SPEAKER_00:** People ask me that. It's really hard to say because of the number of non-official channels and quasi-official channels. Yeah. Guestimate? I would guess there's somewhere between 50,000 and 100,000 of them.

**Chris Gammell:** Wow.

**SPEAKER_00:** Dang. Awesome. I mean, that's still very tiny compared to large production runs, I'm sure.

**Dave Jones:** But as kits and hardware products go, that is an absolute winner. Right. Generally, back from the old magazine days when I was a boy, you know, when you published a magazine, if there was 1,000 of them, that was, you know, you had made it. You know, that was a massively popular project if you sold 1,000. Yeah. But nowadays with the internet and the communications revolution and, you know, where you've got an instant ready, like on Hackaday, you've got a ready audience of, you know, many, many tens of thousands of people. Then, yeah, it's easy to sell 1,000 of something these days if you have the audience or you get it listed on the right blog. So, yes, 20, huh? Yeah, I never thought we'd sell 20. Oh, boy.

**Chris Gammell:** Been there, done that. So, you're still working with Seed Studio on everything though, right? Is everything kind of still…

**SPEAKER_00:** Yeah, it's one of the things that makes us sort of unique. We are almost exclusively an open hardware design shop. I have never sold anything myself. I don't run a website that takes money. I don't do any of the fulfillment stuff, what I derisively call putting things in boxes, stamps on them and taking them to the post office.

**Chris Gammell:** So, you're the smartest electronic designer in the world. Is that the idea then?

**SPEAKER_00:** Well, I think what I'm good at is designing hardware, writing documentation, keeping a blog going. What I'm not good at is doing the fulfillment side. Yeah, yep. And Seed Studio is there in Shenzhen, China, where the vast majority of the world's stuff is made these days. And they're right in the middle of it and have experience doing it and they do quite a good job. Yeah. Especially for very small runs, which, you know, nobody's doing these tiny runs. And to have someone supporting open hardware with batches of 100 to 500 to 1,000 is just really excellent. And they do a fantastic job at that and they work with other designers too. So, it's not just my stuff on a site I'm trying to promote. I have the benefit of other people coming to the site for other people's projects and seeing mine and wanting those as well. So, what we do is exclusively the design. And what I like to say the stuff we're good at, I'm not sure everyone would agree with that. But I'll say that now. I think the stuff we're good at is the design and the documentation, writing firmware, providing user support. And we farm out all of the manufacturing, all of the fulfillment, all of that stuff to see the studio. And to a lesser extent, of course, our distributors. We have distributors around the world who also take care of selling things and advertising our projects.

**Dave Jones:** You're saying we there. Have you got more than one person working at Dangerous Prototypes?

**SPEAKER_00:** Yeah. That's sort of a unique thing about us as well. There is no central office. Everyone works wherever they are. But what we generally try to do is hire people out of our forum. So, if we have people somewhere where we can afford them who are looking for a job and we can arrive at some agreement that everyone's happy with, we try to hire people out of our forum. That's the advantage of they already know our stuff, generally inside and out because we're open source. You don't have to train them. And you get to see what they can do up front.

**Dave Jones:** Yep.

**SPEAKER_00:** Without having to go through any sort of job interview.

**Dave Jones:** Got it. Is that like a – so, they're not really full-time employees as such. Do you do it like on a contract basis or you just – is it a very informal handshake kind of, yeah, we'll pay you X a month and you write some documentation for us or something?

**SPEAKER_00:** For – well, we have three full-time contractors.

**Dave Jones:** Oh, okay.

**SPEAKER_00:** Right. Yeah. And that, of course, we have contracts and everything is fairly official.

**Dave Jones:** Right.

**SPEAKER_00:** Then aside that, we have a number of part-time contributors, both people who are more like contractors who have a contract for X number of hours or X number of dollars per hour or something like that. And we've got probably four or five of those who work to varying amounts. And then we pay people who contribute to open source. So, if we have a contributor who drops by and puts a new chunk of code down, if we have people who are active and providing user support in our forums, if we have someone who contributes a new project and says, will you guys please consider making this, then we will pay them as much as we can. Nice. Whether that's a chunk a month while they're contributing or royalty for a project or whatever. We just try to find some way to make open source pay because I know one of the coolest things for me is that open source could actually pay money.

**Dave Jones:** Yes.

**SPEAKER_00:** Not just something I'd love to do as a passion. I would do it regardless of whether I got paid. Yeah. But what's really cool when you actually get a check from that work that, you know, you did for fun, not because you needed to eat at the end of the day. Right. And I like to give other people that feeling with, you know, as often as I can as well.

**Chris Gammell:** It's like in Fight Club where they get to go from just the one day a week to seven days a week, right? That's what it enables. You know? I come Tuesday and Thursday.

**Dave Jones:** And the interesting thing there is that you're still able to do that while still taking the minority of the retail price. Because as, you know, like as everyone knows in this kind of business, the person who makes the most money on this stuff is the retailer, i.e. seed studio who do it all. I mean, you're only taking a relatively small percentage of the retail price there. So it's amazing that you're still able to do that and run that business and pay these people even though you're sort of – don't like to say getting the breadcrumbs. But, you know, you are probably getting the smallest percentage, not actually retailing the hardware yourself.

**SPEAKER_00:** Yeah. To some extent, I would agree, especially when it comes to distribution deals. You know, we really take a hit to get our stuff out there at the distributors. And that's fine because it's a partnership where we make some money, they make some money. But more importantly, we have a larger presence. And that has a value too. But with Seed Studio, it's not quite the same as licensing deals other open hardware designers have with, say, SparkFun or some of the other companies out there. We actually get a quote at $100,000, $500,000, $1,000, $10,000. And then we decide how many we want to order.

**Dave Jones:** Yep.

**SPEAKER_00:** And then we set the final price. So we get the difference in price there. We're not just working on a percentage royalty with Seed. Oh, okay. Right. Got it. And just, you know, when I privately compared what other people are doing with their projects, I think Seed treats us extremely well. I think that model – we come out on top with that model compared to what I've heard other people doing before. Got it. But I still want to object to the breadcrumbs comment. Okay. We're doing a little better than breadcrumbs. I don't want someone to think – No, you certainly are.

**Chris Gammell:** I mean, you guys support a lot of people, though, Timmy. Like, your forum is huge. And, I mean, is that – so you said you get contributors from there, but you also get new projects from there. Are you guys still doing the – was it every week you said that you do new projects? Is that still – Month. Every month?

**SPEAKER_00:** Sorry. We try to – on average, we try to have 12 new projects put into production a year. That's crazy. Now, because of the absurdity of getting a project produced, that may be five projects one month and then a project every couple months. But we try to think on average, we get 12 new projects a year into production. And if we're having a slow year, sometimes that can include revisions as well. Okay. We're counting it. If they took us any amount of time.

**Dave Jones:** Although, granted, these are mostly bareboard-type projects, right? It's not like you have to design whiz-bang enclosures. Oh, here comes Dave talking about enclosures. You're not selling that commercial product. Yeah, yeah, yeah. Exactly. Yeah. No, you're absolutely right. It is substantially easier to get just a bareboard out there than it is to – Absolutely. Yep.

**SPEAKER_00:** Yes, yes. We do only bareboards.

**Dave Jones:** Because otherwise, you wouldn't be able to do 12 a year, I think, if you had to develop a full-on – No, no, I don't think so. You know, a full-on commercial-looking product.

**SPEAKER_00:** Now, we do have a standard PCB size now. Oh, yeah? And we can come back to that. It's supposed to make it much easier to kit things up and to case things. But we're still working on that. That's good. Right. Besides the 12 boards we try to produce every year, right now we're R&Ding about one project a week. Wow. And most of those go up onto the blog. Most of them are ideas where we put up a schematic or a PCB, and that's the end of it. Many of them will send out and have the PCBs made. And we have a store that we call the Free PCB Store. It's just a simple Zen cart store. And I keep an inventory of all the boards I've had made there. And then people can get a free PCB coupon and check out or buy a board with their free PCB coupon. And then they can build the project themselves. So a lot of our projects we'll design, we'll open source it as public domain, take it and make your own fortune off of it. But we decide ultimately that the cost-benefit ratio of getting it into production versus supporting it and what we're going to make on it in the end just isn't worth it. But because we're all open hardware buffs and what we want to do is design hardware, we do that. Even though it's not necessarily a profitable part of the business, we're still designing things that have no chance of being produced. And I think that's one thing that you can do as a very small, very loose-knit open hardware company that I could never do if I had an actual manager telling me how I should spend my life.

**Chris Gammell:** Well, I had this great idea. We're going to give stuff away.

**Speaker ?:** Yeah. You're fired.

**Dave Jones:** Well, that's essentially all part of the game, really. I mean, if you enjoy doing that sort of stuff, that's what you do. And it helps build up your rep as well when you're doing stuff like that.

**Speaker ?:** Yeah, absolutely.

**SPEAKER_00:** It's great publicity.

**Chris Gammell:** Yeah. I like it. So what about travel? I mean, you've been – you said your manufacturer is out in China, in Shenzhen, or – I forget how Zach pronounced it. I always get it. Is it Shenzhen, right? That's how Zach said it.

**SPEAKER_00:** Yeah, I am not a China-phile yet. I've only been there a couple times. So give me a few more years and I'll have the proper pronunciation now.

**Chris Gammell:** But looking at your YouTube channel and talking with you online, you go everywhere. Is it like you've been listening to Johnny Cash songs and you've been everywhere, man? Or what's your deal?

**SPEAKER_00:** Well, for about the last year and a half or so, I've been doing the Maker Faire circuit. A year and a half ago, it was the very first Maker Faire I went to was the Bay Area Maker Faire in California. And Seed Studio was a sponsor that year and had a big booth and invited me as well as some of their other open hardware designers to come and exhibit there. And at the time, I had avoided going to Maker Faire's. I had avoided going to DEF CON, things like that. I just – I wasn't interested in being out there in that way. I'm kind of a shy, geeky guy. I didn't want to be seen. I didn't have my picture on my blog. Seed Studio thought I was a 50-year-old engineer.

**Chris Gammell:** I would – well, maybe you've changed, but I don't think you like that anymore.

**SPEAKER_00:** Well, no, and that's what I decided. After going to this first Maker Faire, it was like, wow, you actually have to put yourself out there. You have to be the face of your business. You have to own the process of pressing the flesh, shaking hands, saying hi, meeting people. And besides all that business garbage, it's actually quite fun. And you meet really cool people who know – well, for me, people who know way more than I know.

**Dave Jones:** There's always people who know more than you do.

**SPEAKER_00:** And are just brilliant people to talk to. Yeah. You know, it's just been amazing to meet all the people. And so after that, I went to Maker Faire in New York and the Open Hardware Summit. And from there, it just sort of cascaded into a year-long circuit of doing these Maker Faires in Japan, in Singapore, in Shenzhen, China. Goodness. And just all over the place, the UK and on and on and on. And when we go, we try to hook up with the local hackerspace. And we try to hook up with readers. You know, we have readers all over the world. So we try to hook up with some local readers and visit their local electronics part markets. And now in some of the places that used to be manufacturing capitals of the world, like Japan, you know, in Tokyo, they have Akihabara, which is a fairly well-known electronics part market. It's – now it's in decline. There's no question it's in decline. You're going to find more anime and more – Really? Made cafes and more, you know, weird, crazy Japanese stuff in Akihabara than you're going to find electronics now. But back in the day, it was the heyday for all the Japanese manufacturers to go there and buy parts that they would use in manufacturing. And people would go there to buy the absolute latest electronics stuff. So we did a video there. That was our very first video we shot in an electronics part market. And we went with Tokyo Hackerspace and shot a film. And I'll admit, the very first time we went was the Tokyo Maker Faire. And I – the video was unusable. We were gawking so much at everything, mouths hanging open, just sort of staring and pointing. There was nothing usable in this video whatsoever. Because you should post that if you can. I do. I do. If you can, you should just see all some cut takes. It's me and our regular shock. And we're both just sort of, uh, uh, and nobody said anything. So we had to go back in February and reshoot the whole thing with actually making an effort to talk a little bit.

**Dave Jones:** Oh, that's great.

**SPEAKER_00:** And so that still stands out, I think, as our most popular one. There's something about geeks in Tokyo.

**Dave Jones:** Yep.

**SPEAKER_00:** That, uh, they just go together well. And that's, that's been our most popular video. But from there, we made an effort to shoot a video in every, um, parts market we visited. So, uh, from there I went to Seoul, South Korea, which has a parts market called Chungachong. And the, the, the hackerspace there is right in the middle of that. So we shot a geek tour Seoul. And, uh, from there we went to Shenzhen, China, which has Hua Chongbei, which is, I guess, the world's largest wholesale part market. Mm-hmm. There's thousands of little stands covering six floors of 20 buildings. Oh. Uh, you know, over a whole neighborhood with nothing but switch samples and connector samples. Yeah. And, uh, you know, crystals and resistors and, you know, anything you could possibly want. And we've been doing our best to shoot what we call our geek tour videos there and show what it's like, how people buy things, and importantly, how people like us, how hobbyists can actually use these markets. Because most of them are intended for big manufacturers. But you can get in there as a hobbyist and buy things as well.

**Dave Jones:** Yep.

**SPEAKER_00:** So it's just been, it's been an amazing last year and a half to do all of that travel. Put in a lot of miles. Learned how to do a long-haul flight, which was something I was not a fan of before. But now I can kind of lean over and sleep. Yeah. Well, I think putting the tray table down and sleeping on it, that's how I made it to Tokyo and back this time. Oh, dearie. And recently we did India, which was, you know, that was an amazing trip. We went to India and met up with 20 readers in Bangalore and rented this crazy painted up magic mystery bus, we called it. And they took us all around Bangalore and we visited all of these industrial sites. Nice. And we saw, you know, a PCB stuffing factory and we saw open hardware shops and we visited their local electronics wholesale markets. And we actually did that throughout three cities in India. And it was just an absolute hoot. Nice. Amazing time.

**Dave Jones:** Dilly Billy.

**SPEAKER_00:** You mean did I get sick?

**Dave Jones:** Yeah.

**SPEAKER_00:** Dilly Billy. Oh, no, no, absolutely not. The food was amazing. I was quite careful about what I ate. I'll admit that. I have a rule on all of these trips. Right. Just because when you're on business and you're having a really tight shooting schedule, you actually feel like you're making a TV program. Right. Which is, you know, it's very hectic and you're up really early writing up your locations and what you're going to say there and what you need to show.

**Chris Gammell:** Gabe, is that how you do it?

**SPEAKER_00:** I don't think that's how everyone does it, Ian.

**Dave Jones:** I have to say, I think. That's what. I remember getting sick once, like when I went to the US. I got food poisoning at the Hilton of all places. And that knocked me around for two weeks. I didn't, almost didn't eat anything for the next two weeks. I was, and I came home and I had lost like 10 kilos. I was like, it was shocking. And yeah, that, yeah, that sort of thing. You have to be careful. It can ruin your trip.

**SPEAKER_00:** Yeah. I'm very careful on all the trips, even ones in first world countries for that, that very reason. And you're eating on the roads. You're always eating things that are questionable quality anyways. But you know, my rule is hot and fresh. If I can see it cooked, I'm okay. If it's steaming hot, I'm okay. But, and it doesn't matter if it's from the street, you know, street. Food or restaurant or whatever. Those rules usually serve me well because there's nothing worse than getting sick on one of these trips where every minute is already accounted for. And you can't lose it. And even if you are sick, I'd probably have to go shoot the geek tour video. Sick.

**Chris Gammell:** I have your next, you know, monthly project. You could do a DIY IR thermometer and you could just point it at stuff. Be like, I'm not eating that. It didn't cross the threshold.

**Dave Jones:** All you've got to do is just deep, deep fry everything. Just live on deep fried grease for two weeks, you know.

**SPEAKER_00:** In a lot of the places, that's pretty unavoidable. That seems to be what their local cuisine is.

**Dave Jones:** Yeah. Oh, man. Speaking of India, we have a question from, I will not even attempt to pronounce his username on Reddit, who's from India. He met you in India. Yes. His name is Yagnesh. We hooked up with Mumbai. Yagnesh. Yes. He already says you've answered this question, but it could be of benefit to a larger audience. And you've read the question. You've probably already got a response to it. How do the seed guys produce the bus pirate? And can you step us through the process from the start? How do you do DFM and all that sort of stuff? How do you load the firmware on the bus pirates? Is it done one by one? Or is there a custom jig? All that sort of stuff.

**SPEAKER_00:** Sure thing. Sure thing. So DFM is designed for manufacture. And in my experience with seed, since we hand prototype everything and we use 0603 size and no chips smaller than SSOP and fairly hand solderable friendly stuff, we don't have to do a lot of DFM. We don't have to do a lot of prep to get something ready to be manufactured. Most of our stuff has to do with sourcing, getting the right parts, making sure that the parts they can source in China are the same as the parts we use. Yes. And also making sure, you know, seed is very keen to make sure that everything works perfectly. So if I give a part number for a 3.3 volt regulator and it's not available in China, they will sometimes go out of their way to source it from the US. Yes. And then they're importing it back and paying duties when, in general, we use very generic parts where that's not necessary. Right. So sometimes a quote will come in and I'll say, well, that seems really expensive. And I'll ask and it'll be because they were worried that the part they could source locally wasn't good enough. And so they went ahead and sourced from the US and then it costs more than expected. So we have a lot of back and forth on that. But as far as modifying our actual hardware to prepare it for a pick and place, we've never really had to do that because we already designed fairly, you know, to lose standards. To something many people will be able to hand solder. We also design according to a standard part list now. So most of the things we do, we don't have to tell them a specific part number. We just tell them what from our standard part library we're using. Right. And so you can go out and get that much faster then. And they stock basically a set of parts that work on all dangerous prototypes boards.

**Chris Gammell:** Oh, so you got to watch out there, man, because now you're becoming the bigger company now. You're going to have your own part number system and then it gets all crazy.

**SPEAKER_00:** We're actually in the process of doing that very thing. We want to put together a part kit of our parts enough to build essentially 10 of any board we have. And, you know, we've got all these free PCBs so people can then use the part kit to build the boards and have all the parts without hiring them.

**Chris Gammell:** That is a great idea. But looking at old schematics, I have an old Wurlitzer and the part number is like 111124. So don't do that. And that's it. That's the only Disney that has written marking on the schematic. And I know it's an NPN. That's about it. So good luck. But that's an interesting topic, too. I mean, that's great. I mean, blog fodder, too, of just like how you're setting up part numbering systems. Of course.

**SPEAKER_00:** Yeah, we're going to design our own data sheets on the weekend. Really? That's cool. Along with, you know, basically a minimum set of tolerances, saying a part should fall within these tolerances, not specifying necessarily a part number. We will, of course, specify maybe three dozen part numbers from different manufacturers that would fit these criteria. But, you know, generally, unless you're when you're just doing digital work and you need an NPN transistor, there's only two or three you really need to stock.

**Dave Jones:** Yep.

**SPEAKER_00:** You know, a big current one, small current one, and generally you can get away with one. I mean, we use 99% of the time one general transistor. My inner analog guy is screaming right now.

**Chris Gammell:** No! Yeah, exactly.

**SPEAKER_00:** The thing that's cool is analog people are going to, like, bash me over the head and never want to read my blog. And that's understandable because analog is not my thing and I don't do a lot of analog. But in the digital world, we can get away with a very select, limited part list along with a good resistor kit, you know, with plenty of values and 1%. Exactly. You're good to go. And it's all done and dusted, yeah.

**Dave Jones:** I mean, they're almost entirely different worlds because you essentially cannot do what you're doing with more complicated analog or more specific products, you know. No, absolutely not. Yeah, but then it's not mass market either. I mean, it seems every – well, that's right. I mean, that's the main thing. It seems like every project I'm doing, I've got – I'm using 10 new parts in it that I've never used before, you know, and I have to use them because I'm trying to meet some cost or performance target for a particular project. And I just, you know, can't just, oh, use exactly the same part I used last time because it just doesn't fit the bill either in size or price or functionality or whatever. So –

**Chris Gammell:** Well, you've got to change your specs though too. That's the other thing. But, I mean, I think that the stuff – I mean, the stuff you guys are doing is still really advanced for a lot of commodity components. So it is cool that you're able to, you know, make these standard kits. I think that that's going to be really helpful in the future.

**SPEAKER_00:** Yeah, there's been some requests for it and we're just interested in getting the parts out there and making it easier. So people – I met with this guy Mitch in Shenzhen. He's doing Hackvana. Oh, yeah. We saw the video. And he's trying – right, currently he's making PCBs and solder stencils but he wants to get parts out there to hackers from the, you know, the flow of parts moving through Shenzhen. And one of the things he said that I just totally agree with is that, you know, you can spend 10 hours sitting there trying to fill your BOM with the cheapest, most appropriate part that you can get locally or doesn't cost a million dollars to get shipped from another country or blah, blah, blah, blah, blah. And you can spend 10 hours just sourcing parts for a project when somebody else has already done that. And maybe hundreds of people have already done that. And sort of the goal was just to make it faster and simpler to pull these parts out and build our boards specifically because we do give away so many boards. And we also spend a bit of time telling people where to find the parts that go with the boards if they're not on our standard list. And I think having this stuff available would be handy. Though I'm sure, you know, the open hardware – I did two years ago the Open Hardware Summit with Eric Pan. We gave a presentation and he talked about a standard part library that all of open source can use. And I think that's a very lofty goal. I'm not sure I would propose what I'm doing for all of open source. But I think for my little tiny corner over here, it could make it easier for people to build our crap. Crap. Come on, man. But I can continue talking about the seed building process if you like. Yeah, please do. Okay. So basically I wrote down some steps. I think some of them are pretty obvious, but I'll lead you through what I understand to be the process of getting a board made at Seed. On our side, the first thing is we get a quote. We send our part list and our board files, and we get a quote at – it used to be $20, $100, and $500, but they stopped doing $20s, and now you do $100, $500, or $1,000. And depending on the price and what we think we can sell, we'll order however many of them, and they'll build them and put them in the store. So I understand, you know, the first step is they send out all their PCBs. Many people may be familiar with Seed's inexpensive PCB prototyping service. My understanding is that the boards that are done in volume go to a different facility that doesn't specialize in quick turn. They are always a different color. They always seem quite – the more bulk boards seem to be higher quality. I'm very happy with the proto boards as well, but the bulk boards just seem to be, you know, like they're done through a proper PCB process instead of a quick PCB process. Yep. From there, they source all the parts, you know, from all over Shenzhen. If they can't find a part that matches, they'll import when they have to. But it's actually quite expensive to import American parts into China. There's fairly high tariffs on that, as I understand. That's interesting. And then for small batches of, say, 100 and sometimes even 500, Seed will do pick-and-place in-house. You know, they have their own pick-and-place machine, the same one SparkFun has, the same one several open-source hardware shops have. And they'll pick-and-place batches of 100 to 500 and things that need to be turned very quickly. They'll do right there in-house. For big things, you know, if we do a batch of 1,000 or more than 1,000, those get sent off to the professionals all over Shenzhen that do nothing day or night but assemble boards. You know, they're very good at it. It's what they do all the time. And they have very high yields. From there, I guess they inspect visually. For a new run, they'll inspect absolutely every board visually. I think for runs that are established, they depend more on the self-test than the visual inspection. So then from visual inspection, they'll move on to be programmed. With our boards, we do basically a ROM. The same way you have a ROM from a video game or a ROM, like an ISO from a CD-ROM, is an image that has all the information you need to put into the chip. So if there's a bootloader for doing upgrades, it's got the bootloader. If it's, you know, as a firmware, the firmware's in there too. So it's a single step. You program this one manufacturing image into the device, and it's got bootloader firmware, unique ID, whatever you've got to put in there. It's all in there in one programming step. And someone mentioned on the Reddit that it wasn't SparkFun bootloading. And yes, that's true. At one point, SparkFun was building the Bus Pirate, and they were programming the bootloader. And there was a little quirk in one revision of that silicon where the internal oscillator wasn't stable enough to support 1500 BPS.

**Dave Jones:** Right.

**SPEAKER_00:** 115,000 BPS, whatever, on all the chips. Some of them wouldn't program at that rate. So they had to back it down to 9,600 BOD. So they were programming the bootloader and then connecting to a computer and programming it over the bootloader at 9,600 BOD for each board they sold. And SparkFun was selling quite a few of these. And I eventually found out about this, and I immediately wrote to Nate and said, you know, you guys, we have this manufacturing image. You just program it in there, one fell swoop. It's done. No bootloading at all. So the Reddit mentioned that, so that's why I bring it up. So we program one master image with a PIC programmer and then run an internal self-test on the Bus Pirate. So basically you can jumper two pins, and that allows the Bus Pirate to turn on its power supplies and measure the voltage, make sure it's what we would expect, to test various chips on the board like the 4066 that's used to control the pull-up resistors. We can check that. We can check various parts of the board to make sure basically the pins are moving the way they are. There's nothing that's soldered together. No two pins are soldered together. There's no problems like that. So every board we do with Seed, they run some sort of internal self-test like this on the board. So we know when it leaves Seed, it's in good working order. That doesn't mean things don't happen along the way. You know, shipping is brutal sometimes, and bad boards do get out there. But we actually have very high success with our self-test, and it's so high that when we have a complaint in the forum, we immediately say, we're just going to replace it. It's very rarely we have something that's a defect, and when it shows up, it's fairly obvious. And we say, we'll just send out a replacement. Don't worry about it. You don't have to return anything. Just, you know, we'll give you a new one. And that's my understanding of how the process works with Seed.

**Dave Jones:** Did you design that built-in self-test from the start? Did you go, right, we're going to manufacture a zillion of these things. We really need to think about how we're going to do the built-in self-test? Or did it just go, oh, yeah, look, just by coincidence, we can just write a few lines of code, and the hardware is already capable of doing that?

**SPEAKER_00:** Well, yeah, I give a presentation on getting your stuff made. And one of the steps I mentioned is that to design your self-test, some way of testing this widget, before you get to that stage, you need to think of it from the beginning, because it's so hard to either bring out test points and design a rig or reverse engineer a test into it. Now, with the Bus Pirate, I got extremely lucky, because it's a tool essentially for measuring things and debugging things. By jumpering a few pins, we got it to test and debug itself. So that was really just an absolutely lucky break. But I highly recommend people design it in from the beginning. And now everything we make, if we need extra pins to do a self-test, we'll move to a bigger chip if we have to. Because the added cost of having to reverse engineer that test into the device at the end, instead of doing it from the beginning, is not worth the extra cost for our low volumes of using a bigger chip, using a bigger CPLD or field programmable Gatorade to get a little bit of extra test logic in there or something. You know, you got to design for tests from the beginning. It's absolutely necessary.

**Dave Jones:** Now that you know, right? Yeah, now that I know. Yeah, exactly. Everyone has to make that mistake.

**SPEAKER_00:** Yeah, yeah. One thing I haven't been able to cover is people often ask me how you do the self-test. And of course, that's going to depend on how your hardware is set up and what you're doing. But obviously, I generally say, you know, have some spare analog to digital converters so you can measure voltages from anything that's supposed to be voltage-based. Have a few pins so you can detect logic one or logic zero from things that are logic-based and start from there. It doesn't have to be very complicated. It just has to be on the board and ready to go.

**Dave Jones:** That's the advantage of using a larger pin count micro than what you need, for example. Like, you know, if you need 20, you know, say 18 I.O. pins, don't use a 20-pin device because then you've got no spare pins left over to do anything like that. So that's the advantage of choosing a larger device up front that has more capability built in. And then just all those spare pins, well, I've got a dozen spare pins. What do you do with them? Well, don't leave them floating. Connect them to various points in your circuit just so that later down the track you can implement that stuff in software rather than have to mod the boards later or not do the test and be caught short.

**SPEAKER_00:** Yeah, absolutely.

**Dave Jones:** Trap for young players, folks. Which I do time and time again still, you know, because I just like the elegance. Well, because I like the elegance of using just an optimized chip for the, you know, for the job and not just using some big-ass one.

**SPEAKER_00:** You just sneak it in and out of the wire. Yeah. Have you worked with any chips with the programmable pin placement?

**Dave Jones:** Yes, yes. That's really nice. So you can send the UART to any one of the pins, for example. The PICs have that capability. Well, many of the PICs have that programmable pin. Yeah, the PIC 24s have that capability. I've used that. And that is quite nice. If people don't know what we're talking about there, it means like all your internal stuff like your UARTs and your SPIs and your ADCs and all those, you know, all those features built into the chip. Most micros on the market, they are two fixed pins. They're connected up to fixed pins. But some micros, like the PIC 24 we're talking about, you can actually, they have an internal routing logic, kind of like, you know, an analog FPGA routing thing that allows you to route that UART to any two pins that you like. And it's just really nice.

**Chris Gammell:** Yeah, that really helps during those oh crap moments, right, where you're like, oh, oh no.

**Dave Jones:** Those oh crap moments, yes, yes.

**SPEAKER_00:** No, that's the principle that the Bus Pirate is based on as well. It uses one of these chips with selectable pins so that we can move all of the hardware modules to whatever pin combination we need for whatever test mode the Bus Pirate is in. And you just mentioned loving a very simplified and direct design. And it made me think of that. I know there's several other chip families that now have programmable pins as well. I've worked with some of those. And I just love it for the routing, the elegance of the routing. When it goes essentially straight out from the chip, you don't have any vias jumping under and coming back up the other side. And you're not routing things around in snake-like fashion. You literally come straight out from your chip and everything hooks up just perfectly and nicely. And I'm a big fan of that too.

**Chris Gammell:** Yep, me too. So have you had any big oh crap moments with, you know, with, I guess, I guess the open source hardware side of it would probably have a couple more eyeballs on it than maybe a proprietary project would. But have you guys had any, you know, huge defects that, you know, maybe might be lessons for people or?

**SPEAKER_00:** You know, we've been very fortunate that so far we haven't produced a batch of anything that, for example, had to be reworked. Oh, that's good. Or modified or anything like that. Yeah, I've been very fortunate so far. I'm also really paranoid. Back on wood, right?

**Dave Jones:** Damn, he's not going to sleep tonight. Yeah, right?

**SPEAKER_00:** It scares me to death to put something with a problem into production. And then what would happen with those boards to have, you know, a hundred or a thousand of something rotting in a warehouse in China somewhere that I can't do anything with.

**Chris Gammell:** I think you have a lot of goodwill as well, though, from it being open source, right?

**Dave Jones:** Oh, people would understand. Yeah, exactly.

**SPEAKER_00:** And part of doing the free PCB giveaway is that most of our boards, by the time I get around to building and programming and testing it, somebody else has already done it. Maybe two or three people. Oh, really? So we actually, you know, crowdsource that side a lot. Right. And so we actually have not just many eyeballs on the design, but we make it possible for people to get a hold of the board and build it themselves. And, of course, anybody who's building service mount stuff themselves and just wants the PCB and has their own parts, they're pretty bright. You know, these are really talented, amazing people. And they always point out a number of things that, you know, we should consider before we put it into production. And on top of that, we also generally do our development in the forum as well. So we're not just open source, we're open development. Nice. And our projects will be in our, you know, in our SVN archive, in our file repository. We'll post progress on the blog. We'll post updates on the forum. So a lot of the time, even before we send off the first PCB, there will have been a dozen or more people who have looked over it and told us these horrible, horrible mistakes we're about to make. I was going to say, an electronics designer always has plenty of time to go back and fix them. Yeah. That's brilliant. One thing I did have a minor problem with was the second project I did, which was the Twitter watcher, a little network appliance that would connect to Twitter and get the most recent trending topics, as well as some tweets to go with them. They needed a unique Ethernet ID. Oh, yeah. I forget the whole IEEE whatever ID. It's sort of like a USB ID, only instead of being a per device, it's like each individual unit should have a unique ID. Yep. And nobody, I hadn't planned for that. I hadn't really thought that through. And so I ended at the last moment buying a bag of those, Microchip makes some EEPROMs with a built-in Mac, their Mac address. Yeah, 24-bit unique ID stuff. A built-in Mac address. Yep. And so I just pulled one out, and they all got that same Mac address.

**Speaker ?:** Yep.

**SPEAKER_00:** But at least, you know, the license said I couldn't, you know, I couldn't use microchips that they had used in their demo. That was against the license. So it was a whole oh, crap moment. And I ended up taking a train to the nearest parts supplier that had them on stock, getting them that day, reading it out on the train so that by the time I got home, I could recompile the firmware with our own custom unique ID in it. And then, you know, putting a screwdriver through that chip and mounting it in a frame to say this is our destroyed Mac chip with our official Mac number in it.

**Dave Jones:** Nice.

**Chris Gammell:** Should you, like, encase it in amber and it's like the holy grail chip then?

**SPEAKER_00:** Oh! I should do that. I could put it in a big block and use it as a paperweight.

**Chris Gammell:** Or you should, like, wear it around your neck or something, you know, be like, this is the one. So what about some of your other projects? I mean, you have, I mean, I'm looking at the forum, and there's a really nice layout of all the different projects and stuff. But could you maybe give us some of your other favorite ones to work on and, you know, how other people helped contribute with all that stuff as well?

**SPEAKER_00:** Yeah. Okay, well, our number one thing is the Bus Pirate, and it's basically a tool for talking to chips. So you have a little terminal window, and you can type in the values you want to send to a chip, and it will send it and get any reply. That helps you avoid that development cycle where you write some code, program it to your microcontroller, you know, try it out. It doesn't work. So then you make some changes, compile again, program again, try again, and you go on this loop trying to learn how a new chip works. With the Bus Pirate, you just type a few commands. It sends it out. You know the protocols most likely correct and working. So if there's a problem, it's something to do with how the chip is working or how you've got it connected. So you're eliminating a lot of the problems you have with learning how a new chip works. Some of our other popular stuff is, like, the Bus Blaster is extremely popular. And this is a JTAG debugger. And JTAG is the programming interface for lots of modern chips. ARMS use it, but also field programmable gate arrays and CPLDs and things like that. Lots of chips have this standard programming connection. And there's lots of open source software out there to support JTAG, like OpenOCD is a full debugger for ARM chips. URJTAG is used to program field programmable gate arrays as well as CPLDs. But most of them are still using commercial programmers. Most of them support a range of commercial programmers and a few homebrew sort of hack kits. And I thought, you know, I'd really like to make open hardware to go with open source software. So I designed the Bus Blaster as sort of a universal JTAG debugger. And what we did was we took the same chip that's in every manufacturer's low-cost JTAG debugger, as well as most of the hobby debuggers, the FT2232. It's the bigger brother of the little FT232 that's on the older Arduino. And it does USB to serial conversion, but also USB to JTAG. And it has two JTAG channels. So we thought, well, the only difference amongst manufacturers' programmers that use this chip is the buffer logic on the front that translates voltage. What if we used a CPLD and made the buffer logic programmable? And then to one-up that, we'll connect the CPLD's JTAG connection to the secondary JTAG connection on the Bus Blaster on the FT2232. That way, you can, over USB, upload an entirely new programmer logic into the CPLD on the fly. So if you want a KT-Link programmer that supports the new two-wire debug protocol, you got it. Just upload it over USB. You want the classic JTAG key programmer that works with just about everything. You upload that buffer image. You got it. It's good to go. And along with that, I might add, that CPLD is able to help out with the self-test so that we know all of the things are functioning properly. Right. And that has been one of our most popular boards. And I might also say the one that requires the least amount of support. Probably. Since it's all dependent on the software and it's very much just a hardware design with a little bit of programmable logic, we hardly have to support that at all. So I'm a big fan of the Bus Blaster. Another one we did recently that was surprisingly popular is our ATX Power Supply Breakout.

**Dave Jones:** Oh, yes.

**SPEAKER_00:** So lots of people use an old ATX Power Supply from a computer to make a bench lab supply. You know, you've got plus and minus 12. And if you're working with an op amp, having that negative voltage rail is a lifesaver. And if you're like me and you're in the digital world most of the time, you won't usually use it or need it. But then you have that one project where you need an op amp and you just don't have a negative rail. So a PC Power Supply has plus or minus 12 volts, a big hefty 5-volt supply, and a 3.3-volt supply. So just about everything you need on a day-to-day basis. And a lot of our forum users have hacked their power supplies to be a useful bench tool. But many people like me don't want to go in there and mess around with something that's UL listed and rated and where there's big coils and capacitors full of dangerous AC electricity. So we built a breakout board where you just plug in an ATX Power Supply into it, and it brings all the main voltage rails to screw terminals that also have banana plugs that accept banana plugs in the top. There's indicator LEDs, so, you know, each line is good. And it's fused at 1.25 amps, which we thought was a respectable amount because it's comparable to what you would get out of a TO220 voltage regulator. You know, you can obviously get 30 amps off of the 5-volt rail of some power supplies. But you probably don't want it. But, you know, you short that out, you don't want to get a lot of trouble. Right. So we thought the 1.25-amp resettable polyfuse was a safe way to go. And people who want more than that can solder a coat hanger over it or whatever. Yeah, exactly. You know, you have the option to go dangerous if you want. Well, there's dangerous prototypes, right?

**Dave Jones:** Well, you can have a jumper on there labeled dangerous, and it just shorts out the fuses, you know? Boom. A little jumpy.

**Chris Gammell:** Engage danger mode. Yeah. I mean, this board is incredibly affordable, too. I mean, like people listening might think, oh, well, you know, that's probably going to be, what, like $20 or something. It's like $4. That's insane. I mean, you get an old computer and a $4 board, and you're ready to go. That's crazy.

**SPEAKER_00:** Yeah, I think right now, actually, I think it's coming in at $13.

**Chris Gammell:** Oh. Oh, no. I'm looking at the case. Sorry.

**SPEAKER_00:** Oh. Ah, sorry. Yes, no. We're going into cases because we're trying to put everything into a standard board size.

**Chris Gammell:** Oh, yeah. Oh, that's right. Okay.

**SPEAKER_00:** And that way it's easier to recycle cases. We have, you know, there's, for the bus pirate, there must be 200 user-designed cases on Thingiverse, on the various sites that let you put up an open source 3D printed or laser cut thing and then buy one of your own. And we keep changing form factor to fit whatever cheap case we could find in China or whatever manufacturer's case looked cool. And they're always so ugly. They're these ugly, ugly beige cases. So I looked at all these parts markets when we went on our geek tour. I was on a singular quest to find a cool-looking project case. You want something where you can show off your work, where you can go to your local hackerspace and say, you know, I made this. And let me explain to you how it works. And you don't want to hide that in some ugly beige plastic box. So we set out to do something a little better and make those user cases recyclable, not just amongst our own projects, but for people who want to use them in their own projects. So we standardized on a set of, I believe, 11 circuit board sizes. There's a golden ratio size, a golden ratio rectangle, as well as just a square size starting from, I believe, 3x3 centimeters going up to the Eagle CAD free maximum of 10x10 or 10x80, I believe. Somewhere in there. And we also have, so we have a footprint library for Eagle, where literally you toss whatever standard board size you want on your schematic. And then on your board automatically appears the nice board in the right size with the nice rounded corners. Oh, yeah. Mounting hole placements in the correct places, as well as suggested placements for things like USB mini B jacks, headers, things like that. And then the idea then is that the cases that are up online that someone designs for the bus pirate, then you just use the bus pirate footprint, which I believe is the 60x37 millimeter golden rectangle. And then if you design your project on that and use the USB placement and whatever, anything that works for a bus pirate will now work for your project, too. And so we're also going to say, now Dave can stop complaining.

**Chris Gammell:** All right. Thank you, Ian.

**SPEAKER_00:** So we've got it not only for Eagle, but we also have the library available for KeyCAD. Yay. And we're working on getting it available for more professional suites as well. But most of our users are still in the hobby or pro hobby space. So we don't have a lot of people using Altium or those really expensive CAD packages yet.

**Dave Jones:** I'm frantically looking for this enclosure now. Dave's going to design it by the end of the show.

**SPEAKER_00:** The system is called Sick of Beige, both for the sort of lewd innuendo, but also just because it really, I said, I'm fed up and sick of these beige cases. Am I able to, oh, here we go.

**Dave Jones:** Yes, I'm able to Google that, Sick of Beige. It's the first link. Let's have a look.

**Chris Gammell:** Oh, boy. All right. We've lost Dave for the rest of the show.

**Dave Jones:** Yeah, just keep on talking.

**SPEAKER_00:** We've set out to do, just to start off, you know, we're not, I'm not a mechanical designer. I'm not good at that. That's not really the thing I like to do. But just to kick things off, we've designed simple laser cut acrylic cases, you know, the simple sandwich case with a plate on the top and a plate on the bottom and some standoffs. And the small ones come in, I believe, at $3. And the big one, like for the ATX case, $4. Yeah. So these are very inexpensive to manufacture and to sell.

**Chris Gammell:** Yeah, that's great. And I'm sure, you know, we're going to start seeing a lot more of those just pop up everywhere, too, because it is.

**SPEAKER_00:** I've actually seen a surprising number. You know, we started off just to do it for ourselves. So we stopped jumping around and following various manufacturers' own preferences and said set our own. And that way, if we do things using the same basic size, we can recycle the case even amongst our own stuff. So if we want to injection mold a case for the Bus Pirate, well, if Bus Pirate version 4, 5, 6, 7 all use that same profile, then our investment in injection mold is, you know, we can drag that out over some time. And it's not such a big upfront investment that we don't recoup over, you know, multiple versions.

**Chris Gammell:** It'll be crazy when you actually see vendors start matching that, too, right? That'll be the point where you know that you win when you see. That would be excellent.

**SPEAKER_00:** For now, I've seen it show up on Hackaday. I've seen it show up in a lot of the projects that users are doing in our forums. And, you know, I didn't expect that. I really only designed it for us to use, so we stopped jumping around and torturing our case designers. But I think some other people are seeing the value in it, if only because it's one step to throw down the thing on your schematic, and you get the board with the nice round corners. You know, there's no work involved in that.

**Chris Gammell:** Man, that's how a lot of the best tools come out, too. I mean, you know, you talked earlier about the bus pirates starting like that, the cases starting like that. You know, you look at some CAD programs. You know that some of them are probably internal to start with with companies. And they're like, oh, well, we should just sell this. You know, like that. It's just it's those are how the best tools are made because it's made for people that want to use them. So I don't know. I always like stories like that. I think I think that's a good thing.

**SPEAKER_00:** The case design especially comes from with help of our forum. We enlisted all of the case designers who had kicked out multiple cases for our projects and brought them in and said, hey, you're mechanical guys. You know, what what would your dream situation be? And we spent, you know, we spent probably two or three months going back and forth and working out the details on this until it was something that they were satisfied with. So we really tried to work with our community of designers to make it as easy on the case designers as possible.

**Dave Jones:** I'm looking at these now. Are they just so they just clear acrylic sheets? Is that the yes. And there's no side panels. There's no it's just a top bottom held together with spaces. Is that the idea?

**SPEAKER_00:** Yes. Yes. It's just a simple sandwich case. The idea is to keep fingers out and, you know, to keep your board from shorting out on the random screw underneath of it on your work. Right. And we provide everything is done in Google SketchUp. So it's a free, though not open tool.

**Dave Jones:** Yep.

**SPEAKER_00:** And we provide a tutorial so that people can customize these to fit their own projects quite simply. The idea is to make it really easy to use in your own stuff and then send off the sheets to whoever's cheap laser cutting service and have it customized for yourself.

**Dave Jones:** Because I've been thinking for my new project, I've been thinking about this exact concept, because if you don't have sides on it, then you don't need cutouts for anything. Right. You just have your right angle connectors on your board and that's, you know, bingo. You're done.

**SPEAKER_00:** If you don't have any high voltage. Yeah. Yeah. I agree. I like that concept as well.

**Dave Jones:** Oh, well, you know. Yeah. But then, you know, you get all dust in there and everything else. So it's not, you know, it has tradeoffs both ways. Yeah. No, you guys do conformal.

**Chris Gammell:** Ian, do you guys do any conformal coding or anything like that?

**SPEAKER_00:** No, no. No? Okay.

**Chris Gammell:** I don't think there's any need to, but it's just wondering because of that.

**SPEAKER_00:** In terms of cases, we just hope to get it started and then see what would happen there and also provide a modicum of protection with our otherwise bare boards. Yeah. You know, I'm so far away from putting something in a proper case or box that I, you know, wouldn't even be able to tackle that. That's something like, if we ever case things, it will come from the community. Right. Someone will design some awesome case. You got it. And then we'll say, oh, can we injection mold that and pay you some money? Right. And I imagine that's how casing will happen at Dangerous Prototypes. Right.

**Chris Gammell:** I'm guessing you're probably like me and you have it dangling from the USB while it's plugged in. You have it like dangling there so it doesn't touch the short out or anything. Absolutely. That's the way to do it, man.

**Dave Jones:** Can you see this, you know, you can buy this kit, right, this case kit. Can you see there being a service where you can also order a custom variation of it? For example, like I need 10 laser cut holes on the top of this, but I will use your existing format, but I need 10 holes cut in it and I need 100 of them. Is that or are you leaving that up to the individual to take care of that?

**SPEAKER_00:** I mean, until now, we've just left that up to people. We have a tutorial on how to do it yourself and all of our files are open source so you can grab our blanks and add your holes wherever you want and send it out. I don't really foresee us doing that. Right.

**Chris Gammell:** It sounds like a job for Pinoco, really. Something like that.

**SPEAKER_00:** Anybody who wants a side business and has a laser cutter is welcome to take our stuff and do that.

**Speaker ?:** Yeah, yeah, exactly.

**Dave Jones:** That's what I was getting at. There's a business there for somebody who, you know, can, yeah, you can buy these things in bulk and go, yep, you can use this same size and I'll laser cut your custom holes for it.

**Chris Gammell:** They can call it slightly less dangerous prototypes.

**Dave Jones:** Well, we've got a question from Gibbled on the, great username, on the Reddit list. When will the Bus Pirate 4 be officially released?

**SPEAKER_00:** I love that one. Yeah. Let me give a little background on it first. Yes, please. Bus Pirate version 3 uses a PIC24F along with an FT232 USB to serial converter as the interface. Now, you know, when I started the Bus Pirate, my goal was to have human scale interaction with chips. Literally, you need to write, you know, the value 255 to register number one while you type in one space 255 or 0xFF or whatever format you want to type it in, enter, and those values get sent to the chip. And that was the extent of my planning on the Bus Pirate hardware when we started version 3. And then, you know, over the years and now five years going on that it's been out and about, I think. Probably three years in serious production. People have hacked on and added so many features, not just user scale stuff, but, you know, a binary mode so you can write a script. It's supported by Flash ROM for programming, you know, little Flash chips and motherboards and things like that. And some of those are quite huge, like a 64-mbit chip programmed over a serial connection with all the overhead of a binary protocol. It would take hours on some chips. So, you know, we needed a way to make a faster interface. So Bus Pirate version 4 came up and we used a bigger PIC chip with more pins, four times more storage space, and most importantly, an integrated USB peripheral. Now, the problem with integrated USB is that you then have to have a USB driver for it in the chip. But Microchip provides what they call a Microchip Application Library or MAL. I can see where this is going. Which I like as malware because it comes with a license clause that says you can use it freely, but you can't actually include the source when you distribute it. So we could use their USB drivers with our firmware, but when we wanted to share the source, which is under a public domain license, we had to keep all the USB stuff separate and pull all of it out and then just distribute our source. So what good is that for somebody trying to learn something new? And I like Microchip's products and I like the people at Microchip, but that license is still the stupidest thing they're doing. They're trying to get students, people who are used to Arduino, to come aboard and do free demonstrations of their project, what essentially amounts to free publicity and free application notes. But they're going to stop a beginner from a one-click compile over this stupid licensing agreement. So at the beginning of the year, we were still, this year, we were still using Microchip's USB stack and pulling everything apart and the developers had their own version locally and blah, blah, blah, blah, blah. And at this point now, we had a user come and basically dump upon us a open source USB stack for PIC microcontrollers. Over the last few months, we've worked out most of the bugs. I think it's running pretty solidly. I think the latest firmware for the Bus Pirate version 4, the USB part is working without problems. And writing a USB stack is no small thing. I could never have done it myself. It's not a project I would be willing to take on. It's something, you know, you'd have to have a passion for doing it. I know the AVR one, the open AVR one, Lufa, you know, someone did it as a senior project, right, or as a university project. It was definitely a labor of love. And it's high-quality code, very well done. And I just don't think for a USB stack, I personally would sit down and do that. So I'm totally indebted to the community that made that happen. So we started off the year using Microchips Mal, and now we actually have an open source USB stack integrated there. The whole code base is available for download. You can do one-click compile and get into hacking the Bus Pirate version 4 yourself now. So we've come a long way. I would say a huge way, considering the amount of stuff that had to be done to really get this to be an open source project that I would want to release officially. Now, there's still a lot of things that have to be hunted down. There's still a lot of things that need to be moved from the old serial interface to the new USB interface. And that's before we even start taking advantage of all the new speed and opportunities we have with a direct USB connection. So there's sort of an instant speed-up because we're still using the USB CDC ACM, which is the USB to serial converter class for USB. And so it doesn't matter what you set the virtual serial port at. Most operating systems will just give you as much speed as they possibly can. So you automatically get that speed up with the new Bus Pirate. But in terms of taking advantage of the double buffering and all the really fancy features that we have in this open source stack, features I might add that aren't available in the microchip one, that's going to take a lot more work. And especially bringing that to some of the user-supplied features, things that people came and tinkered with and integrated into the code and we accepted. But they're no longer there maintaining. Call them up and admit that. It's a huge task. You know, it's just a huge chore. Yeah. And I keep telling people, version 4 will be ready when we release firmware version 7. And I have no plan for that. I have no roadmap for that. I'm just saying that will be, you know, the starter pistol when version 4 is something I would recommend to use in your lab for a project that you actually have to get done. You know, for now, version 3, it does everything version 4 does. It's tested, you know, it's been tested 10,000 times in 10,000 labs around the world. You know, it's been used in very brutal conditions as well as, you know, there's maybe 100,000 of them out there being used in hobby conditions. So you can be pretty much certain that the Bus Pirate version 3 will do the right thing for you when you're trying to figure out why your chip isn't working at midnight. Now, if you're doing version 4, you may be chasing down bugs that are my fault. Right. Bugs in the code base. Bugs in the compiler. Bugs who knows where. And that's why I keep telling people version 3. You know, it's tested. It's not the new sweetness, but it's tested well. And it's still the one we highly recommend that everybody go for. But version 4 is great for developers. It's sort of like being able to get the new iPhone before it's available.

**Dave Jones:** Yes. But Murphy will get you every time.

**SPEAKER_00:** Absolutely.

**Dave Jones:** So if you use version 4, Murphy's going to get you.

**Chris Gammell:** Absolutely. It sounds like a call for Amp Hour listeners to come and help contribute and help Ian with this next firmware release and to jump in on the project wherever people can.

**SPEAKER_00:** We're absolutely, you know, any developer's welcome. From one line of code to a spell-checked comment to whatever. We're just grateful for everyone in our community and anybody who wants to join is more than welcome.

**Chris Gammell:** Yeah. You mentioned SVN.

**Dave Jones:** Yeah. How do you find that that SVN thing works for developing firmware for an open source product like this? Like, is there one central person who goes, no, we're not going to include that in the official, in quote marks, you know, version of the firmware? How does that all work? Do you find there's an issue there?

**SPEAKER_00:** Well, you know, everybody's got their own style on that. Every project maintainer does their own thing. I'd really like to move to Git. There's a lot of pressure to move to Git. And I like Git because people can then push things to you instead of saying, here's a patch. Will you apply it? Or will you give me SVN access? Or whatever. People can just push things in. And I definitely see the advantage to that. I'm just not ready to move our whole shop over to it yet. But with SVN, right now what happens is we grew pretty organically. You know, it just grew as a community over time. And I'm just in the habit of giving anyone SVN access who wants it. Cool. If you're willing to write an email and say, I want SVN access, I give it to you. You know, I get an email for every commit and I look over it. If it's something I have problems with, then I might say, you know, can we fix this? Or can I fix it? Or someone on our team fix it? As of yet, no one who's committed has committed terrible code. I haven't had any problems with chasing people down or kicking code out. But maybe my standards are much lower than some other people. I'm fairly lax on those things. And I'm just happy to have people help out. I'd much rather have someone help out and clean up their code a little if it's not to my style than to lecture people on how their code should be to get into our repository. That just seems unproductive on everyone's part. So we're pretty open.

**Dave Jones:** Yeah, I've been involved with like I – when I did my watch, my scientific calculator watch, I released the, you know, source code out there as, you know, under open source. And I had somebody basically rewrite the entire thing. Like they just didn't like the way I did it. So they rewrote it from scratch. And they – well, almost, you know. And they just coded it in a completely different direction to what I was, you know, happy with. But in the end, their code was much – hugely feature rich and much more capable than what my code was. But it just – you know, they completely redid it just in their own style because they didn't like mine. So that – I imagine that sort of thing can happen.

**SPEAKER_00:** Were you happy with that?

**Dave Jones:** Well, I was happy with all the features that he added. And that's – and I ended up actually selling the unit with that firmware, of course, because it had all the cool features. And you can play chess on it. And you can do all sorts of stuff. But in terms of the code, I couldn't follow it anymore, you know, because it was just completely different to the coding style that I was used to personally. And I just couldn't maintain it myself after that.

**SPEAKER_00:** So, yeah. I think it's great that you went ahead and used it. And I was just going to say, did you even host it? But obviously, if you put it into a product, you went ahead. Full hog.

**Dave Jones:** Yeah. But then it got to a point where I couldn't maintain it anymore because I had no idea what he was doing, which is good and a bad thing. Like, you know, he did all the hard work, which I'm very grateful for. And it was great. Firmware, it's just that I couldn't – it had the side effect of me not being able to maintain it personally anymore. I 100% agree with that.

**SPEAKER_00:** Yeah. We have the exact same problem.

**Dave Jones:** Because I'm not a huge C coder. Like, I can write in C and I've got my own little style. But apparently, it's, you know, totally different to what all the professional, you know, code monkeys out there do. So, they took offense to my style and went, no, no, this is amateur hour, you know.

**Chris Gammell:** Wait until they get a load of me, buddy.

**SPEAKER_00:** Yeah. Setting your best joker voice. No problem. We have fairly advanced features that people have added to the code base at times. And then when we do something and someone reports a problem, or especially when we have a cool feature, but no one's really explored it at the outer limits. Right. And then we get someone who says, well, they've done it up to here, but I want to do it at 100 megahertz. And it's like, well, you know, I doubt it's going to work. Yeah.

**Dave Jones:** Because if you want to do that, you'll have to change the whole underlying infrastructure or something. Yes.

**SPEAKER_00:** And then I'm in the code, in the guts of it, trying to figure out exactly what's going on and how I would be righted and whether we can actually get to this point. And I would definitely say that's certainly a danger with open source. And there's certainly the danger of losing control of your code base. And I certainly know I can, in my mind, I can picture the gray areas and three or four projects, which I know are both things people have done that worked great in the beginning, but have over time not aged well or been kept up as well and are now becoming problematic. And it's on my to-do list to get in there and rewrite all of that and redo it so that it's not a problem for our users.

**Chris Gammell:** Do you consider it your, I mean, like, I guess that's a larger question is, I mean, how much of this is, do you see it as yours versus like community? I mean, I'm sure that, I've never open sourced a project myself, so I don't know. But I assume that some of it is hard to, you know, kind of push it out there and just be like, well, whatever, right? Because it's also a business. So where is that line drawn for you?

**SPEAKER_00:** I'm fortunate enough I've never had that issue. Yeah, that's good. I mean, for me, the code belongs to the community. The code belongs to everyone. Public domain means I don't claim any rights on it at all.

**Chris Gammell:** Mm-hmm.

**SPEAKER_00:** And when people contribute, generally, especially if it's a public domain project, because there's no, there's technically no license. We actually have to have them fill out a little form or send an email saying they're dedicating this code to the public domain. Oh, interesting. And if they're in a country that doesn't allow that, like Germany, there's like actually a contract they have to sign off on that says that they're transferring the code to me and then I can release it into the public domain.

**Chris Gammell:** Oh, goodness. They have to like send you a piece of mail and then you like make a little paper airplane, you throw it off the roof or something.

**SPEAKER_00:** Yeah, you know, all this licensing stuff, it's really just a formality and it's a huge pain. In my opinion, public domain should be the default. Yeah. If you put something down and you don't say it's copyright, if you draw something and you don't put copyright on it, if you code something and you don't put copyright on it, then it should be public domain. People should feel free to use it however. But that's not the way of the world.

**Dave Jones:** Unfortunately, legally, that's legally not the case. Because lawyers. Absolutely.

**SPEAKER_00:** It's the opposite. And so we run into the situation in order to not claim rights on something, we have to jump through all these hoops. So weird. So I see the code base as belonging to everyone. I generally know which parts I've written and I know other people's code when I run into it. But, you know, I'd say the code belongs to the community, the user base and the people who maintain it. And people, of course, are welcome to take it and fork it and use it on their own and call it their own. Yeah. For all I care. Interesting.

**Chris Gammell:** Well, one last topic. I wanted to ask about the 7400 series competition. Oh, yeah. What was your final take on it? What was your favorite?

**SPEAKER_00:** Oh, it's so hard to have a favorite. You know, we've done it for two years now and it's a competition to see who can build really the most interesting, creative, wacky, odd, whatever using 7400 discrete logic chips. And it really will take any logic chip. We always say we leave it to the judges. So if you wanted to use a CPLD, but it's still consistent with the spirit of the contest. If you write 7400 logic and mix it with CPLD or do something innovative and it still reflects the nature of the contest and the spirit of the competition, I tell people that's fine. It doesn't mean you'll get first place. Right. But anybody's welcome to submit anything innovative based on discrete logic. And this is the second year now. Dave judged last year. This year we had a pool of community judges as well as a forum voting. And I think, you know, there's one guy who makes really incredible projects. Last year he was the grand prize winner. And this year he did a RFID card made entirely from discrete logic. I thought that was cool, not just because doing all that work with the discrete logic, but because by looking at the design, I understood more about how RFID works than any other RFID project I've been involved in. You know, I've made a pick tag readers, pick tag clones, stuff like that. But that really, I just looking at the layout of that and seeing how he did that, it was just mind blowing.

**Chris Gammell:** Yeah.

**SPEAKER_00:** You know, and that's what I like about the 7400 competitions. You see these things that we now do with the microcontroller reduced to the discrete logic components. And then you can sort of see how it would happen. And I find that really fascinating. And this contest, I would love to take credit for it, but it's actually Squeaky Beaver, one of our community members, came up with it last year and did all of the heavy lifting last year to get it off the ground. So he definitely deserves credit for the creative side of that.

**Chris Gammell:** Yeah.

**SPEAKER_00:** Now, this year was quite good as well, but I think doing a yearly 7400 contest is difficult because you run out of the obvious projects and you get into some really, really serious work, which is very cool as well. Right, it shrinks the pool, though. Yeah, exactly. Yep. So I think we're going to put it on hiatus for a few years and come up with some contests in the interim. And one that came out of the forum that I'm particularly fond of, and I'm sure it's going to be our next competition, is lab equipment. Ooh. With no specific definition. Okay. Just make some useful lab tool.

**Chris Gammell:** Oh, yeah. That'll be like the spawn of DIY everything. I want that. Yeah, yeah.

**SPEAKER_00:** That way the effort, the creative energy and the engineering is going towards something maybe useful for everyone. Yeah. And the community. Instead of just some simple learning demo project oddity, we're actually starting to get a body of open source tools.

**Chris Gammell:** Yeah. So you name the end product as the goal instead of the ingredients. Yes. Huh. Yes. That's a great idea.

**Dave Jones:** I like it.

**SPEAKER_00:** So I think that would definitely be...

**Dave Jones:** I would weight that one, the more universally useful it is, the higher it would be ranked. That's how I'd run that one. Oh, yeah. Absolutely. Because, yeah, you could get something to someone really obscure, so obscure. It's really cool, but it's so obscure that nobody else would ever want to make it, ever. You know? Right. It's such a specific use, you know? Right.

**Chris Gammell:** This test when flies take a crap. Yeah. I mean, that's a great idea. And just like the commodity side, too. I mean, like seeing what commodity equipment now can do, it's... I mean, it'll probably have some test and measurement companies perk up a little bit, I'm sure.

**SPEAKER_00:** Oh, right. And I would love to build and sell a test batch of the things, both from the 7400 contest or a lab equipment contest or whatever. Yeah. And people suggested it, but my feeling is I don't want to infringe on anyone's project.

**Chris Gammell:** Yeah.

**SPEAKER_00:** Yeah. I don't want anyone to feel like I'm taking something from them or capitalizing on that. So I've been very, very hesitant. Yeah, that's tough. But I think next time, we may offer the winner the option of having a test batch done.

**Dave Jones:** I would do that, yes. You have the option to get it, you know, assembled and we'll take care of it all for you and cut you in on the profits.

**SPEAKER_00:** Yeah, yeah, absolutely. But even, you know, even with a licensing deal, I'm just so nervous and so scared about getting someone upset and appearing to use someone's project, you know, in that way. I know I've, you know, I've been in that space. People have cloned work I've done and it's made me really nervous, especially when you're just getting started.

**Chris Gammell:** Yeah.

**SPEAKER_00:** You don't have the resiliency to say, yeah, people have been cloning my stuff for years now and it's really done nothing but help me. Really? And in the beginning, it's nerve wracking. You know, you have that knee jerk reaction to say, oh no, this is going to ruin me, going to take me down or they're getting all this credit off of something I've done. And I would never want to give anyone else that feeling. But I really would like to offer the option of having a test batch made, especially if we come up with some really cool test tools.

**Dave Jones:** Ian from Dangerous Prototypes, without a last name.

**SPEAKER_00:** Of course.

**Dave Jones:** Thank you very much for joining us. I think our capacity is well and truly up here.

**Chris Gammell:** Definitely.

**SPEAKER_00:** Well, thank you guys for having me. It was really nice to talk to you. And I know we've been working on this for a while to get all the times lined up. Oh, yeah. And I'm glad we finally did it. It was a lot of fun. I agree. It was indeed. Thank you very much. And where can people catch you? Yeah, I'm available at DangerousPrototypes.com. I'm at DangerousProto on Twitter. I do tweet. Watch out. There's some tweets about food there that seem to upset people. Excellent. Our blog has six to ten posts a day. All user projects or stuff we're working on. And, of course, if you want to get involved in our projects, our hardware, our forum's always open. We have 24 hours a day. You can get a hold of somebody in the forum almost immediately. There's a great community there. And they're always working on projects. They're always hacking something, debugging something, or fixing something.

**Chris Gammell:** That's awesome. Well, thank you again, Ian. It was great talking to you.

**SPEAKER_00:** Hey, thank you guys. Thank you so much. Catch you later. Bye.

**Speaker ?:** Outro Music
