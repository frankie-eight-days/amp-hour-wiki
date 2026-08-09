---
episode: 357
title: An Interview with Rick Altherr
url: https://theamphour.com/357-an-interview-with-rick-altherr/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released August 28th, 2017. Episode 357. An interview with Rick Alter. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Rick Altherr:** And I'm Rick Alter, a Googler and also electronics hobbyist.

**Chris Gammell:** Welcome, Rick. I'm glad to have you here. Thank you. So you and I met through the meetup in San Francisco, but I think we had followed each other online prior to that. And you said you're a Googler. Maybe we should start there because I think there was a disclaimer in that Googler statement.

**Rick Altherr:** Yeah. So I've been at Google for eight years. And I do work in the platforms group, which designs all of the equipment that goes into data centers. So that includes servers, storage devices, networking equipment, et cetera. And I think we were going to talk primarily about server equipment. And so the disclaimer is I can't talk about work in terms of the...

**Chris Gammell:** Right. And in RAN 4044, right?

**Rick Altherr:** Yeah. Specifically, I cannot speak anything authoritatively as Google. But I can certainly cover any sort of industry trends and things like that.

**Chris Gammell:** Well, lucky for you. No one ever speaks authoritatively on the Empire, specifically me and Dave. We have no authority over everything. We mostly just make it up as we go along. So excellent. Excellent. So the reason I was... You know, you and I had talked, obviously, before. You gave a great talk about car stuff. And we'll probably get to that at some point here as well. But you first showed up with, like, a server box under your arm. And I kind of realized I don't know much about, like, you know, okay, so yes, obviously, servers are made out of electronics. They're computers, blah, blah, blah. But I don't really know the state of the art. So I was actually really interested to kind of figure out where we are. Where are we? Like, where, you know, what is the normal kind of processor power that's in a server these days? And then what are some of the other challenges that we're kind of facing as the cloud and everything keeps scaling? Yeah.

**Rick Altherr:** So, you know, when I came to HHCG with the Zaius machine, you know, I think a lot of people have this mindset still of 19-inch rack machines, kind of 1U standard stuff. And the world's really changed a lot. You know, that's still very true for traditional enterprise deployments. They deploy in that way. You know, that's what you'll buy from HP or Dell. And you might use that if you're deploying up towards of, you know, tens of thousands of machines. When you start getting into the, like, 50,000 or more machines deployed, you start to realize that you're paying for a lot, especially things like plastics and front panels. And there's a lot of missed features that don't make sense. Like, do I really need an LCD panel to tell me the system health for each machine on the front panel of it? I see. I see. An entire room full of machines that no one's going to see. So, yeah, there's just all these different considerations that come into play when you start hitting these extremely large scales.

**Chris Gammell:** That's interesting. Yeah, I guess to put that in... So, like, the 19-inch 1U rack, first off, that's like, when you say 1U, that's one unit, right? So, like, because you can start to stack them up taller and fit other things in there, right?

**Rick Altherr:** The 19-inch standards for rack mount machines, there's a standardized unit. It's 1U. It's roughly 1 3⁄4 inches. And there's various depths. But basically, it's sort of the mechanical form factor has been set up so that you can buy equipment that's 19-inch compatible and put it into a rack. And so you can mix and match.

**Chris Gammell:** Uh-huh. Okay.

**Rick Altherr:** When you look at the Open Compute project and some of the more, what they call, hyperscale type deployments, people have moved away from that.

**Chris Gammell:** Well, maybe, could we step back as well, too? So, like, so you're kind of talking about, like, I forget what it's called. Is it co-location? Is that right? Is that, like, what you mean when, like, you say that someone might buy a rack unit off the shelf? Is that what you mean by that?

**Rick Altherr:** Well, yes and no. So, if you're looking to purchase rack space as an individual, not the company, but the space. Right, right. Just a space and a rack. Yeah, right.

**Chris Gammell:** Your box goes here, right? We made that joke before the show. Everybody's Silicon Valley fans out there, right?

**Rick Altherr:** Yeah. Yeah, so when you are going to purchase a rack, like, space in a rack, at small scale where you're deploying a couple of machines, as an individual or as a small business, you might go to a co-location facility. And basically, they sell you, effectively, space, power, cooling, and networking bandwidth.

**Chris Gammell:** It's like an RV hookup, right? You're basically buying an RV hookup. You bring your own RV.

**Rick Altherr:** Exactly. You come in and stick your equipment in there. Now, I mean, there's a lot of other ways you can purchase, you know, virtual servers and things like that. But this is when you're actually deploying your own physical equipment.

**Chris Gammell:** Right. And I think Dave actually has... Dave couldn't make it. Sorry. I should have said that at the beginning. But yeah, I think he actually has that for his forum. I remember him saying something like that. So, as a reference.

**Rick Altherr:** Yeah, it's a pretty common thing, especially when you get into reasonable size. Yeah, millions of hits per month kind of thing. Yeah, because virtual services can get expensive. And some people just like having the ownership aspect of, it is my equipment. As you move up to the larger and larger, eventually you get to a point where you're buying whole racks from a co-location provider. And then you're buying a cage where you have, you know, it's basically a fenced off area inside the building that you own that space. And then you get to the point where you start questioning, should I just own my own facilities? Right, right. And that's where you're getting into medium to large size enterprise deployments.

**Chris Gammell:** Can you give us an idea on like another company that might be like of that scale? I'm going to assume your employer is monstrous, but just off the charts.

**Rick Altherr:** I think you'd be surprised if you think of any large company, they are likely to have their own on-site premises. Oh, really?

**Chris Gammell:** Okay.

**Rick Altherr:** For IT infrastructure. It's extremely common that if you're a fairly large employer, you would have at least a small IT staff and hundreds of machines in order to run your mail services and development works, backend services and things like that. So it's extremely common even for, I would say on premises, you know, one or two sites is common even for relatively small companies. When you start getting into many sites and owning large facilities, you start moving up the scale and you get into people like Fidelity, you know, basically like financial. Yeah. Financial services is one, insurance. Basically anybody who has a lot of data processing that has to do or, you know, those types of backend applications where they just have a lot of work that needs to happen and a lot of data to be managed. And so they do it all in a data center.

**Chris Gammell:** And when you say this too, so can we break out the processing versus storage you're talking about as well? Does storage still happen in these racks as well or is that like a different style of thing?

**Rick Altherr:** It varies from space to space. So I tend to think of things as there's the traditional enterprise world, the large enterprise world and the hyperscale world. And they all behave differently in terms of the types of equipment they buy and what they do. So traditional enterprise, you're likely to buy a SAN application or like a NetApp filer or, you know, some sort of dedicated storage system that lets you map iSCSI volumes onto individual servers. So every machine has its own boot drive, but you're actually trying to leverage central storage applications with high redundancy.

**Chris Gammell:** Got it. And then like really, really fast IO links to get the data in and out of that as fast as you can, that kind of thing.

**Rick Altherr:** Exactly. And depending on what your needs are, you know, you might have a machine that actually has a lot of direct attached storage, like a database server. But often, SANs are very common in the traditional enterprise. And that could all be in the same rack or you might move it into different racks. It just sort of depends on what you're trying to do.

**Chris Gammell:** Are there any like visualizers online that kind of show like example of how disparate, like if I go to like a shopping page and I'm looking at two pairs of sneakers, right? It's probably that those images are stored relatively in the same area, but it's also possible that they could be cached across the world or something like that, right? So like, is there, are there any like visualizers online for that kind of stuff? Do you know of?

**Rick Altherr:** Of where information comes from?

**Chris Gammell:** Yeah. Just like, yeah, where it might end up all going, like even like visualizing inside a data center kind of thing. Are there like?

**Rick Altherr:** I'm not aware of any. I mean, when you're, the example you're giving of like fetching static images would often get into content distribution networks like Akamai. Akamai. That's what I think of because they're so fast and just like crazy. Yeah. And that is a one particular deployment model that that's a little different. But when you're talking about the actual data flow inside of a data center, I think the big thing to think about is when I talk about traditional enterprise, it's the distinction between that and large enterprise for me is traditional enterprise. You, you build a server for an application. So this is my database server. This is my exchange server. This is my web server. And that is its purpose. You install an OS on it and you load all the applications on it and you manage it that way. And if it dies, you lose that application. So, I mean, that's a traditional way of doing things. That's just how you would manage it. Right. And people do things like move to virtualization and run, you know, ESX clusters and things like that to try to give some fault tolerance to it. But it's still this classical model of I installed an OS and that OS runs my application as a single instance. When I think of large enterprise, what I see is people adopting what the hyperscale folks, the cloud providers have called, you know, scale out architecture. So it's using things like OpenStack and other job scheduling systems to launch an application and you don't actually care what machine it's running on. Right. Right.

**Chris Gammell:** It's just whatever's free. Right.

**Rick Altherr:** Right. And the advantage is it sort of bin packs across all the machines. So it finds the storage and the network and the processor and RAM that's available in a way that can be used together for your application. And you just get that dynamically allocated to you across whatever resources are available.

**Chris Gammell:** And so just to tie it back to the previous example, you said in the past you would have had an OS doing that. So is there some kind of like higher scale thing where it's just raw resources and there's like some monster OS that's doing this resource allocation? Or how does that? When you said RAM, that's the one actually kind of tweaked my brain. It's like, wait, you could just tell it what brand, I guess you could tell it what address to do, but then how big is the address space?

**Rick Altherr:** Well, so an example of this, there's a variety of scheduling systems. But if you look at Kubernetes, Kubernetes is one I'm pretty familiar with. The tech lead happens to be a former manager of mine. And you describe the resources you need. And the whole point is that Kubernetes as a system knows what every single machine provides in the entire cluster. So then you're able to make these requests and it goes out and figures out, oh, well, this machine has enough CPU and RAM for you to run your job and you don't need any local storage. So you fit here. So let me just go ahead and launch your application on that machine for you.

**Chris Gammell:** Oh, OK, so it is quantized at the machine level then. It's not like it's not like taking RAM from machine one and processor from machine seven. Right. It's just saying, is there enough on this one machine for this one job?

**Rick Altherr:** So most of it is is around trying to bin pack at a machine granularity. Sure. Sometimes it isn't. It depends on how sophisticated you get. Storage is one of those things where you can have the concept of local storage, but you also have cluster level storage.

**Chris Gammell:** Yep.

**Rick Altherr:** So RAM isn't quite at that point yet, but I know that's one area that people would love to see because you often have stranded RAM where I'm not a CPU on this machine, but I have plenty of RAM. Huh. If I could give it to somebody else, I would. Exactly.

**Chris Gammell:** Pass it out. Yep. Yeah. So. But then like, doesn't the IO become a huge thing because you're pushing data in and out between machines then? Or is that.

**Rick Altherr:** Of course. Which is why you see at the large enterprise and hyperscale, networking development has been at ridiculous pace. You know, 10 years ago, 10 gigabit to a server was unprecedented.

