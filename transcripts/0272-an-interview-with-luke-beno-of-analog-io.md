---
episode: 272
title: An Interview With Luke Beno of Analog.io
url: https://theamphour.com/272-an-interview-with-luke-beno-of-analog-io/
---

**Chris Gammell:** This is The Amp Hour Podcast, recorded October 21st, 2015. Episode 272, an interview with Luke Bino of Analog.io.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Luke Beno:** And I'm Luke Bino from Analog.io. Hey, Luke. Welcome, Luke. Hey, guys. How are you doing?

**Dave Jones:** Well, we were talking out our ass last week about the Internet of Things, weren't we?

**Luke Beno:** Yes. I think everybody does that.

**Dave Jones:** Right. And we've actually... So, Luke, apparently you know something about this sort of stuff. Tell us.

**Luke Beno:** So, a little bit about it. I run a service called Analog.io. And it was an entry in the Hackaday Prize this year. Basically, it's kind of born out of a need that I had to...

**Dave Jones:** Oh, hang on. I'm a judge in that. Should I... He is.

**Luke Beno:** No, I don't...

**Dave Jones:** Should we not be fraternizing?

**Luke Beno:** Oh, I think it's over. It's over for me. I'm done.

**Dave Jones:** Oh, right. Okay. Right. Fine. You may not know it, but you didn't pick me.

**Chris Gammell:** Well, I didn't get your one. So, it was like... Yeah, my round. Sorry. No, no problem. I didn't see yours, so...

**Luke Beno:** No hard feelings. Okay.

**Dave Jones:** Yeah, because they're sort of... People don't know they're split between different judges this year. Whereas before, it's like the judges reviewed all of them. Or at least all of them that came to the stage for the judges. But this year, it's different. They only give each judge a little parcel of ones. So, I didn't see yours. It's all right. Okay.

**Luke Beno:** No. No worries. So, yeah... All right. Sorry. Continue. Yeah, no problem. So, Analog.io is something that I created because I had a pretty big interest in logging information about beekeeping. And so, as it started, I started to connect sensors to a beehive that my in-laws maintain. And then I kind of found a need for this online plotting tool and wanted to create a community where other people can share similar data that they've collected out there on the internet. So, now there's probably about 630 people that become members of Analog.io and they have interests like monitoring the pH level and temperature of an aquaponics tank or there's a couple other beekeepers on the site, things like that.

**Chris Gammell:** How well their pot's growing, right?

**Speaker ?:** Right.

**Chris Gammell:** Yeah, definitely. And that's not pot plants, folks.

**Dave Jones:** My first question that immediately springs to mind is why did you have to do that? Aren't there 20 million bazillion internet of things service companies that do this sort of stuff?

**Luke Beno:** Yeah, that's a really good question. So, I did it because I wanted to learn web programming. And it was just kind of a slippery slope that I kept going down where I just created at first a plotting tool for myself and it just grew into this and I didn't really think about the other services.

**Speaker ?:** Right.

**Dave Jones:** So, it wasn't so much that the other sites couldn't do what you wanted. It's just that you went, oh, that sounds fun. I'll do it myself.

**Luke Beno:** Yeah, exactly. And, you know, SparkFun has a server called data.sparkfun.com. And that's where I started. And that service actually doesn't have a plotting feature. So, that's what I added. Oh, boo.

**Dave Jones:** Yeah.

**Luke Beno:** Right. So, that was kind of a really essential feature. They didn't have it. So, I created, well, at the time.

**Dave Jones:** Well, what does their one do if it doesn't plot? Right. I mean, that's the whole idea of data. Right.

**Chris Gammell:** Can you walk us all the way down the stack too? I mean, that's kind of the main thing that, so this is like the, we're looking at the output. The graph is the pretty, pretty output, but there's other pieces in there, right?

**Luke Beno:** Yeah. There's a lot of other pieces. It can be really simple. Like, if you use a device like the electric amp or the particle boards. And so, you have a sensor that's connected over, say, Wi-Fi, and it's pushing data over HTTP requests. And then that's stored on the data.Sparkfund server. And then analog.io just connects to that server, pulls the data records, and plots them for you in an easy-to-use manner.

**Dave Jones:** Oh, so you're not actually hosting the data, serving the data yourself. You're plugging into the Sparkfund one.

**Luke Beno:** Right. That's right. And actually, my goal is to connect to all of the different data servers. So, right now, I only support the Sparkfund server, but in the future, it would be sort of like the one front end that would connect to the Zively and Thingspeak.

**Dave Jones:** The new Amazon one? What about the new Amazon one?

**Luke Beno:** Yeah, I think that's also possible. Have you had a look at that? I'm just starting to look at it now. You know, actually, that one is also more of a quote-unquote back-end tool.

**Dave Jones:** Back-end, right. So, it doesn't have front-end capability, like doing graphs and stuff?

**Luke Beno:** I'm not sure yet. I haven't gotten that far into looking at it. But my impression from reading some of the press releases was that it did not, that it was just the back-end storage and messaging service.

**Dave Jones:** Right. Is that kind of what Sparkfund are doing with their one? Is that kind of what theirs is? Is it equivalent to, like, what Amazon are doing?

**Luke Beno:** Yes and no. I think the Sparkfund service is very much geared towards hobbyists, and it's more of an enabling tool for Sparkfund hardware. I don't think that they're trying to, you know, take over the Internet of Things cloud services like Amazon is trying to do. Got it.

**Chris Gammell:** Yeah. Okay. So, the idea would be, like we said, we talked about this last week. So, if people are unsure what we're talking about, and you want to hear us talk more about what we don't know what we're talking about, you can hear last week's episode where we talked about the Amazon thing. But the way I understood it was, if you use the back-end Amazon thing, as far as I understood it, it would be like spinning up your own version of the Sparkfund server in multiple, multiple locations, and then being able to service more and more devices over time because it just keeps replicating and having more servers that can collect data. And then something like your service would then go into that singular point, which is actually a distributed point, but it looks like a singular point of data. And then you could pull, you know, pull the aggregated data from every device. Does that sound right? I think that sounds right. Okay.

**Luke Beno:** Well done, Chris.

**Luke Beno:** Yeah, I think that, you know, the Amazon service, from what I understand of it, it abstracts the concept of a server, right? So you just have an endpoint that you're connecting to, and it may be multiple machines or it may be just one. You don't really know. But you're just putting data into their service and then, yeah, just the same way that you can put data into it with a web address, you can pull it out using an API, like a REST API, like every website has these days. Yeah. Okay. So, and I think the other thing is, you know, the hardest thing about Internet of Things or however you, however, what term you want to use is reliability, actually. So a lot of these servers, they go down quite frequently. And the problem is you don't know almost immediately if it happens. And for certain things, that can be, you know, a problem.

**Dave Jones:** Right, because if you've developed a widget that you've sold to a million customers and the data goes down, you know, and it goes down and you're not aware of it, then those million customers are not getting their data. Right.

**Chris Gammell:** Right. They just say their device is broken when, in fact, it just could be a layer in the whole piece could be broken.

**Dave Jones:** And as we discussed last week, the other, that's probably number one, is server reliability. But I would have thought that would have been pretty much, you know, taken care of these days. I mean, systems are generally, like Amazon, are pretty reliable, you know. Generally speaking, like, you know, like my, even my lowly EEV log stays up 99.99% of the time. You know, like, it's, you know, it's not too bad. But the other issue is longevity of service. Will it still be there in five years' time, 10 years' time? You know, will your widget still work in 10 years' time? And I've got a temperature logger here in my, you know, I plugged it into the Internet of Things. It came, it was using one of the big services, and it was only a year or two back, two years ago, and now it doesn't work anymore. Because that company's gone out of business, got bought, changed their protocol. I don't know. It just doesn't work. So that's a real concern for me. If I was developing an Internet of Things product long-term that I was going to sell to customers.

**Luke Beno:** Yeah, I 100% agree with that. You know, because if you don't plan your product properly, too, you have a recurring expense of keeping those servers, you know, keeping the lights on. And if you only get one paycheck, you know, there has to be some end of service. Otherwise, it'll start to cost you money, right?

**Chris Gammell:** Yeah, that's what's happening with the Wink, I think. I mean, the Wink is part of the quirky, that was one of the products they did, and that's the only piece that's staying around is basically the Wink because, you know, people bought these products and they expect it.

**Dave Jones:** But how long will that stay around?

**Chris Gammell:** Right. As long as they can make money around. You know, like they're saying it's staying around. Yeah, exactly.

**Dave Jones:** You know, yeah, like in a year's time, it could be gone, too.

**Chris Gammell:** How are people going to be making money here? I mean, like, is it all going to be in the hardware? I mean, like, you don't charge for your service, right? Right. Yeah, that's right. I mean, you could at some point.

**Dave Jones:** Have you thought about a premium service? Yeah, like, you know. Yeah, I'm working. Okay, you get these features for free and then.

