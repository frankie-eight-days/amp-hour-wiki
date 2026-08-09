---
episode: 149
title: An Interview with Laen - Purple PCB Philosophy
url: https://theamphour.com/the-amp-hour-149-purple-pcb-philosophy/
---

**Lane:** This episode of the Amp Hour is brought to you by ContextualElectronics.com. Are you an advanced Arduino user? Perhaps you're a hardware engineer who's still a student or just getting started. Maybe you're a software person who's being asked to design the products you normally just program. Contextual Electronics is a hands-on course taught remotely. You'll learn all about how to design your own PCBs from scratch using KiCad and get timely instruction about the nuances of working with electronics. You'll learn theory alongside practical and be able to apply those lessons alongside your peers. For more info, go to ContextualElectronics.com. This is the Amp Hour Podcast. Recorded June 10th, 2013. Episode 149. With guest, Lane of Oshpark.com. Purple PCB Philosophy.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog. And I'm Chris Gammell of Chris Gammell's Analog Life.

**Lane:** And I'm Lane from Oshpark.

**Dave Jones:** Hey, Lane.

**Lane:** Welcome, Lane.

**Dave Jones:** Hey, thank you. That's not even your real name. Shall we continue to use the pseudonym? Yeah.

**Lane:** Yeah. I mean, my real name is James Neal. Oh, did they?

**Dave Jones:** You just ruined it.

**Lane:** But there are a lot of James Neals in the world. So I've got to differentiate myself somehow.

**Dave Jones:** There's a lot of James. There's a lot of David Joneses. That's why I had to put David L. Jones in all my – everything I've ever published. I had David L. Jones just to differentiate myself.

**Lane:** You should try your last name backwards. No.

**Dave Jones:** Okay. Sinaj.

**Lane:** Sinaj. Sinaj. It's right. Everything's Pig Latin. Yay. Yeah. You youngsters wouldn't know what Pig Latin is. Oh, I know what Pig Latin is. Uh-uh. There you go.

**Lane:** All right.

**Lane:** This actually – so this happened at Maker Faire – was it last year, right? And I started hanging out with Lane, right? And I'm calling him James. He's like, you know, people usually just call me Lane. Yeah. And I'm like, oh, okay. And then he gave me the whole story. Because didn't you say there's like some random negative person on the internet?

**Lane:** Yeah. There's another James Neal who lives in Portland, who is a year younger than I am, who is in the same line of work as I was. And also, I actually held one of the same jobs that I did after I left it. So we have a matching line on our resumes. And he's a little bit of a curmudgeon. So I didn't really want to associate myself.

**Lane:** What if indeed this is like a fight club type thing and you actually are him? It's just like you're only him at night or something like that.

**Speaker ?:** Right.

**Lane:** That very well could be. I was hoping it would be more like a Highlander thing. Oh, yeah? Like only one can – Yeah, there can be only one. Right.

**Dave Jones:** And he's wearing a cape right now. Boy. Well, thanks for joining us. You're from – you're another Yank. I'm outnumbered again.

**Lane:** Oh, yeah. I'm from Portland, Oregon.

**Dave Jones:** Portland, Oregon. It's like halfway there.

**Lane:** In the U.S.

**Lane:** It's basically like – Yeah, it's – It's basically Australia. Right. The Oregon outback. Exactly. Exactly. It's a little greener, a little bit more good coffee.

**Lane:** We have eucalyptus trees. Oh, yeah.

**Dave Jones:** And you're still in Portland?

**Lane:** Yep, yep. I'm still in Portland. I live in a little suburb about 15 minutes south of Portland.

**Dave Jones:** No plans to move to the Big Smoke, i.e. Silicon Valley?

**Lane:** No, I have a family here and I have a daughter here. So I'd like to kind of keep her in this school district for as long as we can. Of course.

**Lane:** Plus, you got – I mean, Portland's a great town. I mean, it's totally weird.

**Lane:** Portland's a great tech community. Yeah. Yeah, we have a great tech community.

**Lane:** So, like, who are you seeing as the tech community these days? Because, obviously, my former employer overlord is Tektronix, and that was a big one out there. But, like, who are some of the other big ones out there these days?

**Lane:** Oh, well, Intel, of course, is still based here. Oh, yes, I've heard of them. There's Maxim, I see, has a fab here, I think. And there are a bunch of, like, Tektronix spin-offs, like Xerox. Right, the Pfizer printers. Yeah, so that's where I worked a few years ago is at Xerox in their – what used to be tech.

**Lane:** Oh, right. Okay. Interesting. Like on the same campus and stuff too?

**Lane:** Yeah, it's the same campus. Right, same campus. They just bought that part of Tektronix and moved in.

**Lane:** Oh, right, because, yeah, yeah, yeah, yeah. Because Nike did that too. Tech is right next to Nike, I think.

**Lane:** Oh, yeah, Nike – and that was my previous employer just now is Nike. And they took over – they still call the building, like, the Tektronix Building 58. Oh, okay.

**Dave Jones:** There you go. Yeah. Because, of course, Tektronix is going down.

**Lane:** Well, they're owned by the same company as Fluke now, right? Danaher.

**Lane:** Yeah, Danaher Group. Papa Danaher, yeah. Danaher Group. Boo. My former overlord. Yeah. Yeah, Fluke and Tektronix and Keith Lee and a bunch of other – And there's quite a few others, yeah. Yeah, Seabird or something like that. Well, that's cool. And, of course, the biggest industry of all out there, the Purple PCB company known as – Oh, that's right, yes. Is that how you say it? Is it Oshpark? Is that the official name? That's how I say it is Oshpark. Oshpark, okay. Yeah. Like Oshkosh-Bagosh. Like Oshkosh-Bagosh. What?

**Dave Jones:** Sorry, you want to explain that to this uninformed Australian. Okay.

**Lane:** It's overalls. It's a brand of overalls here in the US. Yeah.

**Lane:** They used to have these iconic commercials of these little kids trying to say it. Right, okay. Because they never could, right? Got it. Right. Do they make big-person overalls too? Is that a thing? I don't know.

**Lane:** Yes, they do. Oh. I think they do. I'm pretty sure they do.

**Lane:** I'll have to get a pair.

**Lane:** Straight up farmer. Well, if the tech thing doesn't work out for you. Yeah, right. Of course. Of course. I could fall back. Yeah.

**Dave Jones:** You could fall back to Iverolls and Julie Banjas. De-da-de-da-de-da-de-da-de-da-de-da-de. Out in Cleveland.

**Lane:** That's right, yeah. Yes. The rural outback of Cleveland.

**Speaker ?:** Right.

**Lane:** So tell us about Oshpark. I mean, we have all seen the purple PCBs cropping up. They're like... Awesome. They're like the Borg, right? I mean, they're everywhere, man.

**Lane:** They do seem to be everywhere, and that's why I chose this with purple.

**Dave Jones:** Start from the beginning. Tell us how it came about.

**Lane:** Yeah, so it started out, we have an electronics group here in Portland called Dorkbot PDX. And this is just like a bunch of us hobbyists who get together in kind of a geek-themed bar downtown. And we all bring our projects, and we all hack and stuff. And we were all kind of... It got to a point where we were all doing our orders. We're designing our own boards, ordering them off, ordering them from batch PCB or directly from Fabson, and having these long shipping times from China, and kind of a high failure rate. And we're having some problems with it. So we kind of figured out that we could... That we had enough people in the group to justify our own panels from a U.S. fab. And so we started... I said, okay, well, I volunteer. And I started taking orders and putting them on panels and sending them to, at the time, advanced circuits here in the U.S. And then I'd get them, break them apart, and hand them out at the meetings.

**Lane:** That was the humble beginnings, huh? It was just...

**Lane:** That was the humble beginnings.

**Lane:** So your entire business was based on you volunteering? Is that what I'm hearing? Unfortunately, yes. Yeah, that's great. I mean, that's awesome. I mean, that's, you know... You were a nice guy. That was really nice to you. Because that's no easy task, is putting all that stuff together.

**Dave Jones:** No, no, it's not to get all those gurus together. To stick them all on a panel. Pain in the ass, actually.

**Lane:** Well, I mean, I'm kind of a software guy. So that part was kind of interesting, kind of fun. Working out ways to automate that. And it quickly became obvious that our group couldn't keep doing it on a... It wasn't enough to justify it on a continuing basis. Because I was doing a panel every month or two at the beginning. Like maybe one a month. And I was getting maybe like 30% full, even at that.

**Lane:** Oh, wow. Yeah, that's not enough.

**Lane:** Yeah, that's not enough to justify it. Because when you order from a USFAB, you're paying pretty much the same amount for a 5-square-inch board as you are a 300-square-inch board.

**Lane:** Yeah.

**Lane:** Because most of the cost is in the setup.

**Lane:** Right.

**Lane:** And so with that, with only filling up 30% of panels, it wasn't going to be something that we could sustain. And so we kind of opened it up to people outside of our local group. And they would just email me the files and I would take the attachments off their email, add them to a panel, send them back a PayPal link. And kind of go from there and then just mail them to them when I finally got the boards back. And so that allowed us to kind of kick up the frequency. And as news spread, we got it up to like once every two weeks, to once every week, to multiple times a week. And that's kind of where we are now.