**Chris Gammell:** Yeah. Another 100 gig.

**Rick Altherr:** Yeah, exactly.

**Chris Gammell:** Yeah.

**Rick Altherr:** So it's moved pretty rapidly because you're actually shipping a bunch of data around between all these machines, either in a rack or even across racks within a cluster.

**Chris Gammell:** Okay. So it's just about kind of shortest path, but almost on a room scale instead of on a processor, well, a system scale or a processor scale or whatever. Right. Wherever it's going.

**Rick Altherr:** Right. Now, the other part of this is a lot of the reason these enterprises are moving toward the scale out architecture is it's self-healing. When a machine dies, it moves the job somewhere else.

**Chris Gammell:** This is going to start sounding creepy, isn't it? It's going to be like, well.

**Rick Altherr:** Well, it's mainly a lot of the hyperscalers started to realize that as you get larger and larger number of machines, all of those machine failure statistics that you see, the probability that a component will die start to become rates of occurrence. You're going to see failure all the time. So instead of trying to design every single component to tolerate failure at an individual level, you tolerate failure at a cluster level.

**Chris Gammell:** You just make a fast eject rack where you can just pop the server out and pop a new one in, right?

**Rick Altherr:** It's not even about fixing the hardware necessarily. Though, if you look at the open compute designs, they are designed for rapidly being removed and ease of...

**Chris Gammell:** Modularity kind of...

**Rick Altherr:** Yeah. And just tool-less removal, very easy to operate on for repair. But at the software level, instead of trying to deal with things at a single machine level of having rate arrays and things like that, you bump it up to, well, when the machine has a problem, you just move the job to a different machine.

**Chris Gammell:** Uh-huh. And then if you can use some of the resource, then you could turn that bar back on. Is that kind of the idea?

**Rick Altherr:** Yeah. And you can decide when you're going to go fix that machine. So I can just over-provision by so much so that repairing machines in these large-scale deployments is a constant activity. It's not that you wait for something to fail and then you go fix that. It's every day somebody walks in and there is a queue of, I need to go fix these hundreds of machines.

**Chris Gammell:** And when you say fix, you mean just replace, right? Just rip out, do something new or put something new in, right?

**Rick Altherr:** It's going to vary from provider to provider. Uh-huh. Often it's actually more beneficial to fix the machine in place. Basically, you know, walk up to the machine, pull it out onto a mobile cart, swap out the couple of components that you know are bad, put it back in the rack and walk away.

**Chris Gammell:** Interesting. So does that mean that you have a lot of, like, onboard diagnostics as well then? So you can say, oh, well, I already know machine 58 has the 12-volt rail is looking a little low. I'm going to go just go change the power supply and then see if I can fix it later on a bench?

**Rick Altherr:** Yeah, pretty much. I mean, we're never going to actually fix the power supply on a bench. We're going to toss it in a bin and send it back to the manufacturer and tell them it's broken and let the RMA process sort it out.

**Chris Gammell:** Right, right. That makes sense.

**Rick Altherr:** But it's a very common thing that if you look at the components in a data center, hard drives and DIMMs fail a lot. I mean, I don't think that'll be a surprise to most people. But so when you see a hard drive fail, you just have somebody go pull that hard drive out and set it aside in the pile of to be sent back to the manufacturer.

**Chris Gammell:** Right, right, right, right. Seagate gets a two-ton box of platens and whatever, right? Well, I guess full drives probably. Yeah, that's crazy. So specifically for hard drives, too, because this is really interesting to me. As you were saying all this stuff, too, you know, Dropbox, Google Drive, all these services that are just living in the background obviously are helping us out. But I don't think about them on a daily basis. I'm sure you do. But so much stuff is just behind the scenes now that I don't even think about it. But things like that where you say a hard drive dies, well, I've lost pictures before. I've lost music before or whatever. But like how many redundant copies are there in those? I mean, there are always RAID setups or how does that work?

**Rick Altherr:** Actually, nothing in the environments I work in is RAID at all.

**Chris Gammell:** Oh, okay. So it's just super...

**Rick Altherr:** It's, again, that principle of you work at a higher level in the stack. I'm not trying to resolve the problem at a machine level where RAID would apply.

**Chris Gammell:** Because that's actually doing like bit copying and like checking on itself at the bit level.

**Rick Altherr:** Right. Instead, what I try to do is... What a lot of providers do is deal with it at the cluster level. So if you look at something like Gluster or the paper on GFS, they discuss a lot of these concepts of you're actually splitting it up and distributing the files across many machines. And you're doing things like either having a set number of replicas or you're doing Reed Solomon codes so you can actually recover from a subset of the overall availability. And that's there not only because of hard drive failures where you actually have true data loss, but simply unavailability of a machine. It might be temporarily unavailable because it got restarted.

**Chris Gammell:** Uh-huh. Or someone else is accessing data when you write when you need to get it, right?

**Rick Altherr:** Well, that's more dealt with in terms of a performance issue. And so you get queuing. But it's things like firmware updates. They have to happen. Oh, sure. Yeah.

**Chris Gammell:** Okay.

**Rick Altherr:** OS updates. Gotta happen. Mm-hmm. Even testing the battery on the battery backup to make sure the machine will survive. Right. You know, the machine might actually die. That's how you find out the battery is bad.

**Chris Gammell:** Right. I mean, this sounds like this rapidly moves towards like an industrial system where there's planned maintenance, there's unplanned maintenance. There's just, yeah.

**Rick Altherr:** That's exactly what it is. Yeah. That's crazy. Now, the interesting side effect of that is if you start thinking about the probabilities, you know, I mentioned like you see all these, what you would often think of as occasional failure type things. You know, how often do you see a hard drive fail? At one point I did the calculation and I was seeing a hard drive fail every five minutes. Oh, my God. That's a lot of clicks of death. And it's just like that's the nature of having so many devices that the MTBF becomes those rates.

**Chris Gammell:** Yeah. Right. Which is mean time between failures for people that are not playing along at home or playing along at home, whatever. Yeah. That's significant. And that's probably still really good from the manufacturer side of things, right? Oh, yeah. It's not like they messed it up and they have the untenable MTBF. It's just that there's so much M.

**Rick Altherr:** Right. Well, it's, you know, when we talk about MTBF and you think of it as mean time between failure, I know I fall into the trap of saying, oh, well, that's the time between failures on a single device. Well, that's not what it is.

**Chris Gammell:** No. It's like it's a group, right? Or it's taken in.

**Rick Altherr:** It's the total number of active hours in a population.

**Chris Gammell:** Yeah.

**Rick Altherr:** The amount of time in a population's working hours that you will see one failure.

**Chris Gammell:** Right. It's like saying the average age of death of an American, right? It's like it's not like everybody's going to die at 77 or whatever it is. Right. Or every male will die at 77. Right. It's that, yeah, over time, that's what it's been.

**Rick Altherr:** Right. And so if I say I have a million hour MTBF on a hard drive, but I have a million hard drives. Yeah. You start to see the problem of they're on power for one hour. Yeah. One of them is likely to die. Yeah.

**Chris Gammell:** Right. But it could also be 20, right? I mean, that's the other thing. Is that? Yeah. Because it's averaging over even more than the million, isn't it?

**Rick Altherr:** Yeah. I mean, it depends on what your actual population size is. But yeah, I mean, those factors become very important. And that's why approaching it as I'm going to wait for things to fail and I'm going to go get that machine back up and running just doesn't work. You just have to have everything assume failure will happen constantly. Right.

**Chris Gammell:** Instead of success is assumed, it's failure is assumed. Pretty much, yeah. Yeah. At least one level of failure.

**Rick Altherr:** And you start getting into things that are incredibly unlikely events becoming plausible. Such as? Such as? I often tell people that their product is not done being shipped at work until one of them has actually caught fire in a data center. Because even though it is extremely unlikely that your power converter is going to fail in such a way that it will catch fire, deploy enough of them and it will happen at least once.

**Chris Gammell:** Wow. And so that means that you've been on hand with a fire extinguisher? How does that even work?

**Rick Altherr:** Well, not me personally. But yeah, there's actually a thread or a forum that records just things that caught fire in data centers. It's just pictures. Wow. You know, it happens on a semi-regular basis and it's expected. It's really good information when you pick apart why did it happen. And in some cases, you just find it was a one-off manufacturing defect. But that's what you would expect.

**Chris Gammell:** Yeah. Yeah. Yeah. Interesting. And then is that something that like a team would go in and actually do like a failure analysis on that kind of thing? Or is it like an army process?

**Rick Altherr:** Yeah. Especially if it's a fire. If it's just a, you know, a failure to operate, maybe not until it becomes a consistent problem. Yeah.

**Chris Gammell:** That's interesting. So when you say your product is not shipped, do you mean like if you're talking to like a software engineer at a hyperscale thing because it has to be on enough machines to have that happen? Or you mean the hardware side?

**Rick Altherr:** I mean the hardware side. Okay. So, you know, I work with a lot of hardware folks. I primarily work on firmware and the software side, but we design a lot of equipment at work. And so it's knowing when that hardware is shipped in enough volume that you've actually seen what the failure modes are going to be.

**Chris Gammell:** Got it. Yeah. Well, that is, that's, man, that's, I don't think I've ever shipped enough hardware to have that failure kind of happen, but I guess that's good too. Yeah. Yeah. Man, that's nuts. And so does that mean that, okay, so, so then designing the hardware, does how much, how much planning? So I kind of, I kind of already alluded to like, like self-monitoring and stuff like that. And then talking, I'm guessing, assuming talking up through the firmware, up to the OS, whatever, of like monitoring itself. But how much is there for, like UL testing is for like safe failures, right? Not, and not whether or not it's get UL tested, but how much is it like trying to, to make sure that the, there's like fire retardancy and stuff like that, if, if that's a real concern? Yeah.

**Rick Altherr:** So when you're designing your own equipment for your own use, you have to be a little careful with, you need to meet the safety considerations of whatever nation you're shipping into for use, but you get to skip some things because you, you can assume a lot about the environment. It's a lot like an industrial environment.

**Chris Gammell:** Uh-huh. Yeah.

**Rick Altherr:** I have full control over it so I can make statements of only people who have proper training to deal with this can actually be there.

**Chris Gammell:** Oh, I see. I see. So you don't have to like protect the user from themselves because your users are expert users and they're also under your, your employer's employee kind of thing.

**Rick Altherr:** Yeah. And it's, there's a lot of nuance and detail there that is going to vary from company to company. Uh-huh. But yeah, of course. When you, you just think of it as the data center is the computer. So you have to think of things at a building scale.

**Chris Gammell:** Yeah.

**Rick Altherr:** In terms of where does it make sense to do the, the right type of analysis and regulatory enforcement.

**Chris Gammell:** So, uh, when you say hyperscale as well, I mean, I can think of some, some internet giants that would probably fall under that. Do all of them have hardware groups? Is that like a thing? So I don't, I can't say extensively.

**Rick Altherr:** Sure.

