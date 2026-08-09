---
episode: 348
title: An Interview with Art Kay
url: https://theamphour.com/348-an-interview-with-art-kay/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released June 18th, 2017. Episode 348. An interview with Art K.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Art Kay:** Hi, I'm Art K. from Texas Instruments. And just a little background on myself. I've been an engineer, practicing engineer since around 92. Graduated from Georgia Institute of Technology. And most of my career I've been working in semiconductor applications. Also semiconductor tests. So it's a very rewarding career. And I get to put together a lot of interesting collateral. I like to teach. Even did a little teaching on the side. You know, at different tech schools and so forth. And so as an applications engineer, I get to put together learning type collateral to help our customers with analog electronics. Awesome.

**Dave Jones:** Thanks for joining us, Art. Thanks. I notice I've got a comment. Semiconductor. Yes. Is that commonly how it's pronounced inside TI? Or is it a local thing? Is it a local dialect thing? I don't know. Because like to me, it's semiconductor. Right. Not semiconductor.

**Chris Gammell:** Yeah, but Dave, you say a lot of things weird. Come on, man.

**Art Kay:** My own pronunciation, I guess. Right. Okay.

**Chris Gammell:** That's cool. It's Art's own style. Of course, we've got to start out with the important stuff, don't we?

**Dave Jones:** Yes. Right.

**Chris Gammell:** Well, it's great. And so I was mentioning to Dave as well. So you're down in Phoenix, right? Or Phoenix area? Tucson. Tucson. Sorry. Tucson area. That is the former Burr Brown facility as well.

**Art Kay:** That's right. Yes. I started out my career at Burr Brown. And, you know... Oh, there's TI rubbish. No.

**Dave Jones:** So you're still a Burr Brown man?

**Chris Gammell:** Yeah, there's the holdouts, right?

**Dave Jones:** Like, are you still like, yeah, it's Burr Brown.

**Speaker ?:** Yeah.

**Art Kay:** In a way, I think there's, you know, a good bunch of us still in the, you know, the facility. And we definitely, you know, are proud of our heritage.

**Chris Gammell:** That's great. Excellent.

**Dave Jones:** So it's still a separate facility. They didn't try and integrate it with TI facilities and move you guys? Or is there, like, are there physical reasons you're still remaining there? Or...

**Art Kay:** No, there's, you know, there's a couple hundred engineers in Tucson. And so it's really the core... You know, of course, we've hired many people since Burr Brown was acquired. But there's, you know, three buildings. It's a pretty substantial engineering facility. It's basically R&D. We're not doing production there. But when we were Burr Brown, we used to do production. We had our own wafer fab and so forth.

**Dave Jones:** Oh, so you had a wafer fab on site? Yeah, we did. Oh, right. So what happened to that?

**Art Kay:** Well, they shut it down. It was a four-inch wafer fab. And really, by the time we were acquired, it was obsolete or becoming obsolete. So it was a timely kind of change that was important for, you know, Burr Brown to stay viable. You know, they just didn't have the kind of wherewithal to, you know, create a huge semiconductor fab.

**Dave Jones:** Given that the fab, though, was already sort of like bought and paid for, would there have been any value in keeping that as like a teaching, training facility? Or I don't know. You've never had to pay for a fab, have you, Dave? No, well, yeah. What cost would go into maintaining it, I guess? I'm sure it's pretty huge. Pretty huge. Okay.

**Art Kay:** And I think a lot of the equipment was probably, you know, I'm just as conjecture, really, because I wasn't in the fab. But I think the equipment was becoming obsolete and difficult to maintain and that kind of thing. Right, okay.

**Chris Gammell:** Yeah, getting kits and everything.

**Speaker ?:** Gotcha.

**Chris Gammell:** Yeah. So, Art, I mean, you mentioned kind of the evolution of Burr Brown into TI and just the change over the years. I mean, how maybe we could start there from, you know, where you started in, you know, the educational world and then kind of seeing how applications has changed over time. I mean, what is your view on the industry?

**Art Kay:** So, I started in 92 in test engineering, which was pretty challenging and interesting because we would test the wafer and package level devices, including trim, you know, do a laser trim on the resistors to, you know, increase the accuracy and so forth.

**Dave Jones:** As in, you're talking about the silicon resistors?

**Art Kay:** Yes, right on the die. So, on a microscopic level, you know, you cut little chunks of the resistor away and, you know, trim the offset or the drift or the gain error or what have you.

**Dave Jones:** Now, I've seen – I've got a technical question there, if I may. Sure. I've, like, under the microscope, I've looked at these things, you know, fairly often. Like, you can see different types of cuts. Like, there's L-shaped cuts and there's square and there's longitudinal and there's chunk cutouts. And there's – is there something to all those different geometry cuts?

**Art Kay:** Oh, yeah. There's different geometry resistors. There's plunge resistors and top pat resistors. And basically, you know, it amounts to whether you want to do a coarse change, a very wide change in resistance. Right. Or a very fine change. And frequently, you'll have a coarse resistor and a fine resistor. And so, you'll do a plunge and that, you know, creates a massive change in resistance. And then you'll do a more refined one where you keep cutting smaller and smaller pieces. And actually, the parameters are often measured while you're doing that cut. So, you know, you're measuring offset and you cut a little piece of the resistor. Sometimes, there's some settling because the light from the laser disturbs things.

**Dave Jones:** I was going to say, doesn't it heat it up? Does it, like, heat it up? Because you're burning or are you burning away the material?

**Art Kay:** You do. I would have thought there'd be a thermal issue. You do. But to my knowledge, there isn't much of a thermal issue. It's more of a settling issue from the light. And certain wavelengths of lasers are important. And, you know, the kind of focus of the laser to – you have to cut through the, you know, the top layers. And, you know, there's a lot of physics behind it. And once you have that equation, you know, you can do a pretty good job of laser trimming. And even today, you know, a lot of times people think of laser trimming as sort of archaic or older technology. But it's still being used today because for bipolar devices, you can't really do digital circuitry on there. So, a digital-type trim isn't really feasible.

**Dave Jones:** Oh, okay. So, the other way to do it is like a modern digital trim, for example. Yes, exactly. So, are TI parts moving in that sort of direction where they can do it digitally instead of process-wise?

**Art Kay:** Yeah. Both ways. Right. You know, generally, the bipolar devices will be laser-trimmed or, you know, and the CMOS devices will be digitally trimmed. Right.

**Dave Jones:** Because I'm guessing here, and correct me if I'm wrong, but because you're mostly dealing with analog parts here, you're not dealing with, you know, 10mm by 10mm dyes or anything like that, right? They're really quite tiny dyes. So, you would have the extra room, wouldn't you, for like the digital trimming and stuff like that? I mean, what percentage of the dye would be taken up with that sort of extra trimming?

**Art Kay:** You know, on the CMOS devices, I'm going to just guess some 30% or something like that.

**Speaker ?:** Oh, okay.

**Art Kay:** Yep. On the bipolar devices, those resistors can actually be fairly large and take up, you know, a good percentage of the dye.

**Dave Jones:** Yep.

**Art Kay:** Hmm.

**Dave Jones:** For like power reasons, or is it just for value reasons? They physically have to be that big?

**Art Kay:** For value reasons, in the sense that to properly, you know, cut with the laser, you have to have enough space, physical space. Right. There's a certain width to the laser cut and, you know, to get a fine change in resistance. Of course, you know, I mean, economically, you always make the dye as small as possible. And if you look at dye from the, you know, when I started till dye now, it's quite different. Right.

**Chris Gammell:** And what was the node when you were getting started and doing all the test engineering?

**Art Kay:** The node, did you say? Yeah.

**Chris Gammell:** Well, I guess it's different for analog, but just, yeah, I guess generally what node it was, even though analog is usually trailing a little bit.

**Art Kay:** You know, I'm not really sure, to tell you the truth. But I can say that the dye were large enough to physically see. Yeah, right, right, right. And now they're not.

**Chris Gammell:** And I guess like a four-inch wafer as well. I mean, you could probably just tell by how many parts you could even fit on a four-inch wafer, whereas, you know, there's still some operational four-inch wafer fabs, but they're getting even more parts on there just from efficiencies and process and stuff like that, right?