**Luke Beno:** I'm thinking about that, and I kind of have a prototype of hosted instances of server that are off from the main SparkFun server. And I'm testing that out to see whether or not it makes sense. And again, it's all about, you know, making sure then when you're taking money from someone to have a service that they feel like they're getting value from. So, you know, I'm being.

**Dave Jones:** So, would that be hosted on your own server?

**Luke Beno:** Well, I don't have any servers. I just buy server space from DigitalOcean. Got it. Yeah, I think that the cost of the VPS cloud is so cheap that there's no.

**Dave Jones:** It's becoming almost free.

**Luke Beno:** It really is.

**Dave Jones:** It's converging towards free. I mean, you know, bandwidth is converging towards free.

**Chris Gammell:** I know the book Dave's reading, so he's on this kick right now. He's reading one of our past guest's book, Chris Anderson. He's reading free. And, of course, like a chump, I started reading again, too. I'm like, oh, I got to keep up with Dave.

**Dave Jones:** Well, it's entirely true. These things are becoming free, you know, essentially.

**Chris Gammell:** Yeah. Well, and it's that freemium service. So, if you're trying to build a business around it. Yeah, you got to have some other piece.

**Dave Jones:** If you're trying to build a business around that, you're going to go out of business. I mean, it's just, you know, you've got to find some other avenue to do it. Right.

**Luke Beno:** And I think that there are certain services that people would find valuable enough that they would be willing to spend, you know, a few dollars a month to keep them up and running. Like, for example, a lot of people use analog.io to monitor the temperature and humidity of a vacation home. So, if you're trying to just, you know, monitor your vacation home when you're not there to make sure that the furnace is working properly, I think that that's a service that people would be willing to spend a little bit of money on. Yeah. So, it's finding those types of applications that is where it becomes most important. But I would say most certainly the model has to be some kind of recurring payment that, you know, you make a profit off of the service. And then you need to have some type of hardware that's, you shouldn't give it away, but it should be very low cost as a low barrier of entry to start using that service. Yeah.

**Dave Jones:** Agreed. One thing people will pay for is simplicity and ease of use.

**Chris Gammell:** Yes.

**Dave Jones:** People will pay for that. You know, people will pay not to have any hassle. I'll pay that. You know, I hate hassle. I hate things that require, you know, me to go learn something. Right. You know, spend days learning something just to get an Internet of Things thing running. You know, I just want to plug it in and it works. You know, I'll pay for that.

**Chris Gammell:** I think it's also about timing too because you got to like, so if you sell Dave a vacation house, and then you say, oh, well, you just bought this, you know, $500,000 vacation house because Dave's rich. And then you say.

**Luke Beno:** Is that a shed or something in Sydney? Yeah, that's a shed. Yeah. No, no.

**Chris Gammell:** His vacation house is in Cleveland. Come on, man. Oh, okay. Yeah.

**Dave Jones:** Well, my lab here is a quarter of a million bucks for 50 square meters.

**Chris Gammell:** Yeah. There you go.

**Dave Jones:** That's Sydney. There you go.

**Chris Gammell:** But, okay, so anything in Sydney though, right? And then you say, oh, and for three bucks a month, we'll make sure that your heat's always on and that your office is going to be the right, you know, like that kind of thing where it's like. Hell yes. You know. Yeah. Of course. Like who's going to say no at that point, you know? Especially if you just, if you have that anchor where you're like, oh, quarter of a million dollars, $3 a month, it would take a lot of months to equal the cost out.

**Chris Gammell:** Yeah.

**Luke Beno:** And also, instead of selling to consumers, helping companies where they have servicemen that go out all the time, if they can have a low monthly cost to monitor something that they would normally send a service guy out for, the return on investment is pretty quick on something like that.

**Chris Gammell:** Yeah. So, let me ask a little bit about, so I'm looking at some of the, me and Dave are both logged in right now. Well, obviously you are too, Luke, but we're looking at data streams and people can sign up and log in and see a lot of these data streams because they're public. And, but how far back can it go? Like, how much data do you store in this kind of thing?

**Dave Jones:** Well, he doesn't store it. I don't. He just grabs it.

**Luke Beno:** Yeah, I don't store the data. SparkFun does. Their policy is that each stream is a 50 megabyte rolling log. So, as you add to the front, it goes off the back. And you have to push to it once every, I believe, six months. Otherwise, they'll, you know, consider it all.

**Dave Jones:** A dormant account. Yeah.

**Luke Beno:** Okay. Okay.

**Dave Jones:** All right. Is there an option to, see, that's where you can add value. Like, you know, yeah, your free service for this is only, yeah, only holds a 50 meg rolling buffer. But if you want to keep it forever, you know, you can pay your $10 a month and you get unlimited storage kind of thing. But that's not your end. That's, I'm talking about, you know, the SparkFun's and the Amazon's, et cetera.

**Luke Beno:** Right. So, the other thing about the SparkFun service is that it's completely open source. So, you can get your own SparkFun server running on a local machine or you could spin up your own VPS. Yes. And that could connect to analog.io as well. So, if you're someone who wants to have the server within your own firewall, you can actually run that on a machine in your house. And then because the majority of analog.io software runs in client side in your browser, it can actually access data servers that are within your LAN as well.

**Chris Gammell:** Oh. Right. So, if I wanted to make like a HVAC monitoring system for my house, right, I could have a server running on my like HTPC, sorry, my home theater computer, and then have it like show on the screen there and then just basically. So, then what's the piece that talks to the analog.io part?

**Luke Beno:** Well, the server itself is written in Node.js and it runs on the machine. It has a HTTP port built into the server that would connect to it. So, you would basically need to tell me the IP address of that home theater PC. Uh-huh. And then I would just do requests just like any other HTTP server would do.

**Chris Gammell:** So, how would it get through the firewall though? Is it because it's running on my side? It's inside the firewall. So, yeah.

**Dave Jones:** That doesn't mean much to us. Sorry.

**Luke Beno:** Well, yeah, I'm trying to. I've run Node before, but it's, yeah, it's not like this. Right, yeah, no, I've done zero. I guess I can explain it quick. So, if you had a server running on your local network and it connects to your router and then your router connects to.

**Chris Gammell:** I'm sorry, like a SparkFun server? I'm sorry. Yeah. Like the SparkFun open server thingy?

**Luke Beno:** Right, anything. Even if you wanted to run a web server or anything. A good example is some of those really inexpensive webcam or network cameras. They're inside your LAN and you go to like 192.168.1.4 and you get it. But if you went outside of your home, you could not access that IP address unless you did port forwarding in your router, right? And your router is acting as a firewall. Got it. So, it's essentially the same thing is that you could go to analog.io, type in that 192.168 IP address, and it can access things that are inside your firewall when you're inside your home. Then when you leave it, it wouldn't be able to access it.

**Chris Gammell:** So, what's the function that, so analog.io is pushing that node code down into my browser and then it's all running the server within the browser? Is that the idea?

**Luke Beno:** It runs the front end. So, anything, the application itself is run inside your browser in JavaScript. Gotcha. Like, the tool that does the plotting, the tool that does all of the REST API requests to the server is all running in your browser. It's not running on a server.

**Chris Gammell:** Okay. That's kind of cool. So, you mentioned that all the streams are public. Does that mean they're public by default or no? I mean, like, because it requires determining where it is.

**Luke Beno:** Everything is public by default. So, because I don't give any guarantee of any form of privacy, I just have to default to offering all streams as public content. Okay. So, you know, I would say that if I wanted to create private streams, then there would need to be some extra level of robustness to guarantee that those are private, right?

**Dave Jones:** Which probably costs money. So, therefore, it would be a paid service. Yeah. Exactly. Exactly. Yes. Yep. Yep. Well, that sounds reasonable. Now, the first thing that springs to my mind is what happens, viewing all these graphs is all well and good. It's all funky. I love graphs. But what happens if I want to be alerted?

**Chris Gammell:** Yeah.

**Dave Jones:** Good question. I want to be alerted when something goes over threshold. For example, temperature. Oh, it's too hot. Send me an email.

**Luke Beno:** Mm-hmm.

**Dave Jones:** So, you would – How is that possible?

**Luke Beno:** So, it's not possible in analog.io right now because that would be a server-side function that would need to happen in real time. And so, for that, you would need –

**Dave Jones:** It has to be polled. Yeah.

**Luke Beno:** Right. So, you know, I've thought about things like actually creating a monitoring service, but then I think that that would be something that would need to be paid for. Either that or some type of application that you run in the background like a Google Chrome extension or something like that that's constantly polling and monitoring that stream. But then it comes into the reliability of is that service going to be reliable or not? Of course. Yep. It takes time to develop something that would be reliable.

**Dave Jones:** Well, ideally, the best place to do that would be on the data server itself, i.e. the Amazon or the SparkFun server, right? Doing it on your layer is just seems – or on the user's layer, as you said, like a Chrome plug-in or something. That just seems two levels extracted in complexity to me.