**Chris Gammell:** I mean, yeah, I mean, best guess. That's fine. Yeah.

**Rick Altherr:** Well, so, so I'm heavily involved with the open compute project, uh, which is a group that was started by Facebook back in, uh, 2009 or so. Yeah.

**Chris Gammell:** I remember when that was announced. I thought, I always thought it was just a power supply for something like that, but no.

**Rick Altherr:** So, yeah. So they actually do, uh, the rack designs, they do servers, networking equipment, and a lot of other companies have joined in. So you actually see things like telco equipment, like passive optical networking. Um, lots of different technologies are showing up.

**Chris Gammell:** Um, and so, and that's great. It's like ad hoc standards pretty much without a standards board. I'm assuming it's like shared knowledge mostly, right?

**Rick Altherr:** Yeah, exactly. It's, it's an attempt to drive some standardization between these players that do make their own equipment. Yeah. And a lot of it's toward interop and being able to share, uh, equipment designs because if Google designs their own and Facebook designs their own and Microsoft designs their own, then we're kind of locked in to one path. Uh, if we can all share at least at a maybe machine level or rack level, then that helps a little bit in terms of being able to explore different opportunities.

**Chris Gammell:** Well, and how much is it? So I would, I would assume that the, that there's some kind of competitive advantage from designing custom hardware that the other players don't have. But is it like, I would, I would also assume that the, it's more about how much you can deploy at scale versus, you know, how much, you know, using a slightly better processor than the other person or a slightly better power supply than the other person. It's more about just, can you get it out there? Is that, is that a correct statement?

**Rick Altherr:** I think there's two different avenues. There's having a competitive advantage. So where does it make sense for me to invest my specific resources to be better than my competitors? Yeah. And where should I be investing to help keep competition going inside the overall marketplace?

**Chris Gammell:** Right. Right. Cause you're also trying to broker deals with all these vendors that are selling you the parts and everything too. Right.

**Rick Altherr:** Right. And, and it's not, it's really about trying to make sure there are options available and that we're keep the innovation going in terms of new development. I want to see multiple processor vendors trying different things.

**Chris Gammell:** Yeah. Right.

**Rick Altherr:** And that doesn't necessarily happen unless we're all able to be in a space where we can adopt new technologies quickly.

**Chris Gammell:** Right. I was, I was, I mean, this is not server based, but I was really surprised about the USB-C thing. It seemed like a lot of tech giants kind of getting together and on an actual standard as well with the USB, you know, working group or whatever it is. But like, that makes a ton of sense. Like, I don't know. I, I think, I think that these kind of like standards and stuff like that, yes, there are hassles at the beginning, but the dividends in terms of like driving down hardware costs and increasing adoption over time, like that kind of stuff. Like thinking about, again, just to use the USB-C example, then you have five different chip vendors making hardware for it. And then that competes with one another and the connector vendors and everybody, you know, right. And that's just one thing versus an entire server. Yep. Exactly.

**Rick Altherr:** So through OpenCompute, I've gotten to know folks at Facebook and Microsoft, Rackspace, Fidelity, Nokia, you know, there's a whole bunch of these different companies. I would say everybody tends to know the top tier folks, you know, the largest deployments. And then, but there's actually quite a few that fall into this. I think it was large enterprise. They're not trying to be public cloud providers. They're not offering it as a billable service, but they have something that resembles a private cloud.

**Chris Gammell:** Got it. Interesting. I mean, I don't know what I was thinking about. Like, I guess I was kind of envisioning like, if you'll excuse it, like, you know, like buying from Dell or something, you know, like, like just buying the whole rack. So I guess I never really thought about this, but of course, you know, everything you've been saying has made a lot of sense in terms of why, why would you buy all the other accoutrement? Well, you know, you don't need that other stuff. So open it up and get your airflow optimized otherwise.

**Rick Altherr:** Yeah. If you look at what a Dell machine offers and its form factor and everything, and then you go look at a open compute leopard machine or a, or a Zaius machine. I mean, you can see there's a night and day difference of there's like a U shaped piece of sheet metal that holds everything. It doesn't have a top cover, no front panel. It's all optimized for airflow. It's about efficiency. How cheap can you make this thing while still having it perform reasonably? You, you want to optimize as much as you can around getting cost effectiveness for performance and the lifespan of this thing.

**Chris Gammell:** Yeah. Huh. So, okay. So it's a thing of sheet metal, right? I guess that the Zaius, Zaius, Zaius, how do you say it? Zaius. Zaius. Is it like Dr. Zaius? Like the... Yep.

**Rick Altherr:** We have a habit of...

**Chris Gammell:** Dr. Zaius, Dr. Zaius.

**Rick Altherr:** Giving our server projects a lot of interesting names.

**Chris Gammell:** Yeah. Okay. So can you give us... I mean, we'll try and link whatever pictures we can, but could you give us kind of an idea as well? Like what else, what else is in there? I guess there's like a audio picture.

**Rick Altherr:** Inside of a Zaius machine? Sure.

**Chris Gammell:** Yeah.

**Rick Altherr:** So a Zaius machine is a dual, dual socket power nine server from... So those are power nine processors from IBM. And basically our design there, Rackspace is also using it. It's heavily dominated by the processors and RAM. It's really about getting those two pieces deployed. So the bulk of a PCB that's, you know, think of, oh, 16 inches wide, maybe 20 inches deep. And a single PCB.

**Chris Gammell:** I remember that piece. Yeah, it's a single PCB. That's insane.

**Rick Altherr:** Two very large processor sockets. I think there's either 16 or 32 DIMM slots and a bunch of PCIe slots. That's more or less what's there. There's space to put one hard drive or an SSD as a boot device. And at the back is a HotSwap blind mate power connector. In Open Rack V2, it's a 48 volt distribution system. Okay.

**Chris Gammell:** And like when you say 48 volt too, is it like a 200 amp supply or are they all like individually for each connector has its own supply? No, it's a giant bus in the back. Oh, it is. Oh, it is really? Oh, wow. Yeah. Okay. So give us, could you give us an ampers range?

**Rick Altherr:** It varies on. I really just want to hear the high end. I mean, let's be honest. I believe the Open Rack V2 spec allows for up to a 25 kilowatt rack.

**Chris Gammell:** Oh, my God. That's insane.

**Rick Altherr:** That's a lot of copper, folks. Wow. And that's all battery backed at the rack level too. So the intent is that you put in AC to DC rectifier shelf to feed it. And then you put a bunch of battery packs also on the bus. So the bus actually isn't exactly 48. It floats with the battery voltage.

**Chris Gammell:** Sure.

**Rick Altherr:** But yeah, all of it powers off of one shared common power infrastructure there. And then all of the 48 volt power conversion happens on the server PCB. So one of the things with Zayas is actually it does 48 volt to point of load power conversion. So the CPU core rails at 1.2 and 0.8 volts are actually done in single step, 48 volt to 0.8. Oh, seriously? Oh, yeah. That's amazing.

**Chris Gammell:** Is it like those super high frequency converters too or what?

**Rick Altherr:** So it's actually I know Intersil makes them and a couple of other people are now selling them publicly. They're actually finding a lot of interest in the automotive groups. Sure.

**Chris Gammell:** Yeah.

**Rick Altherr:** Yeah. It was a really big deal of getting those parts available because you couldn't find that before. Yeah.

**Chris Gammell:** Right. Right. Yeah.

**Rick Altherr:** The silicon, like why would they make that? Right. Right. And now that they do, it's actually really, it gives you a really good power conversion efficiency. Got it.

**Chris Gammell:** So you kind of sit up on the curve up near the 95% or whatever they love to talk about. But if you're not in the right, if it's not designed for it, you don't actually get that full conversion.

**Rick Altherr:** Right. And I think specifically here it's 95 would be low. Right. Sure. Yeah, of course. I know I'm still stuck in the pasture, Rick. Sorry. Well, it's just when you're thinking about these designs, if it's a two kilowatt server design.

**Chris Gammell:** That's a good point. Yep.

**Rick Altherr:** The CPU and memory is considerable on these.

**Chris Gammell:** Yeah.

**Rick Altherr:** Yeah. So, yeah, it's really optimized around getting the CPU and RAM deployed. There are usually other server designs that are more about just bulk loading disks into the rack and making those accessible to the network. And those often are deployed as two separate solutions.

**Chris Gammell:** Got it. Okay. Interesting. So, well, let's, I mean, we got to get there eventually. I mean, you already mentioned it with the efficiency side. So, how the hell do you get all that heat out? Because that's certain, I mean, like, this is, when you and I were talking about you coming on the show too, I was like, I said, this is where electronics people should actually learn thermodynamics. It's like, okay, we're moving some heat here, folks.

**Rick Altherr:** So, how the hell do you get all that heat out? Yeah, there's a lot of different approaches. If you walk into a normal colo environment, co-location environment, you would see 1U servers with usually a front-to-back airflow. So, they've got fans to draw air in from the front of the chassis and blow it over all the components and blow it out the back. And they will do thermal control where they have a management processor that monitors the temperatures of heat components and locations inside the chassis and usually break up the actual airflow into zones inside the chassis.

**Chris Gammell:** Okay. Okay. So, like, the processor would be the hottest zone kind of thing or what?

**Rick Altherr:** Well, it's more, if you think of a channel of air going from front to back, you might put baffles in to separate that. So, the processors are going to be hot, but they're going to have a lot of airflow, whereas the dims might be less hot and need less airflow. So, you want to be able to control those two zones independently in terms of fan speeds.

**Chris Gammell:** Got it.

**Rick Altherr:** And overall airflow.

**Chris Gammell:** Yep.

**Rick Altherr:** Because the more you spin the fan, the more power you're bringing in your fans.

**Chris Gammell:** And that becomes a consideration too because there's just so many fans or what? Yep. Wow. So, it's about efficiency of electricity to CFMs or what?

**Rick Altherr:** Yeah. I mean, it's a factor. Yeah. You have to consider how much electricity you're burning in actually creating airflow.

**Chris Gammell:** Everything not processing bits is overhead, huh? Right. Right.

**Rick Altherr:** And there's a, the industry measure for that, it's called PUE. And it's basically a factor of energy consumed over energy used for actual IT load. Right? Like doing P-O-E? P-U-E.

**Chris Gammell:** P-U-E. Okay.

**Rick Altherr:** Interesting. Okay. Yeah. Power usage effectiveness. Okay. And it's a, it's a pretty standard term at this point in the industry, but it was not a big deal for until a decade ago. And the goal is to get to 1.0, right? If you could do 1.0, it means literally you're spending no energy on anything other than running the actual machine to do work.

**Chris Gammell:** Yeah. Right.

**Rick Altherr:** But yeah, everything from, you know, spinning the fans to pumping water to cooling water to whatever you need to do to actually do the thermal management, keep the lights on, etc. Falls into that.

**Chris Gammell:** Well, you said, so you said that the old way of doing it was moving air front to back. So does that allude to something else happening these days or what?