**Lane:** To Lane's wife wanting to beat them into the ground. Right. Exactly.

**Dave Jones:** And it's more automated now? So it's a more automated – is it a fully automated process in terms of people uploading their files? And like do you actually have to shuffle the Gerbers anymore?

**Lane:** Nope. Well, that's automatic. The only pieces that I have to do manually now are a little pre-inspection check before I send it to the fab. Of course. And then, of course, breaking them apart when they get here.

**Dave Jones:** Right. Interesting. Manual labor? I know.

**Lane:** I know. I'd really love to automate that last piece.

**Dave Jones:** Right. So you've got to break them apart and then pack and ship them.

**Lane:** Right. And I got ideas on how I can automate that. But it's – Robots. I think it's going to be kind of a project. Yeah. The Roomba so far has been a horrible failure. Yeah, right.

**Lane:** Well, he just cleans up after the shards of FR4.

**Lane:** That's about all it's good for.

**Lane:** What about the – I mean, why did you decide to go with US fabs though? And like how did you start finding them?

**Lane:** Oh, so the US fabs were – it's mostly about the speed and the quality. Since our two big problems were that we had to wait for like a month or more to get these boards back from China or then to get some back. And we had a pretty high failure rate of about one in four.

**Dave Jones:** Really?

**Lane:** For some of them.

**Speaker ?:** How?

**Dave Jones:** Failed in what way? Annular ring breakouts or what?

**Lane:** That sort of thing, shorts, solder mask not being quite right, a wider range of things that we were getting, a pretty reasonable failure rate. And so, I mean, I've tried since to order from Chinese fabs and they either don't want to do it based on the complexity of the panels or the samples have come back and have had big problems. And like my failure rate through the US fabs is about one in 40,000 boards.

**Lane:** Holy crap.

**Lane:** And from the Asian fabs, it's getting maybe 5%.

**Lane:** Wow. Wow. That's – yeah, that's pretty crazy.

**Dave Jones:** So how are the boards done on an individual basis? Are they fully routed with tabs or do you do V-grooving? So can people like send you – because I've never used the servers – can people like send you a really weird shaped board?

**Lane:** Oh, yeah. They're all routed out with route and retain tabs. So whatever strange shapes you want to do on the outside is just fine.

**Lane:** Yeah, and you have a thing on your site as well about internal routes as well for like isolation, right? I think that was –

**Lane:** Yeah, you can do isolation routing. You can do routes inside. You can do cutouts. I've seen people do funny things like make big O-ring donut-shaped ones and then put a board in the middle, in the space in the middle. Right, really?

**Lane:** Yeah, that's quite common. What's the final use of that?

**Lane:** Well, it's wasted space otherwise, right?

**Lane:** Oh, so you're saying – oh, I see what you're saying. You're saying that they order – it's like they order a second board within that circle. That's what you mean? Yeah. Right, right. Oh, okay. So then they basically do like a board service within board service kind of thing. They actually add their own grooves for breakouts, tabs and everything. Right.

**Lane:** You don't even have to do that. I mean, the fab does that.

**Dave Jones:** Now, your automated software obviously adds the routing path. I assume it's a standard 2.4 millimeter routing bit, is it?

**Lane:** Yeah, it is. My software doesn't do that. My software just keeps the spacing in between there and the fab has an engineer.

**Dave Jones:** I was going to ask because – right. So you're not that tightly integrated with the fab that you're producing the exact format that they want with the routing toolpath already programmed in. So, yeah. When you send the board to them, they have to actually manually program their machine with the routing toolpath. As with most – you know, almost every order they have to – Right, right.

**Lane:** And my boards are hugely complex.

**Dave Jones:** Because there's possibly potential if you could automate that to sort of talk to whatever software they're using and eliminate that step automatically, then they might be able to sell you the boards even cheaper again because that's one extra step they don't have to do is programming all that. You know, a lot of people don't realize this is that when you send your panel into a PCB company and you specify a routing path, they have to manually – some poor bastard has to manually sit there and actually program that routing path into their machine. So –

**Lane:** I would hate to have that job. Yeah, I know. It would be so monotonous. I would hate to have that job. It's awful. I mean, one of my panels has like 90 different boards on it. Yeah, yeah. I know. And they – with internal cutouts and like milled paths and slots and all this and they have to – and some poor guy has to go through there and do it.

**Lane:** What is the reasoning that that's not already – I don't get it. Like, so why can't that be automated yet or is it just –

**Dave Jones:** A lot of PCB companies will use different software. They'll all have different Gerber programs to actually – and talk to their machines. They'll all have different types of CNC routing machines and, you know, all that sort of stuff. So they have to translate it into their particular machines format that's needed.

**Lane:** Well, Lane, once this whole collecting orders thing runs out, you can make the software that standardizes it. Good luck with that. Sell it to people.

**Lane:** Yeah, I got ideas on how you can do it. But, I mean, people send such wildly weird things. Like, they'll – it seems to be very common that people will like leave out one edge of their board.

**Speaker ?:** Hmm.

**Lane:** And so like there – you just have like a big U shape for the board outline. Right. And with a whole edge missing. And the fab can figure that out. The poor cam engineer can figure that out. But that would be kind of difficult to do by software.

**Lane:** Well, I mean, that's like a watertight figure then, right? I mean, that's kind of the –

**Dave Jones:** So it's humans for the win, right? Humans for the win. Just cannot be done by –

**Speaker ?:** For now.

**Dave Jones:** It cannot be done by robots or artificial intelligence.

**Lane:** It totally could be. Right. It totally could be.

**Dave Jones:** Come on. You're designing this all out of a job.

**Lane:** So what about – what about yours? I mean, so I've used your software before. I've used it a couple of times now. And I love it. And I've – everyone I've ever talked to has said the same thing too. It's just like super simple. But could you just walk us through the flow real quick about how, you know, someone go about getting it up – getting their board up onto the site?

**Lane:** Yeah, sure. So it's pretty simple. You go to oshpark.com. There's a big friendly button to get started. You upload either an Eagle board file or a zip file full of Gerbers. It does some layer identification magic behind the scenes. Spits up a couple preview images to show you what your board will end up looking like. And that's a pretty good way to figure out if your files are right. Yeah. Then – and like even when I'm designing a board, I still send it through the site to get that preview instead of just looking at it through a Gerber viewer.

**Lane:** Yeah, that stupid swap in KiCad where it mirrors the drill file for some reason.

**Lane:** I have no idea why that exists. Who came up with that? Yes, that's the number one cause for the listeners who might not have been cursed by this. When you're generating drills files in KiCad, the default setting is to mirror the y-axis of the drill file. So all your drills are way off board and floating out in space.

**Lane:** And it also makes your board look huge. It makes it look like it's like three times as big as it normally would be so you could charge more too and everything.

**Lane:** Well, no, you only build for the board outline on the site, so it doesn't care about – it'll just –

**Lane:** Oh, I thought it did build for that.

**Lane:** It'll happily trim out all those drill files and you end up with a board with no holes in it.

**Lane:** Yeah, with no holes in it, yeah.

**Lane:** Because there's no holes. There's no holes where there should be holes on the board. They're all way off board.

**Lane:** You should send a little note that says – It's the most ridiculous thing. You have a drill press at home, right?

**Lane:** You'll be fine. Yeah, exactly. Mind those traces. And a plating bath.

**Dave Jones:** Yeah, right? Is there any limit to how many holes you can have per panel? Because a lot of manufacturers will limit you to that. Otherwise, you pay a big premium for the number of drills.

**Lane:** Yeah. As far as an individual user of the service is concerned, no. Right.

**Dave Jones:** I bet on your end, I imagine there is in terms of number of holes and drill changes as well is another big thing.

**Lane:** Yeah, the fab gets cranky if I give them a panel with more than about 40 holes per square inch. Right, okay. But that's only happened once. Right. And people have done big batches of perf board, 100 drill per inch perf board. And still, that only brings up the averages a little bit.

**Lane:** Oh, okay. So it's average for the whole panel. Is that the idea?

**Lane:** Yeah, exactly. Your average across the entire panel. As long as – most boards are in the 20 or 100 drills per inch. Yeah. And then – so it doesn't matter. There's really no way that an individual can do it without actually paying enough that I can afford to upgrade the number of holes per panel.

**Dave Jones:** And how about the number of drill changes? Because I can imagine every man and his dog sending in different – you know, someone uses a 1.05 millimeter drill bit instead of a 1 millimeter just because they're not aware that, you know, their board uses 20 different drill sizes. You know, they're not aware that that's an optimization step you should do on your final board before you send it out is optimize your drill holes.

**Lane:** Yeah, and that's kind of a problem. And then one of my fabs doesn't like it. Well, it doesn't like it if you do more than 25 because most drill presses have spots for 25 different tools. Yep. But most of my fabs are – I now run – I now have four fabs behind the scenes who are making the boards. Oh, okay. Right. And the other three are just fine. If I hand them a file with 50 different tools in it, they go, all right. Fine.

**Dave Jones:** Yes, sir. Are these all still based in the U.S.? Yep, they're all based in the U.S. Excellent.

**Lane:** With those numbers he gave, why wouldn't they be, man? I mean, like, say, you know what? I'm okay with 5% this week. Yeah, exactly. 5% errors is cool.