**Art Kay:** Yeah, you know, you'd have maybe a couple hundred dye on a four-inch wafer in the old analog days or analog processes, and now you get thousands to 50,000 dye. 50,000 dye.

**Chris Gammell:** And that money, that savings comes right down to us. I don't mind. Yeah.

**Dave Jones:** Now, I've actually recently looked at a test wafer under a, you know, times 400 microscope and stuff, and I can actually see.

**Chris Gammell:** I feel like Dave's just like, I have a microscope. Everybody, I have a microscope. Yeah, I've got a microscope now.

**Dave Jones:** I like know all this. I'm an instant expert. And do you guys put like test transistors on like the side of the dye so that you can actually like test the parameters of like a transistor or some other thing on there, or do you just leave that at the entire dye testing level?

**Art Kay:** There's usually, well, you know, I haven't done it for a while, the testing, but when I did it, there was four tests. Five test sites, one in the middle and then, you know, three or whatever, four on the periphery. And they had different transistors and resistors. And, you know, at the wafer fab, that's how they would make sure that the processing was being done correctly. Yeah. And then after the wafer fab, they would take the wafers and run them through a more comprehensive test, measuring everything, and that decide whether or not to even use the wafers. If they failed that more comprehensive test, maybe the whole wafer lot could be scrapped. And, of course, this is a long time ago, but I assume it's similar now. And after that, then my part would come in where I'd actually test and trim the wafers, and then they'd dice them up and package them. And then I'm back again and working with them in package form.

**Chris Gammell:** Oh, really? Okay. So you would see wafers twice, or I guess parts of wafers twice, huh?

**Art Kay:** Right. Yeah. Yeah. Encapsulated or packaged and then, you know, in wafer form.

**Chris Gammell:** That's interesting.

**Dave Jones:** So how did you test these? Are there commercial universal testers that you can program to test analog parameters like this? I mean, it's easy to do some sort of digital testing, but analog is like, you know, you require a lot of, you know, testing functionality to test the functionality of wafers. Or did you have custom-made gear, or was it some sort of universal test system that cost a million bucks or something?

**Art Kay:** Well, when I started, we had a lot of homemade testers. And some of them were IEEE, rack and stack type things with, you know, a lot of Hewlett Packard equipment. Right.

**Dave Jones:** GPIB control. Exactly.

**Art Kay:** Yeah. Yep. And then later, there was also some hand-built, you know, testers that, you know, we designed ourselves in-house. And those would be less expensive than the rack and stack. And then now there's commercial test systems, you know, which test extremely fast. And that's probably a different modern difference as well. The test times have gone down to seconds or sub-seconds. And, you know, you might test multiple devices, four or devices, eight devices at a time. And so then, you know, they're being tested in parallel. And then you divide the test by the number of devices. You divide the time by the number of devices being tested. So you can get testing very quick on these modern testers, whereas it would be, you know, I don't know, 20 seconds, sometimes minutes per die in some of the older devices.

**Dave Jones:** Right. And the testing's still done per die?

**Art Kay:** Yeah. Every die is tested. Yep. And every packaged device is tested. And that's actually an important point that a lot of our customers don't realize. Sometimes they think maybe some statistical means is done. But not only is every device tested, but almost every parameter you see in the data sheet, not quite every parameter, but almost every parameter is actually tested.

**Dave Jones:** And that is why you can pay $50 for like a real high-end op-amp, right, is because of the sheer amount of test involved.

**Art Kay:** Well, I mean.

**Dave Jones:** Test and full characterization.

**Art Kay:** I don't think any of our modern op-amps are quite that expensive. No, but you know what I mean. But, yes, I mean, you can definitely, you know, it definitely affects the price, the comprehensive nature of the testing and, you know.

**Chris Gammell:** Right. Yeah, there's different speed grades and everything as well. Well, I guess speed grades are different. And if they're tested over temperature. Yeah, binning and everything. Yeah.

**Art Kay:** Yeah, temperature testing's quite expensive.

**Chris Gammell:** And so when you were doing this testing, Art, I mean, like, what level of the design process was this? Are you talking about the actual manufacturing level where it's going through these ATs? Or is this more you were working with the first silicon or pilot runs and stuff like that?

**Art Kay:** Yeah, that's a good question. There's two categories we call characterization and test. So characterization is what you were just mentioning. When the parts first arrive, a whole wide slew of different tests that usually make up the characterization curves in the data sheet are done. And that's a one-time kind of thing. And it's often statistical in nature. We, you know, we look at distributions. We look at curves over temperature. And a lot of data, a huge amount of data is collected. So I was not a characterization engineer. I developed the production test. So my goal was to, you know, work on these test systems and get the test time down as small as possible and make it as accurate as possible. And it would usually test the kind of parameters that you see in the data sheet table as opposed to the characterization engineers generally test the curves, all the various curves. So if you look at a data sheet, usually there's a data sheet table first and then there's curves. So the one-time kind of tests are done by the characterization engineer in the curve area. And then the production test where each and every device is tested before it's shipped is done, you know, by the type of engineer I was, test engineer. Very cool.

**Chris Gammell:** Yeah. And so, and you would probably, so when you would see issues, right, it was that mean that you would go and feed it back to like a QA or a FA, like a failure analysis team? Or how did that end up working in the, in the, was it in the FAB?

**Art Kay:** Well, it would be, it would be in a final test, you know, facility, which is a kind of clean room, but not the same level as a FAB. Yeah. And what I did was I did the engineering work and, and part of that is to kind of do a capability study to make sure that the test equipment and program and so forth is all accurate. And, and we're going to have a good yield and so forth. And so a lot of effort goes into making sure that it's a robust solution. And then once everybody agrees and all the, you know, kind of meetings have concluded, then it gets released to manufacturing. And so once it's released to manufacturing, product engineers would then take care of production issues. And they would, you know, of course call the test engineer if there's something they had difficulty with. But once it's released, normally the test engineer would work on a new project, a new device getting released.

**Chris Gammell:** Right. Setting up the next, the next line to make that nice and efficient, right? Right. Yeah. Cool. Okay. That's great. So how did you make this hop then from, from test engineering? Where did you go from there in your career?

**Art Kay:** Well, in test, I started testing instrumentation amplifiers. Then I moved to Delta Sigma converters. And then I moved to temp sensors. And, and finally I decided, well, I want to kind of do something different, you know, completely different than test engineering. And I didn't even really know much about application engineering, but I heard a little bit and it sounded kind of interesting. And I had, you know, in grad school, I was a teaching assistant and I had taught at a couple tech schools. And I liked teaching and I thought this might be a good thing. And I'd written a couple articles prior to moving into applications engineering. And I heard that the apps engineers wrote articles. So I inquired a little bit and the more I heard about it, the better it sounded. And it was really the best decision I ever made in my career because applications engineering, very, very interesting. You get to do, I think customers will come to you often with, with their difficult problems. And you get to help solve those difficult problems. So you get kind of the, the fun part, I think. Yeah.

**Chris Gammell:** You're like the paratrooper of, of the engineering world, right?

**Art Kay:** Right. Paratrooper.

**Chris Gammell:** You, you come in and you fix the, you know, you got to fix the emergency problem and you just, you move on to the next thing, you know? Yeah. That's great. So what, I mean, do you have any examples you're allowed to talk about that were like just off the wall, uh, kind of problems?

**Art Kay:** Hmm. Hmm. Let's see. Uh, oh boy, that's hard.

**Chris Gammell:** Like I always think about like the, the, the month long ones and then you have the eureka moment. You know what I mean? Like the, uh, like that's, that's, that's usually the ones that I think about. Like I had a memory issue in an FPGA a long time ago that I will never, ever, ever forget.