**Rick Altherr:** Well, it's more that you move out from the mindset of a freestanding rack, pulling air out in through the front and shooting out of the back with open space on other side. That would be a traditional colo, right? Just like a rack sitting in the middle of a room.

**Chris Gammell:** Yep.

**Rick Altherr:** A lot of colos have moved to a hot aisle, cold aisle scenario where basically you think of putting a baffle or a divider over the middle of the rack, cutting it into a front section and a back section. So the front section is where you pump in your air conditioned air, your cool air. So that's your cold aisle. And the machine then pulls the cold air through the front, pushes it out the back and goes into the hot aisle. And then that you put your air conditioning system. So it draws air from the hot aisle and pushes it back into the cold aisle.

**Chris Gammell:** Right. It's like a heat exchanger, except the heat exchangers also happens to be processing bits.

**Rick Altherr:** Right. Right. Yeah.

**Chris Gammell:** Yeah.

**Rick Altherr:** So that was a fairly common approach. And then when you're actually moving into extremely high workloads, you start moving the cooling infrastructure closer. So if I was using a normal chiller setup and I was taking that hot aisle air and having to blow it out to a mechanical equipment on the roof and then pump it all the way back, that's a really big cycle to move the air around.

**Chris Gammell:** Yep. Exactly. And then you lose efficiency as you blow it over the coils and then it comes back down. Right. Entropy just increases the heat of that air, right?

**Rick Altherr:** Right. So instead, you can imagine moving using chilled water where you put your chiller to cool down the water supply somewhere convenient. And then you run that chilled water up to near the rack and put the heat exchanger there. So the air to water exchange happens very close to your actual heat production.

**Chris Gammell:** So it's like a radiator type thing?

**Rick Altherr:** Yeah. Yeah.

**Chris Gammell:** Okay.

**Rick Altherr:** It's a heat exchanger that's going from air, you know, the hot air coming out of the server. You're transferring the heat through the heat exchanger into water, chilled water. And then the water carries that heat out to a chiller that actually, you know, extracts that heat out somewhere else.

**Chris Gammell:** Big ass thing, huh? Yeah. Big ass compressor. Yeah.

**Rick Altherr:** Yeah. And so that's, you know, you hit on the number two concern in deploying systems is the overall, how much heat can I actually take out of that space? Uh-huh. Um, number one is usually how much power can I get into that space? Uh-huh.

**Chris Gammell:** So you mean like power delivery over that 48 volt thing?

**Rick Altherr:** Right. Well, actually, and down into the rack. Even if I'm running, you know, 208 three phase into the rack, there's still a limit as to how much power I can actually deal with inside that rack. How, how size, um, what's the size of all of the wiring?

**Chris Gammell:** So the size of the inverter or the size of the rectifier, size of the- Right. Or the, yeah, the copper in the wiring, stuff like that. Right.

**Rick Altherr:** So, and then it turns into, well, all of that power that you can deliver in has to turn into heat, which then you have to deal with the cooling side. And the third one is actually the, the weight of the equipment. Can the floor actually support it?

**Chris Gammell:** Holy crap. Right. And you're trying to keep costs down on the infrastructure level as well. So you don't want to have to make some like triple reinforced steel beam thingy. Exactly. Yeah. Right. Yeah. I remember the, uh, the infrastructure underneath a semiconductor facility, like, man, that, that is some intense shit. And I can imagine that you don't want to have to do that. Right. Like the, especially if you're trying to like rubber stamp these things all over the country or different countries as well. Right.

**Rick Altherr:** Yeah. I mean, ideally in a data center application, you want things to be really inexpensive. So if I can just have a simple poured concrete floor, that's great. But that means I can't use a raised floor system to run all my cooling pipes and all that kind of stuff. Right. And wires and, yep. How does that change? And where does all that equipment go?

**Chris Gammell:** Hmm. Uh, well, okay. So, uh, you had mentioned a connector and I didn't write it down. So you said the 48 volt rail has some kind of standardized connector. Is that right?

**Rick Altherr:** Um, it does. Uh, it's actually, I, it would be a part number, but it's a blind bank connector. It's. It's. Oh, blind mate.

**Chris Gammell:** Like you could plug in without looking kind of thing.

**Rick Altherr:** Yeah, exactly. Like it self aligns. Yeah. Yeah. It's, it's designed that you can take, um, uh, a tray, which is effectively a machine, um, and slide it into a slot and it just blind mates directly into the power rail. Oh, nice. And then the hot swap connector or a hot swap controller powers up and brings the machine online.

**Chris Gammell:** Right. And for those who don't know, could you explain what a hot swap controller is?

**Rick Altherr:** So hot swap controller, you, you essentially, if you've ever, you know, plugged in a charger or something with a high capacitive load into a wall outlet and you see the sparks fly, you know, if you put an immediate load onto a power delivery system, you can have a lot of problems of like pulling the rails down or arcing or whatever. So hot swap controller basically just monitors the power coming in on that connector, waits for it to stabilize and then allows the rest of the system to start powering on.

**Chris Gammell:** Yeah. Yeah. Those are, those are great. And, and actually I didn't realize. So when I went to an industrial company, I didn't realize they used to do that mechanically where they would just like, they would move the, so it would be like a card edge thing. And then the card edge finger, the finger on the card edge quote, air quotes, you know, just feel one would be a little bit shorter. And so that would contact second kind of thing. Right. But that doesn't, that doesn't quite do it when you're, you know, doing a ton of swapping out and stuff. So. Right. Yeah. Hot swap controllers are, they're great little chips. I mean, they're just, usually it's like a P channel FET and a little like a, what is it like a boost converter pretty much? Or not even boost converter. It's like a, it's just monitoring current draw.

**Rick Altherr:** Yeah. Yeah. It's something that has to decide if the power's in a good enough state. Is it okay to actually start powering it up? And maybe a soft start of some sort.

**Chris Gammell:** Yeah. Yeah. That's great. That's cool. Yeah. It's, it's really interesting too, because like, as you're going through these different types of silicon and stuff like that too, you know, you get, I used to have sales guys walk around and, you know, tell me about these new chips. And sometimes I just didn't know what they were for either, you know? And obviously some of it, I can assume that this is a huge part of the industry as well. Like just a ton of silicon going towards this stuff.

**Rick Altherr:** Yeah. There's a whole bunch of specialized components that go into these servers and into the racks and all sorts of places. It just, there's any part of the system that you look at, there is a small sub problem that has a specific solution that you need to find a way to solve it.

**Chris Gammell:** Yep. Yep. So another thing you would kind of alluded to is, I guess we were talking about power wiring and that's a huge concern, but what about the actual networking side as well? So like, is it all ethernet? I mean, are there non-standard things that I wouldn't expect connecting between boxes or how does that work?

**Rick Altherr:** A lot of it is pretty standard at this point. A lot of it is really moving into the really high bandwidth stuff. So not things that you would find at your average, you know, going to Fry's or at your desk type thing, but 10 gigabit or higher switches and things like that.

**Chris Gammell:** But it is still ethernet based. It's still squeezing it down to a single pipe instead of doing like some monster parallel connector or something like that.

**Rick Altherr:** Well, I mean, it depends on how you look at it. Like 40 gigabit connectors with QSFP is sort of a parallel scheme over it because it's really designed to run over multi-wave fiber and yada, yada, yada. Oh, really? You know, it's basically as you get into these really high bandwidths, you're trying to figure out techniques to squeeze more stuff. Right, right. Through a single fiber.

**Chris Gammell:** Like when we talked to Dave, it's going over the transatlantic fiber cable thingies, right? And it's packing in as many bits as it can because there's only so many fibers going under the ocean. Right. But it is fiber optic though. It's not like Cat5, like copper.

**Rick Altherr:** It's changed over time. It originally was a lot of copper. And as we move from 1 gig to 10 gig to 40 gig to 100 gig, you just get to a point where fiber makes more sense everywhere.

**Chris Gammell:** Okay. And then, but like connector wise as well, like is it like...

**Rick Altherr:** It's all standard stuff. I mean, SFP and QSFP modules with fiber connections. Okay. It's not going to be a Cat5 because that would be copper.

**Chris Gammell:** Right. Okay. I guess I don't know any fiber connector names, so that's really what I'm getting at. So, yeah. I mean, like I have no need for that ever. So, that's cool though. And so, okay. So, then what about like hooking banks together, machines together, all these things? Like do they all go back to switches? Are they going machine to machine like daisy chaining? How does that work then?

**Rick Altherr:** Well, the goal, again, as we touched on before, is moving data between machines as fast as you can. All right. Especially at a cluster level, which is sort of, think of it as roughly a room of machines as a cluster. Okay. So, if I want to have a fully connected mesh between all of those, that would be interesting. And so, that's not particularly practical. But what you really want to do is build a networking topology within the cluster that lets you have as much bandwidth as you possibly can get from any to any.

**Chris Gammell:** Okay. So, yeah. Yeah. You're saying because if they have to all go up to some master machine and then go back down, then that's a longer traverse pass rather than going, you know.

**Rick Altherr:** Well, you have a fan in problem. If I have a thousand machines that all have 10 gig connections and they're all saturating it, then I have a thousand times 10 gig data coming into that central point.

**Chris Gammell:** Aha. Okay. So, that would be like a hub and spoke model versus mesh would be like everything's connected to everything. Is that kind of the idea?

**Rick Altherr:** Yeah. And so, you can think of it as a whole bunch of machines connected to a rack switch. And they are all, you know, single connections from the machine to the switch. And then at that top of rack switch would actually have maybe 16 connections that fan out into different switches that make up part of the cluster fabric. Oh, okay. And because it has all these different paths it can possibly go, it will spray that traffic across all of the different ports. So, you're actually balancing over all of the available links on the network.

**Chris Gammell:** So, are you guys like starting to replicate like neural connections as well? Like is it like starting to look like that of like a really big brain or how does that?

**Rick Altherr:** I don't think so. I mean, I'm not a specialist. Just tell us what's going to happen.

**Chris Gammell:** Just give me like a rough year when I should expect to, you know. Lock myself in.

**Rick Altherr:** AI has not replaced my job yet. So, I don't even know.

**Chris Gammell:** I'm still trying to figure out what the hell you do, man. That's crazy.

**Rick Altherr:** Mostly, I go to events and write firmware.

**Chris Gammell:** Yeah. That's, yeah. Okay. Well, this is, that's crazy about the, I mean, just because there's, I mean, so much data too. So, okay. And I also wanted to get, because this is an interesting segue as well. So, what's controlling all this stuff? I mean, like, so you mentioned OSs at one point. At like a machine level. But then there must be another layer on top of that that's kind of like scheduling, telling it where to go or giving it addresses or how does that all that work?