**Dave Jones:** Well, granted, that's not indicative of Chinese labs in general, though. I mean, you can get the utmost highest quality boards from China. You just pay for it, you know.

**Lane:** Absolutely, yeah. You pay for it. And at that point, the cost advantage is eaten up because in the U.S. fabs, particularly the ones around Chicago, which were around Motorola, the quality of these fabs is top-notch. They are expensive, but actually on par with Chinese manufacturing.

**Lane:** Mm-hmm. Nice. Yeah. That's like feet-on-the-ground kind of numbers there. And, like, we always talk about that, too, just, you know, like, just the advantage of labor and everything. But, yeah, when you normalize for everything else, I'm sure it does at least get close, if not, you know, if not even exactly.

**Lane:** Because, like, say I wanted to order these from China. I could order the – I could send off my standard panels. If I wanted them back in the seven days that I currently do, that I currently get them back, then I'm paying for three-day turn times in China. Mm-hmm. I'm paying for overnight shipping.

**Lane:** Yeah.

**Lane:** Practically. Yeah, FedEx. Yeah, one- or two-day shipping. And, right, FedEx. And at that point, the shipping cost eats up most of it, and the three-day turn time eats up the rest of it.

**Lane:** Yeah.

**Lane:** So I can get them in that small – in that short window of – oh, and customs can get involved and delayed indefinitely.

**Lane:** Yeah. Oh, yeah. That's a logistic nightmare.

**Dave Jones:** Something just occurred to me. Is there a way that you could possibly franchise this system so that people in other countries – like here in Australia, we have one PCB fab left here in Australia that does – no, maybe two. Yeah, yeah. But, right, that do PCB panel prototypes, right? And, yeah, that's how barren this country is. And, like, you know, is there a way maybe that service could be franchised to other countries so that you could take advantage of that localized pricing in each country?

**Lane:** The problem is that – and I've looked at this. I've wanted to – I want to do this especially, like, just most of my customers are in the U.S. Right. The rest – the next largest chunk is in Canada. The next largest chunk is in – Germany. Is in Europe. Yeah. It's just Europe. Yeah. And then Australia and New Zealand. So, for Europe, there are still many very good PCB fabs there, and I'd like to do that. Their costs are actually pretty high even compared to U.S.

**Dave Jones:** Oh, right. Okay.

**Lane:** So, like, I've gotten quotes, and I've tried to figure out what it would take to do it over there. And really, I think I can – the way I can best deal with that is to just speed up my shipping time to Europe and to Australia. Right. Okay.

**Lane:** Right. Interesting. Okay. You know, you should probably take the wife and kid over to Europe for a couple weeks, though, on a business trip. Just saying. You better go – You know, just to check. Just to check. Yeah. Every country, you know, you could take your time, right? You don't want to be stressed. Right, right. So, do the fabs in the States – so, we haven't mentioned even yet to the purple side of things. Obviously, everybody knows you for the purple, but do the – Yeah. You know, for panels, do they give you any hassle for purple sonder mask or, you know? Yeah.

**Lane:** Yeah. That's been the most challenging part of when I – like, before I allowed myself to quit the day job, I wanted to make sure I had redundant fabs. And I had just gotten lucky that the fab that I was using had purple. The other ones that I had to add in did not carry the purple, and I've had to order it for them. Really? From the sonder master player. And so, yeah, that's – I pay for all the purple sonder mask on that. It's not one of their standard colors.

**Lane:** That's good, though. It's – you know, it's –

**Dave Jones:** Is it that important for you? Yeah.

**Speaker ?:** It's definitive.

**Dave Jones:** Is that sort of like a trademark of Osh Park being purple? Is it that important?

**Lane:** Well, the reason that I started in the first place was just so that I could spot my boards on Flickr and stuff. Now, I just want everyone to have – now, I just want all the fabs to produce a consistent product. I want them all – so, like, if you order from me that, you'll get – Right. Got it. You'll get a board that looks the same depending on which fabric I'm from. So, yeah, that's the main reason it was important there.

**Lane:** Yeah, because I remember seeing a picture you posted of – or someone was talking about it on Twitter of there being slight differences from one of the early orders or something. It was, like, lighter, but it didn't look bad. It was just once you put them together, you know, then you could notice it next to each other.

**Lane:** Yeah, that was when I was adding a new fab in, and the sample panels I'd gotten from them were correct. But they had mixed a little bit – they mixed it too lightly, the color too lightly. So, it ended up being more of a pink than a purple, and I was – I didn't like it, but, I mean, yeah. And we got it fixed for later ones.

**Lane:** The softer side of Ash Park.

**Lane:** Right.

**Dave Jones:** Because I can imagine if you did attempt to offer a selectable soldermask color, it would become a nightmare because everyone would want something different. Oh, yeah. And then you'd never fill up your panels, and it would just be a shocking mess, really.

**Lane:** I mean, I have ways to – like, very soon, as soon as this feature is added to the website, I'll be able to do other colors.

**Dave Jones:** Oh, okay.

**Lane:** The other colors will be on a slower basis. So, like, if you want – if you must have green, then that panel goes to the fab once a week instead of every day.

**Lane:** Got it. So, that's almost like a crowdfunding side of things, right? Because you can get four or five other people together with a couple boards and say, hey, we need to – or is it just going to be one day a week no matter what?

**Lane:** No, I mean, that's exactly what it would be. Oh, okay. Yes. Well, it would be one day a week, and I would – because no one wants to wait forever for the boards, and they don't want the uncertainty of, like, hey, I ordered this board of green soldermask. No, you're not going to make it.

**Lane:** That's true, yeah.

**Lane:** So, I mean, it's got to be consistent. And so, whether I get the people or not, I have to order it and therefore eat the cost. So, I pretty much just have to hope that enough people will sign up for it if I offer it.

**Dave Jones:** Got it.

**Lane:** From what I've – yeah. So, I have ways to, like – because I can print more than one soldermask color on a single panel.

**Dave Jones:** Really? I didn't know that. Yeah. Yeah, that's not cheap, though. They charge you a bit of a premium for that.

**Lane:** It's not cheap because you're setting up – it adds about 50% to the price of the panels because that's – Holy moly. Because you're making a totally separate set of screens.

**Dave Jones:** Yeah, exactly. I know somebody who wanted an Apple – the original Apple color logo on their board. You know, the one with the seven colors or however many colors are in there. And they actually ordered, you know, seven different colored soldermask on the one board so that they could get that Apple logo. You know, it's like – I've got a photo of that somewhere. I'll have to – That's dumb. You know, hey, it did look cool. Yeah. It looked very cool. But they paid for that. So I'll have to see if I can find a link. I'll find a link to the photo of that and post it because that's pretty good.

**Lane:** I would love to see that.

**Lane:** Excellent. How many panels are you sending out a week now? I mean, is it daily? Like daily sendouts? I mean –

**Lane:** Yeah, it's daily or more now. Wow. About in early May, I bought Batch PCB, which is SparkFun's PCB service. Oh, I didn't know that. And that was – and at that point, the business went up to the point that it was now more than once daily. Yeah.

**Lane:** Oh, really? Okay.

**Lane:** Yeah. So it ends up being about seven to ten a week. Dang.

**Lane:** Wow. That's great, man. That's really great. And that allowed you to quit your job, right? I'm going to ask.

**Lane:** It kind of forced me to quit my job because at that point, it was just going to be too much work. There was no way that I could do my day job with any sort of professionalism.

**Lane:** Yeah.

**Dave Jones:** How long had you been running this thing before you ended up quitting your day job?

**Lane:** Well, the first Dorkbot PDX PCB order was in December of 2009. So what's that? About four years? Oh, okay. Three and a half years. Yeah.

**Dave Jones:** Three to three and a half years? Yeah. Yeah, sure.

**Lane:** And then Osh Park, when it actually split it off from Dorkbot and incorporated it and said, okay, I guess this is actually a business now. That's been about a year.

**Lane:** It was said with real confidence there. Awesome. I'm sure future investors would love to hear that, right? Like, oh, yes. We're a business, we think.

**Lane:** It's hard to consider yourself a business. Yeah.

**Dave Jones:** Right. Is it just you or OD? Do you?

**Lane:** It's just me doing the board stuff. And then I have contracted out to Sociable, James Harton from New Zealand, who does the web design stuff for it.

**Dave Jones:** Oh, awesome.

**Lane:** Yeah, that's what actually has the front-end interface. You kind of do the back-end stuff, right?

**Dave Jones:** Right. Yeah. So, Sociable, is that one of those, is that like a people-per-hour kind of website?

**Lane:** Yeah, exactly.

**Dave Jones:** Is it? Right. Is that where you go to find someone to do something for you?

**Lane:** Oh, no. No, Sociable is a, no, it's not. It's a, that's just this person's web design firm. Right.

**Lane:** Right. Is it, he didn't change his thing to resistor.io as well?

**Lane:** That's right.

**Lane:** It's resistor.io. Right.

**Lane:** Yeah.

**Lane:** Right. Got it. Yeah, I follow him on Twitter and I ask him, like, why, why did you change your web company name to resistor.io? And he's like, well, you know, Osh Park was one of my clients. So, I think that was part of the reason. So, yeah, that sounds great.

**Lane:** Plus, he himself does a bunch of electronics work on his own. He does, like, audio boards.