**Art Kay:** Hmm. Let me see. Uh, you know, I, I guess I've run across a lot of, um, electrical overstress issues and sometimes those can be interesting and challenging where, uh, where the part is blowing up in their system and you got to kind of try and figure out, um, if it's, it's not necessarily a repeatable thing. It happens once, um, every, uh, so often they just see a higher failure mechanism in this device and, uh, something in their system is feeding through an overstress voltage and you just got to try and, um, guess at what that is. And you don't really know for certain because, um, it doesn't happen so often. You just make some recommendations as to, um, you know, what, what kind of corrective action you could do. And, uh, and then, um, if they don't call back and say, it's still blowing up, then it's all.

**Dave Jones:** Yeah, right. So do you get a lot of customers like wanting to use parts outside of spec and asking if you, if that's okay and if you can qualify it and.

**Art Kay:** Yeah, it definitely happens. Um, and, uh, you know, they often want characterization done beyond, um, what we've done. And, uh. Okay. So is that a service that you would offer them? We try not to. Yeah. That makes a bad habit right there. Yeah. You're right. In general, um, you know, I mean, it's really a bad idea to violate the specs because they, they're usually set that way for a reason. I mean, uh, there's something we discovered during characterization, some temperature, um, you know, limit or whatever. And we always put guard ban in, but just, uh, pushing the limits is not a good idea. I don't think.

**Chris Gammell:** Right. Yep. Definitely did that way too much. Yeah. So, uh, which, uh, which division were you in when you were, when you, when you got started in applications, uh, there's a lot of divisions there. So which ones did you end up, uh, sticking in?

**Art Kay:** So I was, I was working in temp sensors from test point of view and I moved into the, um, the analog group, which, which at the time, you know, they change from time to time, but at the time covered all op amps and instrumentation amplifiers, temp sensors, references. Um, and, uh, yeah, that's it. Um, and there was a separate group for data converters.

**Chris Gammell:** Oh, okay. Okay. Yeah.

**Art Kay:** And, and actually I was in that group for, um, quite a few years. Uh, and, uh, you know, after a few years I, uh, became manager and then, um, just, uh, a year ago, um, decided, well, I've done enough op amps for a while. I think I'll, I'll try data converters. And so I switched from the op amp team to the data converter team to SAR data converters.

**Chris Gammell:** That's awesome. Yeah. And that's nice that you have that flexibility too. You can go between different groups and obviously you're, you're changing different roles and all the, all the time as well. Um, I, how long, how long, so you've been at it since 92. So that's what, 25 years, right? Yeah. Man, that's, that's another thing that's interesting to me is that like, we don't really hear about that that often anymore, you know, of just people staying at company. So that, that's a good sign that you're doing interesting work and you, you like what you're doing.

**Dave Jones:** Yeah. Why do they separate out data converters?

**Art Kay:** Well, I mean, I guess it's from, uh, expertise product line perspective. Um, they're, they're broken down into product lines and you'll have, um, a design engineering team, a test engineering team, characterization team, uh, marketing team and, you know, applications team. Um, and, um, it would be, uh, it's easier for people to develop expertise, I think in one, one area, you know, op amps for example, and, and, uh, to have somebody work on, you know, the op amps one day and then, um, you know, uh, data converters and other, um, maybe from an app perspective, it wouldn't be bad. In fact, it might be good because really applications is always systems level, you know, kind of thing. And you can't work with op amps and not work with data converters, but from a product line perspective, it makes more sense to, you know, separate it out.

**Chris Gammell:** Yeah. It's probably a lot of working together anyways, between the different groups and, and creating, creating, uh, creating different app notes and stuff like that. I mean, is it, is that, that is a big part of, of what your job was is kind of doing this is like factory applications. Is that right?

**Art Kay:** Or yes, it is. Okay. Um, as opposed to field, which is more working directly with customers in a certain region.

**Chris Gammell:** Right. Yep. And those, those are the ones that I used to interact with a lot. Um, and so, but you know, every once in a while it felt like the, the, the factory, or the, sorry, the factory applications engineers would come out and also kind of go through the product lines. And that's always, I mean, that's, it was a really nice, nice treat actually, just to sit down and talk with people that really knew the stuff deep.

**Art Kay:** Yeah, we, I like, definitely like traveling out into the field and, um, you know, we'll go out and give seminars to, uh, customers. We'll, um, we'll, you know, directly work with the, uh, field apps engineers, um, you know, provide, uh, literature for them, you know, uh, app notes, articles, uh, presentations. Um, we have training seminars for the field themselves, um, where we can get a little deeper, uh, on amplifiers or, you know, data converters than, than they're, you know, normally getting. Uh, the thing about being a field engineer is you have to cover a wide range of different products and it's very difficult for them to, you know, become a super expert in, let's say precision amplifiers. Um, and so when the, uh, the factory people go out to the field, they can kind of, um, jump start them and get them, you know, help them learn, uh, in a lot of details about, you know, whatever the product line is, um, in a very short amount of time.

**Chris Gammell:** Right. Yeah. It always felt like a, uh, like a support organization. I mean, well, I guess just a technical one, right? I mean, but you kind of raise the, uh, you know, if there's a problem that the FAE can't solve, then they kind of send the email up the chain to whoever. And eventually, eventually I'm sure it lands on your desk.

**Art Kay:** Yes, exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** And then where does the level stop at someone with a long, a long gray beard where, you know, if they write, we, we have to send out the gray beard to get that bad.

**Art Kay:** It does occasionally. I mean, people will be sent out for, um, you know, kind of a customer direct customer assistance. You might end up at a site. Um, you know, I, uh, ended up once, um, in a China for a week, I'm working with the customer. So it doesn't happen very often, but, um, it occasionally happens. You, you directly sit down with the, the field apps guy and the, um, and you and the factory and the customer all work together.

**Chris Gammell:** I'm sure the, uh, the bigger, the bigger companies get the, uh, get the parachuting in a little bit more often, huh?

**Dave Jones:** Right. Are there actual gray beards there of like, you know, tweaking stuff with their tongue at the right angle? Sorry. I just have the Bob Pease picture in my mind of, you know, tweaking something until like, are there like real old timers like that?

**Art Kay:** Sure. Yeah. There's, there's definitely, um, a good number of them and, and, uh, a lot of them from the Burr Brown era. And, uh, you know, of course the different groups at TI national, um, they have their fair share as well. So sure.

**Dave Jones:** So it's still an old timers game sometimes.

**Art Kay:** Um, well, I mean, you know, it's, it's interesting. Uh, I think the young guys ramp up much quicker than, than we did when, when I first started and, um, I think part of that, um, I'm happy is, uh, is part of putting together this good training because I was kind of left, um, to figure it out. You know, it's just like, Hey, I figured it out. You figured it out. Right. Right. Right. Trial by fire and blowing up objects. Yeah. Exactly.

**Chris Gammell:** Trial by smoke. There we go.

**Art Kay:** But we, we try to make it easier. You know, we, um, you know, with this precision labs, uh, training system and, and so forth, we, uh, you know, I actually put, uh, interns and, um, people, uh, interns that come into TI or new college grads, um, put them through a training course and, uh, at the end they take an exam. So, um, and so it's, it's kind of fun. It's a, you know, I tell them, yeah, it's a pretty comprehensive exam. It takes, uh, four to five hours and, uh, you know, so do they, they write, write, write

**Chris Gammell:** back at the end and they're like, thank you. Or they like, see you later.

**Art Kay:** You know, it, sometimes it depends on the group. Frequently they get really excited about it and they're very competitive and, um, they form study groups and, um, and they work on the weekend, you know, they're like really into it. And then other groups are kind of, um, sort of say, well, I've, uh, I've already done this in school. Why am I doing this again? I thought I was done with the test. Right, right, right. So, um, yeah, it depends on the group, but I say more often than not, we get very good response from, from the interns and they're, they're pretty excited and they like to, you know, I always let their score be confidential, but it never is because they always start comparing scores to each other and so forth.

**Chris Gammell:** How do you see the, uh, how do you see the engineers changing as like from what they're coming in as, I mean, I'm always interested in, you know, are the interns prepared for what you're putting them through or is it, you know, they just kind of pick it up, pick it up as they go. What are you seeing?