**Rick Altherr:** Yeah. There's a lot of different solutions for that. But essentially, you think of it as at the machine level, you probably have a management controller that it's basically like a lights out management type system. So, you have a dedicated way of talking to the machine to do power control, monitor the system health, collect inventory information, etc. And then you would boot an OS on the host machine that is often Linux, but it doesn't have to be. So, you would run away from a new feature that deals with making that machine useful and participating in the network. And then you'd run some software on that OS that connects it into a cluster level scheduling system of some form. Kubernetes is one approach. The OpenStack software stack has an approach to that. Another one is called Metal as a Service. That's by the canonical folks. And basically the whole idea is the machine has to advertise what resources it has available to the cluster scheduler. And then that gives an endpoint for people to actually either request a machine or to request specific resources. And there's different usage models. Like the MOSS model is I want to be allocated a machine. I don't care which one it is. Just give me a machine and install the OS I want on it. Whereas Kubernetes is more I want you to run my Docker container and I don't really care where it gets run. But there are all these different models and it's still an evolving space where you might run multiple models in the same cluster and divide up the machines or they might build on top of each other. You might have it be that Kubernetes is using MOSS to request machines as necessary.

**Chris Gammell:** Interesting. Yeah. Okay. So can we maybe take a journey as a packet of data? I mean I'm trying to put all this stuff together. I know this is in your head but man this is a whole like and I really feel for people like I'm at least I run virtual servers sometimes and so I'm like I'm a little bit in there but not even close to this level. And I was expecting to go the other direction and talk more about hardware. I mean we can do that. We still can talk about that more too. But like this is just there's so there's so much vertical space between like I enter a URL and then you know it gets to silicon and it bounces something back to me. You know I mean like there's a lot of layers in there.

**Rick Altherr:** There are and especially when you talk about like an actual public cloud service you might pass through 10 or 15 machines before it actually ends up at your application. Yeah.

**Chris Gammell:** And that's the other thing too is that like so all this stuff is abstracted and automated and whatever and it's like and people are deploying these services that have existed and are evolved. But now I'm trying to think about it all at once and it's like a fire hose right. So that's why.

**Chris Gammell:** It's crazy.

**Chris Gammell:** Yeah. Okay. But the thing I'm really wondering about is is that the networking level machine to machine. So okay. So machine number one has a packet that it needs to send to machine number two. Does it have an address that it sends it to or how does that even work.

**Rick Altherr:** I mean it looks very much like a standard network at least as far as the machines perspective. Okay. Often what you see is a rack is assigned a subnet and it's treated like a layer two switching domain which is very similar to anybody's home network. Okay.

**Chris Gammell:** And you might. Machines behind a firewall that could switch in your house. Yeah exactly.

**Rick Altherr:** And so you would have an address per machine and they're all on the same subnet. They can all talk to each other directly and that works for a rack of machines and a rack can fit you know 72. Machines no problem.

**Chris Gammell:** Right. So just about keeping which 192 168.0.0 you're actually talking to and what track. Right. Right.

**Rick Altherr:** Keeping those straight. Right. And that's really a management problem and people build custom systems for tracking which host name is what you know. Yeah. Which IP address and serial number and all that kind of stuff. Got it.

**Rick Altherr:** All right.

**Chris Gammell:** So then that's interesting because then that that kind of does remove at least it's a little bit standardized. It's just behind. It's just at a lower level than I'm ever used to interacting with.

**Rick Altherr:** Right. And then as as you're leaving the rack then things get more interesting of you're moving into a layer three switched system usually which so you're actually going through many different switch chassis and it's forwarding it along based upon the IP address rather than MAC addresses. And and so that's where you're connecting all of these layer two subnets together. Got it.

**Chris Gammell:** Hmm. Yeah. I never even knew what subnets were for. So yeah that's way beyond my pay grade already. So. Okay. Well let's let's dive way back down to the silicon then because that's I think what you're talking about like this stuff and wherever you want to go.

**Rick Altherr:** I mean I'm like I said I do a lot with open compute and I know like when we when I brought Zayas in everybody was pretty shocked that like you can actually go get server designs that are all the schematics are available all of the board layout files are available like there are fully documented server designs actually on GitHub now.

**Chris Gammell:** Yeah. And we will link to them. I was I was actually really blown away by that. Yeah. The whole the Zayas thing. So. What else is I mean. So. I guess some of that is kind of organizational to like what's coming what's in the pipeline but. What else should we know about the Zayas. I mean like maybe from firmware is perspective as well because that's what you're you've you've done in the past like. Yeah.

**Rick Altherr:** What is what is the firmware on there. I don't even know. Well. So my team deals with the management controllers primarily which in this case we run a software stack called open BMC that's a Linux distribution. That was the specific version we're using was started by IBM and we work with them as an open source community to basically build. If you've ever had a server that has an IPMI connection or you know those lights out management processors on them. That's exactly what this is. And so we're just re implementing that as a standard Linux distribution.

**Chris Gammell:** Could you define light up management. Does that just mean like a headless system. No displays. Yeah. Interfaces.

**Rick Altherr:** And nobody physically in the in the presence of the machine I should be able to power the machine or like turn power on to the machine remotely. Oh OK.

**Chris Gammell:** Interesting.

**Chris Gammell:** Yeah. And so this is kind of supervising all that's looking at everything on board and is it also scheduling stuff you said the management system.

**Rick Altherr:** So this is actually so these they're chassis managers they're basically a processor whose sole purpose is to make sure the hardware is functional and to control the power state. You know I can turn the power on turn it off I can restart the machine I can collect the serial numbers of each component. Oh cool. I can pull the temp sensors and things like that and it provides a way to do that even when the host processor is actually turned off.

**Chris Gammell:** So is that like a separate connection then or how does how does that actually do that.

**Rick Altherr:** Often it is separate connection there's usually a second Ethernet jack on machines. There's actually a newer standard called NCSI that is a way to connect that Ethernet interface into your separate NIC and have a single connection going off to the RAP.

**Chris Gammell:** Cool. Network interface controllers at NIC.

**Rick Altherr:** Yeah. OK.

**Chris Gammell:** Wow.

**Chris Gammell:** That's cool. So who's watching the Watchmen. Who's watching the Watchmen. Yeah.

**Rick Altherr:** Like how do you know if you're processed the open BMC is dead. Well I mean you see that remotely. I mean that's where you have a cluster system that that knows that there's supposed to be these management controllers out there and it's asking them status of are you alive are you powered on. Have you what temperatures are you seeing right now on all the components.

**Chris Gammell:** But what about like if you're all your temp stuff out of spec. I mean like how do you know or maybe it's not it's really isn't necessary.

**Rick Altherr:** Well think of it as I have a cluster of machines so I can use that cluster of machines to run software that monitors the cluster of machines.

**Chris Gammell:** Hmm.

**Rick Altherr:** Hey bro. Yeah.

**Chris Gammell:** Got it. OK. Yeah. Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** OK. How important is accuracy I suppose is a general question to. Um.

**Rick Altherr:** It depends on what you're what you're dealing with. I mean temperatures can be quite important like you're trying to keep control at maybe a degree or a degree or a degree. Control it maybe a degree level degree Celsius. OK. Um. What you're really looking for is cases where things are out of thermal spec you want to know when things are going to start exhibiting problems.

**Chris Gammell:** So like SPC like trending type stuff or what.

**Rick Altherr:** Um. Really you're looking at the manufacturer probably has a max temp spec for their part for operational range. Uh huh. And you're trying to compare to that to see how close am I to that actual top of spec margin.

**Chris Gammell:** Got it. OK.

**Rick Altherr:** Um. But you might also be looking for things like is the fan speed seem plausible or is it zero. Uh huh. Right. Yeah. Right. Yeah. How do I know if a problem has occurred or a problem will occur. Right.

**Chris Gammell:** Uh. And then who is. So you mentioned that the servers are watching the specs kind of thing or it's reporting back up to some supervisor somewhere. Uh. Which might be running on the same server or whatever. Right. But. Um. How does that. End up impacting other things then like so is it just like go no go like if it's too hot you just say shut it down and don't use this machine.

**Rick Altherr:** Yeah. A lot of it is is very heavy handed that way. Um.

**Rick Altherr:** If we notice a problem you want to stop using it. Right. And shut the machine off and have somebody come fix it. OK. It depends on exactly what the failure is. If I go to a temp spec maybe I really what I need to do is just turn the fans up. Um. Oh OK.

**Chris Gammell:** Yeah.

**Rick Altherr:** Right. You know another option is maybe I just need to tell the OS. Um. By the way I'm going to throttle your. Your scheduling so that you use less power. Um.

**Chris Gammell:** OK. And so it is dynamic like that then too it says. So. You talk up to the the scheduler up top and it says you say machine whatever is a little underperforming. Don't send as many jobs that kind of thing. Uh.

**Rick Altherr:** It's. It's more local than that for that rapid response problem. You know if I'm actually in a in a thermal situation that's usually more dealt with at a single machine level. So it would be the host processor software would be talking to the management processor. Um. It would notice when it's getting out of spec and it would go ahead and take action. And then. The higher level software would get a notice that says by the way. I gotta slow things down a little bit.

**Chris Gammell:** Got it. It's like a flag system kind of thing. Yeah.

**Rick Altherr:** OK. But other issues like if I see a hard drive experience a read failure. That's something where I'm just going to stop using the disk. Uh huh. And I'm going to notify the job scheduler system. Hey this disk needs to be replaced. Figure out when you should do that.

**Chris Gammell:** OK. Interesting. So how does all this stuff interact then at like a community. Because I have to imagine that this is. So you've got all these deployments. You said hyperscale is 50,000 plus units whatever out there out in the world. Uh huh. Um. And probably many more. But then. I mean hardware evolves. So there's different revs of each thing. Is there a standard even just for how it's talking up to the scheduler saying like oh this temperature is too hot. Don't use this machine. Is that like a standard API or how does it actually interface between these machines at a programmatic level.

**Rick Altherr:** Well so this is a lot of what my current work is around. Um. Essentially the standards for system health monitoring or remote management functions. Uh. The common standard is IPMI. It's a standard that was created by Intel back in the late 90s. Um. It's still very commonly used. It's controlled by the DMTF now. Um. And. It's OK. But it really doesn't address some of the concerns that you have when you're dealing at these larger scales. So for example. The way it models the system. It. It. Really tells you things like there are temp sensors. But it doesn't tie those temp sensors to what components they affect. Oh OK.

**Chris Gammell:** Yeah. Right. It just says. In box one. There is a temperature of. 75 degrees. Whatever it is.

**Rick Altherr:** It may have multiple temp sensors. It might say CPU zero is. Uh huh. This temp.

**Chris Gammell:** OK.

**Chris Gammell:** Like. Like. Like. Like.

**Rick Altherr:** Like.

**Rick Altherr:** Like. Like. Like. Like. Like. Like. Like. Like. Like. Like.

**Rick Altherr:** Like. Like. Like. Like. Uh huh. Uh huh. Uh huh.

**Rick Altherr:** Uh huh. Uh huh. Uh huh.

**Rick Altherr:** level. And a lot of it comes down to, you know, I have many generations of hardware, I need a common way of viewing that information so that these higher level systems don't have to care about