**Luke Beno:** Yeah. To me. I completely agree with that. Right. The server is, you know, it's always there. It's always on. Correct. You can count on it. That is the best place. And I'm fairly confident that that is a service that Amazon would need to offer. They probably have it in their offering already.

**Dave Jones:** Because they have to do the processing to get the data, you know, to your little temperature sensor in your house is sending data to the Amazon server. The Amazon server has to store that. Well, at the same time it stores it, why doesn't it do a compare with some threshold you've set, you know? Right. And bam. Yep. So, yeah, that is the place to do it. Anything else is just adding levels of complexity that can just fail.

**Luke Beno:** And so, yeah. And so, the beauty of, you know, the SparkFun service, which is actually called Phant, P-H-A-N-T dot I-O, is that, you know, anyone...

**Dave Jones:** What does that stand for?

**Luke Beno:** It's like an elephant. Like an elephant doesn't forget.

**Chris Gammell:** Phant? Yeah. If you go to that, that's their logo too.

**Luke Beno:** Right. Right. So, you know, those features could be added to that code base and then the whole community would benefit from someone adding those features. It's something that I've thought about, but, you know, everything lately for me is a decision on where to spend time and that hasn't bubbled up to the top priority-wise recently.

**Dave Jones:** So, what is your highest priority at the moment?

**Luke Beno:** Well, I also have a day job and...

**Dave Jones:** Yeah, that sucks, doesn't it? Yeah.

**Chris Gammell:** Luke's Patreon page can be found at.

**Luke Beno:** No, but recently, you know, I was competing pretty heavily in the Hackaday Prize in trying to do a lot of project updates there. So, that was a focus for me for a while. And then, you know, with a community that's growing to over 600 people, there's a fair amount of time just spent interacting with those people and making sure that, you know, you're getting their feedback and making sure that the site is working for them. That's my highest priority.

**Dave Jones:** Chris wasn't kidding about the Patreon thing. When you've got that many people, you should set up a Patreon page. Hey, help me, you know, earn a living doing this sort of thing.

**Luke Beno:** Yeah. Maybe I'll do that.

**Chris Gammell:** Yeah. You should. Yeah, I mean, especially if this is... I mean, this is offering... This is valuable for people. So, that's interesting.

**Luke Beno:** Yeah. Ideally, you know, what I... My vision in the short term is, you know, I'd like to see people using it as a medium to exchange data for a certain hobby that they're interested in, right? So, if there's an aquaponics group out there that, you know, everybody wants to collect pH information for their aquaponics and compare it against someone else who's doing the same thing. You know, make a group of people in analog.io where, you know, everybody's kind of collecting the same data and they can look at each other's and collaborate on that. Yeah. And I think it's fascinating to me to just see trends and, you know, even just the outdoor temperature over time, you know, just to see, you know, today was a cold day or whatever, right? But it's... Maybe I'm alone, but I think that that's interesting. No, no, no.

**Chris Gammell:** I'm just saying, we have this thing called going outside. I know most of us don't do it. But it's not the same, Chris. I don't know. No, you're right. It's data. It's charting. I mean, this stuff is actually really interesting. And so I come from the world of layering even more stuff on top of it, which I never even realized is kind of, you know, the big data-y, but SPC, like looking at statistical type stuff. You could start to chart, okay, like you said, temperature outside. And you could chart throughout the month of May, there's a, you know, there's the, this is the average temperature. You got the mean and median and stuff like that. And then you can start to have banding and error bands. And you can tell one a day's an outlier and you could do, I mean, like home science type stuff. I mean, granted, like I said, you know, you could go outside and do this stuff, but having this kind of data and having it across locations and really starting to bundle it together can prove for some interesting stuff on the output.

**Luke Beno:** Yeah, I agree. And I think that the nice thing is, is that when you're going outside, you're only getting one snapshot in time. When you're looking at a plot of a very slow changing data stream, like temperature or things like that, you get to see that compressed, you know, detailed view over many days. And that's, that's interesting, right? So like in the case of, of the beekeeping data, I'm monitoring currently the temperature at three different, three different levels inside of the beehive, as well as the, the overall weight of the beehive. And, and so it's interesting because you can see, um, the time of day that all of the bees are, are leaving the hive to go forage. And then at the end of the day, you can see them all come back with, um, you know, whatever they've, they've gone out and retrieved nectar and whatnot. And you can see the, the weight of the hive increasing day over day. And, um, and then on, on certain days where maybe the weather isn't so nice, you can actually see that the bees don't leave the hive and they, they stay home and, and that's apparent in the data. So, um, from that perspective, I, I think it's pretty fascinating.

**Dave Jones:** Have you seen that Australian, uh, Kickstarter for the beehive thing? I don't know what it's called.

**Luke Beno:** Yeah. They, I forget what it's called, the, the beehive that the honey flows out, out the side of.

**Dave Jones:** Yeah. The, uh, tap, it's on tap, you know. Yeah.

**Luke Beno:** It was very, very successful from a funding perspective. But, um, I think I'm just a, uh, my in-laws are actually the beekeepers. I've been getting more involved with it, but I know within the beekeeping community that, that Kickstarter is kind of viewed as, um. Lowbrow. Sensational. Yeah. That's not quite how. It's not only great. Right. Yeah. That's not quite how honey extraction works though. So, um. It's called honeyflow.com. Yeah.

**Dave Jones:** What you're saying, it's like, um, sacrilege, is it? Because like, oh, real beekeepers, yeah, get their suit on and, you know, none of this turning on the tap rubbish.

**Luke Beno:** Well, you have, you have to go into the hive and make sure that the colony is healthy. Yeah. Yeah. There's a lot of.

**Chris Gammell:** Especially with the collapse stuff, right? Like all the stuff that's happening with bees these days.

**Luke Beno:** Right. There's a lot of things that can afflict a beehive that, um, take a long time for them to recover. So, um, beekeepers need to go into their hives and inspect them anyway. So, um, you know, it can't be as easy as just put a box out in your yard and turn on the tap and get honey out. Right. As they make it look.

**Speaker ?:** So.

**Luke Beno:** Right. Right. Okay. Devil's in the detail.

**Chris Gammell:** Yeah.

**Luke Beno:** Right.

**Chris Gammell:** That's like being like, I bought, uh, I bought the cowinator and, uh, I have this box in the yard and there's a cow inside. And then in two years I get a hamburger. Right. Or a steak. It's like, Ooh, that's, that's, yeah. That's silly.

**Dave Jones:** Oh, goodness. Sorry for that tangent, folks. So who are your, who are your competitors in terms of like this visual? Cause your one looks suspiciously like the one that I used to use. And I can't remember the name of the one I used to use, but like it's graph as well. It's almost like you're using the same code. You probably are. There's probably some standard graph. It's like libraries, right?

**Luke Beno:** Yeah. There's a, there's a graphing library called high charts. You can actually see the link in the bottom right corner. So a lot of, um, web graphing, uh, utilities are leveraged that same library. Um, the same thing with the overall.

**Dave Jones:** So do you pay for that? Is it free? Open source? What?

**Luke Beno:** It's open source as long as you have attribution. And, and actually I think too, if you're, um, not making money off of the use of it. So.

**Dave Jones:** Oh, okay. But if you do make, if you make money from this, you have to then pay them some coin. Do you?

**Luke Beno:** A little bit. It's, uh, it's fairly reasonable to license. But yes, it would cost something.

**Dave Jones:** So you're sorry. Your competitors. Yes.

**Luke Beno:** So other popular services that, that people use are a website called Sively. Um, another one called ThingSpeak. And there's a couple other, other ones as well. And there's new ones that pop up every day.

**Dave Jones:** Yeah. That's, that's our concern. Yeah.

**Luke Beno:** It's, it's, it's expanding market right now. Definitely. Uh, but, uh, you know, like takes up, I believe for example, they are, uh, a company who started as a, as a hobbyist enthusiast type thing, but then, you know, eventually they realize that they, they really need to go after business customers to, uh, grow their company and make money doing this.

**Dave Jones:** So that, that I'm pretty sure that's actually the one I used. Zively through this little, um, temperature kit I've got. Yeah. It used Zively, but Zively were bought out or merged or something. And it just, yeah. And it, yeah. And it just broke. I mean, it just, my thing just stopped working one day, you know? Well, thanks for that.

**Luke Beno:** So Zively still exists and, and people still definitely use it, but they have kind of shifted focus to more, um, corporate type accounts. So there, there isn't as much, uh, you know, love being put towards the hobbyist community.

**Dave Jones:** Cause there's no money there, right? So the investors want return on their investment.

**Luke Beno:** So yeah, that's exactly it. Gotta follow the money. Yeah, that's exactly it. So with, with analog.io, you know, I'm not, I'm not chained by, by investment, you know, so I can do things that I think are interesting or fun. Um, so I have to do my best Yoda voice here.