**Lane:** Cool. Very cool.

**Lane:** And he was in the, that's how I found him. He was in the Dorkbot PDX PCB order. He was one of the people who used it. And I'm so glad he was free to do it.

**Dave Jones:** Terrific. I love this industry. Yeah.

**Lane:** That does help.

**Lane:** Right. So, speaking of that, so I was, so former guest of the show, Ian Danaher, who had done the Nonolith C, that little, like, smooth thing. Yeah. So, I was having drinks with him on Friday and then I mentioned that you were going to be on the show. He's like, oh, no way. Thank you for me. I'm like, for what? He's like, well, Lane is the reason that I got started in electronics. And I was like, holy crap, that's a cool story. That's awesome. So, what was it? I mean, like, you guys were on some forum somewhere or chat something. I don't know what it was.

**Lane:** It was probably just Twitter. And this was kind of the time when the great internet migratory boxes of electronic junk were roaming the earth.

**Lane:** That's what that is. I was looking at that acronym wondering what the hell it was.

**Lane:** Yeah. That's something that I think it was Evil Mad Science Labs that started this, the great internet migratory box of electronic junk. And you just throw all your extra electronics junk into a flat rate shipping box. Yeah. In the U.S. we have these nice flat rate shipping boxes. It's like $10 anywhere in the U.S. and like two-day shipping. Got it. So, you just fill that up with whatever parts from your junk drawer that you hope somebody will use. But, you know, you're not the person to give it a good home and send it off. And one came through me and I tweeted about it. And he said, yeah, I'll take it.

**Lane:** That's awesome. Yeah. That's great.

**Lane:** So, it's really Evil Mad Science who's to take there.

**Lane:** Those guys are awesome. They are. Hello, Wendell.

**Dave Jones:** I wonder if there's one in Australia. Has somebody contacted me about one of these? I'm going to have to go find their email. But I think it may have been one of the overseas ones. So, obviously, you know, shipping stuff overseas is really expensive.

**Lane:** Yeah, it is. Yeah, you want to bounce between Australian back, right? You'd want it to.

**Dave Jones:** No, no. It'd cost $100 each time, you know.

**Lane:** Yeah, but you could do it all over Australia. You could certainly have an Australian one, right? Yeah. It's a shipping ship there.

**Lane:** Yeah. Dave, you can start it. You can start shipping.

**Dave Jones:** Certainly. I will note down. I will go back and find that email. And if there isn't one in Australia, I will start one.

**Lane:** There you go. So, what kind of things are in these things? I've heard about them once or twice. But, like, I mean, just like relays and stuff like that?

**Lane:** Yeah. Anything, dude. Exactly. It's anything. So, like, one that I got had, like, a game controller and a bunch of, like, SSRs. They had, like, some LCDs and then, like, some sort of radio thing. A bunch of stuff that I didn't really know, to be honest.

**Dave Jones:** Okay.

**Lane:** Especially back then.

**Dave Jones:** It's just like a movable geocache. Sorry. Geocache for you, Yanks. If you've ever done geocaching, right? It's a similar sort of thing. Are the rules the same? You take something and you put something back in?

**Lane:** Yeah. Is that the rule? You're supposed to open it up. You're supposed to take pictures of what you take out and what you put in, post it to a clicker or something and then send it on its way to the next person.

**Lane:** Got it. I guess what I'm trying to ask is how do I get one of these things? I want to participate. It just sounds like fun. I mean, it's like a, I don't know, it's like a, it sounds like a cool tradition, you know?

**Lane:** It is. Yeah. There's a, there's a website for them if you search for that acronym. Okay. I'm not going to try and spell it out.

**Lane:** G-G-A-M-B-O-E-G-A. Yeah. Yeah. That's it. Yes. Okay.

**Dave Jones:** They, they should do like a geocaching thing so you can see where its current location is on a map, you know? They should. And then you can like track it all around and stuff like that.

**Lane:** Yeah. Well, and I think, I think kind of the day of it is, and it was, it was pretty big for, for maybe a year. And then I think people get lazy and hide them in there and like forget to send them off. Yeah. Because I haven't seen the updates. Yeah. If you get it. Yeah.

**Lane:** Oh, yeah. Right. Yeah. There's a, there's a, it looks like a wiki page for it and it says there's a page for greedy participants as well. So the people who don't pass it on. Yeah. Right. Yeah.

**Dave Jones:** So what happens if nobody passes on? It just stops. Yeah. It's dead in the water.

**Lane:** It's dead. Yeah. Yeah.

**Dave Jones:** Hmm. Hmm.

**Lane:** Hmm.

**Lane:** That is fun. Yeah. Searching, searching for it on Twitter there. The last update was, uh, the last time anybody tweeted this acronym was, was in March of 2012.

**Lane:** Oh, well maybe the air power can revive it.

**Lane:** Fail. I hope so. Cause it, cause it is fun. Yeah.

**Lane:** That sounds really cool. Well, yeah, we'll, we'll post about it at least. And maybe people can start this back up, especially in, I mean, there's a, there's links and stuff. So. Yeah.

**Dave Jones:** Well, we find the bastard who's currently got it. Just go around on it. Somebody's got to live nearby. Go around.

**Lane:** Steal it from them. Ship them a gym sock with a virus open it. It's a warning.

**Lane:** Go find Ian. Go find Ian and see if he's had his on. That's right. Yeah, exactly.

**Dave Jones:** Oh boy. I, back onto the, uh, Oz Park thing. Um, I noticed everything you do is except the layer of the bar, except the thickness of the board is all in Imperial measurements. It's true. Even your drill sizes, your angular rings, your, your track and space, which is okay. It's true. You bloody yanks.

**Lane:** It's, it's awful. And, uh, and like when I first started making boards and coming up with the, finding the, uh, the unit of measure of the mill, I was like, wow, that doesn't make any sense at all. 64 millimeter thick boards. That's, and that's huge. And, uh, yeah. It's like a sandwich. Right. A mill is a thou. It's a thou. It makes sense, doesn't it? Yeah. And a thou didn't mean anything to me either. So.

**Speaker ?:** Right.

**Lane:** It's just because that still seems to be the units of measure for, for circuit boards. And, um, it's never gone away.

**Dave Jones:** Well, no, the fab, the fabs in America, it is most other countries. Um, well, it's an interesting mix. I'll still use Imperial for track and space. Uh, sometimes like, you know, six, six thou, six thou track and space, but drills are all metric. Um, you know, board sizes, all metric, all that sort of stuff. So. And of course, when I, when I submit. It's a very interesting industry. It's a.

**Lane:** When I submit these things for manufacturer, they're going through, they're going into metric. Of course.

**Lane:** Yeah.

**Lane:** Just because that's what, that's what, that's what the manufacturing is. Even if the, uh, even if the designers are still stuck in these Imperial units. Yeah.

**Lane:** Well, it's, I mean, the, how big are your components? Right. Oh, 0603. Right. I mean, like that, that's kind of just babed in too. Right. I mean, it's just these legacy things, but I've talked about moving over, but man, it's, it's tough. You know, like unless you do that final conversion, right? Like where you start associating it. I don't know. I.

**Dave Jones:** Well, I've moved over for a lot of stuff, but something, as you said, like a component size, 0603. Right. I, you know, I'm just so used to doing. It's an association at that point. 0603. Yeah. It's, it's. Yeah. Whereas, you know, it's, that's like 1608 in, you know, metric, you know, it's just crazy. No, I've been using that for 20 years.

**Lane:** What's really annoying is a 1206 has a meaning in both metric and Imperial, right?

**Lane:** That's the worst part.

**Lane:** Exactly. That bit me very early in my circuit board designing career.

**Dave Jones:** So no, officially now all of the standards have changed over to fully metric. So if you, yeah, yeah. If you strictly want to follow the IPC standards, yes, they are all metricated. I didn't know that. There is none of this Imperial rubbish anymore. Excellent.

**Lane:** Yep. Do you, do you have to deal with IPC much, Len?

**Lane:** Well, I have to be familiar with the, with the specs since, since that's, that's how, right? That, that describes every, every part of circuit board manufacturing. I mean, technically I could do this without knowing them, but I make a better product by knowing them.

**Lane:** Yeah. That's good. I'm glad you do it so I don't have to. Because I've tried reading that stuff before and good Lord, that's a snooze fest.

**Lane:** It is. It really is. I, I just, I just sat through the, uh, the ones for, um, uh, electrical, uh, Enig plating, gold plating.

**Lane:** Oh yeah.

**Lane:** And just so that I could, just because I was having a plating issue with one of the new fabs and I, and I, or at least I thought I was. And, uh, and so I, I just wanted to go through it and, and figure out what, what the stuff was and, and oh my God.

**Lane:** That's right, folks. He does it so you don't have to. Right. That is a service provided. Yeah. So most of your boards are gold. Cause the purple and then gold is, is, it is Enig usually?

**Lane:** Yeah. It's always Enig. Yeah. Okay. It's all, it's all a nickel and gold.

**Lane:** Okay. And that's, yeah. So Enig stands for immersion nickel, immersion. Uh, electricless nickel immersion gold. Yeah. Okay. Electricless nickel. Immersion gold. Okay. That's right.

**Lane:** Yeah. It's just a, it's just a, I think a much better finish.