**Chris Gammell:** every individual generation. Right. Yeah, exactly. You would never want to expose that, but you still need, but if there's no, you know, quote unquote standard, then yeah, how do you actually, you still

**Rick Altherr:** need to transmit that information somehow. So, right. So a lot of my work is, well, now that we've all done that individually and come up with these standards, we're trying to figure out how to share. And we're doing pretty well at sharing at the hardware level. If I look, Microsoft makes their Project Olympus motherboards and they're available through Open Compute. And I can buy one of those and I can figure out how to adapt that and stick it into a rack at my work. But then when I look at the interfaces of how to integrate that into higher level management systems, I am missing a lot of detail. I would basically have to do all that work from scratch because it's all custom.

**Chris Gammell:** So like go and write, you mean go write new firmware that works with your system?

**Rick Altherr:** Well, I mean, they have firmware that probably already written for that system, but I at least have to go in and write an implementation of the protocol that I use to talk to my cluster level services. Got it. Got it. Got it. And a lot of that's probably describing the hardware to those higher level systems. You know, oh, this PCIe lane and this I squared C bus are on the same physical PCI connector. Right. I need to know that in order to know where all the sensors are and what devices I'm talking to, to trace down error information to individual components. Is there like a grid system

**Chris Gammell:** or anything like that where it's like, no, no, before you've sunk my iceberg C bus. This is a wild

**Rick Altherr:** west situation right now. So it's something that I aspire to build more in that space of developing standards there. Trying to figure out how to actually move that to a model where the hardware designers can actually just specify this is how the hardware layout occurs at a logical level and a physical level. So that the software can just examine the hardware and say, oh, you know, maybe it's putting things in the ACPI tables or other things in the system firmware that say, this is how all that stuff is connected. But it doesn't exist there today.

**Chris Gammell:** If you do a grid system, can you call it the GAML system? Is that, is that, are we, we're agreed on that? Is that cool?

**Rick Altherr:** Uh, I will take that under advisement.

**Chris Gammell:** Okay, great. That's all I really want. I mean, it's fine. Yeah.

**Rick Altherr:** You just want your name somewhere in the history of competing.

**Chris Gammell:** Somewhere, exactly. Right. And then at some point they'll be, I'll be, it'll be cursed out. But that, that damn GAML system. Yeah. Uh, uh, so I mean, so this is, does it all flow up through the open compute project then? Like how do you actually, I mean, you said you can buy this, this project Olympus, but like, how do you interface? These are just like you email Bob at Microsoft or whatever, like, you know, the people there or how does that work?

**Rick Altherr:** Um, so the open compute group has a structure of, there are members, um, that develop new standards and, um, as well as new products. So there, there's implementations of these standards. So like project Olympus is a set of standards. They have one for the motherboard form factor, for example, and where connectors should be and things like that. And then there are implementations of that where they have an Intel based server and they might have an AMD based server in a caveat on base server, um, that are specific implementations of that. Okay. Then they have other members that are called solutions providers that work with the, uh, ODMs to actually manufacture the equipment and sell it to end users. So you would actually go to an ODM like penguin computing or horizon solutions, uh, to actually order the equipment. Okay. But the, the intent is that we're all sharing the designs.

**Chris Gammell:** I'm going to say a plebs like me could go and do that if I had enough cash on hand.

**Rick Altherr:** Yeah. Yeah. I mean, if you go somewhere here, uh, on the open compute, uh, dot org website, there's a marketplace link and it has a link to all, you know, it has a list of all the different types of machines and who you can order them from. So if you're a large enough volume, you can go directly order that from an ODM, you know, be prepared to buy 40,000 of them. Um, but if I go to penguin computing, I can probably buy them in much smaller units, but it's also a higher cost per

**Chris Gammell:** unit than, right? Yeah, exactly. Yeah. Yeah. Yeah. Wow. This is insane stuff. Like this kind of scale, like, well, it's a good name hyperscale. That's definitely a good name. Uh, but damn,

**Rick Altherr:** that's like the second thing I see on the list here is actually from HP enterprise and it's a, uh, a 48 port 10 gig switch with six 40 gig ports and x86 CPU. Um, you know, that's, that's a standard

**Chris Gammell:** rec switch for us. Okay. I don't, I don't, I don't have any reference point, I guess. Well,

**Rick Altherr:** I mean, how many people are going to have 48, 10 gig ports on there on a switch? Yeah,

**Chris Gammell:** that's true. That's a good point. Sometimes I plug a raspberry pie into mine at home. So pretty much the same thing. Uh, wow. Yeah. But the cool part about a lot of these, um,

**Rick Altherr:** when you look at it, they'll have the links to the actual specifications and you can download a lot of the information on the schematics, the, the board layouts and that kind of information.

**Chris Gammell:** Hmm. And so what is, what is the, uh, what is the layout program du jour? Is it all a mentor?

**Rick Altherr:** It varies from, from company to company, um, and ODM to ODM. Often you see a lot of cadence,

**Chris Gammell:** um, okay. Cool. I mean, is it, is it worthwhile for people? I mean, I guess you can go, that means people listening to the show could go and like open it up with one of the viewers. Usually they have free viewers, right? You can go and look at it and see how they do the crazy DDR4 layouts and

**Rick Altherr:** stuff like that. Right. Yeah. I mean, uh, part of the challenge that I've faced is, well, okay, we provide these server designs to the public there. They are available. Uh, what can people actually do

**Chris Gammell:** with them? Now what? Right. Well, first off you go and you buy a cadence license for 20 grand and,

**Rick Altherr:** and then you open a 400 page schematic and then you, then you look at a 20 layer board layout and yeah. Oh yeah. Right. Right. Um, there's a big skills gap there that, uh, honestly, I don't know how to fill that in. I've talked with a variety of folks who understand that, that the knowledge of building this scale of design is very niche and very isolated to these very large companies. And they're trying to figure out how, how to make a model out of bringing that more to the masses.

**Chris Gammell:** Um, I mean, well, I mean, I guess this is kind of an open source question in the first place, right? Is just that, uh, how many people even open the schematic, right? Or even open the layout in any case of it. But I think at the base of it, the, the fact that it's the people that really need it are already working together, it seems like. So that's a great, that's a great start in terms of building out alliances and standards and stuff like that. The rest is just kind of

**Rick Altherr:** nice to have. Well, and a lot of this, um, as the standards show up in the open compute group, often those become, once they stabilized a little bit there and gotten a little bit of runtime, they seem to get pushed into, uh, the larger industry standards. So I know there's some work on hard drive firmware and hard drive features where the T11 and T13 groups, um, or sorry, T10 and T13, uh, the ATA and SCSI, uh, standards groups have already said, whatever you guys decide that you're going to do in the open compute world, we'll use that as the, the preview of the standardization process. So when it comes into ours to actually put into the formal specs for hard drive manufacturers and storage controllers. Oh, that's great. Yeah. You know, it's been pre-vetted as this is probably only going to make sense to data centers. Yeah. Yeah. Right. But why, why not standardize on it?

**Chris Gammell:** Right. Right. Exactly. Yeah. Yeah. Wow. Uh, okay. Well, let's talk a little bit about data centers because, uh, this is another thing you sent me, you sent me the, there's a, uh, uh, Google seems to have a good, a good page about their data center. I was just watching a, uh, 360 tour inside there, stuff like that. What should people expect to see when they, if, if you went into a data center, I guess you, like, like I said, you can go and watch this 360 video. So that's very interesting, but like, is it just all pipes and I don't know? Yeah. How much does that stuff impact your work?

**Rick Altherr:** I suppose. Um, actually quite a bit. Uh, one of the things with the hyperscale is we design the machines. We have the machines manufactured. We have the machines deployed into data centers. We see them through their full life cycle until we decide they're no longer worthwhile keeping. And then we deal with the, just the end of life and destruction, um, and recycling aspects of it. So the time where it lives in the data center, we have to understand how people interact with the machines there and what that environment is like. So a lot of, a lot of it is really just putting ourselves in the shoe of these are who we make the machines for. There are the people who have to actually go walk out on the floor and touch each machine. Um, but for the most part, they are very industrial settings. Uh, as you'll see in the pictures, if you go to the google.com slash data centers, um, it's, it's a lot of, you know, in our case, colorful pipes. Um, those are nice. Those are really nice. Uh, but that's like the cooling plants and things like that. Um, and then, yeah,

**Chris Gammell:** all this, all this like heat, heat exchanger stuff, all this stuff, like the subfloor stuff that actually was very reminiscent of below a fab as well. I mean, more individual gas pipes and stuff,

**Rick Altherr:** but yeah. And then the actual data center floor is just row after row after row of racks. I mean, it's machines as far as the eye can see, um, to give a sense of scale, uh, room can easily be 300 yards by a hundred yards easily.

**Chris Gammell:** Yards, huh? Wow. We're really, we're really going American on this one. Yeah. Yeah. Well, you always say that though, because they always give it in the, uh, three football fields, right? Yeah. That's what they love talking about. Yep. Yep. Yep. I used to work

**Rick Altherr:** in a nine football field, uh, situation, but to, uh, to help out our non-American friends, let's see. So, you know, yeah, think about 300 meters by a hundred meters as a building.

**Chris Gammell:** Yeah. Yeah. It's pretty, I mean, it's pretty close. It's pretty close. Yeah. Yeah. But, uh,

**Rick Altherr:** yeah, it's okay. So that's massive. And, and so you end up in these situations of, um, even locating a machine inside of a data center is a problem. Really? Oh, okay. So like when the

**Chris Gammell:** scheduler says machine, whatever, ABC one, two, three is down. Yeah. Where, now what, where is it?

**Rick Altherr:** Um, and, and I have lots of fun stories about that. I mean, there's just the problem of you're in a, in a closed building. So GPS isn't going to work for you. You're talking about really tight locations anyway. Um, and probably highly dynamic as well. Right. Of like high RF emissions, just from the sheer amount of machines around you. Um, lots of metal and things. So most low locationing systems don't work very well. Um, maps are, need to be very dynamic because equipment's constantly being moved around. Yeah. Right. Right. Right. So it's very common to get lost into a data center. Um, most of them have incorrect signs. Uh, sometimes you're just wandering down the aisle looking, going, okay, so I'm in the, you know, I'm near this section of machines. It should be the next section. Oh wait, it's not there. Um, and they've tried different things. You know, maybe we, uh, paint an artificial star scape with paint balls on the ceiling and then use a camera and constellation tracking software to figure out where I am. Oh, that's a cool idea. I like that. Um, you know, there's QR code, stuff like that. Yeah. I mean, it's just trying to find ways of actually being able to navigate the facility is, is a challenge. Um, could you just make like little robot carts

**Chris Gammell:** that just take you where it's supposed to go? Wouldn't that be cool? Wait, is that yes? Are you going to do that? You should do that. You can call them gamble carts. I'm sorry. I'm not really, I don't really propose that you call anything. But then they'll get confused with the gamble grids