**Dave Jones:** You will be. You will be. It might come to the day where you are. Yep.

**Luke Beno:** Yes. Yes. Exactly.

**Dave Jones:** Yes. Have to answer to it.

**Chris Gammell:** Money changes everything, man.

**Luke Beno:** Yeah, I know.

**Dave Jones:** Hmm. Sucks. Yeah.

**Chris Gammell:** So, okay. So the idea though is like, do these other ones, do they have the same kind of thing? So I see a lot of these like, like I'm looking at just like the analyzing and data and, or sorry, like charting and stuff like that. But what is the ultimate output? Is it, is it always to have that dashboard look or is it to talk to other things? Like I think about like, if this, then that, like that's interesting as a layer in between hardware and other stuff. But is it supposed to, is it always just supposed to be like looking at what's there or, or do some of these guys, some of your competitors do other things with the data at the backend or at the end rather, not the backend.

**Luke Beno:** Yeah. They'll be doing like, like Dave was talking about earlier, the, the threshold detection type thing. Um, I think, I think it's still emerging to have, you know, the, the cloud actually make decisions and actuate on it. Um, that's not a mainstream application yet that I'm seeing it at least from a, uh, you know, from a consumer point of view.

**Dave Jones:** But what does your consumer, but your consumer wants that event driven stuff. Why does your consumer care about looking at charts and data? Most of them don't.

**Chris Gammell:** Right. They want to be alerted. Right.

**Dave Jones:** I mean, yeah, yeah. They, they want to be alerted when they're, you know, something happens. That's basically the consumer world, isn't it?

**Luke Beno:** Yeah, I agree. And, um, and it's not today, that's not something that I'm necessarily targeting. I think that there's probably other services that, that could, um, service that better.

**Chris Gammell:** Yeah. It's interesting. I saw some of these things, it also seems like it's, I mean, I, like you said, we're in the early days here, but some of it seems like when, when it's, you know, we think about localized examples, right? So like, and even I'm looking at thingspeak.com and looking at this, it's like, oh, well, when your temperature and your humidity goes up above a certain point, turn off your humidifier and tweet about it and do these other things. It's like, you know, we think about that. We're like, well, why don't you just run a wire? You know?

**Luke Beno:** Right. My, my humidifier has been doing that for the last, for my entire lifetime and well, you know, for the last 50 years or however long. So that's, that's not a new concept, right? In fact, the latency and performance of that local system is actually much better. So, yeah, there's a lot of throwing things at the wall and seeing what sticks right now. I think the other thing with Internet of Things is everyone is trying to make it into one, one concept. And the reality is that it's, it's such a broad term. It means so much. It almost means nothing. Yeah. You know? Which is why I think everybody groans when they hear the term. Yeah, exactly. Yeah.

**Dave Jones:** Yeah. But it's, it's gotten to that point. Yeah.

**Chris Gammell:** But I think it's getting to the point of being useful too, finally. I think.

**Dave Jones:** Oh, true. Yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** But you can still groan about it and use it. Well, we sure, we sure do. Yeah.

**Luke Beno:** There certainly is a lot of marketing force, you know, behind those, those three letters. So. Yes. You'd be, you'd be missing an opportunity if you don't, you know, use them to your advantage.

**Dave Jones:** It's almost a shame because like, it's almost as if like some big tech companies are expected by their investors to have a solution for the internet of things. You know, why don't you have it? You must have it. So that you, I don't know what it is. Oh, I'll buy this company. Bingo. I've got an internet of things, you know, like, oh.

**Luke Beno:** Yeah. Yeah. You're seeing a lot of thrashing like that. And, you know, personally, I think that there are companies who, big companies who don't understand it yet. At least my personal interpretation of it. So, you know, everybody has their own that they compare it against. But still a lot of experimentation with it, I would definitely say.

**Chris Gammell:** When I saw that IBM was getting into the space too, I was like, ooh, big blues here. You know, there's a lot of word and a lot, or a lot of money and a lot of buzzwords flying around here. Yeah.

**Dave Jones:** IBM are in their death throes, I'm afraid. Right. They're, yeah, almost inconsequential these days.

**Luke Beno:** It's their, be their saving grace.

**Chris Gammell:** I wanted to mention as well. So, I had mentioned imp.guru before. That's what you used to be. Right. And, and you had sent me that little tiny sensor board, which is great because it plugged into the electric amp. It was a super simple setup for that kind of stuff. What do you think, like, okay, so people want to use analog IO. How do they get started? What's the easiest way? Like, what platform do you suggest to getting started and getting stuff out there? Just to do something simple.

**Luke Beno:** Yeah, I certainly think that one of the best out of the box experiences is electric amp. You know, it's easy to, to connect that device to Wi-Fi. Since you program it over Wi-Fi, there's no debugging cables or anything like that to use. And, you know, I, I have a tutorial for that temperature sensor that's basically, you know, plug it in, copy and paste the code and you're up and running and you can read the code and see what, you can actually understand what it's doing in like 10 lines of code or less. Right. So I think that that's a really, really good way to get started. Depending, you know, maybe, maybe there's some lower cost ways of doing it, but I haven't found anything that's nearly as, as seamless as that.

**Dave Jones:** So it's the imp. So you used to run imp.guru and people presumably used that service. What happens to them? Well, there's imp.guru is now becoming analog.io.

**Luke Beno:** Right. It's, it's basically, it's running the same thing and it's, you're still using the SparkFun backend. So all of those users, you know, can transition over to analog.io with, the only pain is creating a login.

**Dave Jones:** But they have to transition. So their device would stop working.

**Luke Beno:** No, their device would, they don't have to do anything with their device because it still just pushes to the same SparkFun, SparkFun service. If SparkFun went away, then yes, they would have to change their device. So it kind of uses that as the foundation for, to build upon.

**Chris Gammell:** So, so we're at the hardware level now. Well, sort of, kind of, but with the electric imp too. So the code, so if people haven't, I've done a little bit with it and there's like the, the device side code and the server side code. But so that means the electric imp is, or sorry, their servers are also involved. Is that correct? Right.

**Luke Beno:** Yeah. Yeah. They basically have a device that that's running and then they have a proprietary communication method between their device and their server, which they call the agent. And the server is just a very, very small bit of code running, running in the cloud. It's not like a full blown, you know, server like you would traditionally think of.

**Chris Gammell:** Yeah. So, yeah. And so you, you're basically writing scripting code for both, right? So you're writing scripts for down on the, on the actual electric imp piece of hardware. And that's that squirrel script stuff. And then there's an interpreter there. Like the amount of layers here is actually kind of mind boggling. Right. Yeah. Yeah. To measure this stuff. I would recommend just not thinking about them. You're wrong. But that's the thing. I mean, you know, you, I mean, so people should also know Luke is a hardware guy. Like this is not like, this is, this is Luke's interest, but he's a hardware guy. So you, I mean, you understand all these layers. So like we, we got to get to that point at some point, right? This is a hardware show. We should talk about the hardware down to that level. So. Yeah, certainly. So why are there so many layers?

**Luke Beno:** Well, fundamentally you, it's two things don't mix. It's the internet and low power microcontroller systems. So you can't take a, a $2 or a $1 microcontroller, run it off of a CR 32 battery for two years and push data straight to the internet with it. So there has to be some layers of hardware in order to do that. Electric amp. Yeah, you can, you can sleep it and wake up every 15 minutes and push off some data and go back to sleep. But, um, uh, I personally think that there, that's, that's even overkill for a lot of applications. The other thing is with sensors, um, it's all about cost because let's say that I want to spend a hundred dollars to instrument my house with sensors. Well, uh, I could probably buy two wifi nodes for that price, but I could probably do 10 or more, you know, low power microcontroller based systems with that hardware. So, um, that's the other thing that I, I spend a lot of time on is trying to figure out a solution that's easy to use. That's, that's the keyword. And, uh, and also using these low, low power systems.

**Chris Gammell:** So, so you mean like ESP 8266 type stuff or what? I mean like when you say low, low cost type stuff, so you are, so you are also making some hardware to try and talk up to the other servers that then analog IO talks to. Is that right? Right. I'll, I'll add a couple more layers to the stack, right? Well, it actually sounds like you're removing them if you're not using electric imp though. Or is that wrong? Maybe.

**Luke Beno:** Um, so I guess I'll run through one scenario that, that I've been playing around with recently. So I have a, um, a low power sensor node that's based on an MSP 430 processor. And then it, it connects over, um, uh, I use this off brand, uh, Nordic semiconductor NRF 24 radio that transmits to. So, and I have lots of those, uh, nodes around. You can see on my Hackaday video, I did a demo with 16 of them all transmitting to a central, um, hub. That basically has that same radio, but then it, it takes those packets from the proprietary communication, puts them on the wifi. And then from there they, they go to the cloud.

**Chris Gammell:** Okay. So that's like a hub and spoke where you have a centralized sensor receiver basically. And then that translates to the web stuff.