**Art Kay:** Well, um, I think they, they pick it up as they go. Uh, um, I do a lot of college interviewing as well. And, um, I think that there's so much that the university has, uh, increased the amount of different subjects. Um, whereas when I, when I was in college, it was a lot more analog and I guess there was, you know, there's still digital, right. But, um, it was more focused and now there's, um, you know, quite a bit more.

**Dave Jones:** I mean, I really talked about that on the show a lot. Is this a good or a bad thing or is it just a thing? Right. Yeah.

**Chris Gammell:** That's a good point. Yeah. It's just a thing.

**Dave Jones:** It's just so much more stuff.

**Art Kay:** It's just the nature, but what it, it does have a negative consequence in that. Um, I don't think there is prepared from an analog perspective in general. Sometimes you find superstars, right. But, um, in general, I don't think they're as well prepared as, as they were, you know, 20 years ago. Um, and then again, I'm not trying to be negative. Uh, it's just more stuff, you know, is that more prepared from a practical point of

**Dave Jones:** view or from a theoretical point of view? I would say both.

**Art Kay:** Yeah. Right.

**Chris Gammell:** Um, definitely both. So just like less, less exposure to analog. So not that it's not capable. It's just that there's less time. That's kind of the, no, there's just more stuff to cover in a course. Yeah. Right. Yeah.

**Art Kay:** That makes sense. And some, you know, so you, you'll occasionally get a guy who comes in and can, you know, solder surface mount components and knows everything about everything. It's, it's just amazes me. Um, but, uh, more often than not, um, there's some learning. Yeah. Yes, probably. So. Yeah, probably. Almost certainly.

**Dave Jones:** So what, what are you looking for when you're interviewing college graduates? Do you like not give a rat's ass about their scores and stuff like that? Are you looking for that hobby interest side projects?

**Art Kay:** What are you looking for? Definitely hobby interests are really good. I mean, if they show me a project they've done, sometimes people bring a little pamphlet in or pictures of their project and that's pretty good. Um, and, uh, I'm always, you can tell the excitement in a person if, if they're really into their project or, you know, if somebody's kind of trying to fake it, you can tell that as well. Yeah. Right. Yeah.

**Dave Jones:** You can tell in a split second we've just got a nose for these things.

**Art Kay:** Yeah. And then the other thing I do is I ask, uh, fundamentals, um, fundamentals of electronics and, uh, some people get it, um, very quickly and easily. And, um, they're, they're almost, um, insulted by the simplicity of the questions.

**Dave Jones:** I was going to say, can you give us an example of how simplistic the questions are? Cause I, I ask real simplistic questions at interviews and it's like.

**Art Kay:** Yeah. I'll, uh, I have a whole slew of them. Um, I do an RC circuit with a DC voltage source, close the switch and say, draw for me the waveform versus time, uh, you know, charging the capacitor. And I give values and I, um, you know, I ask them to, um, mark the time on the axis. And you'd be surprised how many people really struggle with that. Um, they start, start breaking out the calculus and so forth. Yeah. Right. The delay tactics, right? File, file. And, um, let's see what else. Uh, I draw an op amp circuit. Um, I asked some basic math questions. Like I'll draw a graph of a offset parabola and say, what's the function for this? Um, you know, you'd be surprised. Yeah. Yep. I'm out. Yep.

**Dave Jones:** So, yeah.

**Chris Gammell:** Yeah.

**Dave Jones:** Are you, are you sometimes looking, depending on the position, sometimes looking for those theoretical geniuses who can't, who don't know which end of a soldier in iron to hold?

**Art Kay:** Yeah, sure. I mean, there are some people who are, um, very, very theoretical, but they're, they're good. I mean, they're really good. And, uh, not everybody needs to be able to, you know, solder a board together. Um, oh, I might take a little, may take a little on that there. I don't know.

**Chris Gammell:** I mean, like one board, maybe one board, right? But yeah, I, I know what you mean. Like, yeah, some, some roles do not require it, but still everybody goes through basic training camp for the army, right? Yeah. Yeah. Exactly. Yeah. Well, uh, I think a great, uh, a great way to get prepared for it would be this, uh, book. So why don't you tell us about this, uh, so this Analog Engineer's Pocket Reference Guide. I think we talked about it when it was released. It was a couple years ago, right? Oh, probably. Yeah. Yeah. So tell us about it. What's, what's the idea behind it?

**Art Kay:** So, actually, Burr Brown had a little pocket reference. Um, and, uh, my colleague, Tim Green and I, um, we got together and said, this is a neat little thing. And it's been long since not published. What if we, you know, resurrected this and created a new one? And so we just got to, uh, basically collecting equations and graphs and, um, relationships, all these kinds of things that, um, people probably have bookmarked in their computer. Yeah. Um, on a million different things or a hundred tabs in certain books and, you know, standard resistor table, for example. Um, you know, different things like that. And, uh, we put it all together in one book and, um, we're continuing to update it. Uh, in fact, later this year, I hope to do an update on it. And, uh, my, my goal is to, to kind of make a little, just a handy book that has various, uh, useful relationships. I even use it myself all the time. I mean, um, so.

**Chris Gammell:** Right. It's just like, it's like you're storing part of, it's like, all right, my brain doesn't have to remember this part. Now I just go flip up the book, the book open. Right. It's like, it's like how we use Wikipedia, you know?

**Art Kay:** And, and we, we recently, uh, put out a, a calculator version of it. It's called the analog engineers, um, calculator. And, uh, basically it has a lot of the relationships that were in the pocket reference, but, um, there's some additional things that can't be done in, um, a hard copy type, uh, type format. And, uh, you know, for example, um, what if you have a voltage divider and you want, um, a ratio of 0.372? What two standard resistors?

**Dave Jones:** I've written one of those myself. I know. Exactly. I've written my own one just to do that. It's like, yeah, it's something you can't get from a table. Yeah, exactly.

**Chris Gammell:** Or you do a lot of guessing and checking, but yeah, it'll save you. It'll save you a good 20 minutes, right? But you've got to guess in. No.

**Dave Jones:** Exactly.

**Chris Gammell:** Yeah.

**Dave Jones:** No, it just runs through all the, all the possible values in a split second and bam, it gives you the answer of, yep, you can combine these two resistors from the E24 range to give you this particular tolerance, you know? Yeah. Yeah.

**Chris Gammell:** Yeah. That's really nice too. And then if you can switch it so that it's like, oh, if I switch to E96, then it, you know, my error goes down by this minus second. It gives you other ones. Yeah.

**Art Kay:** That's great. Yeah. It tells you the error. Same thing with amplifier gain. And we have data converter tools in there, you know, figure out the noise for a data converter or noise of amplifiers. Oh, really? Different sensors like RTDs, for example, you put in the temperature and then it tells you, depending on what our type of RTD is selected, it tells you the resistance. Thermocouples, a whole slew of different stuff. And again, that is going to expand with time too. So I'm always looking for good feedback from people.

**Chris Gammell:** Cool. Cool. Yeah, that's great. And we'll hopefully send you, send a bunch your way. You know, I think there's a lot of analog fans out there in the listening audience right now, or maybe even just people that are looking for a little bit of help on that kind of stuff too. It's like, you know, having, having these kinds of guides, it feels like, you know, like Dave and I are very big fans of art of electronics and, you know, that's on my desk all the time. But at the same time, it's like, yeah, you know, I know where stuff is roughly in the book, but there's just a lot of stuff there. So having it boiled down like this is nice as well. Is this, is this something you actually carry around with you? Is it truly a pocket reference for you?

**Art Kay:** People have complained about that. Oh, really? Actually, they said pockets must have gotten much larger in the past 20 years. Okay. Because it's small, but it's not.

**Dave Jones:** Well, it is kind of A5 size or something. You could like print it out on A5, but yeah, get a little, you know, and it's got to be in the ring by that, you know, the ring type thing. Flip all the way open. Yeah, the flip, so you can flip it all the way open.

**Art Kay:** Yeah, actually, you can go on TI.com and you can actually buy a physical book. So if people want that, you don't have to get it in PDF version. And it's, I don't know, it's something like $10. It's not, you know, super expensive or anything. Right.

**Chris Gammell:** Yeah, and if you have an FAE that your buddy's with, sometimes they give you one.