**Dave Jones:** Oh yeah, definitely. But you can, there's a lot of, quality difference between a good gold, uh, finish and a poor one from China. You know, there's a, there's a huge range. How does yours stack up in that regard in terms of, um, the quality of finish in terms of like tarnishing and things like that?

**Lane:** Uh, I haven't had any tarnish issues, uh, at all with that. Um, the, uh, yeah, I've, I've had, I've, I had what I thought was a, uh, was a plating issue at one time, but, uh, I think it was, I think it was actually a bad contamination issue. I think somebody put a fingerprint on the board. Oh, uh, in between the, uh, the, in between the etching and the plating steps.

**Lane:** So, uh, that's a hell of a, hell of a look on the board, right?

**Lane:** It is. It is.

**Lane:** On the bright side, you can go find that person. Do a little CSI work. Yeah.

**Dave Jones:** And is there any, um, uh, sorry?

**Lane:** Let's go ahead and, and boy, is it a, is it just a lot different than, uh, than like the, uh, the solder finish, the hassle finish that, uh, that.

**Dave Jones:** Oh yeah. Yeah.

**Lane:** It's just, it's so nice to, um, they get this nice flat surface, uh, with, with, uh, the, the leaded solder or the solder thing where they have this hot air solder level, hot air hassle. Yeah. Hot air solder level. And, uh. Yes. So, um, uh, especially at small, uh, trace, um, clearances, that really opens you up to shorts. And I think that was the big reason that I was having problems at first with the, with, with the panels we're sending to China.

**Lane:** Hmm. Got it. So your stuff is six, six right now. Is that right? Six mil, six space. Yeah.

**Lane:** The four layer order is, uh, is five, five. Okay. Yeah. The two layer is six, six.

**Lane:** Okay. So is, is that, uh, you guys have to excuse my name. I never do BGA layouts. Cause I just like, I just push that off to my layout guy and I'm like, no, thank you. Right. Right. Is that, so can you do, can you do, uh, BGA's with that?

**Lane:** I mean, or is it, is it, is it like one mill, one millimeter BGA is no problem.

**Dave Jones:** So yes, you can do BGA is one millimeter is no problem. Once it gets smaller than that, it's, it's pushing it. Yeah.

**Lane:** I, I, I, a lot of people ask me for rules that can do 0.8 millimeter BGA. And that's why, um, that's why I, I upped the design rules for the four layer order. Uh, so now it has the, it has five, five, uh, trace spacing, and then it has, um, 10 mil drill and four mil annular ring. So that's, that's enough to, to just barely squeak through. Plus, um, these design rules that I have with my fabs are, uh, uh, are the guaranteed numbers. Um, the fact that I don't, uh, I don't enforce these and neither does the fab. So I've seen people try and like sneak in three, three rules.

**Lane:** Just by accident.

**Lane:** I think, I think they didn't know that they were, that they were violating the rules. I, I can only, I can only think that because most people think that there's, that there's something that'll keep them from being able to submit boards that, yeah, that have them.

**Lane:** But yeah, it's just something that they might edge through your line, right?

**Lane:** I mean, it just, all my fabs are three mil capable. So, um, uh, so sometimes it's just not guaranteed because three mil, what happens is they just have a lower yield on them.

**Lane:** Yeah. Right. And they want a hundred percent tested. They want to have high quality stuff, right? Right. Right. Yeah.

**Dave Jones:** Well, and what, what happens with that? If one of them fails testing because some idiot put through, you know, two thou, two thou on there. So, you know, it fails all the electrical testing. Then do you tell them, look, we still want that panel because everyone else's design is going to be fine. Oh yeah, absolutely. I hope they wouldn't scrap that panel because.

**Lane:** No, no, they just scrap that one board. Uh, and, and typically what they do is they just, they just put a, a, uh, an X on it to, to show that it's a bad board.

**Dave Jones:** A marker on it. Yep.

**Lane:** But, uh, our boards actually aren't electrically tested there. Uh, they do, uh, automated optical, they do an automated optical inspection throughout the whole process, which is, uh, they compare scans of the board with the Gerbers in order to make sure that it, that there are no shorts or, or, uh, or breaks, but, um, uh, they don't do the final electrical test, which would tell things like, which would expose things like plating issues in vias. But, um, like if a via didn't go all the way through or something, um, but as I say, in practice, this is a reported failure rate of about one in 40,000.

**Lane:** Wow. That's great. So are you at a one ounce copper still? Is that the, I've looked at your specs a couple of times, but I always forget. I mean, yep. Yep. It's one ounce. You, so, so, I mean, you mentioned solder mask moving out. Are you going to, are you looking at maybe moving other stuff out too? I mean, like Ash Park's getting bigger. So is this a, does this mean options are bigger too?

**Dave Jones:** Different thickness boards, flex, you know, it's it. Right.

**Lane:** 0.8 millimeters is coming. I mean, that's, that's another thing that as soon as the, the, our, my web designer can put that, um, that into the, that feature into the website, I can start doing it.

**Lane:** Mm-hmm.

**Lane:** Um, the, uh, probably not thicker boards, probably not different copper thicknesses, because really what I want to do with the half, with the half width boards is say, uh, is if you don't specify that you must have, uh, 1.8 millimeter or, I'm sorry, 1.6 millimeter or 0.8 millimeter, then just, uh, then it, then it can go on either panel and you could get either back. Uh, but, but you can, of course, always say that you, you, I must have the half, the half or I must have the full.

**Lane:** Ah, okay. Okay. Right. Yep.

**Lane:** But most people are just doing prototypes and they don't care. So, and that's, that's the vast majority of the, of the order is prototypes.

**Lane:** Yeah. Well, doing, I mean, doing a BGA in a four layer is pretty tough to start with. I mean, like just breaking out all those signals and everything. Right. I mean, like it seems most BGA boards.

**Dave Jones:** Well, it depends on the BGA. It depends on how many levels of, uh, pads you've got in there, you know?

**Lane:** So, oh yeah, I guess smaller parts aren't as big a deal, but I've, I've, some of that stuff I've looked at. I mean, like I said, I haven't, I haven't done one, so I don't really know, but, uh.

**Dave Jones:** No, well, you wouldn't be able to do, you know, a huge, you know, 800 or a thousand pin BGA on a four layer board or something. Um, unless you're only routing out 10 signals, you know, unless you're only routing out the ones on the outside, you know, but, but sometimes some people have to do that. You need, you know, a thousand dollar FPGA, but, but you only, you know, and a thousand pin FPGA because you need it for the logic density, but you only need to have 20 signals. Yeah. Like a, you know, a serial in and out. That's it. Right. But, but you need this thousand pin BGA. It's insane. That is pretty crazy. I've done that before. If you, I've, I've had that requirement, two serial buses in, two serial buses out. Right. And, but we had to use a 1500 pin BGA.

**Lane:** That sucks.

**Dave Jones:** Because that was the, because that was, because we needed the density in there. Yeah. You know, so we needed the highest end part. It was crazy.

**Lane:** So, so Lane, I have to imagine that looking at a panel is probably really fun because you get to see projects like Dave's crazy, you know, huge FPGA type of thing. And then you also get to see, you know, like an led blinky board. Yeah. I know that you, you keep, I've asked you about this before too, because I wanted my stuff to be a secret at the time, but what, what kind of crazy stuff do you see? Like in a general case, nothing like that anyone would be unwilling to, you know, have told about, but have you seen anything like super, super crazy?

**Lane:** Let's see. So I, hard to say. I mean, I, so lately it's, it's, it's now just such a, just such a race to get things depaneled and, and, and shipped off that I don't really get to see what's on there anymore. It was, it was certainly a lot more fun when I was just doing like a panel a week and then I could, I could like spend some time and look through it. But, but yeah, I see, I'll, I'll sort of, it's, it's a really amazing to me the number of tube projects that like every single panel has, has a, has a tube socket on it somewhere. So there are tons and tons and tons of tube projects.

**Lane:** And, uh, and, uh, let's see.

**Lane:** So there, and, and then of course, like just your, your standard compliment of like Arduino shields and, uh, and little breakout boards. And then, and then every now and then like these, like, uh, people started doing like the front panels for audio decks, uh, that started to mill those out of the board because I mean, a PCB is a, and it, it's a piece of nice thick fiberglass.

**Dave Jones:** It makes a great front panel.

**Lane:** Exactly. So people, so I've, I've started seeing those in the order, but it's purple though.

**Dave Jones:** That's not that great. That's awesome, man. That's when, that's when you need the selection of colors is when you're doing front panels.

**Lane:** Yeah. Well, purple makes it distinctive. I like that. It's, it's regal.

**Dave Jones:** Regal. I don't know. It's very 1980s prints, isn't it?

**Lane:** Well, and a trick that people can do is, uh, is you print out it. So you take your front panel board, you, uh, put a, a copper fill across the entire thing and then you, you expose the text out through the solder mask layer. So now you have this, this, this gorgeous purple front panel with a gold, uh, legend on it. Yeah. Gold text for all this stuff.

**Lane:** Yep. Yeah. I like that. The magics of PCB. That's great.

**Dave Jones:** Comes back to, if you got poor quality gold, that can then tarnish that, you know, over time. So that can be, you know, it's great when you get it. Oh, look at this beautiful gold text. And then it's, uh, you know, six months later, it's, uh, it's like tarnished. Yeah.