**Luke Beno:** Exactly. So, um, so ESP 8266 could reside in that hub. And, uh, and that would be one pretty nice, uh, solution from a cost perspective. There are some really big advantages to having the electric amp, uh, layer in between. Because even ESP 8266 is not going to be exceptional at, uh, doing all of the HTTP requests and things like that to connect, connect to the server. It's, it's way more convenient to, to use some of the libraries that are built into the imp.

**Chris Gammell:** Okay. So.

**Luke Beno:** And the other thing too is, is that, you know, uh, like we were talking before. My sensor network is, is a hundred miles away from my home. So if I want to write code for it with electric amp, I can actually sit at my desk a hundred miles away and develop code for it and, you know, push updates to it without needing to be there. Or, you know, for example, needing to be in a bee suit standing next to a beehive. Writing. Yeah. Yeah. So.

**Dave Jones:** Plug in my pick a program. Let's open this beehive suit up. Right. You gotta put the smoke in there, right? I've seen that for beginners. Plug in your ISP program.

**Luke Beno:** So it's definitely something that I've done, but not something that I like to do frequently. So, uh, that, that is a nice, a nice thing.

**Chris Gammell:** Yeah. But it makes you check your code better.

**Luke Beno:** No, it doesn't. Yeah. When the, when you, when you want to write code quickly, it never ends well.

**Chris Gammell:** Yeah. No, that's a good point though, about the, like the dynamic, you know, rewriting code, stuff like that, that, that does make things really convenient. Uh, so.

**Dave Jones:** Well, I thought that was the Holy Grail. That was the whole idea of the internet of things is that these things are connected to the internet and you can do anything with them from anywhere in the world. Be it getting the data or reprogramming them or doing, rebooting them, doing whatever.

**Luke Beno:** Mm-hmm.

**Dave Jones:** I thought that was the whole Holy Grail concept.

**Luke Beno:** Yeah. It is the Holy Grail and we're, we're not there yet, but there are, you know, certain solutions that, that are working towards that. But again, I go back to though, the, it's, it's all about those low cost nodes at the end that are, you know, so, so important because like I said, wifi isn't going to work for those solutions. And, um, it's arguable whether or not Bluetooth low energy would work for those systems. So.

**Chris Gammell:** Just because of the, the distance or, or power or what?

**Luke Beno:** Distance and, in proximity to a phone. So, you know, in the case of the beehive, Bluetooth low energy doesn't really buy you anything because the value that that system has is when you're not around. So your phone isn't there. What, what good is Bluetooth if you're not within proximity of the device? Right. Yeah. That's a good point. So there are, um, like for example, Google released a, uh, wireless router that, that has, um, some of these low power RF networks built into it.

**Dave Jones:** Ah.

**Luke Beno:** And I'm hoping that. Right.

**Dave Jones:** So you don't need your phone. You can just, it just works like wifi, right?

**Luke Beno:** Right. Yeah. A low power version, low power, low bandwidth version of wifi. Um, so.

**Dave Jones:** It has to be built into the router because the router is the internet hub of every home, every location, isn't it? It's, you know, you've got to have it. Yeah.

**Luke Beno:** I think that that's, I think that that's a big, big piece and it's just starting to happen now and it's definitely not mainstream. So there's, the problem is, is that, uh, when, when it goes into a solution like that, it drives a really complicated protocol. Something like, like thread or, or that IP over RF. But it needs to be really simple and something that doesn't require this huge software library. And it should run on, you know, a couple K of code on these embedded devices so that they can cost $3 and, uh, you know, work. I think that that's a, and, and work and do that at, at low volume, like, uh, a hundred pieces as opposed to, you know, a hundred thousand pieces. And that's when you'll really see a lot of things come online, I think.

**Chris Gammell:** Yeah. Well, so like, this is almost like a re-imagining of like server and thin client type stuff, except now the thin client is so thin it, it can barely power itself. Right. I mean, it's just spitting. I mean, like, so like when we talk about the sensor, like the one you made, I'm sorry, I didn't see the one that you made, but like the idea is it's just waking up, spitting data, going to sleep. Right. Waking up data. And it's stupid. It doesn't know. Does it even know if the data has been received?

**Luke Beno:** No, no.

**Chris Gammell:** Yeah. I mean, like, and that's kind of almost what you have to do because then you have to versus transmitting versus receiving type of thing. And the amount of code you need, like that's, that's kind of crazy. Yeah.

**Luke Beno:** It's like, you know, it would be ideal if I could just wake up, shout something, have a router, collect it, push it off to the internet. And then that, that's, you know, the end of it. Right. And in the case of temperature and humidity, well, if I miss a sample or two or, or even 10, it's not the end of the world. You know, that, those are the kinds of systems that I like to work on because then there's, there's, it's not so high stakes. Yeah.

**Chris Gammell:** This is, so this actually all kind of parallels another job I've had with distributed control systems when I was working on. And they did all this stuff, except they just didn't trust any of the wireless stuff. So it was wires to everything, but still it was about passing, you know, when you're passing a pressure sensor from like on a four to 20, you know, pressure sensor that has a four to 20 milliamp output. But you can program it, you can tell what's in an error, but like, it's a dumb node. It's just spitting data, spitting data, spitting data. You need some kind of intelligent controller that then handles that, reacts to that, maybe actuate something else. And then can still talk to the network and get new code and stuff like that.

**Dave Jones:** Well, is, is the internet of things destined to be a one way type thing? Is that going to be the majority of applications where data is pushed out rather than, you know, interacting with stuff?

**Luke Beno:** You know, I think that there's going to be a pretty decent percentage of those nodes that are exactly that. I don't know what the number is, but, you know, when I think of applications, I can think of a whole lot of them that are just monitoring a one, you know, a one way link that are monitoring certain things. Right.

**Dave Jones:** Yeah. And, and, and local processing is, is everything, right? If you, if you want to do something locally, you do it locally. You don't spit it out to the internet of things cloud and then do the processing in the cloud and then spit it back to your device. Right. I mean, that's just adding layers for the sake of layers. Right.

**Chris Gammell:** But I think that's how people do it right now. Right. They're like, like even with, I mean, with wireless, it makes it kind of weird where the line of demarcation is. But like, when you think about if you go into your house and your foot crosses through a laser trip wire type thing, right? And then it goes and that says, okay, the line's high. We're going to send it to the cloud and it processes it. And it says, Dave's in the room now or Luke's in the room now. And then it sends a thing back all the way down through those layers. It says, turn on the light.

**Dave Jones:** That's just, yeah, it's stupid. Right.

**Chris Gammell:** Like you said, it should be laser trip, if laser trip, then light. And it's all in the same controller. Right. I mean, that's. And then later, if you want to rewrite the code for that, like if laser trip, wait 50 seconds.

**Dave Jones:** And then if you want to be able to monitor that from the cloud because it's the internet of things, okay, you can monitor it. But that's not where the processing should be.

**Luke Beno:** Right. Yeah, I agree with that. And I mean, that specific example is like not exactly one of the biggest problems that, you know, that I have in my life right now. But there are a lot of manual processes that we do that are really easy but could still benefit from the internet of things. And a lot of it is, I mean, just think about like people who heat their homes with propane tanks and they want to, you know, are you going to go out in the freezing cold? Because I live in Wisconsin where it gets cold. Go out there and read the gauge, right, to see if you're about, if you need to order more propane or not versus, you know, log into analog.io and see, you know, well, this is how much propane I had two weeks ago and this is how much the slope of how it's going down. And you can kind of interpolate in your mind, you know, I need to order this by next week. Otherwise, I might run out. Right.

**Dave Jones:** Sure. But that's a simple data presentation issue, a data collection issue. Why does that have to go to the internet? Why does that have to be an internet thing? Why can't you just have a little display inside your home and a wireless, you know, a local wireless thing that just connects to a sensor out in your propane tank?

**Luke Beno:** So I think the question back, Dave, is which one is simpler? You can, but which one is easier?

**Dave Jones:** Well, the local one. Well, it depends on the platforms you've got. It depends on the devices and modules and tools you've got to implement it. But ultimately, the local solution has to be the easiest. It has to be.

**Chris Gammell:** You're thinking like the light switch type.

**Dave Jones:** Yeah. Like, it's got to be easier.

**Luke Beno:** So take the propane tank example. Right. So you have one device that goes out on the tank and measures the sensor. And then you'd have another device in your home that would show this graph dedicated. And when you wanted to check it, you'd just walk over to it. Is that?

**Dave Jones:** Yeah. Like, it sits in your kitchen, for example. Like, in our kitchen, we have, like, an indoor-outdoor thermometer thing. So it's got one of those wireless thermometers. So the wife is paranoid about, you know, what temperature it is today. So I know what layers of clothes to put on. Right. She just looks at it as she's in the kitchen. It's the hub of where she, you know, where we live. And there it is. It's displayed. There's the outside temperature. None of this Internet of Things rubbish, you know. It's just, like, a little cheap wireless sensor. It has its own protocol. It just works. It gets a couple of years' battery life, you know.