**Art Kay:** Yeah, I mean, when we go visit customers, it's a nice giveaway. Yeah. That's great.

**Dave Jones:** Do you remember the point when PDFs took off and it's like, oh my God, my entire data book collection of 500 data books is now obsolete?

**Art Kay:** Yeah. There's a few people around that still can't give up the books and they have these old yellow books. Yep, yep.

**Dave Jones:** I had four bookshelves completely full of just data books, like at home. This is my own collection at home because it was the only way that you could get data on stuff before the internet and before PDFs were online. But it was obsolete within, what, two, three years, I think, when, you know, the companies just sort of like switched over and digitized everything.

**Art Kay:** Yeah, definitely. Definitely. It's nice having the, you know, the digital version because you could search through it and so forth.

**Chris Gammell:** Yeah, and I'm sure that, well, like you mentioned before, too, you mentioned, you know, it takes a little bit, it took a little bit longer to kind of find the knowledge that you were looking for when you were getting started, right? Yes. I'm sure that some of that is also, you had to dig through all those books versus being able to search through and go straight to what you wanted.

**Art Kay:** Yeah. Yeah, the internet didn't exist. Right. No, it just changed everything.

**Chris Gammell:** Yep, yep.

**Dave Jones:** So were you guys, do you remember the days of Maxim, for example, who were just churning out like 500 new chips a year? How many chips were you guys doing at the time?

**Art Kay:** Hmm.

**Dave Jones:** You know, I don't know. Because that was like mid-90s, I think, where it was that peak time of like, they were releasing a new data book that was like three inches thick every like six months of just new chips. It was crazy.

**Art Kay:** Yeah. I don't know the answer to that one, but.

**Chris Gammell:** Well, maybe a good question is, do you know how many are out today? I mean, like how much are coming out this year, like from your group? Maybe that's a good reference point, too.

**Art Kay:** Well, I could tell you that there's thousands of op-amps out there, you know, already. Just from TI? Yes, just from TI. Thousands. Oh, wow. Thousands. And then hundreds of data converters. So, you know, it's quite a list. And sometimes it can be a challenge to figure out which one you've got thousands to choose from. Of course.

**Dave Jones:** Like, are there that many different disparate customer requirements that warrant that many? Or is it kind of like, oh, we need to bring out something new and we'll just tweak this, tweak this?

**Art Kay:** Well, it's partly, you know, the marching technology moving on. The older parts don't really disappear. You know, we keep supporting those. And thank goodness for that, by the way. Let's just say that up front. And, you know, some of those even are the best sellers, some of the oldie but goodies. But, you know, with modern devices, you can get smaller and smaller packages, lower power, better performance. And then if you look at any amplifier, there's so many different parameters. And you can't optimize all the parameters. So, if you think of the different permutations, it does end up creating a need for a lot of parts. I mean, you know, it happens all the time that a customer will ask us for a particular amplifier or data converter. And we say, well, we've got this one. It's pretty close. But it doesn't meet quite on this spec. And they're not satisfied, you know. And so, we think about developing something new. And so, in general, you know, the new amplifiers and data converters aren't really being – they're not being developed just to create a new product. But they're filling a need. Right.

**Chris Gammell:** It always felt like there was certain groups that as well, right? So, like, I would hear – so, I would, you know, I'd be talking to an FAE. And they'd be telling me about these new parts. I'm like, oh, that sounds great. And then they'd be like, well, this is really for the automotive people, though. And then you could kind of see that there was very certain specs on there, the temp rating and the price usually for low quantity. I was like, oh, God. Okay. But, yeah, I mean, it does feel like it's, you know, it's kind of just trying to fill all the holes in the marketplace, especially as new things come up, right? I'm sure that bio stuff and IoT stuff and all that crap is starting to change things, too.

**Art Kay:** Yeah. Lower powers, lower package size.

**Chris Gammell:** Right, right.

**Art Kay:** That's probably the biggest new trend, I would guess. What about levels of integration?

**Chris Gammell:** I mean, how does that interface – sorry, how does that affect you? Because, I mean, you said that op amps and data converters are different groups. But so many times I've seen these AFE chips, the analog front-end chips, and it's the same thing now. So, how does that work?

**Art Kay:** Yeah. Well, they definitely – I mean, we have groups within TI that will, you know, integrate, you know, pretty complicated solutions. And those are popular. But there's always some limit, you know. They fit a certain set of categories and not everything. So, the discrete kind of amplifiers and data converters, they're not going away anytime soon. I mean, there's just – you have so much flexibility. Maybe at some time in the distant future. I mean, I remember 10 or so, maybe 20 years ago, I don't know. They were talking about building, like, programmable arrays of analog electronics. Analog arrays. And that never happened. Yeah, no.

**Dave Jones:** It just wasn't.

**Art Kay:** Why? Because it just couldn't give you the kind of accuracy and capability that you wanted. And maybe the day will come for something like that. But right now, usually when you see this very high-level integration, it's for a very specific problem. And it works well in that circumstance. And usually, it's hard for a discrete solution to compete with that, you know, integrated solution.

**Chris Gammell:** Yep, yep.

**Art Kay:** But then everything else is discrete.

**Chris Gammell:** Yeah. Yeah, that's true. And it does seem – well, I mean, so I used to work at Keithley, and it was like, yeah, any kind of integrated solution, we always said, no, no thanks. You know, because so much of it was that's very specific, you know, need this spec, need that spec. It was very, very hard requirement kind of things. And like you said, I mean, like the LMP lines that are meant for, like, sensors, which are great for someone like me now just, you know, doing a quick off-the-shelf kind of thing, that's great. But it wasn't good for doing a, you know, a high-end piece of test equipment. Right. Yeah. So, well, speaking of some high-end stuff, what about – how are you teaching people about the, you know, the really, really advanced stuff? I mean, tell us about Precision Labs.

**Art Kay:** So, this is, yeah, definitely my favorite topic. We put a lot of time and effort into putting together video series. But it's not just a collection of unrelated videos. It's really meant to be like a classroom. And the courses are sequenced in order of, you know, increasing complexity and there's an interdependency. So, the first – the second course requires the first one and the third requires the first two. And it's just like a college program. In fact, at the end of each video, which normally ranges from 10 to 15 minutes, there's a quiz, which can be multiple choice, but it's frequently much more complicated, like written out problems, including simulation. So, a person can go through a video, learn about how to drive a SAR data converter, for example. And then afterwards, they can go through some exercises that – where the problem is given to them, design a front end that does such and so. They do it and then they can look at the solution and see, you know, how close they were. Or maybe it's some more general things, multiple choice, and they can test their knowledge on that. That's great. So, yeah, love it. And there's even – so, we have two different branches right now. And we're planning on expanding it beyond that, but we have Op-AmP Precision Labs and SAR Precision Labs, or actually A-to-D Converter Precision Labs. And the Op-AmP Precision Labs has an evaluation module that is a PC board with a bunch of different Op-AmP circuits, inverting, non-inverting, cascaded, and so forth. And you can plug in different amplifiers. There's dip adapter cards that you plug into the different Op-AmP circuits, and you can do experiments. So, that's why it's called Precision Labs because it has a hand-on component. And so, for example, you can measure offset voltage, noise, slew rate, you know, what else? Yeah, that's the only ones I can think of off the top of my head.

**Chris Gammell:** Power and temperature, noise, low distortion. Exactly. I'm looking at it, so don't worry about it. Yeah, it's not like I'm just coming up with it. Yeah. No, that's good, too. And I really like ESD. That's a great one, too, where you're actually measuring. So, what is it, like testing the input ESD diodes, those kind of things? Or is that what?

**Art Kay:** Yeah, so ESD and electro overstress, those don't have a lab component to it. Okay, because you blow it up. Yeah, exactly. It would be a very short lab. You blow it up and you're done. Right. But, you know, when we characterize devices for release, like my old job, the test engineering job, we would plug a device into an ESD simulator and it, you know, applies a pulse to the device and to eat different pin configurations. And you test it before and after and you look for degradation in the performance of the device. Oh, cool. So, yeah, that's the kind of thing that we talk about in Precision Labs. So, how do we do our ESD testing? What are the different levels? And how do we protect from electrical overstress? What kind of external devices, like transient voltage suppressors or input resistors or what have you, can we use to protect circuits and make them more robust?