**Lane:** So now I've been doing, um, the, the gold finish for about two years and I have boards from, uh, I have boards from two years ago and, and I haven't seen tarnishing issues just on the shelf. Certainly with like fingerprints on it and stuff. Cause, uh, like just the acid.

**Dave Jones:** Fingerprints that causes a, yeah.

**Lane:** Yeah. Just like the acid from your fingers. It can, can eat through the tiny layer of gold that are on these boards. Cause it's, most of the finish is nickel and then there's just a gold, uh, uh, the gold finish on it to, for a solder ability.

**Lane:** Trap for young players. That one. So you see a lot of, uh, cool projects. The other question I had for you before we get to the, I should, we should have probably gotten to some of the, uh, listener questions too. Uh, but before we do that, uh, we've talked about the, so what is the mix you're seeing of, of, uh, CAD programs? Cause I think I've asked you in the past, but I'm always curious about that.

**Lane:** I would love to have this just as a thing as this, uh, like a, uh, a counter on the front page of the website because, uh, cause it is interesting to see how, how things have changed over time. Um, when I, when I, when I first started it, it was all, uh, Eagle, uh, with, it was almost all Eagle with a little bit of, uh, Kaikad and then, um, uh, a little bit of, uh, and then like vanishingly small of everything else. Uh, about a year ago, uh, Kaikad kicked up, um, is more than, yeah, is ended up being like 75% for, for a long time.

**Lane:** Wow.

**Lane:** Uh, with Eagle dropping down to a quarter or to less than a quarter. And, uh, and then just a few, then the smattering of other ones. Uh, now it's, now I'm getting a lot more, um, I think professional boards like from engineering firms and not just the open source hardware community. So, uh, I've seen, uh, a rise in, in Altium and, uh, or I said Altium and, and, and Orcad and, uh, pads and things like that. But I'd say right now it's probably at about, um, I would say that Kaikad probably still has the majority. Um, Eagle is, uh, or maybe not a full majority, but most of the boards on in there are, uh, are Kaikad followed by Eagle probably neck and neck. And then Altium, uh, a little bit of design spark. And then, uh, actually I'm, I'm seeing a few from like the, the web tools, the web layout tools. Oh, interesting. Like circuits IO.

**Lane:** Yeah. Right. Yep. I'm sure that'll get, uh, bigger too. I mean, I don't know if you're working with any of them or anything like that, but, uh.

**Lane:** Yeah, I do the, I do the boards for a circuits IO. Oh, you do. Okay.

**Lane:** So that you're like tied into that.

**Lane:** Yeah. So that like when you order for it through them, it comes out to me.

**Dave Jones:** That, that reminds me, by the way, I have to do my video beating up Altium because they haven't released a hobbyist version. I'll have to do that shortly.

**Lane:** I'd like that because, well, I mean, they have that, they have the new kind of like, well, they have the student rates and they have the new kind of, what is it? $50 a month rate.

**Lane:** Like a cloud rate kind of thing. Like a subscription.

**Lane:** I don't know what it is. Yeah. It's a subscription thing. And, but I guess there's a good student rate because I see a lot from students or that it's the, the, the piracy rate. Yeah.

**Lane:** Yeah. Eagle and Altium seem to both have both high piracy rates from what, what I've, I've heard from everyone.

**Dave Jones:** Altium is the, Altium is the de facto standard in China. Not a lot of people know this. It's used almost exclusively in China, Altium Designer, but nobody pays for it.

**Lane:** Yeah. You know. It's a, it's a Chinese company now, right?

**Dave Jones:** Well, yes. Yes, it is. That's right. Yeah.

**Dave Jones:** Yeah.

**Lane:** That will be really interesting though. When you get that on the, on the front site, I mean, that's just to see how trends change over time and everything, you know, like that.

**Lane:** Yeah.

**Lane:** So that'll be good.

**Dave Jones:** I would, I would definitely do that. That's a useful industry resource.

**Lane:** Aside from the PCB service.

**Lane:** Yeah. I'd like to see, I wouldn't have like the top, I wouldn't have like the list of here's the top parts that people use and here's the, uh, the top CAD packages, uh, and, and that sort of thing. Yeah.

**Dave Jones:** That'd be great.

**Lane:** I still consider this kind of a community circuit board order. So like when you order something, it tells you like the number of boards on the, it gives you a few simple statistics about the panel that you're on. Yeah. Like the number of designs and the number of people. So it would be, it'd be really cool to also have in like, and here was the mix of CAD packages and here was.

**Lane:** Oh yeah. That'd be really cool. I'd like to, if you could, if you, I know this would be tough, but I'm going to ask anyways. Uh, you know, like on maps where it says like, you are here, if you had like the whole panel and then you just had a little bit that you're doing, you are here, you know, that would be cool too.

**Lane:** But well, we're going to have the, this, uh, a project sharing thing, uh, popping up soon and that will, that'll capture whether or not people are sharing their designs and in which case you can have here you are in the panel and here are the open source designs that are right next to you.

**Lane:** Oh, name and shame. I like that.

**Lane:** Which I think would be really fun.

**Lane:** Yeah. That's a great idea. You just get like, add the little, the little logo with the gear and the keyhole, right? Yeah. That's awesome, man. That's so what are these, uh, what are these features rolling out? I mean, is this obviously you're, you know, I'm sure the day to day is pretty busy, but, uh, you know, the whole pushing features is fun too.

**Lane:** Yeah. And, uh, well, I, I, I don't have, uh, I don't have my, the web designers full time. So, uh, that, that slows things down a bit, but, uh, but soon I'm really hoping within like the next month we'll have the, at least the project sharing and the, and then I'll be able to start capturing, uh, uh, things like that. Like whether or not something is, is, is shareable in which case I can collect more statistics about it.

**Lane:** So that will that be like, uh, so it'll say, yes, this board Dave, Dave Jones uploaded this board. It is open source hardware licensed and then it's like click order, that kind of thing or what?

**Lane:** That too. Um, but, but also that like you were on a panel with, uh, right next to Dave Jones's board, this, here's the list of open source designs that were on the same panel as you.

**Lane:** Oh, that's really cool. Yeah. That's a great idea. It's like, it's like a active wiki kind of thing. It's like, cause then you're going to, of course you're going to go look up those designs, right? It's like, I want to see what this thing is. Yeah, of course. Right.

**Lane:** And that kind of, it kind of builds on the sense of community. Like it does take, it takes, it takes, um, 80 people working together to, uh, to justify one of these panels.

**Lane:** And one lane. Don't forget that. The one and only. One lane of traffic, right? That's great. So, uh, so we should get to some listener questions. Yes. Questions. Okay. How about the one at the bottom first? Uh, so some, there was rumor about, uh, gift certificates. Uh, I don't know if that was, you were going to give me a gift certificate or David a gift

**Lane:** certificate, but, uh, that's a, that's kind of a, it's a, it's a lower priority feature on there, but, um, but yes, I would love to be able to just kind of go, okay, you know what, um, here, here's a list of codes that I can, that I can generate on the site and, and hand out or people can, can order a gift certificate for him. Cause it does get requested pretty frequently. And it's something that I would like to have just to like reward people for doing good things or, uh, um, to, to like promotion type stuff, right? That or, that or, Hey, I really like your project. If you want to make it through the site, here's a gift code. Oh, that's kind of cool. Yeah. Cause that's, cause I do that to a limited extent right now. I'll see something, something interesting on another site and I'll go, Hey, I think that's, there was one that's a, um, an open source, um, uh, it's called a Puff and Sip, um, interface. And it's for people who are like, uh, quadriplegics who, uh, they, they, you can, it's a pressure sensor connected to a straw. And so you can blow in it to go to enable or, uh, or yeah, or, or suck to not to disable. And, uh, and that's a project that I would have really liked to have supported in that way of just being able to say, say, Hey, that that's neat. That's great work. Here's a, if you'd like to order it through my site, please.

**Lane:** Yeah. Yeah. Like the Osh Park, uh, philanthropic arm.

**Lane:** Right, right, right.

**Lane:** I've got a question.

**Dave Jones:** Yeah. Where, where do you currently sit in the, in terms of competition? Where do you currently sit in terms of lead type? Well, with PCB, it's all about lead time and price. Yeah. Right. Fairly much. I mean, quality is like, eh, you know, almost secondary for these prototype boards. It's like, how much does it cost and how quick can I get it?

**Lane:** Yeah, exactly.

**Dave Jones:** Where do you sit in terms of competition? Who's your main competitors?

**Lane:** So for, uh, so I'm, I'm in the same group here as like, uh, uh, price wise between, uh, seed studio, it studio, uh, of course my, my two main competitors, uh, Sunstone in the U S and, uh, and kind of advanced circuits. Um, since they have the $33. Right. The $33. Yeah. But, um, but for prototypes, it's all about your, uh, it, it's kind of like you want one board. And so the 33 each, you have to buy five. Um, so it ends up being $150.

**Lane:** Yep. Um, but you can get 60 square inches. I think that's the only.

**Lane:** You can get some, you can get some nice big boards for it. So, uh, but let's see. So I said $150 divided by five means you get a 30 square inch board for me for the, for the same price. Yeah. Right. Uh, lead time. I, I, I, lead time is definitely where I win because my average order to shipping time is now eight days. So, uh, and inside the U S that means the, that means you, you'll, you'll very likely have your boards in 10 days.