**Luke Beno:** So I guess, and I completely agree with that. The counterpoint is when you get 10 of those little sensors that are monitoring all kinds of different things in the home, you kind of get this whole remote control. You need a control. Yeah. Like, you know, when you have a home entertainment system with 10 remote controls.

**Speaker ?:** Sure.

**Dave Jones:** Sure. But it's still easier to do it. By definition, it is easier and simpler to do it locally, though. Surely.

**Luke Beno:** I'm sorry, but...

**Dave Jones:** What happens if your Internet connection goes down?

**Luke Beno:** Then you would have a problem.

**Dave Jones:** You've lost all your sensors. You're screwed. Right? You can't even measure something that's just out in your backyard. That's just dumb. Right? It's, you know... So, therefore, that's what I'm saying. By definition, it's more complicated. Being an Internet of Things service. Right. But I think... I'm not saying it's better or worse. I'm just saying, by definition, it is more complicated.

**Chris Gammell:** I think part of the problem here is, though, that we are using simple examples for the sake of being simple, right? And like Luke's saying, it's also... It's, you know, it's not the simple stuff. It's when it starts to expand out. When you have... When you're a service provider. Now, I guess maybe that's maybe the better place to look at it, too. Say you're a service provider and you're willing to give people discounts on their propane tank if they, you know, if they have these tools in there because then it makes your monitoring easier because you're monitoring 50,000 homes at once type of thing. I mean, I... Again, you know...

**Dave Jones:** Oh, yeah. That's a whole different...

**Chris Gammell:** Yeah.

**Dave Jones:** That's a whole different level.

**Chris Gammell:** Yeah. But I think that's where... I mean, that's where the money is, too, right?

**Luke Beno:** Yeah. So, there's no hard and fast rule. I guess that there's no one magic solution, but it... You know, I think that in the long run, as those sensor devices become cheaper, you will find a situation where this connecting to the cloud solution will be a lower upfront cost. And, you know, if more and more things become connected, it's really just preventing the number of devices that you have in your home that are cluttering up things, right? Because everybody carries one universal monitor, which is their cell phone that, you know...

**Speaker ?:** That's right.

**Luke Beno:** Right. Yep. So, it's a recognition of those dedicated displays onto a web browser or onto a mobile phone or something like that.

**Dave Jones:** Here's one thing that just popped into my head, and I don't know why, but it could be important, right? If the whole world goes into things, everything's connected. Everybody's light bulb is connected, right? So that they can, no matter where they are in the world, they can see if they left their light turned on. And if they did, well, they can switch it off, you know? Fantastic, right? We're living in the Jetsons' age, right? Or back to the future. Come on, man. Well, it is back to... Yes, it is today, isn't it? We should at least make a mention of it, right? It is today, isn't it? Well, yesterday here in Australia was the 21st of October, and I believe it's still the 21st there, is it not?

**Chris Gammell:** It is. Yep. October 21st, 2015.

**Dave Jones:** Anyway, yes. Yes, it's back to the future day. Fantastic. So, we now live in a world where the back to the future was yesterday. Is the past. Yep. That's scary. Anyway, what was I saying? Yes. If everyone's got this, and we're talking scale, right? When you've got tens of hundreds of millions of people, a billion people, all with their internet-connected freaking light bulb and every other sensor, right? In their home. What does that do to the amount of power we're consuming? Sure, you could, you know, where is, you know, you have to look at the data, right? But no, that's a big deal. I don't want to live, like, you know, people, we're trying, as a society, trying to minimize our power usage, right? But it's a good thing, you know, with all sorts of, you know, the Energy Star compliant, you know, things that draw less than a watt when they shut down and blah, blah, blah. I don't think, I think that's. If everyone keeps adding sensors to everything.

**Chris Gammell:** No, you're barking the wrong tree there.

**Dave Jones:** Wouldn't that use more power just for the convenience?

**Chris Gammell:** No, I think you're barking the wrong tree there.

**Dave Jones:** Why?

**Chris Gammell:** Because these are not designed to be high power. I mean, these are low power sensors, right? I mean, like, these are all. Well, but.

**Dave Jones:** Yeah, but when you have a hundred of them in your home.

**Luke Beno:** To Dave's point, we're getting away without having them today. So even if they can consume a nanowatt on scale, that it would be more power, right? You know, because everything. Well, yeah, exactly.

**Chris Gammell:** Everything is dropping in general anyways, right? Do you guys run any desktop computer? I mean, I'm running one in my lab, but, like, do you run desktop computers in your house? Even that, like, not having a desktop computer versus having a laptop. You're burning way less energy, you know? Like, just because it's, like, the not always on thing. Everything's designed to be mobile. Everything's designed to be handheld and battery powered. Or it's just the trend is going down. I know that there's more devices, but.

**Dave Jones:** It is, but the numbers of devices permanently on and connected is going up. That's what I'm saying.

**Chris Gammell:** Yes, but I don't think. I don't think that this stuff is actually permanently connected. That's the thing. Like, these are all designed to be low power, shut off. I understand what you're saying, but I'm playing devil's advocate because I think I actually can. And I think I'm right here.

**Dave Jones:** No, but the whole definition of these things is that they're always waking up 24-7. Wake up, send data. Wake up, send data. Wake up, send data. Everything. And if you've got 100 of them in your home. Let's defer to Luke on this.

**Chris Gammell:** Luke, come on. Tell us the answer. What's the real thing here? Come on.

**Luke Beno:** Well, I don't like the analogy of the connected light switch, personally. I'm a pretty early adopter of technology, but I'm with Dave on that particular one. I am perfectly okay, you know, going over to the light switch, flipping it on, and that's a great, simple, elegant solution.

**Chris Gammell:** Oh, I'm there, too. Don't get me wrong on that stuff.

**Luke Beno:** Yeah, but so I think the efficiencies that we get from connecting sensors are to prevent mistakes that otherwise cost us a lot of money and energy. So in the instance of, let's say, water monitoring, and I've personally suffered this myself, right? If you could actually detect a leak in your home before it becomes a really bad situation, and the Internet of Things helped you with that, the net gain on the environment…

**Dave Jones:** Then it's worth it. Your payback is, yeah, your payback makes it worth it.

**Luke Beno:** Right. But I don't like technology for technology's sake, you know, so there's a lot of shades…

**Dave Jones:** That's what I'm talking about, yeah.

**Luke Beno:** A lot of shades in between, but the nice thing is that, you know, consumers are efficient in that way, and that they'll buy solutions that they get value from. And so I think that some of the connected light bulbs are struggling to get traction because consumers are telling those companies that, no, we're really not that interested in a connected light bulb.

**Dave Jones:** Yeah. It's a toy. It's pointless. Yeah, I agree with that. Yeah.

**Luke Beno:** And who knows? Maybe there are applications that you would think would be technology for technology's sake, and they actually turn out to be killer. I can't think of any examples off the top of my head, but that's the kind of, you know, things that people are experimenting right now, and I think that, you know, it's good.

**Chris Gammell:** Yeah. Can you… Can we go back to the hardware real quick for a little bit? Yeah. That stuff that you designed. So could you… Like a packet that you would send out of this sensor node, right? So you have a temperature… Is it a temperature sensor on the MSP430 board? Yeah. Okay, so like, what does that packet look like? I mean, is it just, here's my temperature, here's my ID, or…

**Luke Beno:** Just, here's my ID, and this is the raw binary of my temperature. There's nothing more to it than that.

**Chris Gammell:** Okay. And so that squirts through the NRF24 off-brand radio like you're talking about. Yeah. And then that lands on what?

**Luke Beno:** On that hub device that has that same radio, plus then it bridges over to a Wi-Fi connection.

**Chris Gammell:** Via… Like a module?

**Luke Beno:** ESP8266 or Electric Imp are the two that I've used so far.

**Chris Gammell:** Okay, so ESP8266, great. So what… Does it actually do the numbers conversion in the hub?

**Luke Beno:** Yeah, I would… I actually do it in the node just because it's easier to do there from a coding perspective. I'm actually kind of allergic to code, so I try to write as little of it as possible. Okay. I'll do it worse most…

**Dave Jones:** I'm sorry, that's funny because you're running a web site. It's efficiency.

**Chris Gammell:** It's efficiency.

**Luke Beno:** It's a necessary evil, right? I would much prefer to spin boards and solder chips to boards all day, but at the end of the day, you have to be really, really proficient at software to make world-class things. That's just how it is right now.

**Chris Gammell:** Yeah, true. Oh, me and Dave are learning that one. Don't worry about that. Oh, yeah. Okay, so…

**Dave Jones:** So, hang on. Why… So you're using this two-step RF process. It goes through this, like, you know, proprietary kind of thing, and then it goes to another node, which then transmits via Wi-Fi. Why not just put Wi-Fi on the node?