**Rick Altherr:** and yeah, right, right, right. Um, yeah. Yeah. So that's one issue. Another issue is just the sheer quantity of parts that you need to have on hand to repair machines. Yeah. Like a stock room

**Chris Gammell:** kind of thing. Oh yeah. Yeah. Wow. I'm, I'm paused at like, sorry, I don't mean to be, I'm staring at this, this 360 video and this is actually a great use of 360 video, which normally I'm like, man, whatever. Um, but like I'm, I'm keyed in on what 445 on this video that I'll link in, but like, it's just like rows. I mean, it looks like the, the, the weirdest looking library ever, but man, it just keeps going to like it perspective runs out basically. Yeah. Yeah. I mean, it really is. What the hell is on all these things? Is this like, this is my email somewhere on these things, right? Yeah. Yeah. At least one copy of it. Yeah. Right. Right. Man, that is nuts. There's so, I mean, how many servers to humans are there? I mean, like, is there a measure of that?

**Rick Altherr:** Um, I, I never think about it that way. Actually, I had a coworker who asked us to think about it in

**Chris Gammell:** terms of people per megawatt deployed. Yeah, that's okay. I was going to ask about power stuff too. So

**Rick Altherr:** keep going. Sorry. Well, it's just a, when you think about your operational load, it's, it's really how many people do you need to maintain a certain number of megawatts of deployed capacity of machines? Um, and that was really the, the optimization metric that we were trying to think of. How can you use the machines and, and software and other things to reduce the number of times a human has

**Chris Gammell:** to touch things? Yeah. Right. Cause that's what a true dark, uh, what do you call it? Like a lights out facility. This does not seem lights out because there's just so much maintenance to be done. But like that, that was always the promise of like robotics facilities as well as like, Oh, you just turn off the lights and it just keeps going. Right. That's the idea. Right. But damn, I mean, what is, I mean, so like that 300 by a hundred meter facility, how many rough people

**Rick Altherr:** would you even need? I mean, is it like, it could be as small as, you know, a hundred. I mean, it depends. It's still a lot of people. It's still a lot of people, but it's, it depends on exactly what you, what is being done there and how often things are turning over. Sure. Sure. Sure.

**Chris Gammell:** Like something like super high powered or specialized that specialized then. Well, and don't forget you,

**Rick Altherr:** for any site you have, you're going to have the needs of physical security and sure. Yeah. You know, HR and all the associated things. So it, it builds up staff a little bit quickly. Yeah. Well,

**Chris Gammell:** more reasons for robots, I suppose, but damn. Um, well, okay. So I want to ask about power as well. So what, I mean, a data centers in the megawatt range or multiple megawatts, gigawatts, what is,

**Rick Altherr:** why I don't actually know? Um, can't really give a specific numbers. I, that's okay. Yeah. No, it's, it's a fair question. Um, I mean, certainly thinking in megawatts is, is reasonable. I would say anybody who's, who's dealing in large enterprise or, or hyperscale would also be in, in that range.

**Chris Gammell:** Okay. Yeah. I mean, cause the reason I ask is cause the, well, one of the things right on the, the data center page is talking about renewable energy. Right. And so like, just talking about like cooling is one thing, right? So again, like you said, you're in the nineties for efficiencies, but, uh, I assume that overall efficiency of a data center is probably not more than, you know, 90%, you know, power into, to actual, well, I guess it doesn't all get turned into heat. Right. But there's a lot of heat coming out of there. And so you think about like, not only do you, if you have a one megawatt facility and it's 90% efficient, then you still got a hundred kilowatts of, of, uh, of heat that you got to get out of there then too. So like talking about just the, the infrastructure stuff of powering the facility and then cooling it for whatever the waste heat is. So that, that number seems monstrous. Yeah. Right. Yeah. I mean, when choosing data center locations,

**Rick Altherr:** you got to think about, I need a place that has a lot of space. I need a lot of power. I need a lot

**Chris Gammell:** of networking bandwidth. Oh yeah. Right. Yeah. Backbone, backbone, backbone, backbone. Right. And those

**Rick Altherr:** become your selection criteria. Um, it's not, but then they, then they like end up in like Iowa.

**Chris Gammell:** I don't get that. Like sometimes I I've seen like some of the, it seems some of them are really remote, you know, I don't get that. Well, often that can just be the case of there's a lot of

**Rick Altherr:** power available there. Maybe it was an old, uh, manufacturing area that had a lot of power infrastructure built up and that is no longer being utilized to full capacity. Interesting. Okay.

**Chris Gammell:** Yeah. That's cool. Um, and I guess that's the other really interesting thing about data centers in general is that it, it all is down to an equation. It's like how much, how much processing can you do per dollar? Right. That's the per dollar, I guess. Yeah. Yeah. And it's, it's like the whole, like people that are like Bitcoin miners talk about that all the time too, where they're like, how much processing can I do? How much is it going to cost me electricity and resources to get one Bitcoin? Right. It's like, right. That's a similar, much smaller scale kind of thing.

**Rick Altherr:** Right. Yeah. Um, it's a constant question and it, it's a lot of how we have set up our decision making process is around which choice gets us a better return on the, the most compute power

**Chris Gammell:** available to us per dollar. Yeah. Huh. So, uh, well, okay. I was going to say, I was going to ask a question that I don't think I'm allowed to ask, but I would have to assume, I'm just going to make a statement here then, I guess I would have to assume that you, uh, if I was going to do, if I was going to build a data center, there would be times where I would start to do more and more custom things just because the scale makes sense. So like, even to the point of custom silicon, custom capacitors, custom connectors, all these things. I mean, obviously some of that's already in the open compute, but you're trying to get other people to make it, but there's probably a lot of scale decisions that are based on that. Right. You can just, you start to look at like tall poles and say, well, let's get this cost down. And how do we do that? So build versus buy is always a

**Rick Altherr:** consideration. Uh, because we do have people, you know, we have a design people, we have people who

**Chris Gammell:** can design and make equipment. Google, Google hires some talent. Facebook hires some talent. Yes.

**Rick Altherr:** Right. They pay a lot of people. So, but it becomes a question of, is that an effective use of money? Sure. So if the industry is caught up enough and, and delivering something that's good enough for our

**Chris Gammell:** purposes, then go ahead and use it. Um, so it's more like it's when you want to do something new that you can't yet do. That's more of a reason to dive into that thing. Yeah. Yeah. Okay. Or you

**Rick Altherr:** think you can do it in a significantly better way. And there's always trade-offs. Maybe it's time, you know, as you see in open compute, a lot of the ideas are being shared where it was proprietary knowledge before, but it's being pushed into standardization because that customization starts to lock you out from buying the commodities now. Right. Yep. Yep. Yep. Yep. So it's a,

**Chris Gammell:** yeah. And I, I always talk to, to students about that when I'm teaching electronics, it's like, yeah, figure out what a lot of people are using. You're going to find cheaper parts. Right. I mean, if you get locked into that one part, it might be that one spec that you really need, but really make sure you need it first. Right. Exactly. Exactly. Yep. And I'm sure that at the scale you're talking about here too, you probably have chip vendors falling over themselves to offer new solutions because they've got people internally that are doing that stuff as like, well, that, that 48 volt to 0.8 volt converter. That's, that's really fun. Actually. I like that. But like there's, they're, they're out trying to prospect the next chip that can solve these things. Right. So.

**Rick Altherr:** Well, everybody wants to sell to you when you're a large company. I mean, that's just. Yeah, it's true. The nature. The bell of the ball. Um, whether it makes sense for you to buy from. The bell of being very, very rich. Yeah. Whether it makes sense for you to buy from them is a different question.

**Chris Gammell:** Yeah. Yeah. Yeah. Right. Yeah. I can imagine there's times when it's security issues or other stuff like that as well. So, um, isn't it kind of nuts that all this stuff goes, I mean, like the whole thing is that like, when you really think about like a single bit traveling from, again, from my, the URL or some my computer through all the stuff. And then it's, I mean, of course, like this makes sense, but like the fact that it's going down to a server and touching down on a piece of silicon and actually flipping a, flipping a transistor is that is, you know, signifying that. And then it goes all the way back up to the stack, man, we, there's, there's a lot

**Rick Altherr:** of stuff in there, isn't there? There is, there is. Yeah. Yeah. There's a lot of people and a lot of

**Chris Gammell:** engineering time invested in that. Yeah. That's crazy. And so you mentioned like, it started to change 10 years ago. Why, why was that? What was that? What was that shift? Um, you were saying, saying like some of these things had started to change about 10 years ago.

**Rick Altherr:** Um, well, I mean, it's a rough guess, uh, as to exactly when that happened. I think what you look at was there was a time where internet service providers or internet service companies like Google and Yahoo and those folks, they had a lot of machines and they were hitting scalability challenges, but the mindset of moving towards completely custom data centers where you control and try to optimize for efficiency was just new thought process. Um, and so what did they used to, they used to then rent

**Chris Gammell:** other people's data centers at that point? Is that kind of the idea? Yeah. I mean, everybody, when you're

**Rick Altherr:** small, you, you, you do co-location. Um, and eventually you get to the point where you're buying half a building and that's where you start having to question how much space do I need to buy? And should I

**Chris Gammell:** just be building my own buildings and right. And also projecting out and saying, well, I could keep doing this, but maybe it's right. Six months from now, it's a different story. Right. And then

**Rick Altherr:** you hit maybe five or six buildings and you go, well, if I'm building five or six buildings and I know that I'm growing at this rate, can I sustain that? Right. Or do I need to go back and figure out how to utilize that, those existing buildings more effectively? Hmm. So there's just been a progression over time. As the deployments get larger and larger, you start asking different questions.

**Chris Gammell:** Yeah. Okay. And actually that's another good question too. Is there, are there upper limits on scale of data centers as well? Like, I mean, I guess you mentioned the floor in terms of like weight bearing and stuff like that, but is there a reason that there wouldn't be some mega scale data

**Rick Altherr:** center? Um, failure domains become an interesting problem. So as you get larger and larger and larger, if you build it as one gigantic building block, then you have to figure out what are the common failure points? Because if I take out an entire building and it is now a massive building,

**Chris Gammell:** whatever. Yeah. Um, natural disaster. Yeah, exactly. Right. Yeah. Flooding. Right. Yeah. I mean,

**Rick Altherr:** that's going on. Yeah. You have multiple buildings in different geographical regions to deal with that problem, but it's still a massive outage of equipment. So it, you start to question, how do I break things up to reduce the number of common failure points? How, how can I break it up into smaller chunks that can keep operating independently? And what's that optimal point? Where do I make that trade-off between, I would rather it be a big system that's treated as one big block by the end user versus, I really want it to be these smaller chunks that are, can easily come and go on their own.

**Chris Gammell:** Hmm. Is it, uh, is that even to the point where it would make more sense to have two buildings in the same town instead of one big building in the same town? Is that kind of like even to that level?