**Dave Jones:** I'm looking at your YouTube channel now and you've got over 3,000 videos. It's just incredible. You've got like 130 videos just on data converters.

**Art Kay:** Yeah.

**Dave Jones:** I mean, you know, like, and most of them are like, you know, tutorial lessons and stuff like that. It's absolutely amazing. So, do you have like a big media group that actually, well, a technical media group that actually produces all these or do engineers, like the applications engineers just go off and sort of produce their own thing every once in a while or?

**Art Kay:** Well, it's a little bit of both. In the case of Precision Labs, we internally produce them all. And so, those are the ones that I work directly on. And, but there is a media group at TI and they'll put together sometimes marketing videos. So, some of those will be marketing related and some of them will be technical. And sometimes it's engineers within the group that create them. And sometimes it's other groups that are more focused on training that put together that kind of material.

**Dave Jones:** It's absolutely fantastic. Just the amount of material out there is phenomenal.

**Chris Gammell:** I have to ask though, is, am I remembering right? Was it TI who did the Mayim Balalnik or whatever her name was? Is that the one, Dave? Do you remember that? I think we did make fun of that on the show at one point. Was that TI? No, that was Genesis. You sure? Okay. Well, whatever. Yeah, I remember. Yeah, pretty sure it was Genesis. That's where the marketing people get in mind. They're like, oh guys, no. Let ARC make the videos, please.

**Dave Jones:** I think it was anyway. I don't know. Yeah, but yeah, for those who don't know, she's from the Big Bang Theory show. Oh, right. Right. Yeah. And then they, yeah, hired her to do something. I don't know. I thought.

**Art Kay:** No, we don't have that kind of budget. Right. Okay.

**Chris Gammell:** Yeah. Oh man, that's funny. Yeah. Yeah. Yeah. So, I also wanted to ask about, so I saw in the second lesson of this thing, of the Op-Ant Precision Lab, I'm kind of lost now. It talks about the virtual bench. So, is that integral to the, so the National Instruments virtual bench? Yeah. Is that using the actual big box for the test? Or how does that work?

**Art Kay:** Yeah, it is. So, we've got the hands-on experiments and with this big PC board that lets you plug in the different devices. And you could connect it to really any lab equipment. It doesn't have to be the virtual bench, you know, but the virtual bench is really convenient because it provides some signal generator, two scope channels, power supplies, just about everything you would need. DMM, you know, actually fairly good precision DMM. And it's fairly small and compact. And it worked out really well for seminars. We actually took the Precision Lab, Op-Ant Precision Labs, all over the world. So, we toured. Oh, yeah? Oh, cool. It was kind of, we had a, it was a little bit like being a rock star. We had a bus and it was.

**Chris Gammell:** And check companies love those buses too. I don't, yeah. Adwell had one. Who else? Freescale had one at one point. Man. Oh, wow.

**Art Kay:** We go from customer to customer and set up an all day seminar and it was pretty good.

**Chris Gammell:** Yeah, no, those are great too. I mean, like those, that's like, I mean, that's effectively like the electrical engineering version of continuing education for me. I mean, I know that there actually is that stuff for, especially people like who have PEs and stuff. But that's the really valuable stuff to me. It was the vendor-based stuff. It's like, yeah, I might get a little bit of a sales pitch here and there. But really it was the applications engineers just showing me how to do cool things. And I'd happily, you know, hear about new parts because of that, you know?

**Art Kay:** Yeah. And in a way, I'm glad you just mentioned the, you know, the kind of product pitch type thing. One thing I was pretty happy about with Precision Labs is we're able to keep that out sort of for the most part. I mean, we basically, it's strictly a teaching kind of program. Yeah. And the way we sort of promote products in a secondary kind of way is all the products that we're using in the examples are TI products. Of course, yeah. So, you know, there's a little bit of a, you know, promotional aspect to it and you get to see the good parameters and so forth. But we're not, you know, like pitching products saying, oh, make sure you buy this one after you're, you know, done with this. Right.

**Chris Gammell:** This sandwich brought to you by the OPA, whatever.

**Speaker ?:** Yeah.

**Chris Gammell:** Exactly.

**Art Kay:** So, it worked out really good and I'm glad that, you know, my management let me do it that way.

**Chris Gammell:** Yeah. No, that's, I mean, honestly, that's the best way to sell to engineers in my opinion. I mean, I think, yeah, you just give good technical overview stuff and I'm going to go and search your site for other stuff later. Right. I mean, that's, that's content marketing at its best.

**Speaker ?:** So.

**Dave Jones:** Yeah. Who gets to decide what banner specs go on a data sheet? Good question, Dave. And which ones are buried down in the. Oh, the marketing. The marketing specs. The asterixers. Marketing.

**Art Kay:** That's the product definer. The guy that, they actually go from customer to customer and visit with the customers and try and understand their applications and which specs are most important. And, and they, they put the data sheet together and decide, you know, what it's going to look like. And then, you know, the apps engineers get to review the data sheet and we might say, oh, change this or add that. And, and frequently we, you know, we try and be consistent with the industry. So, you know, we, we just, we work towards making a clear data sheet that, that people can, you know, compare well.

**Chris Gammell:** Yeah. Right. And honestly, that at the end of the day, that's what we want. We want apples to apples comparisons. That's always the hard part, especially when there's like specsmanship kind of intermingled. But yeah, it's, it's appreciated when it actually is upfront, you know.

**Dave Jones:** Have you ever like measured a device like, and got the characteristic curve and went, wow, that looks crap. I'm weird. Not putting that in the data sheet. It's just like, we'll just, you know, put like a rough parameter for that. We won't include the curve.

**Art Kay:** Uh, well, I haven't personally. Right. Yeah.

**Chris Gammell:** It's kind of like asking you to be like, you ever, can you identify yourself here? I know. I know. It's completely, yeah. I was well aware. Art, have you ever, or will you ever be a member of the, uh, the product spec marketing team?

**Art Kay:** Maybe it's better for me to be apps. Yeah. Right. Right. Right.

**Dave Jones:** That's funny. Yep. Cause sometimes there's just a characteristic curve that I bloody want and it's not in there, you know, and it'll not go. Oh, why didn't they include that? Their competitors got that one. Why don't they include it? You know, sometimes it's just an oversight.

**Art Kay:** Right.

**Dave Jones:** Or they said someone couldn't be bothered. No one was tasked with doing it. Yeah. I guess. Right. Yep. Or he didn't, wasn't deemed important by the.

**Art Kay:** Right. You know, That marketing guru you mentioned. If you look at, if you look at, uh, data sheets, modern data sheets compared to some of the older ones, um, the number of data curves is exponentially increased. So in a way they're, they're going in the right direction. Although there's a balance, right? Because too much information can be not so good as well. You know, it just is overwhelming at times, I suppose. Um, but, uh, I think we're moving in the right direction. We're, we're trying.

**Dave Jones:** Yep. It's, it's easier because like a test systems are more, uh, automated now and they can just spit these things out like nothing.

**Art Kay:** True. And, and then also, you know, I mean, we, these, the types of curves or the types of specs more or less have been invented. At some point somebody had to decide, oh, let's create a curve that looks like this, you know, this, right. Yeah. Yeah. Yeah. Yeah. And maybe a customer problem, you know, became the, the mother of that curve. Right. I mean, it's like, oh, well, we need a curve that helps us understand this customer's problem a little better. And then, then you say to yourself, well, that really ought to go on the data sheet. And so I think that's how the data sheets have grown over time.

**Chris Gammell:** Oh, they've just collected more and more. It's like, uh, it's like, it's like baggage, right? It's technical baggage. Yeah. Yeah. Yeah. That's nice though.

**Dave Jones:** What has ever happened to joke data sheets and having little Easter eggs on data sheets? Is that like against company policy? Can you like do a little like doodle on the last page or something?