**Luke Beno:** Cost and power. Mostly power now.

**Dave Jones:** Right.

**Luke Beno:** Okay.

**Dave Jones:** Right.

**Luke Beno:** Yeah, that makes sense.

**Dave Jones:** But overall, it's using more power, right, because you're running two separate RF solutions. So I'm talking about overall system power is bigger. Yeah, slightly. But you're forced into that because you can't battery power the node with Wi-Fi, right? Correct. So…

**Chris Gammell:** Correct. Yeah, so if that keeps dropping in power and cost, then you'd be… And that might be the end goal, right? Yeah, if you… I think that's why a lot of people…

**Luke Beno:** If you had, you know, it's a… Okay, so if you had 20 of the nodes that… And let's say that all of those nodes were Wi-Fi, that solution would be in aggregate higher power than having 20 of the low-power RF nodes and one high-power RF… Correct. …or Wi-Fi node.

**Dave Jones:** Yep. It's a system engineering… Yeah, yeah, that's a good one, actually.

**Luke Beno:** And then the other thing is that you can wall-power the hub, and you can also do things on the hub side to increase the range by… You know, having a more power-intensive but more sensitive low-noise amplifier on that hub or a power amplifier that can, you know, bridge the distance further. So those are all things that you can do.

**Chris Gammell:** Or you could even plug it into Ethernet, you know, like totally crazy. Yeah, you could plug it into Ethernet, too.

**Luke Beno:** But I don't know about you, but most Ethernet ports in my house are, like, in my basement, which isn't a convenient place.

**Chris Gammell:** Where do you spend all your time, man? Come on.

**Luke Beno:** I'm fortunate enough to have an attic for my home office, so…

**Chris Gammell:** Oh, okay. Okay, so let's keep following the packets. Right, so now the packet's in this hub thingy. It gets translated… Or, sorry, then it gets pushed through the Wi-Fi to the SparkFun server. Is that right? Right.

**Dave Jones:** No, it goes to the router. Well, okay, yeah.

**Chris Gammell:** Yeah, the router is a pretty transparent layer, but yeah. Yeah, that's true. You should mention it. You're right. Okay, then it goes up to SparkFun, gets stored in the SparkFun server as the data… So, at 1.23 p.m. today, the temperature in my living room was 54 degrees Celsius or Fahrenheit because it's freezing or really hot if it's Celsius. And then analog.io then goes… When someone accesses analog.io, then that goes and reads from the data stream off the SparkFun server.

**Luke Beno:** Yep, that's the whole stack.

**Chris Gammell:** So, you said, though, that it was… This is what I'm trying to get to, sorry. You said it's more complicated when you're spinning your own thing like this versus using electric imp. What piece would be different if you were using electric imp in that process?

**Luke Beno:** Well, it's just from a coding perspective. Just the high-level code and the libraries that are afforded by electric imp versus writing some of those requests for ESP8266, it's just easier to use. Okay. That's a simplification. It's a higher level of abstraction, which makes it easier to use, but adds complication. When you abstract things, you're adding to the stack, but you're making it easier to use from the user's perspective. Right.

**Dave Jones:** Now, does analog.io only request data from the SparkFun server when somebody is viewing that web page?

**Luke Beno:** Yes.

**Dave Jones:** Right, it does. Yes. Okay. So, if there's suddenly, if a million people log into that one page on analog.io, then that gets a million requests from SparkFun. Yeah. And that's… Each one's an individual connection, so it doesn't…

**Luke Beno:** That's right. There's no caching or arbitration.

**Dave Jones:** Caching box. Yeah.

**Luke Beno:** And I think that that's some of the scale problems that, like, say, Amazon and Microsoft are addressing is how do you deal with those types of inrushes of packet content? That's something that would bring, you know, the SparkFun server probably to its knees. But other more enterprise-grade things, they're thinking about all those types of scale problems, which will become really real.

**Chris Gammell:** Yeah. I think you can even think about, like, Twitter like that. You know, when you think about if each person is a sensor node, right, or each tweet is a sensor reading, then you think about that's all stored centrally, but then that's all distributed as well. And then other people are reading it. And, like, it gets pretty complicated. Like, I always thought, like, why is Twitter so… why does it go down? Why is it hard to do that kind of thing? But then you look at the scale and just, like, how much traffic's going through there. Yeah, it's immense. And that kind of… it's, yeah, it approximates craziness. I mean, like…

**Dave Jones:** So, does your server could potentially have exactly the same issue? If a million people started requesting from your website, I mean… Yeah, it would… It certainly would not… Yeah.

**Luke Beno:** It would not survive that sort of inrush of traffic, I don't think. So. At least… Right. It's not something that I've ever tested. I guess the other… So, one other thing that I think is kind of interesting to talk about, too, is this concept of MQTT.

**Chris Gammell:** Oh, yeah. I saw a great presentation about that stuff, yeah.

**Luke Beno:** Yeah, so it is actually very, very cool because when you send things over MQTT, it basically… Which is what, for those who don't know? So, it's two things. Is it… You can think of it as a lightweight protocol that devices can communicate to what they call a broker, which is essentially the same thing as a server. But I kind of equate it to, like, think about satellite communication. The nice thing about a satellite is that it's way up in space and, you know, in Australia, you can ping the satellite and then it will reflect back to the United States and you can make really long-range communication using that satellite. But MQTT is kind of the same thing where… I think of this MQTT broker as a satellite up in space. Dave, you transmit a packet to that broker. And if Chris is subscribed to it, he can get that packet back anytime that you transmit it. So, it's a published subscribe protocol. But what's interesting about it is that pretty much anything can connect to it. So, say you have an ESPA266. You transmit a packet over MQTT to a broker. You can have JavaScript running in the browser or on a mobile phone that can subscribe to that and get it. So, it's really a pretty transparent way to get data from a device to another device in real time.

**Chris Gammell:** So, it almost, like, shortcuts the… So, like Dave says, he wants to get notifications. It shortcuts, like, the storage and then monitoring and then retransmitting a notification that, okay, now it was 70 degrees in here. Now it's 71. It crossed that threshold. Now it's just Dave's always getting each packet each time on his mobile phone. It's 68, 69, 70, it's 71. Then his phone can tell, oh, now it's 71 and I can just beep for Dave. Is that the idea? Yes.

**Dave Jones:** But I don't want that because then that's using my bandwidth that I'm paying for. Screw that.

**Chris Gammell:** Well, but no, because then you can also…

**Dave Jones:** If I'm being constantly pushed data to my phone…

**Luke Beno:** Only if you subscribe. If you're interested and subscribe to it, that would be one. Right. So, but there are a lot of things where you want to have, like, how do you… Just how do you build real-time messaging into, like, say, a web application? MQTT is an excellent way to do that based on the libraries that exist. So… Right. Just with, like I said, I'm allergic to code. I lose interest after, like, 10 lines. So, you can definitely do this in 10 lines of code, which is pretty impressive, right? So, it's easy to use, I guess you would say. Yeah.

**Chris Gammell:** No, that's really interesting. And I think the Amazon one said… So, part of the thing… They said that, like, in terms of incoming data, they'd be able to subscribe to MQTT packets and then also HTTP 1.0, I think they said. So, that would be, like, sensors can spit out these two types of data, at least right now, and it'll accept it and then start crunching on it, whatever.

**Luke Beno:** Right.

**Chris Gammell:** Yeah.

**Luke Beno:** So, I think you'll see that become more and more prevalent. That's going to be very, very popular technology for Internet of Things. So, the day when I can transmit a low-power RF signal to a router, have it bridge over to an MQTT signal, and then anyone in the world can subscribe to that, that's kind of the day when you see this convergence happen, in my opinion.

**Chris Gammell:** Huh.

**Dave Jones:** I think, as we mentioned before, I think the big deal there is the router. Yeah. The router getting other connectivity options apart from Wi-Fi. I think that is going to be the next killer thing.

**Luke Beno:** Yeah. Yeah. I echo that completely.

**Dave Jones:** Because I don't want to have to add extra layers. I don't want an extra thing, then I've got to plug into the PowerPoint and then maintain it so that, in your case, you know, those low-power RF, you know, the proprietary low-power RF thing. I want that to talk directly to the router, because the router's always plugged in. I have to. It's my internet hub. I don't want to have to have another thing which is then plugged into a PowerPoint, which then translates that into Wi-Fi and then transmits that to the router.

**Speaker ?:** Yeah.

**Luke Beno:** That's just... It's silly. No. And that's the pain that you'll have to go through until that happens. And if people from the router companies are listening to this, you know, I'm sure they're working on it already.

**Dave Jones:** Well, Google have started it, right? Yeah. Google have started it. Google have first.

**Chris Gammell:** Google have started it. Yeah. Yeah.