**Lane:** Nine. If you do priority shipping, which I always do. Yeah. Right. Cause it's five bucks. It's like, all right. Yeah. Whatever. Give me my boards now. Damn it.

**Lane:** But, but as I said, outside of the country, it's, it's, if you want, if you want a speedy stuff at like a, or even a, uh, predictable delivery time outside of the country, that's like UPS Express is, is, is it. And that's like, that's like 50 bucks.

**Dave Jones:** Oh wow. That's crazy. Which is crazy. Yeah. Yeah.

**Lane:** Because like my shipping time to, to Australia, for example, is, uh, uh, it, it seems to be no matter what use priority mail or regular mail, it's, uh, it's 14 days, no matter what.

**Lane:** It's a geographic phenomenon.

**Lane:** That's, that triples the, uh, the manufacturer, your time from ordering it to getting it.

**Lane:** Yeah. That's crazy.

**Dave Jones:** Yeah. It used to be a lot better than that. This is before all, all the security or the U S security bullshit.

**Lane:** Yeah.

**Dave Jones:** Seriously. Yeah. We were, I would order stuff from the U S and get it in one or two days to be on the plane and straight here and bang, you know, well, it's like, Oh God, I've got a bloody scan everything.

**Lane:** So, uh, so now have a crazy. Yeah. Um, so now I'm working on getting a, a faster, a faster service for international. And what I can do is, uh, both UPS and DHL have these international mail products. Uh, once you, um, once you, you ship to a certain amount of volume overseas, you can, uh, what they do is they, they collect the mail from, from me and, uh, they fly it into the destination country. They escort it past customs and then they put it in the local mail system. So the drug smugglers, they claim, they claim 48 days everywhere, anywhere in the world. So, wow, that's killer. I'm, I'm really hopeful.

**Lane:** All right. Yeah. And so that would, would that be like a thing where it's like, all right, all the people in South Africa or some, somewhere where it has the potential for the amount of traffic they need, but you don't have to get over some threshold. Is that like everybody would need to get together and kind of help out with that kind of thing or what?

**Lane:** No, it's a, it, I only have to reach a threshold for all outside countries. I like, it's only a pick, it's only a pickup threshold. It's not a per destination country threshold.

**Lane:** Oh, that's great then. All right. All right. Not America. You win again.

**Lane:** Yeah. So I think those are like my, my main competitors and I think I do pretty well price wise against, uh, against most of them. Certainly quality wise by way by a far margin, quiet quality wise.

**Lane:** I was going to mention there was a, uh, I think there was a document that actually did the comparison too. Cause there's like, there's a balance point from, because of the costs, you know, like, so if your board's over a certain size, I think that's where the only thing that tips the scales is because of size. Right. So if I need a 60 square inch board, I'd go to advance. But you know, if it's, you know, 10, then I'm court, yeah, I'm going to go to you, you know, like just cause of the, the cost trade off. And you know, it's the same, same thing that happens with like web companies too. It's like, you know, if you need, if you want flat rate for some, you know, large amount of downloading, or if you want to on a, you know, go to iTunes and buy, buy one song at a time kind of thing. Yeah. You were the iTunes, except with a better interface. iTunes sucks. Well, thank you. So yeah, Friendly Circuit was asking on Reddit. So yeah, how do you, how do you find new ones? I guess, I guess, you know, you've, you've already scaled up to four fabs. How would you go about finding another fab? Is that just like a site visit kind of thing or?

**Lane:** Oh, so first of all, there's just the challenge of finding them because they, most of them have really terrible web presences. A lot of these companies were started in, were started in the eighties and nineties at kind of the, the heyday of, of circuits manufacturing in the U S not so much. They don't so much have great websites. Yeah. So it was kind of hard to find them. There's a, there's a site called PCB list, which you can search by geographic location. Then I have to contact them and, and, and send them a copy of one of my panels and say, first of all, are you interested in this? And for a lot of them, they just go, no. And that's a really complicated panel. We don't want to touch it. Why is that just too complex? Just the, just programming the router for all those is awful.

**Lane:** It's the cam guy screaming in the background. Yeah, yeah, yeah, yeah, exactly. Right.

**Lane:** No! Right. I will quit if you take on this password. Right. And then I have to send, then I have to send sample and say, okay, I'd like to order that panel. And that panel has a bunch of my, a bunch of normal boards on it, as well as one of my, I have a variety of test coupon boards that I've designed that, that like one of them is really, is really, it's a, it's a two by two inch board. It has 286 linear inches of, of exposed trace on it. Uh, uh, six, six mil parted from another trace, uh, zigzagging all over the place in a, in a, in a complicated curves with lots of acid traps and lots of, uh, um, uh, lots of like vias, like small vias with small annular rings to, to really, um, uh, it's really a fab torture test.

**Lane:** Is that called the bastard coupon?

**Lane:** I think I, I think I do call it something similar to that. Do you have a picture of this?

**Lane:** I, I definitely want to see a picture of this.

**Lane:** Yeah, I do.

**Lane:** I can send you a link afterwards. Okay, great. That's awesome. Awesome. That's a great idea though. You know, that, that's actually how they do it for, um, you know, uh, making chips as well, because you know, you need to test like the smallest features and everything. So that's, that's really cool that you, you kind of do that same thing. I never would have thought of doing that.

**Dave Jones:** Well, a test coupon is standard across the industry. If you're serious about getting your PCBs manufactured, every panel you're design, in fact, it's company policy. A lot of companies I've worked at, yeah, you put a test coupon on there and, you know. Yeah, the test coupons. Just so that you can track individual boards when they come back.

**Lane:** Yeah, IPC has a, has a, has standards for this. Um, but, uh, and they're okay, but mine are, mine are, are really a lot more rigorous, I think. Um, uh, theirs are like, okay, here's like 12, 12 linear inches of, uh, of trays right next to each other of various sizes and things like that. And you look at it and you go, okay. But, um, but I need to know like, um, like solder mask alignment, uh, top, top, top copper to bottom copper alignment, uh, drill, uh, registration, drill sizes. Um, I need to know if they, uh, uh, trace width tolerances and, and, and all of these things.

**Lane:** And so you just measure it when you get back then? Like you just measure each of these things visually and?

**Lane:** When I'm selecting the new fab, yes. Um, uh, after I've selected the fab and they passed the tests, then I, I just do a random sampling every so often, or if I've gotten a complaint on a panel.

**Lane:** Okay. Huh. That's cool. That's really cool. Uh, so obviously my panel knowledge is low as has been shown throughout this entire show. Uh, but for the folks at home, of course, not for, not for me. Yeah. Uh, could you help visualize a panel in terms of size and everything? I know Dave's done videos on it, but we all know I don't watch those videos. So. Yeah.

**Lane:** Well, there's a, there are standard panel sizes. The, the, um, the regular standard panel size is, uh, 18 inches by 24 inches. And, uh, which is, uh, what a foot and a half by two feet. Okay. Um, that's, uh, uh, and, uh, of that there's a, you, you put a, there's a little bit of a frame on it so that the fab can put their, their tooling holes and things like that in it. So you end up with about 16 inches by 22 inches of useful space. Um, and, uh, and that tends to, and for a lot of fabs, that's any board you make through them is going to go through one of these, one of these, because it's just the materials are so inexpensive that, um, it doesn't make sense to, to stock other things. And sometimes they'll cut them in half and things like that, but most won't. They just deal in that one custom size.

**Dave Jones:** There's a lot of waste in the PCB industry.

**Lane:** There is, there is.

**Dave Jones:** But for those out there who don't realize, um, and who haven't watched my video, um, yeah, don't just go making this massive panel because you can fit a hundred of your boards and think that that can then go through the pick and place machine because what? No. Not only can it go through the pick and place. Talk to your assembler first because.

**Lane:** Yeah. Not only can it go through the pick and place, but, um, but there, if you don't have, um, consistent copper coverage across your panel, then you're going to have plating issues, which will cause, um, which can cause breaks and shorts and, uh, and all sorts of problems. And I was plagued by those when I first, uh, when I first started doing the service, um, until finally some guy, uh, I sent it to a fab and said, um, why, why? Like they eventually said, no, we don't want to make these because they're, they're hand fixing, um, hundreds of problems on here.

**Lane:** Wow.

**Lane:** And that, that was the main reason that, uh, advanced circuits dropped me as a, as a customer back in the, back in when I first started this and they go, look, we're, we're fixing, we're fixing 200 shorts and breaks on these because, uh, of your copper coverage.

**Dave Jones:** Oh.

**Lane:** And I was like, copper coverage.

**Dave Jones:** Wow.

**Lane:** And so then I had to write code.

**Dave Jones:** What's that?

**Lane:** Yeah, exactly. It's like, what? I didn't, I had no idea. So, um, so then I found someone to educate me. They, um, and they said, uh, they laid out, uh, he told me, yeah, you need, you need to have similar copper coverage across the entire panel, like a certain percentage of copper coverage and, and, uh, uh, or you can have it gradiated. So you have like a bunch of stuff with copper pores at the top and not a lot of stuff at the bottom and there's tricks you can do. And so I had to rewrite my panelization software to, uh, to take that into account.