**Art Kay:** I don't think that would go on a data sheet anymore. Um, those days are gone, but, um, I did, uh, do, I don't know. Too serious, I guess. Um, no, no, no, no. We did have a blog series or we still have a blog series and occasionally we'll have a joke blog. Blog, like I did one, um, for an April fool's blog, uh, some years ago where, um, I said, uh, something like building an emergency transmitter, you know, um, if you're shipwrecked on an island and it was a whole, you know, Gilligan's Island spoof kind of thing. And, uh, it was kind of, it was fun. It was, it was enjoyable putting it together and people got a kick out of it. And in fact, you know, we had all these technical blogs and that particular one was rated, um, you know, like way, way higher than all the technical ones. And so. Heard some feelings, huh? Well, actually the marketing people all decided, well, we have to do all, you know, spoof blogs now. That is not the right answer, right?

**Dave Jones:** It's getting all the social media engagement.

**Chris Gammell:** Oh, man. So.

**Dave Jones:** It's meeting all those KPIs we need.

**Chris Gammell:** Yeah, that's not good. Yeah. Oh, man. Well, so, okay. So you're, so you're, you're, you're in charge of SAR products now. I mean, where, where does, where are you seeing that going? I mean, what is, obviously I'm sure ADCs are getting faster and faster and less noisy, but what, what other trends are you seeing?

**Art Kay:** Well, I would say that the biggest trend for SAR is, um, that the resolution is getting higher and higher, which I wouldn't have really expected it, you know, earlier in my career. Um, you know, you think of a Delta Sigma converter as a 24 bit converter. Yeah. That's what I normally think of, you know, integrate for three days and you're, you got a great reading. Yeah. But, but now SAR converters are 20, you know, 20 bits, um, 18, 20 bits. It's, it's common for that. Um, and then, um, normally, um, you know, year, a few years back, SAR converters were usually a more, um, basic SAR where, um, it was a switch capacitor input, um, a reference input and, uh, you know, digital output. But now you're seeing more and more levels of integration within the SAR converter, similar to what you've seen in PGA, uh, um, Delta Sigma converters, that is for a number of years. And Delta Sigma converters are normally more, um, integrated, you know, you'll have a programmable gain amplifier and internal reference, um, you know, maybe some current sources for exciting, uh, thermocouple or, I mean, um, um, RTD or something like that, um, bridge excitation. Um, and now you're starting to see that in SARs where you see, um, internal references, internal reference buffers, um, PGAs. Um, and so that's another trend. And then I think the, the last trend is, um, that the size and power of the, um, SAR is getting lower and lower. And so we have one, um, you know, type of SAR, we call them nano-SARs and, and they're, um, you know, it's so small that if you had a pile of them on a piece of paper and you breathe, you'd probably inhale a bunch of them. They'd be in your lungs and so forth. Right. Um, so, you know, they're very, very low power and, and super tiny.

**Dave Jones:** Give us the, for those playing along at home, give us the key differences between a, uh, delta sigma and a SAR, which is successive, uh, approximation. Sure. Converter.

**Art Kay:** So, um, a, uh, a SAR takes a snapshot, um, of, uh, a voltage or a signal. Um, basically it does that by having a switch on the front end. Um, and, uh, this, the switch opens, um, and whatever signals that connected to, um, the, the SAR input, um, gets, uh, stored on a sample and hold capacitor. And, um, there's some resistance associated with that sample and hold capacitor. So you have to make sure that switch is closed long enough for that internal sample and hold capacitor to charge up. And that's one of the big challenges with the SAR is just, um, making sure that you can drive that input or allow that input to settle, you know, in time. But once it's settled, that switch opens and then the conversion occurs. And, um, you can kind of think of the conversion like, uh, a way scale. Um, you, uh, you have your voltage applied to the input of a comparator, um, that's stored on the sample and hold capacitor. And then you have a DAC, um, and the other input of the capacitor and it's, um, surveying through different voltages, trying to, um, match the voltage, um, on the sample and hold capacitor. And once it matches as close as it can, um, all those different, um, comparisons are, are stored in a register and that's the conversion result.

**Chris Gammell:** Yeah.

**Art Kay:** So, um, the, I guess the important thing to take away from it isn't so much how it's converting, but that, um, it will take a snapshot. So as soon as that, um, as soon as that switch on the front end opens, um, whatever voltage we were at is the voltage that the conversion will be equivalent to. Whereas, um, a Delta Sigma converter, it's taking, um, you know, thousands or of, uh, samples on a single bit type, um, converter. And, um, it's, uh, it's, it's using kind of a control system to, um, to average those samples. So over a long, um, you know, period of time, it might be, uh, um, one sixtieth of a second, um, we'll, uh, we'll be averaging, um, the voltage and then we'll get, um, a very, very accurate, very, um, low noise, um, result. But, um, at least for, uh, one kind of Delta Sigma converter, it's normally a much slower, um, you know, very slow. Yeah. And, uh, it's frequently in, um, you know, like one sixtieth of a second. So it could integrate out the power line cycle, um, or one fiftieth of a second, depending on, you know, Europe or U S. Yay. Australia. Yeah. 50 Hertz all the way. So, so that's one type of Delta Sigma. There's a more wide band Delta Sigma type converter, which again, averages, but, um, you can get a faster throughput and that might be used for, um, seismic measurements or, um, ECG or, or something like that.

**Dave Jones:** That's the field I come from.

**Art Kay:** Yep. Yeah. And, um, they have a different kind of digital filter in that than the, the slower ones.

**Dave Jones:** So the DAC in your SARS, how do you normally do the DACs in those?

**Art Kay:** It's a switched capacitor DAC. Um, so it's, uh, you know, CDAC capacitively. Yeah.

**Chris Gammell:** So what is, what is driving these higher, higher bit rates then? Is it just that the, the DACs are, uh, I guess the clock's getting faster, but that's not necessarily it. Is it just that it's, uh, it's just doing more registers. It's able to switch faster. What's going, what's driving that?

**Art Kay:** Well, you, you are, um, you do have to clock it faster. Um, internally, normally the conversion is internally clocked on these precision SARS. And, um, once it's, uh, conversion is complete, um, you're going to, uh, have to read the, um, you know, the data back out of it. And, um, it's actually a challenge, right? Because you have 20, normally most SAR converters will have a serial interface and if it's 20 bits and if we're going at, let's say four mega samples per second, you know, you can imagine that we've got a clock pretty fast. Right. And so we've actually, um, developed kind of a new, uh, SPI, um, we call it multi-SPI and, um, it, it, uh, it does a whole wide range of different, um, capabilities. This is an extended version of, uh, SPI interface, but one, um, one feature that it has that allows it to, um, you know, sort of reduce that, uh, throughput rate or the digital communication rate is that, um, you can have multiple data lines. So it's kind of a hybrid of, um, serial and parallel.

**Chris Gammell:** Yeah.

**Art Kay:** Nice. And so you can have, um, one, you can have a standard SPI, um, so one data line, or you can have, um, two or four and, um, you can even collect data on the rising edge of the clock and the falling edge of the clock. And so by doing that, you can, um, slow down your clock speed and, uh, it's a little easier to communicate.

**Dave Jones:** How do you internally run these, uh, sample clocks? Is it a free running oscillator? How do you do that? Cause it's not clocked externally, right?

**Art Kay:** Right. It's well, it depends on the, the converter, the, um, the older style and maybe the, um, the lower resolution converters, they will be clocked externally or often are. Um, but internally, um, there's going to be an oscillator, you know, um, for the precision SAR, there's going to be some internal oscillator.

**Dave Jones:** Um, and that's just an RC, an internal RC thing, or is it process controlled frequency or how does that, well, I assume there'd be a large tolerance on that temperature dependent.

**Art Kay:** It's gotta be, um, you know, I, I'm not the designer and I, I don't know exactly how they do it, but jitter and drift and all these kinds of things can, um, can impact performance. So, um, whatever they're doing, they're, they're doing it well because they're doing it well. Right. So that's a good question for me to ask those guys.