**Luke Beno:** And the other thing that's happening now is something called LoRa, L-O-R-A. And that's basically the router, but more of a... Like, it's a router that gets seven-mile radius of low-power RF communication. So, you can actually deploy, like, you know, five LoRa hubs in a community and the whole area is blanketed with this coverage. Wow. Yeah. So, it's gaining a lot of traction and there's actually a Kickstarter now called the Things Network, or it's going to be happening soon that, you know, they have these routers that they're like $200 and you can, you know, put one in your home and service, let's just say a five-mile radius of low-power RF nodes. So, that's a pretty... You know, I'm watching that to see what happens. You know, it's like a low-power cell network. Yeah. Yeah.

**Chris Gammell:** Or like running like a APRSnet type of thing for...

**Luke Beno:** Yeah, an APRS, you know, that... APRS, I don't remember. I wish that I knew more about it because it's really interesting. And that's been around for a long time, but that's like a very visionary thing for what the future looks like, I think. It's just, you know, making that more mainstream.

**Chris Gammell:** So, one last thing. So, you walked us up through the packet and stuff like that. Can you just quickly tell us on each of those pieces on your project? Right. So, you mentioned you hate code, but what code was written on each one, on each piece? On each piece? Sorry, what language was running on each piece there?

**Luke Beno:** So, for the MSP430, I like to use Energia, which is the Arduino port for MSP430. So, I write it there.

**Dave Jones:** Haven't heard of that.

**Luke Beno:** Yeah, it's basically Arduino IDE for TI MSP4. For all of the TI parts. So, it's pretty cool. And I'd be missed if I didn't put in a plug for 430.com. Oh, yeah. 430H.com. It's a great community for talking about those projects. It's very project-oriented. But, yeah. So, I use that. And then, for the hub, if I'm doing ESP8266, I like to just use the Arduino package for that. If I'm doing electric amp, I do that. And then, from there, the analog.io backend that does, like, the user login and instores your account information, that's written in Ruby on Rails. And then, most of the web application is written in JavaScript with a framework called AngularJS. And so, that's all the different coding stuff that's done there.

**Chris Gammell:** Yeah, that's good. That's about what I expected.

**Dave Jones:** I don't know. Most of us.

**Chris Gammell:** What was running Ruby? Was on which one?

**Luke Beno:** It's the server that's storing all of the analog.io user accounts and, you know, information about your profile and things like that. Just all of the...

**Chris Gammell:** Gotcha.

**Luke Beno:** Like, the backend stuff for the... Right. For the service itself. That's not running in... Yeah. That's independent of SparkFun. So...

**Chris Gammell:** Right. And SparkFun, do you know what that's written?

**Luke Beno:** It's all written in Node.js.

**Chris Gammell:** Okay. Okay. And that's that font, font.io or whatever. Yeah.

**Luke Beno:** Yeah. So... Man, that's a lot of software. It's a lot of stuff, right? So, you know, if you do become educated in this area, though, I think that there's a huge career opportunity for you long term, just because there are not a lot of people who understand the full stack, right? So, that's going to be a critical skill for people who are just starting out. I'd highly recommend, you know, developing those skills.

**Chris Gammell:** Right. And, I mean, you could replace a lot of this stuff, right? That MSP could have been in C and, like, you could have written some stuff in C or some in Java or whatever you wanted to do.

**Luke Beno:** I'm always going to pick the easiest thing to use that has the highest level of abstraction because I just don't have time to be mired in the details of doing something lower level.

**Chris Gammell:** With this many layers, it's like you have to almost. Yeah. You really do. So...

**Dave Jones:** Yeah. That's why people use Imp, right? Yeah. That's, you know... Yeah. Yeah. Yeah.

**Luke Beno:** Yeah. It's very important because you can write the same number of lines always, but you can do more with less. Do it. That's my policy. So, yeah. So, I guess on the other thing that, you know, kind of a shame if we didn't touch on it was... Dave, I have an answer for you on a longstanding question that you've had about... Excellent. High-density FPGAs that don't have a lot of IO.

**Dave Jones:** Oh, right. In the... Yeah. Well, there's a couple out now, isn't there? There's... But it's taken like 20 years. Right.

**Luke Beno:** And I can explain why. So... Please do. So, okay. So, I guess the other part is in my day job, I'm an ASIC architect for Triad Semiconductor. So, I understand the FAB process. The problem is that, you know, when you're designing a chip, you're either core limited or pad limited. Meaning that those logic elements inside the die itself dominate the die area or the pads do. So, in the case of an FPGA that has a lot of resources inside of it, that would be a core limited design. So, they put the pads there because they kind of... Not to say they come free, but they're kind of along for the ride with the core. So... Right. And then...

**Dave Jones:** Yeah, but you don't have to bloody well hook them up.

**Luke Beno:** And that's true. So, it becomes a packaging type thing. Right. Issue. Yeah, that's right. I think maybe they just couldn't hold themselves back from, you know, packaging a device. Yeah, I know. I know. We've got all these pads. Come on, guys. What are we going to do with them? Get a PGA. Come on. Yeah, yeah. Yeah. So, I mean, there is a limitation. So, I don't know what those die sizes are, but, you know, of what size die you can put in a particular package. So, as, you know, as the process node shrinks, the overall die size goes down to fit actually in some of the smaller packages. But that, at the end of the day, I think is kind of why that exists.

**Dave Jones:** Well, I've spoken to many of them, like many times over the years to, you know, Xilinx and Altera. And they say, they keep saying the same thing. It's because there's no demand for it. Our customers demand these thousand pin freaking packages. They're saying, Dave, you don't matter. Sorry, man. Exactly. I know. Even when I work for the big companies, they say, well, sorry.

**Luke Beno:** Relative to the demand for the higher pin count, yeah.

**Dave Jones:** Yeah. It's, you know. Yeah. They're just saying people who want the real high-density, you know, stuff, like the, you know, the $100 FPGA or, you know, even $1,000 FPGA, they want IO to go along with it. That's just, you know.

**Luke Beno:** Just in case.

**Dave Jones:** So, yeah.

**Luke Beno:** Yeah.

**Dave Jones:** It's just the way it is.

**Luke Beno:** But now with, you know, process nose shrinking, you are getting to the point where you might become pad limited because pads don't shrink nearly as fast as transistors shrink in Moore's law.

**Dave Jones:** Oh, no. So, anyway, but there are a few on the market now. They seem to be, you know, they've gone, ooh, we think there's a niche here now. And, yep.

**Luke Beno:** I think it was more of the process technology caught up, but maybe some. Right. Maybe they heard Dave, who knows.

**Dave Jones:** I don't think so. I think they could always do it. I think they could always do it. But, yeah.

**Chris Gammell:** Well, Dave, Dave got more subscribers, so, hmm, maybe we should listen. He does have a funny guy, folks. There's correlation there. All right.

**Luke Beno:** Correlation equals causation. That's right, yeah. Yep. Yep. I'm responsible, yes.

**Speaker ?:** No.

**Dave Jones:** Well, thank you very much, Luke, for setting us straight on Internet of Things because we just don't know anything.

**Luke Beno:** Maybe we just created a little bit more confusion, but. It's so many layers, man.

**Dave Jones:** I know.

**Luke Beno:** But I do appreciate the amp hour and, Dave, your video blog. It really did actually cause me to get off my butt and do some things in my spare time. Awesome. That's what I want to hear. Thank you. I was just looking back. It's been, like, actually, I think over five years since I've been watching EV blogs. So, it's crazy to think of all the changes that have gone on in that time. So, it's a pretty huge accomplishment for you guys.

**Dave Jones:** And where can people follow you, find you? Are you a Twitter man?

**Luke Beno:** Well, you can follow me on Twitter at analog underscore IO. Also, I document all of my work on Hackaday, on the Hackaday project. Hackaday.io, I guess you'd call it. A lot of IOs recently. Yeah.

**Dave Jones:** What have happened to .com?

**Luke Beno:** Everybody used up all the .coms. Yeah, analog.com's been taking a while. Move on to new territory. By the way, just kidding. What? You're going to buy analog, not Maxim? Is that right? Yeah. I'm saving up my pennies.

**Dave Jones:** Okay. Did you hear how somebody bought Google.com? I did, yeah. For like a day? Yeah. Really? Yeah, that was awesome. I thought it was a minute.

**Luke Beno:** I thought it was like really, really short. I don't know. Something like that.

**Dave Jones:** Anyway, that was great.

**Luke Beno:** And then the trademark lawsuit came out. Yeah, right. Yeah.

**Chris Gammell:** That's awesome. And so I think people should definitely at least sign up. You can see other people's streams. You don't have to like start streaming immediately. You could sign up. You can be part of the community, see other people's streams, kind of see what it's all about, and then follow the tutorials, stuff like that, and get your thing connected to the internet.

**Luke Beno:** Totally. Awesome.

**Dave Jones:** Thanks, Luke.

**Luke Beno:** Very good. Thank you, guys. All right. We'll see you.

**Dave Jones:** See you.

**Luke Beno:** Bye.

**Speaker ?:** Bye.