**Rick Altherr:** Yeah, it can be. Okay. Interesting. Yeah. It's not uncommon to see data center campuses.

**Chris Gammell:** Oh, really? Okay. Yeah. Yeah. They do that with chip fabs too. So I keep going back to that. I know I keep, that's really all I know. That's the only thing that is that the scale that I can even think about. Right. So, uh, and are they all one floor or are they do any of them? I mean, not, I mean, one level, I suppose, not one, I know there's sub floors and sub sub floors and stuff.

**Rick Altherr:** You know, I know that there are places, um, there are facilities owned by other companies that are definitely multi-floor. Some places actually try to mix office space and, and data centers. Um,

**Chris Gammell:** it just depends. You could heat the office space in the winter, I suppose.

**Rick Altherr:** There's lots of different concepts or, or it's just like land space might be a very high premium. So you don't actually want to completely waste it just for a one level building or something.

**Chris Gammell:** Montana is different than Tokyo, right? Exactly. By a, by a couple, a couple steps.

**Rick Altherr:** Yeah. I mean, go look at a data center built in New York, uh, New York city, and it's going to be very different.

**Chris Gammell:** Yeah. Yeah. Right. The cost per square foot is pretty, pretty high. Right. Yeah. Um, I guess there's like, I, I trying to not ask a question specifically about your employer, but like, how, how can I even ask this? I'm just wondering about the scale in terms of a team. Like, so like at a Facebook or, you know, someone else's as well, like how many people even work on this stuff? It seems like it's this whole, like I said, I have, I had no idea about all this stuff to start with, but then there's just like this whole other world of people working on this stuff.

**Rick Altherr:** So, I mean, scale wise, I think it varies from company to company. And I know even within open compute and the people I know there, there's different approaches. There are companies that act more in a developing the specification and hiring out to an ODM to actually build all the equipment. Um, there are companies that take more control of the design and do maybe joint development of schematics, um, in a JDM type model, or it may be that they actually do the full design and use an ODM just to do board layout and, and fab. Um, so your team size can vary considerably from, from company to company, but you can also do a lot with very few people. If you have, you know, talented people and a common purpose, if you wanted to do just servers, um, and do that kind of deployment, the engineering teams aren't necessarily very large. Uh, it may only be 10 people actually required to build a server from a getting the schematics and the overall layout by the time you factor in supply chain and all the people to actually get it to something physical landing at a data center. Of course it's, you know, hundreds of people at that point. Yeah. Okay. Yeah. That

**Chris Gammell:** makes sense. And I guess I, I, yeah, there's also the, uh, like Intel is going to give you reference designs and, you know, field support stuff like that as well, or whatever. Exactly. You're using

**Rick Altherr:** exactly. So, and often when you're dealing with like the electrical design, you might have a lead, uh, electrical engineer dealing with the overall system design and working with, uh, an ODM who's doing a lot of the schematic and, and kind of rough work or, uh, more detail work and then have special, more specialized, um, EEs that focus on maybe power subsystem or maybe a signal integrity that come in to help with the design and different aspects of it.

**Chris Gammell:** Yeah. Right. Yeah. Domain experts around these things. Uh, well, I have to imagine it's, it's still changing a lot, huh? I mean, like, yeah, obviously you've seen it. I mean, the openness is an interesting change, but do you, do you find that it's still as dynamic as it was, you know, five years ago? Oh yeah, definitely. Or more dynamic maybe?

**Rick Altherr:** Uh, is it more dynamic? Uh, I'd say, no, it's always been pretty dynamic. I mean, especially,

**Chris Gammell:** I guess, I guess, is this stuff scaling linearly? I don't even know how, how data centers scale and

**Rick Altherr:** stuff like that too. Um, boy, that's hard to characterize. I mean, the thing is, is that

**Chris Gammell:** data centers are always in flux. So we've like, as, as different models go in and out of vogue kind

**Rick Altherr:** of thing. Yeah. Well, not even in and out of vogue. It's really, when is the right time to remove old equipment and put new equipment in its place? Oh, that's a great question. Yeah. Yeah. Um, so there's always constant evaluation of, is it time to just upgrade the equipment? Is it time to build a new site? Um, what makes the most sense at the time? And it turns over a lot. I think there's still a lot of growth going on overall from what I hear. Um, there's definitely a lot of interest at, at things like open compute events where a lot of companies are getting into these larger and larger deployments and they're thinking about the scale out models. And when you start hearing, you know, a company's, um, talking about, well, yeah, I'm going to deploy 30,000 machines and I want to figure out how to actually buy that. That's, that's really interesting to hear that from lots of different companies. It's, it's becoming a new, new thought process for them. Um, and a lot of new players in the market. Whereas before it was, you know, a handful that actually dealt in that

**Chris Gammell:** sort of quantity. So does that mean that hyperscale is moving up the chain even or? Yeah,

**Rick Altherr:** I think, I think it's everybody sliding up. Um, the hyperscale is getting to larger and larger appointments and, and sort of as the large enterprise moves in behind that, they just keep creeping up into the space that used to be hyperscale. Right. Yeah. I hear this web thing is going to keep going. Um, I don't know. Yeah. Funny that it seems to be really useful. Yeah. Yeah.

**Chris Gammell:** Sometimes. Right. We say, as we talk over thousands of miles, uh, on, on fiber, that's, uh, yeah. Anyways, uh, with near perfect connection. Yeah. Why didn't I do this next week when I'm actually in the Midwest? Oh yeah. Well, there you go. Uh, that's all right. Um, well, so I, we're, we're like an hour and a half in, so I feel like we should, we should start to, to scale it down. I, I feel like, uh, we, we're going to have to call you back at some point, man. Uh, but what, what else should people know like off the bat? I mean, like, especially, I guess, I guess the main thing would be like, if someone's interested in getting into this stuff, what should they be thinking about or studying or what? Uh, that's a

**Rick Altherr:** really good question. So I think what, what I've heard a lot when talking to companies that make server equipment or, you know, switch equipment, um, these are not skills that are taught in school. It's especially when you're looking at the electrical design or even at the firmware design and things like that, the considerations that happen at server scale and, and especially in large deployment scale, um, the cluster level services is becoming more of an open field in that you can get involved in open source, but the electrical design and the firmware design is very much still, you need to go, go to those companies that actually do that and, and get involved and figure out what makes sense. Um, a lot of them and bring in a, or take an approach of bringing in untrained engineers or, or, you know, fresh out of school or have been in the industry for a while, but not in that area. And just expecting that there's going to be a learning curve because where are you going to get the skill of routing, uh, PCIe gen four, you know, that's just,

**Chris Gammell:** Well, who's not doing that on the weekend, man, come on.

**Rick Altherr:** Right. So it's not available to, to anybody unless you happen to be already in these, these spaces. So junior engineers come in and learn that, um, on the firmware side. And, uh, I routinely hire in people that way. Now on software, it's a little bit easier to bring in more experienced people because software at a certain level, there's a general skill set around understanding complexity and problem solving that just maps in. Yeah. They have to come up to speed on the problems that are being solved, but more often than not, people can move between different

**Chris Gammell:** software domains a little bit more easily. Right. Domain specificity is not a, is not a

**Rick Altherr:** prerequirement. Yeah, exactly. But it's also, you got to go to these big companies that actually support, uh, development of these things. If, if you, uh, go to your local large company, if I walked into general electric, uh, they're probably going to say, sorry, right. We don't actually design our own servers. Um, right. Yeah. Right. Right. Right. But for the most part, like I know my team, uh, constantly has a job posting available on the, on our public job, job board. And I think most, most of these companies are the same way. It's, it's an area where they're large

**Chris Gammell:** enough that it's, uh, constantly available. Is it, is it tied to, so I know, I know the term DevOps, but I know that's more on the networking. Well, maybe I don't know what it is, but it seems like that's tied to server stuff as well. But is that more like utilizing the servers or like, are there keywords that people should look for if they're interested in getting into this field? Um, it does

**Rick Altherr:** vary a lot. I would say look for data center is one. Um, uh, I know at Google, we often talk about as platforms and, and there are, that's a somewhat common thing. Um, but that can also get really confusing because of other uses of platforms. Uh, everything's a platform these days. Exactly. A platform is a service, right? I would say it's actually one thing that has surprised me throughout my time here is most people don't even realize these jobs are available. And I think you're, you're hitting on something, which is if they're not easy to find. If only there was some kind of search engine. Imagine that. Um, and, and, and if there were terms that weren't utilized by other sections of the industry. Well, there's yeah, that, but yeah.

**Chris Gammell:** Okay. Well, that, that's a good start though. And I think that, you know, yeah, like server rack, I'm sure, I'm sure that, yeah, you know, use your Google foo people, you can figure it out. And, but, uh, that, that's, that's interesting that it's out there. And I mean, I'm guessing it maybe, I mean, even if does open compute, compute get listed in job recs these days or no?

**Rick Altherr:** Uh, not so much. Um, it's still an area where I think open compute still operating as a way to exchange between the large players for the most part. I mean, individuals are, can be members, um, and contribute and they do, but there's still, uh, um, the heavy players, the big players are still these very large companies. I, yeah. Yeah. I would say it's more, um, there, if you think of the big cloud, uh, cloud platforms that are out there, they're all going to have their own hardware design folks for their data centers. Oh yeah. Okay. Uh, and then there's the ODMs behind that, which are in a similar space. Right. But first you got to

**Chris Gammell:** find out which ODM ODMs are actually in this space and doing this stuff anyways. Right. Right. Yeah. Well, people can do some research. That'll, that'll be good. Uh, I'm sorry. We didn't get to talk about cars too. Cause well, I will, I will link in the car talk. So, uh, you, you had done a great talk at HDDG, uh, about ECUs and what was it called? It was something knocking, right? Uh, I don't remember. Oh, knock, knock, add more fuel. I like that. I like that title. That was a good one.

**Rick Altherr:** Yeah. Yeah. Um, yeah. Cars are definitely a hobby and that was just a fun talk kind of overview of the, the sensors that are used to do engine management. Yeah, it was cool. Yeah. Especially like the tuning stuff. That was really neat. Cool. So, uh, where can people find you online? So I am a pretty active Twitterer. Um, though, though before Warren's, I talk about things other than tech. Um, no, um, uh, my GitHub is, is moderately active. Um, for the most part, everybody can find me via my amateur radio call sign, um, which is KC eight APF. And, uh, basically if you, if you see

**Chris Gammell:** that anywhere, that's me. Okay. That's great. And we didn't talk about any ham radio stuff either. So yeah, yeah, we'll have to have you back on and you can be our resident server. We'll be like me and Dave, you know, talking out our asses about servers and web stuff. And yeah, just make it up as we go along, man. So this has been great. This has been really great. So thank you for, thanks for sharing about this stuff and definitely we'll, uh, link to all the open compute stuff and all the videos we

**Rick Altherr:** mentioned, stuff like that. It's been my pleasure. All right. We'll talk soon. Thanks. Night.

**Speaker ?:** Night.