**Dave Jones:** Yeah. Yeah. Yeah. Yeah. Because like, it's not like they have an internal crystal element. I mean, you know, you've got to do it in silicon somehow. Yeah. I don't know. Honestly. So yeah.

**Chris Gammell:** So what about the, um, is there, is there any requirement for using like SIRTAs these days, like the really high, higher speed transceivers? Is there requirements on the digital side to do that or, or can it just be standard spy ports, but like daisy chaining them, like, or not even as multi-ganging them. I suppose, not daisy chaining.

**Art Kay:** You can, there are some, you know, daisy chained, uh, you know, capabilities and, um, yeah. So.

**Chris Gammell:** But is there, is there a requirement to use like certain, like the high speed transceivers that are, are getting put on a lot of FPGAs and stuff like that? Or is it, is it.

**Dave Jones:** I don't think they're getting that high.

**Chris Gammell:** Right.

**Dave Jones:** They're not that high.

**Chris Gammell:** I mean, yeah, those are like gigasamples sometimes, but starting to push that. I mean, it's hundreds of mega samples, right? So.

**Art Kay:** Well, we're not going into the mega, you know, hundreds of mega samples. Um, the, the SAR converters that, you know, that at least are from my precision group are, um, usually about five mega samples, um, is the, the max. So there's another high speed group. Um, and, uh, you know, I would like to learn more about that, but right now I'm focusing more on the precision. Yeah.

**Chris Gammell:** I guess, I guess the precision starts to fall off as you go faster and faster too. Yeah. Yeah. Yes. Oh yeah. I guess my math was wrong, huh? I have five mega samples. What am I, my math is way wrong then. Okay. Yeah. You're off. Yeah. Okay. Yeah. You know, do it in my head. It's fine. Yeah. I need some kind of, uh, pocket guide or a, uh, you know, analog calculator or I need, uh, Maya Bialik to tell me about zombies. Cause I did look it up and it was her and it was for Texas Instruments.

**Dave Jones:** So guilty as charged.

**Chris Gammell:** I will, I will, I will put that in the show notes because we will have to watch that. It was a little cringy, but you know, it was well-meaning. It was well-meaning. I will say that. And our stance is that it's better to have art doing videos. That's, that's what, so what else, what else should we know here? I mean, uh, you know, we're kind of, we're kind of wrapping up. I mean, what else, what else do you want people to know about, about your group or about the learning opportunities or anything like that?

**Art Kay:** Well, I guess, um, you know, a few things I could mention. Um, one of my, uh, areas of expertise that I spent a lot of time on is noise analysis. And so, um, I wrote a book operational amplifier noise. And, uh, so I've spent quite a bit of time, you know, people, people come to me for noise type questions. And so that's just a good resource on precision labs, op amp precision labs. There's kind of a summarized version of, um, you know, what the book is about. I'm in video form. Um, but, uh, yeah, that was something I spent a lot of time on. Um, my colleague, uh, Tim Green, um, we worked together on a lot of different projects. He, uh, he's working on similar material for op amp stability, which is another kind of challenging. Yeah.

**Chris Gammell:** You know, problem. Yes, it is.

**Art Kay:** Um, so he has an article series and eventually we'll get a book out on that subject. Um, and, uh, hmm.

**Chris Gammell:** So you both, you both write for the, like the E2E blogs and stuff like that too?

**Art Kay:** We have, um, we, I've, I've tend to past, let's say three or four years. I've spent more time just putting together precision labs than, um, putting blogs out. And prior to that, I wrote a lot of articles. Um, there was a, uh, article, um, place called EN genius. Um, and they, they shut it down, but it was a really good website and we could write extremely long, um, detailed articles, which was really nice, um, to have that flexibility. And a set of articles from that, um, magazine, um, became my book. So that's how it worked out.

**Chris Gammell:** Okay. That's great. There's like long, long form engineering stuff. Yeah. That is kind of a, doesn't fit super great with the, uh, with the engine, with the internet these days, but man, when you find that article, it really does it.

**Dave Jones:** It's a five minute attention span. Yeah. Yeah. Yeah. Yeah. We need more Mayim Balik. Yeah.

**Chris Gammell:** Uh, well, where can people find you online? I mean, uh, are you, uh, you're not a Twitter or anything like that?

**Art Kay:** Well, I'm on, I'm on LinkedIn. So, you know, you could search me up on LinkedIn and, um, I guess, uh, you know, there's also an E2E network, which is, um, TI's, uh, way for answering questions. So if a person posts a question, we'll go up there and I, I answer sometimes, um, on the E2E forum or you could befriend me. It's kind of similar to, I guess, Facebook or something like that, where you can have friends. And so you could send me messages that way. Um, and, uh, so occasionally somebody will ask me some noise question or, um, I'll work on the, um, you know, SAR converter type, uh, things. Awesome.

**Dave Jones:** Are you guys hiring at the moment?

**Art Kay:** Yeah, we're always hiring. Um, and, uh, especially, uh, I would say new college grads. Um, there's, uh, um, you know, huge amount of, uh, college recruits. And so, um, and a very good program too. There's a, most, um, engineers will go through a rotational program at TI and it's, uh, it depends on the different area that you're in, but for applications, it's a one year rotational program and you'll go to two different groups and, um, you'll, uh, um, you know, uh, you'll have training in between at the beginning, in between at the end. Um, and, uh, there's a network of young people that work with each other to, you know, uh, you know, go on hikes and stuff like that and to, um, help each other out. And so it's a very good environment for, uh, I would say new college grads. Um, uh, much better, as I mentioned earlier, um, it's a much better way to, to go than what I, you know, um, sink or swim when I was an engineer. Yeah. Um, a lot of, a lot of help and support for these guys.

**Chris Gammell:** Right. And we should mention too, thanks to, to Victor who, uh, introduced you and I through, uh, Victor was one of those, he was, he went through the rotational stuff and he actually introduced you and I. So that was great. Thanks Tim.

**Dave Jones:** There you go. Yeah. It's not as exciting as a dodgy startup though, is it? Yeah, there's definitely. You know, you work with a nice stable company like TI doing cool analog stuff. How do you compete for these graduates these days who are just all schooled to go do startups? Is that a, is it, have you seen like a, a, the interest drop in recent times for, for like, you know, I, I, I don't like to use the word boring, but boring in quote Mark's stable jobs. Cause a lot of, a lot of focus on university courses seems to be entrepreneurial these days.

**Art Kay:** I would say, um, no, I haven't, I've seen it. If anything kind of increase, I mean, we're hiring massive amounts of people, but, um, I would say that, uh, most, many, many, if not most college students focus on digital. Um, and, uh, so very often they'll, um, you know, they'll come to me during the on-campus, uh, interview type, um, uh, career fair. And, um, and, um, I'll say, Oh, you know, what do you like analog or digital? And they'll have all digital on their resume and they'll be, Oh, I love analog. You know, so, um, they're both great. Wait, wait, wait, what is, what does your card say, Art? Uh, Oh, I love analog. So there's more emphasis on digital for sure. And so, um, it's more difficult to find really good analog, especially people who have a passion for analog, you know, um, you'll, you'll have people, um, you know, it's almost easier to find undergraduate students, uh, than graduate because you, you know, you definitely get, um, you know, your first couple labs are doing amplifiers and transistors and you get plenty of analog and then frequently people will go into grad school and, uh, they, they, uh, you know, do, um, a lot of VHDL and Verilog and IEA. How could that? So yeah, I would say that's more of the problem than a lack of interest.

**Chris Gammell:** Hmm.

**Dave Jones:** Okay. Cool.

**Chris Gammell:** Interesting. Well, I'm sure, uh, I'm sure there's some people in our listening audience who are, young, enthusiastic analog, uh, future gurus. So hopefully they will, they'll jump, they'll jump over your way.

**Art Kay:** Send them our way. No shortage of jobs in Tucson, Arizona. Yes.

**Chris Gammell:** Awesome. Well, Art, thanks so much. I mean, uh, definitely some great resources you shared here and, uh, I'm looking forward to checking these out more.

**Art Kay:** It's been a pleasure. Thanks. Thanks, mate. Catch you next time.

**Speaker ?:** Bye. Thank you.