**Lane:** And so now it actually does the analysis based on like percentage of copper and different layers and everything that, so that it matches that standard or what?

**Lane:** Yeah, exactly. So I, I, um, so now really what I do is I just split off all the boards that have low copper coverage onto their own panels. But for a long time I just, I, I'd had it try and lay it out and analyze it and put it in the right spot in the panel, which is a kind of a huge headache.

**Lane:** And right. Yeah. So now your software optimizes for all the spacing and everything too, right? For actually fitting smaller, smaller boards in with larger, larger boards and stuff, right?

**Lane:** Yep.

**Dave Jones:** Yep.

**Lane:** Math.

**Dave Jones:** There's lots of traps like that in, when you get into serious PCB manufacturing, there's just so many of them. In fact, there's probably some that you haven't even hit yet. I'm sure. Yeah, definitely. You know, if you're making really advanced boards and yeah. Serious business folks. And often, you know, and, and sometimes it is fab dependent and assembler dependent and all sorts of things. So, you know, what, what might work at one fab doesn't work at another. What might work at one assembler doesn't work at another and whoosh. Yeah.

**Lane:** I mean, and there are, there are like, like actual manufacturing process differences between the way that U.S. fabs make boards versus how Chinese fabs do because. Oh yeah. Because U.S. fabs have all these extra environmental rules that they have to adhere to. No, cupric chloride going out of the drain here. Is that the. Exactly. And so, and so like in a U.S. fab, the difference between a plated via and an unplated one is if there's a copper on both sides, because anything with a copper pad on both sides will get, will get plated and anything else won't. In the Asian fabs, they have a different process that, that with a different type of resist. So they can send it through once instead of having to do these multi-step processes.

**Lane:** And it's just not as friendly so that that's why we can't do it in the States. Is that the idea? Yeah. Huh. That's crazy. See, I don't know. I'm, I'm fine with like, you know, I've, I've worked near PCB manufacturer, at least the assembling side of things, but I've, I don't, I don't mind not touching this stuff.

**Dave Jones:** You're going to toss it over the wall. Exactly. You're a tosser. Come on. I'm not a tosser, but yeah. You just put that thing over the end.

**Lane:** But I don't mind letting this stuff go. I mean, like there's, there's many more capable people than me. I don't know. Like this lane is a great example, you know, like this is.

**Dave Jones:** Well, no, that, that is very common. I, a designer won't know Jack about either laying out a board or manufacturing. They'll just, what's called toss it over the wall to the PCB guy or girl. You know, they'll, they'll toss it over the wall, so to speak and, and wipe their hands off it and hey, someone else's problem.

**Lane:** Yeah.

**Dave Jones:** You know? Yeah.

**Lane:** I don't ever have to do a, I usually hardly ever do fab drawings, although that is, you know, if you're doing bigger orders, obviously that's, you know, like that's a big part of it, but I, great services like Osh Park allow me not to need to do fab drawings either because it's just all automated. So I like that. I mean, it's just not worth my time. I mean like the fab drawing side of things like that's not worth my time and I, cause I have great services like Osh Park and I do mostly prototyping. So whatever. Thanks Lane. I appreciate it. Oh, thank you. You're welcome. So, so what else, what else is in the future? I mean, we, uh, what are you going to, you know, branch out in other, other ways or just kind of head down, keep quality high kind of thing for now?

**Lane:** No, no, it's a, there's definitely now with the, um, with like the batch of PCB customers in the mix. Now I have, I have a, I have a large enough flow that I can kind of do other things. I can do thinner boards. I can do, um, uh, different colors. I can, uh, um, I'm hoping to offer an assembly service. Oh, fancy. Yeah.

**Dave Jones:** Oh, cool.

**Lane:** Very limited assembly service, but, uh, all the same.

**Dave Jones:** You've opened up a whole can of worms there. Assembly service. Oh man. If you think you're working your ass off now.

**Lane:** Well, very much like the boards, I'm not going to be manufacturing them. I'm going to be sending them off to, uh, manufacturing.

**Lane:** Yeah. But if you can automate that side of thing, I mean, like I know that it happens sometimes.

**Dave Jones:** Yeah, but you've got to deal with the crap though. When somebody's got a complaint, they're going to come to you. It's true. That's the problem. Yeah, it's true. You know?

**Lane:** Well.

**Dave Jones:** And assembly will have order, many orders of magnitudes, more complaints than just bare board PCB.

**Lane:** Definitely. And I'm not looking forward to that.

**Dave Jones:** It's just the nature of the business. Right. You're good as a professional. No, I'm not. Right. Yeah, I am. That's my business.

**Lane:** Oh boy. And you're good at what you do.

**Dave Jones:** Yes.

**Lane:** So Lane, you had mentioned, uh, a couple of days ago when we were talking that you might be looking for people soon. Is that the idea or is that? Yeah.

**Lane:** I'm, I, this is something now that I have to, I have to kind of figure out is, uh, as I, like, I need help. Uh, this is a lot of, most of the PCB stuff is just me. Right. So, um, I'm responsible for breaking up the boards. I'm responsible for answering customer support email. I'm responsible for, uh, trying to find people's projects and publicizing them, things through the order. So, um, yeah, I'm, I'm, I'm really looking for help for both like handling the customer support email, which is things like, Hey, I'm having problems getting my boards to upload or, or things like, Hey, that I just got my board back and it's not exactly like a picture. Um, what's going on? Uh, and that sort of stuff. So I, I, I, I need to, I need to find people to help with that. You need peoples. I need peoples.

**Lane:** Yeah.

**Lane:** I need, I need people to help, uh, blog it, uh, to help, like, cause I, I'd like to have a blog where people can share their designs, like, uh, uh, share the, these open source designs, these cool things, you know, all these cool projects that are coming through the order.

**Lane:** Yeah. Solder mask, uh, art. That's always a fun thing. I've been trying to put solder mask, solder mask art on all my boards. Yeah.

**Lane:** Yeah. You, you, you and John Janier both do, uh, John Janier on Twitter, both do a great job with your, with your, uh, designs in the, your, your like hidden messages on the boards.

**Lane:** Yeah.

**Dave Jones:** Could you like sneak in every, every board that comes through, can you sneak in like a little bit of, can you automatically place like some little, you know, bit of, uh, silk screen on their board? I, you know, like a random little animal or something, you know? Right. Yeah. Yeah. I know. You get a lot of pissed off people. Right. It'd be fun. It would be fun. Until everyone stopped using your service. Yeah. Right. Because they didn't get exactly what they asked for. Yeah. Like, cause that's really annoying, right? I send a board away to get manufactured and the bastards put like their own mark on it, you know? And, and like, I'm trying to do like a front panel or something and they'll put their, you know, their, their date code number or something. It's bastards. Yep. Yep. It's like, just manufacture what I told you to. Nothing more, nothing less. And yeah, it's a, I'm sure you get complaints like that all the time, but I'm sure you use manufacturers that don't put, you tell them not to put the marks on.

**Lane:** Right. Exactly. I get, I get one UL mark for the entire panel. Yeah. For example. And, uh, and, and the date code on the entire panel.

**Dave Jones:** And then it's off, and it's off the design.

**Lane:** And I don't put order numbers or anything on the, on the boards like the, like the cheaper Chinese manufacturers have to do.

**Lane:** Oh, just to keep it all straight. Is that the idea? Oh yeah. Exactly.

**Lane:** For a good time, put some, just throw some random six digit numbers on your boards and send them off.

**Lane:** Random Chinese characters. Right. Oh boy. That's good. All right, cool. So how should, how should people get a, get ahold of you if they, if they are in Portland and they want to work for you?

**Lane:** Oh, uh, they should send me an email at, uh, and they don't have to be in Portland for most of that. It's, it's a customer service.

**Lane:** Oh, that's true. Yeah.

**Dave Jones:** Yeah.

**Lane:** I give them access to an email box. Uh, but I am lane.

**Dave Jones:** There's this thing called the internet, Chris.

**Lane:** I've heard of it. It brings people together. It's I'm lane, L A E N at oshpark.com.

**Lane:** Okay, cool. And we'll post that. We'll post that. So Lane gets all the spam in the world. I appreciate that. You know, all the spammers on our site, but also hopefully the, the soon to be gainfully employed. Absolutely. All right. And oshpark.com is, yeah, that's the place to go. Upload, get purpled, as we were saying. Get purpled.

**Dave Jones:** Get purpled. I haven't done it yet. I'll have to. You have to. Put one through just for kicks.

**Lane:** It is, it is a magical process. Uh, honestly, like just like how easy it is. It's, it's really great. So I highly recommend it.

**Dave Jones:** Thank you very much for joining us, Lane. Well, thank you very much for having me.

**Lane:** Well, uh, we'll talk to you soon and we'll see, we'll see more purple PCBs out in the wild. Awesome. All right. Oh, multiple colors. Once you offer. That's right. Yeah.

**Dave Jones:** Options. That's what we want.

**Lane:** It'll be, it'll be purple in my heart.

**Dave Jones:** Thanks, mate. Catch you later. All right.

**Lane:** Talk to you later. Bye. Bye.

**Lane:** Bye.

**Speaker ?:** Bye. Bye. Bye. Bye. Bye.
