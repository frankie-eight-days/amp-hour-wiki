---
episode: 104
title: Ceramic capacitors & High end scopes - Kempt Kickstarter Kakorrhaphiophobia
url: https://theamphour.com/the-amp-hour-104-kempt-kickstarter-kakorrhaphiophobia/
---

**SPEAKER_02:** This is the F-Hour Podcast, recorded July 15th, 2012. Episode 104, Kempt, Kickstarter, Kakorafia-phobia.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog.

**Chris Gammell:** And I'm Chris Gammell of Chris Gammell's Analog Life. What's up, Chris? Good morning, Dave. Not much around here.

**Dave Jones:** Oh, that's not terribly exciting. I've been pretty excited recently.

**Chris Gammell:** Yeah, playing with your new scope, right?

**Dave Jones:** Playing with $140,000 oscilloscopes. Not every day you get to do that.

**Chris Gammell:** Is that all? Yeah.

**Dave Jones:** Yeah, it's only $140,000 Australian dollars. Not sure what goes for in the US, you know.

**Chris Gammell:** It's just a jump change, right?

**Dave Jones:** Yeah, that's right. For some companies, yeah. I just had it lying around, you know. I completely forgot.

**Chris Gammell:** Yeah, that's crazy.

**Dave Jones:** You want to know what the crazy thing is, right? Is if this was actually mine, and I was bullshitting about lying around gathering dust, of course. If it really was, it actually would. If I really had this in my lab for keepers, it would actually sit around gathering dust.

**Chris Gammell:** Yeah. I would not use it. Because it's got too much horsepower, right?

**Dave Jones:** It's got too much horsepower. The fan is like a wind tunnel. It sounds like a bloody wind tunnel, right? And the horrible touchscreen Windows XP interface just makes you want to, you know, go out and kill yourself. It's horrible.

**Chris Gammell:** Yeah. You know, it's interesting because the high-cost ones are really low volume. So you've got to figure that they don't get as much optimization as like a, you know, a low-cost Rigol. Well, that's really low cost. But even just a high-run kind of piece of test equipment gets the most attention probably because they get the most regular Joes kind of being like, oh, and why doesn't it, you know, do this and that when I touch the screen? Yeah. Yeah, yeah, yeah.

**Dave Jones:** And the people who design the thing, the systems engineers who design this beast, you know, they go, well, we're not going to waste our time making it user-friendly. Jeez, you know, we need to get the performance is the only thing that matters, you know, the performance and the features. Yeah, that's it, you know. And it's got all these weird, you know, and it's not just, this oscilloscope's not designed just to get a waveform on the screen. It's designed to do automated analysis of serial, you know, signals. Yeah, like you use them in like these standards labs where you, you know, if you're designing some sort of high-speed SATA hard drive or something like that, you know, you've got to make sure it meets the SATA spec and stuff like that. And that's the, this is the kind of machine that has software. It's probably not built in. It's probably got to pay a lot extra for it, but it will, you know, analyze and make sure it meets all the spec, you know, it'll analyze all the jitter and, you know, take 10 billion measurements and make sure it's all. That's insane. I'm not kidding. No, no, no, that's. Yeah. I've had to do SATA testing before, but we used our own in-house software to run jitter, you know, and I'd leave the thing running for days, you know. Really? And it would just keep sampling and measuring that jitter to make sure it's, you know, it's all good. And giving you that, you know, that error rate figure, you know. Yeah. And that's what you care about.

**Chris Gammell:** I talked to a guy that actually used to design the oscillators that go into that thing. Because you think about, how many, how big is the sample rate for that?

**Dave Jones:** 13 gig, ah, sorry, 40 gig sample per second. 40 gig, yeah. Each channel.

**Chris Gammell:** Yeah, you figure you have to have a very high rate of, you know, oscillator. And it's got to be really precise too. And so you start getting into these crazy physics. I mean, like, itria-coded, I'm probably totally wrong about that even.

**Dave Jones:** Unobtainium-doped. Yeah. That kind of thing. Yeah. Yeah, transistors, yeah.

**Chris Gammell:** They're definitely working with, like, PhD students, you know, like in high-end research kind of stuff.

**Dave Jones:** Yep. And you can't just go to DigiKey and buy these parts, right? Oh, no. They're all hand-rolled, right?

**Chris Gammell:** Yeah. Yeah, you got to, I mean, and that's really a competitive advantage done too, right? You got to make this crazy stuff. Oh, yeah, of course. Yeah. And then build a scope or a- A scope around it. A signal, signal analyzer around it, whatever. So, yeah, it's crazy. Madness.

**Dave Jones:** And that's why they cost so much. Because, you know, each, you know, input transistor is, you know, manufactured by nude virgins with, you know, with Oompa Loompas dancing around singing songs, you know. And then each one's individually tweaked by the ghost of, you know, Bob Pease, you know, while he's rubbing his beard, right? That's nice. I like that. Yeah.

**Chris Gammell:** It's a heck of a visual.

**Dave Jones:** Right.

**Chris Gammell:** An audio picture. Yeah.

**Dave Jones:** Oh, boy.

**Chris Gammell:** You know, the good thing about that is that you don't feel jealous, you know. I'm not jealous of that because I don't have anything I need to measure that with. I mean, like, 50 megahertz scope, that's fine with me. I don't care. You know, like, even that's probably more than I'm doing.

**Dave Jones:** Well, I have a nice 500 is, you know. Yeah, I mean, it's good for dig.

**Chris Gammell:** It's good for digital stuff, but I mean, like, I mean, for how much I use it here at home, it's like, well. Yeah, yeah, exactly. You know, it's like, when you need it, you can rent it. That's the real thing. Yeah, exactly. And I think a lot of people do that anyways because owning, I don't know, I almost went to work with a company that was doing high-speed transceiver stuff. And, you know, you need that. That was a huge part of their R&D budget was just test equipment. Yeah. And it's rough, man. You got to... I know. And from the business side, it's like, you really got to budget properly. And then, you know, if you're working there, that means you got to sign up for time on the test equipment. I'm sure you've had to do that in the past, right? Oh, yeah. Yep. You know, like, oh, well, 2 o'clock in the morning, it's free. Go ahead.

**Dave Jones:** Oh, man. Have you ever been in a company that just, you know, it pisses money away like there's no tomorrow on these rentals? Like, you'll rent it because they actually have it available now, right? You'd need it today, right? And, of course, the supply, especially in Australia, it's probably different in the U.S., but in Australia, right, not many of the suppliers carry stock, right, of, you know, either an obscure bit of test gear or a high-end bit. So, you know, or they've got the loaners out. Somebody else like me has got the loaner, you know, and you can't get it tomorrow. So you go to these rental companies thinking, oh, yeah, we'll just rent it for a couple of days. And then two years later, right, someone from accounts comes in and goes, do we still need this bit of gear? You know, and we've paid for it like a hundred times over.

**Chris Gammell:** If we get rid of this, we can hire more people, right?

**Dave Jones:** Yeah, we can hire more people.

**Chris Gammell:** Like 10 more people. Yeah, exactly.

**Dave Jones:** Yeah. And they wonder where all the budget has been pissed away.

**Chris Gammell:** Right.

**Dave Jones:** Because, you know, it's under some other budget which disappears into the ether, you know, and nobody, everyone forgets about it, you know. And, of course, the machine is still being used because it's here, right? And nobody, your average Joe engineer doesn't care who paid for it, where it came from, or how long we got it for. Right. You know?

**Chris Gammell:** Yeah, it's just a piece of test gear, right? Yeah. He's flipping signals with a switch or something, and he's measuring it.

**Dave Jones:** And there's only one person in the company who knew that was a rental, you know, and they just keep their mouth shut because they don't care, right?

**Chris Gammell:** Right. Exactly. Exactly. Yeah, and, you know, that's why the lease companies exist, too. Oh, they make a fortune. Yeah, they, I mean, they, it looks like a really crappy business to start with, but then, because, you know, they're always having new equipment and everything, and they swap out equipment a lot, and they have a lot of high costs. But then you get, like, a high-end rental like that, you know, it's $1,000, $2,000 a month, and then it just sits there. You know, the contract just keeps getting renewed because of whatever reason. And once you're in somewhere, then it's just cash machine.

**SPEAKER_01:** Goldmine. Cash cow. Moo.

**Chris Gammell:** You can pay, I mean, you can pay the cost. They're probably getting discounts anyways on the test equipment or, you know, I was actually looking at a 3D printer for that kind of thing, and, you know, like, you pay off the thing, and then it's just gravy after that, so. And they're probably financing it, too, you know, they're just taking out loans or whatever, so. Yep. Oh, yeah.

**Dave Jones:** Speaking of 3D printers.

**Chris Gammell:** Yeah.

**Dave Jones:** I'm finally getting my new MakerBot replicator.

**Chris Gammell:** You're getting one.

**Dave Jones:** It's currently in Memphis, Tennessee.

**Chris Gammell:** Really? That's cool.

**Dave Jones:** Yeah. So, we'll see how an out-of-the-box MakerBot goes.

**Chris Gammell:** Oh, that's right, because it ships all together, right?

**Dave Jones:** And Charles from MakerBot just designed this cute-looking case for my microcurrent. It looks really neat, you know, a little low-profile case. Awesome. Got myself a useful little test break. I saw you tweet that earlier.

**Chris Gammell:** Yeah. That's cool.

**Dave Jones:** And then you realize where the hell I was, right? Well. Yes, I did. I was a bit late for today's show, folks.

**Chris Gammell:** That's okay. These things happen. They do. That's cool, though. Yeah, so that's on Thingiverse. We'll link that in. Yep. But yeah, that's great. And just because, you know, I didn't actually realize about the microcurrent to start with that it was actually all just single PCB. I think we probably talked about it since. Right. Yeah, that's cool.

**Dave Jones:** Yeah, I use it as a front panel and the parts are mounted on the back. And I did that for my micro supply as well. And my micro calc, too. I've done it for three different projects. Although the micro supply is changing in that respect. But if you see my prototype, I've flashed around on the videos that I did a couple of years back. Then, yeah, they were all, you know, parts mounted on the back. And it kind of looks groovy, right? Because, of course, all of the tracks, right, can't be on the single-sided. Although it is on the microcurrent because it's so simple, right? So it's a single-sided layout, effectively, right? There's no tracks going on the top half. But a more complicated one like the microcurrent, of course, with, you know, multiple digit displays and all sorts of things, you know, you need tracks to run on the other side. And you don't want to go to a four-layer board and hide the tracks because then you've just killed your cost advantage, right, of going to a, you know, using the one board for your front panel and your components, too. And so you have the tracks going through to the front, but they kind of look funky, you know, when the tracks are integrated with your front panel.

**Chris Gammell:** Yeah.

**Dave Jones:** You know? Yeah. Because, you know, it kind of looks high-techy if you do it right. Like, you can do it wrong. Good funky. And, you know, and yeah, it kind of looks neat, you know, because these tracks are running around on your front panel. Yes.

**Chris Gammell:** I kind of like it. You know, a dope head with veins running through the front. Right, yeah. Yeah, it's really quite neat. I saw that MakerBot was actually at Comic-Con. I saw this funny picture. Yeah, I don't know why. They had a picture of Seth Green, the guy from, you know, like the Austin Power movies. Oh, yeah, yeah. Voices for Family Guy. But yeah, the picture of him. And it's weird thinking about, you know, like where that stuff all gets mashed together. I'm not sure why they were there. I didn't read about it at all. But, you know, just thinking about when that technology actually does interact with larger scale public, how it all works and stuff. You know, it happens a lot at, what's that January conference? It's the CES. Oh, yeah. And that's all gadget stuff. But it's still kind of cool. And with Kickstarter and everything, there's tons of high-profile stuff now anyways. I mean, there's high-profile projects that anyone could buy or support. It's just nuts.

**Dave Jones:** Speaking of Kickstarter.

**Chris Gammell:** Yeah. We actually had a little thing about that, huh?

**Dave Jones:** A mate of mine. Yeah. Marcus Shappie from Hiddlebird Electronics. Yeah. He said, you know, got like a component and kit supply business here in Sydney. And he's done these Ninja Blocks, which you may have heard about.

**Chris Gammell:** I have.

**Dave Jones:** And, yeah, he did the Kickstarter thing, of course. You know, like he's got a friend in the U.S. because Australians can't do the Kickstarter. You need someone. You need an American patsy. You need a front man. Patsy. Yeah. To actually. Right.

**Chris Gammell:** So if you see me with a Kickstarter, you might know where it came from, people.

**Dave Jones:** Right. Exactly. He'll be fishing off his 10%. Yeah. Yeah. 10. Sure. Don't stop there, buddy. Yeah. Yes. And then, yeah, the interest. Right. There's a couple of interesting things here. A is that he used Kickstarter, of course. And he did like 670 of them or something. And he's still making them. Oh, of course. To actually satisfy the orders that rolled in from the Kickstarter. The interesting thing is that he's the case for these Ninja Blocks is actually 3D printed. And his house is apparently full of 3D printers just running 24-7 printing out these cases.

**Chris Gammell:** Yeah. Yeah. Manufacturing revolution takes a while.

**Dave Jones:** It takes a while. Yeah.

**Chris Gammell:** It's not easy. Not easy to do.

**Dave Jones:** Not at all.

**Chris Gammell:** Do you know how long the print takes? I mean.

**Dave Jones:** I don't know. But, well, just based on it, just from the looks of it, each one, I'd say, would take a minimum of 40, 50 minutes. Something. I don't think you'd get away with under half an hour. That thing's in the palm of your hand there. It'd be an hour, probably.

**Chris Gammell:** Oh, yeah. I think more than that, but.

**Dave Jones:** Probably. Yeah.

**Chris Gammell:** I think probably five or six hours for that kind of thing.

**Dave Jones:** Oh, I don't know. I don't think it's that long. I've done fairly large stuff, which takes like two hours. So. All right. You know. Yeah. I am inexperienced in that way. Let's say it's an hour per case. Yeah. You know. It's to fill an order of 675. That's, you know. That's like, you know. Let's say it's a thousand printing hours. Yeah. You know. For one single machine. That doesn't include handling and all the rest of it.

**Chris Gammell:** Right.

**Dave Jones:** Yeah. 3D printed cases. Eh, folks. Not such a good. They look funky.

**Chris Gammell:** Well, I feel like you've already had them, right?

**Dave Jones:** Yeah. I mean, you know, it looks great. It looks really funky. And it does exactly what you want. And they've got little, you know, ninja symbols sort of carved into it. And it does look great. Yeah. But, yeah. From when you've got to actually produce the things.

**Chris Gammell:** Well, you compare it to like an injection mold, right? I mean. Oh, of course. The mold would be really expensive. But once you get them, I mean.

**Dave Jones:** Exactly. It's like 20 cents a thing. You can churn these out for 10 cents a poll. Yeah. You know. And that's the interesting thing. He now has the money to do it. Because he got venture capital funding. Yay. Marcus. Good on you.

**Chris Gammell:** Right. Which is kind of crazy. So it's like. So we should explain the difference here, too. So he did a Kickstarter. He was funded through Kickstarter. He did start the project. And now he had some venture capitalists who are, you know, very important persons, apparently, that, you know, come and say, we want to give you all this money as angels or whatever else. And we're going to get a chunk of your company.

**Dave Jones:** I don't think they came to him. I think he went in search.

**Chris Gammell:** No. He said they came to him in the article.

**Dave Jones:** Oh, did it? Oh, okay. I didn't read the article.

**Chris Gammell:** Because it said he was trying to find funding in Australia first. Right. Okay. And then later, once he got funded, they came in.

**Dave Jones:** Oh, okay. Yeah. Right. So these venture capital angel investing firms, there's tons of them now, apparently, and then they're sniffing around Kickstarter, looking for the next cool thing. Right.

**Chris Gammell:** Yeah. And that really kind of, you know, that's going to have a lot of problems, right? But it also kind of sweetens the deal, too, right? I mean, it's very interesting what could come out of that. I don't know. It did. Yeah.

**Dave Jones:** And I tweeted him about it, and he tweeted back saying, oh, now it's a lot of work, you know? Now I've got to... Because he's got to run his Little Bird Electronics as well as running this Ninja Block startup now. It's like, be careful what you wish for.

**Chris Gammell:** Right. Yeah, exactly. And actually, Nathan, Nathan Seidel from SparkFun, he wrote about that. He wrote about the... Oh, did he? What he called... Well, he actually talked about it at the Open Source Hardware Convention. And in his talk, he called it the pit of despair. And then he just recently posted an article about it as well.

**Dave Jones:** Oh, okay. We'll have to link that in.

**Chris Gammell:** Yes, definitely. And basically, he said there's like three levels. He said there's like the little one-offs, right? Where maybe you're on Kickstarter, and you do like a little device, and you just barely fund it. Then there's the really successful, like the Pebble Watch was just $10 million. Right. And then you quit your job, and that's your full-time gig, right? You're basically moving to China, or you're going to try and do it wherever you are. And then he called the middle one the pit of despair. And it's interesting.

**Dave Jones:** It's the pit of despair where you haven't got enough money to hire a team of people to take care of it for you, and then you don't have to worry about it. And where you have to... So you have to do everything, and you're working 24-7, and your marriage falls down, and you... Right. Is that the pit of despair?

**Chris Gammell:** Yeah, that's what he was calling... Yeah. That kind of thing. You're in that middle ground. Like an overwhelming kind of thing, right? Yeah. And ironically, he used one of our past guests as an example of the pit of despair. He used Ian Danaher and Nonalith Labs. Oh, okay. And yeah. So actually, Ian is posting a response tonight, which I got a little preview to. But basically, he's calling it the pit of opportunity, because basically, they launched their company out of it. And it's a lot of hard work, but I was kind of talking back and forth with him before, and I brought up something that I had heard somewhere else. It's like, well, they call it hardware because it's hard, right? I mean, like... Of course. That is the basis behind it. If you have a product, it's not easy to put stuff together. And Ian's writing about how he knew that, but he did it anyways, and all the learning he got from it anyways. So I don't know. It's a good article. I have a preview of it. So that'll be posted later tonight. I'll post a link to that as well. I think that'll be good as a good dialogue back and forth, kind of these... I wouldn't call them shots across the bow. But, you know, just like, you know, Nathan sees it from SparkFun, right? They see... Of course. He actually talks about it in the article about, you know, they're actually getting people coming to them saying, help me make this kit. Help me make this kit. And, you know, you think about how many people they have to turn down. It's...

**Dave Jones:** I know. It'd be countless numbers. Right.

**Chris Gammell:** I mean, doing a turnkey kind of operation like that, I mean, that's never easy, right? Contract manufacturing is not an easy thing to do. No.

**Dave Jones:** It's a dog of a business, actually. Right. It's not high margin, right? No one wants to give you margin. Exactly.

**Chris Gammell:** Yeah. And because you think about it, you could charge up front, you could charge, you know, high margins up front where you're doing prototypes, right? But then eventually, if there's anyone worth their salt on the business side of things from the people buying these finished goods from a contract manufacturer, they're saying, no, I'm not paying you this much, you know? And then they just thump on them and they threaten them. And that's just what purchasing does, right? They're good at that kind of stuff.

**Dave Jones:** Yeah, that's right.

**Chris Gammell:** Oh, boy. Yeah.

**Dave Jones:** Yeah. Be careful what you wish for. I don't know. Do you know of any... And you start out wanting to help people and then you get inundated, you know? It's like... Well, yeah. I mean... Well, you know, I'm in a positionalist and similar position where I get so many requests for help that I just have to turn everyone down.

**Chris Gammell:** Mm-hmm.

**Dave Jones:** You know, it's just...

**Chris Gammell:** Like once in a while, there might be a rare opportunity, but still, it just gets lost in the noise.

**Dave Jones:** You know? Oh, look, I've got this great opportunity. Can you help me design this product? And you'll... You know, look, we'll give you shares and we'll do this and we'll do that and we'll...

**Chris Gammell:** Right.

**Dave Jones:** You know, and it's like, no, sorry.

**Chris Gammell:** Right. At that point, it's like, I'd rather be a venture capitalist. I'll just give you money. You go figure it out. Yeah, exactly.

**Dave Jones:** I wish I had money to be able to... You know, that'd be great. If I had, you know, 50 million bucks, I'd love to... Yeah, if you were good at, like, recognizing... You know, be able to help people out with, you know, invest. I can see that. I can see why these, you know, people who make these fortunes in their dot-com, you know, start up and happen to sell out at the right time, they're worth 100 million bucks. I can see why they do this.

**Chris Gammell:** Yeah.

**Dave Jones:** You know, it'd be fun. That's probably what I'd do if I had this much money. I'd be, you know, that'd be my full-time job as trying to find little, you know, startups to invest in, I think.

**Chris Gammell:** Yeah. Yeah. Now, I saw a thing from Elon Musk who, you know, he started PayPal, and people probably know who he is. But he said he sold PayPal for $180 million. He put $100 million into SpaceX. He put $70 million into Tesla. And then he put $10 million into SolarCity, which is the leasing of solar cells. And he said he had trouble making his rent when he did that.

**Dave Jones:** Yeah, I know.

**Chris Gammell:** That's a sign of a crazy person. Like, I love that. That is awesome.

**Dave Jones:** I just watched the other night Revenge of the electric car. Oh, yeah? And he's in it. They actually follow him around with the camera. And when Tesla's actually almost going under, like, they actually let the cameras into the room where he was... He had to call in all the people who had pre-ordered these Teslas, right? Yeah. They each paid, like, $100,000 up front. Wow. And then he had to go in and tell them, look, we need more money. Otherwise, the company's going under, and you won't get your cars. And...

**Chris Gammell:** That is going to be a bad day.

**Dave Jones:** That is a bad day. And he was saying, he was sitting there, and you could see the look of stress on his face. And he's going, I just had to transfer $2 million from my account so that we could pay the wages. And now I'm practically broken. You know, that was my last $2 million or something like that. You know, that he just put into Tesla to pay the wages. I know. That is so awesome. And you could see the stress on his face, and it's like, oh, man. And he was going through a divorce at the time, and he had four kids, and he was trying to juggle SpaceX as well. And he's, you know, telling everyone at Tesla, look, you know, call me at 2 a.m. in the morning. I don't care. You know, look, we have to get these cars out. And he's going around inspecting each one of the cars personally. Oh, man. That's killer. They had so many problems. Anyway, great doco. If you want to watch it, I'm sure you'll love it, Chris. Oh, yeah.

**Chris Gammell:** I bet I would. I would love to get him on the show sometime. So if anyone has any connection at all, if you know anybody.

**Dave Jones:** This man will have a free hour. Yeah, right. Oh, yeah.

**Chris Gammell:** I doubt he does.

**Dave Jones:** I'm sure he would love to be on, you know, if he. I'm sure we could. Yeah, I think he digs into it. If he had a free hour.

**Chris Gammell:** Yeah. Or really anyone from Tesla, too. That would just be interesting to hear about the car. But, yeah. And if anyone knows, let us know.

**Dave Jones:** If anyone's got you right. If anyone thinks you can be on the car.

**Chris Gammell:** I do have one former co-worker that works there now. I'll have to give him a shot. Okay. Right. Right. Yeah, actually, there was a bet that went on, too, about the – because Tesla just released their Model S, which is their sedan. And so it's like half the price of the Sportster and yada, yada, yada. And he made a bet with someone. He said – it was a journalist. And the journalist said, you know, if I win, you have to donate – or I think Elon said that if I win, you have to donate a million dollars. And the other way around, then he realized it was a journalist. He said, okay, if you lose, you have to donate a thousand dollars. And so the journalist signed up losing because they got the car out on time and it actually works. Nice. Yeah. It's a slick-looking car, too. It's, I guess, 300 miles. That's the crazy thing. It's like –

**Dave Jones:** Oh, that's awesome. But have they actually produced it? Because that was the problem with the Tesla. They just underestimated how hard it was to actually manufacture a car. You know? They could make their prototypes, no problems, but mass manufacturing almost killed them. I know.

**Chris Gammell:** We're complaining about boards and all this and that. Yeah, I know. Exactly. Oh, jeez. You know, like, yeah, physical goods is very difficult to make. Yeah.

**Dave Jones:** They're an incredibly – a car is an incredibly complex machine, especially one that, you know, people expect to look and work like the latest Japanese cars, you know? Right. They expect them to be perfection and – And safe and everything. Yeah, they have to pass all the regulations. And tech and all – every single part in there, polished and – Yeah.

**Chris Gammell:** And plus, if you're paying 50 grand or 100 grand, you want it to be super fancy inside. So, you know, like, you probably spend all the time working on the drivetrain and all the important stuff. And then people are like, oh, I'm paying 100 grand. I need it to have infotainment systems.

**Dave Jones:** Yep.

**Chris Gammell:** Barf. That's right. I hate that word so much.

**Dave Jones:** There was this funny point in this doco where Elon's in the factory inspecting each car because each car had some sort of problem with it, you know? And he's inspecting this one and talking to the guy who was trying to fix it, you know? And, you know, he was saying, oh, look, just – yeah, something wrong with the drivetrain. Oh, look, just rip it out and put in a new one. We need to ship this damn thing. And then there was some guy he hadn't met. He was standing nearby and he said, that's my car. And Elon looked around and went, that's your car, is it? Oh, right. Well, you've just heard from the top. There you go. We're going to put you in a new drive shaft and you'll have it tomorrow. And then they showed the, you know, the truck delivering his car tomorrow. Oh, yeah. And it was like, oh, man. How could you do that? How could you, you know, try to run SpaceX as well as trying to – individually inspect every car that goes out the line? It's just – the guy did not sleep clearly. Yeah. Unbelievable.

**Chris Gammell:** I'm not going to complain anymore.

**Dave Jones:** Anyway, the guy has my utmost respect. Yeah, me too.

**Chris Gammell:** And plus, I mean, they modeled Iron Man off of him, right? Tony Stark. Yeah, they did. That's pretty cool.

**Dave Jones:** Andy had a cameo in it. He did. In the second one, yeah. In the second one, that's right. So anyway, we've diverged from Marcus's little startup. Oh, yeah. Yeah, he got like a million bucks or something, which does sound like a lot. But in the end, folks, it's not once you pay your own wages and maybe the wages of one or two others and then you pay for molds at 50,000 bucks a pop or something. You know, the mold to do this little ninja block, which I'm sure is what the money's for, you know, really is to work – A, work on it, hire people to work on it and B, you know, trying to get this thing mass produced because, you know, they can't keep 3D printing the things. Right.

**Chris Gammell:** Right.

**Dave Jones:** You know?

**Chris Gammell:** Yeah, you think about the cost of people, right? I mean, I never really got that either, but I actually sat in with an upper-level manager at one point. They were just kind of explaining budgets and stuff like that. And they said, you know, like, you think about, you know, top-end engineer, right, maybe making $100,000 in the Midwest, you know, because that's kind of top-end around here. Yeah. And, you know, you take that and then you add on healthcare and you add on all the benefits and everything like that and even their, like, bench equipment in a year. And they say – they estimate it like $150,000, $200,000 per person. And at a million dollars, that's five people for a year. That's nothing else. I mean, you don't get anything else at that point. No, no, no.

**Dave Jones:** You get no molds. You get no parts. You get no nothing.

**Chris Gammell:** Right. Yeah. You don't realize how much money – people are almost always one of the biggest costs. I mean, like, NRE kind of stuff, like molds and, you know, like, for early-run protos is a significant cost and test equipment is a big cost. But, man, like, people – people's it. That's where the good stuff comes from.

**Dave Jones:** That's why they lay off people and they don't lay off equipment. That's right. Yeah. Yeah. That's what happens.

**Chris Gammell:** Right. Yeah. Well, Ninja blocks are cool, though. These are – so the Ninja blocks are sensor-based stuff, right? And –

**Dave Jones:** Well, yes. Well, the idea is you can hook, yeah, any sort of sensor up to them and then they connect to the cloud.

**Chris Gammell:** Right. Yeah, and they're based on the BeagleBone, correct?

**Dave Jones:** Something like that. They're based – yes. Yes, I think it is based on that. Because I think they had them at MakerFair. So, obviously, they won't be using the BeagleBone. They'll be rolling their own because that's open source. Right, right. So, they'll be able to just roll their – simply roll their own and – Right. Yep. But, of course, they will have to give back. Yeah. You know, these venture capitalists have to understand that, that you have to release all the design files back if you're going to base it on the BeagleBone.

**SPEAKER_01:** Mm-hmm.

**Dave Jones:** You know?

**Chris Gammell:** Yeah, that's got to be an interesting conversation when, you know, like you have investors who are like, well, we gave you all this money, so where's our money? It's like, well – Where's our patents? Yeah, exactly. Yeah, exactly.

**Dave Jones:** We have to set aside 100 grand to get this patent. Where's the – what? We can't patent it? Yep. Are you kidding me? Well, we can trademark the name. That's about it. You know?

**Chris Gammell:** Yeah. Oh, boy. That might be – I'm guessing they probably brought that up at the front, you know, like – Yeah, probably. Give us as much money as you want, but it might be a while.

**Dave Jones:** And I'm sure, you know, I'm sure the manufacturing is going to move out of Marcus's bedroom now into – Oh, yeah.

**SPEAKER_01:** Yeah.

**Dave Jones:** Into China, I'm sure, because they have to produce these things, mass volume and low cost, because that's the only way it's going to take off, you know, because that's the idea, is that this is almost a consumer-level device. That's why these venture capitalists smell blood, right? It's because, yeah, there's, you know, that huge potential to be – it'll be the next Christmas gift everyone wants, you know? Right. It'll be the next, you know, Tickle Me Elmo. Yep. All right. So – Hmm. Oh, boy. There's actually one other – Anyway, good luck, Marcus.

**Chris Gammell:** Oh, no, that's not going to work. Never mind. So, yeah, speaking of things being made, did you see that link I posted about how capacitors – ceramic capacitors are made?

**Dave Jones:** No, I didn't. I shared a link. Yeah, I found this really – And I'll look at it now.

**Chris Gammell:** Really interesting article from Johnson Dielectric, so I can only assume that they make – they make capacitors, which is – yay, their marketing's working. Haven't heard of them. I haven't either, but maybe they just make the dielectrics and then sell them today. Oh, right.

**Dave Jones:** Okay. Got it.

**Chris Gammell:** But, yeah, they go through the whole process of, like, how they actually put it all together. And, you know, this is another – this is how the sauce is made kind of thing, right? You don't really need to know how this is happening, but it's actually – it's pretty interesting. It's a screen printing process, and then there's, like, a ceramic powder and slurry, and then they kind of just pour it into molds, and then they actually, like, cut it up. You know, like, I never would have thought that that's – they cut it up, and then they, you know, they laminate layers. They push this goop into there, and then they – Goop. Yeah, the goop. Technical term. Right. Actually, no, no, no. They lay the goop down first in layers, sorry. And then they take these sheets, they laminate them all together, and then they cut them up. So it's actually – you'd actually see layers of this stuff, right? You know, it's like – and then they actually cap the end, and they bake them out. I don't know. It's pretty cool. I've just – I never even thought about it. You know, it's like, oh, well, they just – No, it's – They have some process, right?

**Dave Jones:** But you can just imagine the trial and error which went into, you know, doing that and trying to get it right and trying to perfect it. Not only the manufacturing process, but the actual technical side of actually, you know, getting the performance you wanted as well. It's just, you know, so much trial and error.

**Chris Gammell:** And then you start playing with, you know, the chemistries and stuff. Like, I've noticed lately. I've been doing stuff with, like, 0603s or 402s, and I've been trying to see how much I can get in – you know, you can actually get, like, a 10 microfarad – I think it was an 0402, but it was like a –

**Dave Jones:** I think you can get a 10 microfarad.

**Chris Gammell:** It's like a 3-volt rated capacitor. Oh, yeah. It's a very low voltage. Yeah.

**Dave Jones:** It's for, like – So the dielectric thickness is, like, you know, half a bee's dick. Right. Yeah, exactly. It's tiny.

**Chris Gammell:** Yeah. And it's for, like, decoupling right below a chip or something, right? Yeah, yeah. That's the reason you're doing it. But, I mean, I guess if you're using, like, 010 halves or however you say that, you know, there's 0201 and then the next one down is – how do you say it? You say 010 not 5? I don't work that low, so, you know. Yeah, I've seen – you know, you see it more on consumer level stuff. Yep. I mean, definitely there. I mean, I was looking at some teardowns of the new Google stuff that just got released, like the one they worked on with Asus, the pad, the – what are they calling it? The Nexus 7 pad. Yep. That was pretty cool. And you just – these boards are just ridiculously small. You know, just how much – it's all battery, basically. It's all battery and screen now. So now you get – Yeah, yeah, exactly. You get, like, the outside edge. Whatever the battery isn't now. Right. You get that for your boards and there's not much in there, you know. I mean, there's a ton in there, but it's all mostly on silicon now. It's all integrated Broadcom chips and everything.

**Dave Jones:** But the thing is you don't want to go down to those, you know, those level components unless you absolutely have to because the yield, you know, the machines, you've got to use the top-line machines and the yield is trying to perfect it to get it right. It's just horrid. Right. You know, you're really creating a lot of trouble for yourself. So only if you absolutely have to. Right. Otherwise stick with 0402 or something, folks, really.

**Chris Gammell:** Oh, yeah, and even that. I mean, like, for rework and stuff, like, that starts – you definitely need a microscope. Yeah.

**Dave Jones:** Well, there's a bit of a machine – well, I think we talked about this before. There's a bit of a jump between an 0603. Every pick-and-place machine will do 0603 as a minimum. But then there's a bit of a jump to the 0402s. Not all of them can do that. And then you've got to have the special heads to do it and, you know, your yield's not as great. So even that jump from 0603 to 0402 can have consequences in your manufacturing. So, you know, if you don't need to go that low, don't.

**Chris Gammell:** Oh, yeah.

**Dave Jones:** Stick to 0603.

**Chris Gammell:** Are you doing mostly 0603 these days?

**Dave Jones:** I do 0603 for everything as standard. Yeah. Yeah. I'm moving to a – And then if I need, like, higher power or something, I'll go to 1206 or 0805. Like, if I need my 10 mic cap, for example, then I'll go to 0805 because then you'll be able to get, you know, a cheaper one in the larger package. Yeah. That's a good tradeoff.

**Chris Gammell:** Definitely. And, yeah, you know, I'm going to a real – the stuff I'm working on is really space-constrained these days. And so everything's 0402. I don't think I'm going to go lower than – I don't think 0201 is really necessary.

**Dave Jones:** No, it's not. It's not worth it unless you're doing a hearing aid or, you know, something like that. Right.

**Chris Gammell:** And, you know, the problem with all this stuff, though, is actually – so I'm actually pulling in these new parts. You know, this thing I'm working on, it's like all the previous stuff that's at my company has not been that. It's been larger stuff. So I actually have to register all this stuff. Through all. Well, it's not through all. But, you know, it was Keithley, man. Well, some of the old stuff, yeah, Keithley, I guess. But, no, but, you know, it's interesting, you know, dealing with the engineering, like the parts side of things, like the registration stuff. Do you do that now at all for your stuff? I mean, how are you actually – when you're placing a new component, are you just, you know, doing it at the time when you print out your bomb? You're just finally registering parts and figuring out what you'll need? When do you do that personally?

**Dave Jones:** It's ad hoc. It's a real mess. I need to automate this better. But, you know, yeah, new parts is a pain in the ass. But you've got to. Every new design seems like it needs, you know, 10, 20 new parts on it, you know, that I don't have in my library. So I've got to create the footprint. I've got to create the schematic. Then I manually insert it in my bomb spreadsheet. I don't have, you know, my CAD program linked to my bomb and generate it that way. I know I should, but, you know. Oh, you don't have it at the end? No. You just crap it out at the end? Well, no, I've got a manual spreadsheet, which I have to keep up to date. I don't actually sync them.

**SPEAKER_01:** Oh.

**Dave Jones:** Which is, you know, well, I manually sync them at the end. What are you using?

**Chris Gammell:** Are you using DipTrace these days?

**Dave Jones:** No, I'm still using Altium, unfortunately.

**Chris Gammell:** So Altium has like a library manager that I've been using.

**Dave Jones:** Oh, yeah, Altium's got advanced tools to take care of this shit. But, you know, I just have never gotten to the point where I've needed to be invested enough to actually, you know, to do the upfront work to make all that seamless.

**Chris Gammell:** Yeah, that's the exact same problem I'm looking at is like, because it is so much and getting it all hooked up, you basically, you need someone to do that full time for you, basically.

**Dave Jones:** Exactly. If somebody else takes care of it, fine.

**Chris Gammell:** Right. And that's, I mean, like we talked about earlier, that's, you know, if you're a company, that's 200 grants. You really got to need that. And oftentimes it's just like, you tell your engineers, no, no, you can handle that. Go ahead. You're fine.

**Dave Jones:** And I don't do enough designs and the designs aren't hugely complex enough to warrant it, really. So I just keep limping along, you know. Right, exactly. Wishing that I had some automated system. Cursing the whole time, right? Yeah, exactly. Yeah. I know. And that's what you do. But sadly, that's what probably most people do. Oh, yeah.

**Chris Gammell:** Yeah, I don't doubt it. And, you know, I was complaining about it in my work and basically, you know, what my mentor said to me, he's like, well, just connect to the dots. Come on, man. Just put the stuff down. Connect the dots. You'll be fine. Just get it done. It was pretty funny. Oh, yeah.

**Dave Jones:** And in the end, that's what, you know, that's what you just end up doing. You just end up doing it all manually. And, you know, yeah, you'll make the odd mistake, but who cares? You just re-spin the board, you know. It's like.

**Chris Gammell:** Yeah, no big deal. I guess we're doing low quantities.

**Dave Jones:** Big as well, you know, getting it all right in your system is not a, you know, not a guarantee that you're going to get your first spin right, especially if you're putting in 10 new parts, you know. That's true. You can goof up there just as, you know, just as well as you can goofing up by doing the manual way. So, you know, it's not a guaranteed success.

**Chris Gammell:** Hmm. Definitely. You can goof anything up, really.

**Dave Jones:** Heck, I've had recently where, you know, footprints are wrong. Like, well, the pinouts in the schematic symbol are wrong. I've gotten them from the official library, right? I found, oh, great, my component's in the library. And then I've realized, oh, it's wrong. You know, it's like, holy crap. You know, if you can't trust the components in the official library, well, you shouldn't. You know, that's the golden rule, right?

**SPEAKER_01:** Yeah.

**Dave Jones:** If the component's in there, it should be double-checked. So that's why companies have blanket rules. Some companies have blanket rules where you do not use components that come from the, you know, Altium library or come from the Eagle library or whatever. You know, you have to do it yourself and then it has to be triple-checked and signed off and, you know.

**Chris Gammell:** Yeah. Paperwork. Yeah. Yeah. Right. So not on the CAD side, but on the component side, actually, one of our listeners wrote on a discussion board about stuff for actually managing your own stock at your house, actually. It's actually called the component organizer. And basically, it's a way to keep track of your, you know, like what parts you have. If you have the data sheet, you know, it links to that, how much you have in stock and everything.

**Dave Jones:** Oh, right. Okay. Yeah. No, I've kind of sort of implemented that in my home thing, but I just gave up. Now I just order on spec. So, you know, if I'm producing another 200 microcurrents, I've got my bomb. I actually went to the trouble to put my bomb into DigiKey. Okay. And here's the advantage of being able and buying all the parts from the one supplier. Right. I buy all my digi, all my parts from DigiKey. Right. Yeah. It's more expensive, but I've actually went to the trouble to put my bomb into DigiKey. And now I just go order 200. Bang. Yeah. And it orders the correct quantity and done. Like it takes me five minutes to order all those parts from DigiKey. And I don't have to worry about it. I know they're the correct type. I know they're the correct number. Everything's fine. You know?

**Chris Gammell:** Have you run into any points where you're like, they're like, oh, well, we don't have those parts now?

**Dave Jones:** No, I haven't. Okay. But it actually tells you that before you go, before you hit the go button, it tells you live in the bomb whether or not I have stock.

**Chris Gammell:** Right, right.

**Dave Jones:** Yeah. Fortunately, I haven't hit that.

**Chris Gammell:** Yeah. I think this is more for, you know, for your home stuff. So if you knew you had like 15, you know, op amps in your house, right?

**Dave Jones:** Oh, God, no.

**Chris Gammell:** Well, I know. But like, yeah. So you knew you had...

**Dave Jones:** Who does that?

**Chris Gammell:** Some people are very...

**Dave Jones:** Okay. You know. Right anal about their parts collections.

**Chris Gammell:** If you were really good at it, you put little weight, you know, transducers inside each of your part bins. And you'd estimate how many are in there and feed it all back.

**Dave Jones:** Well, you'd put barcodes on them and everything. Oh, God. And you'd have inventory, automated inventory systems.

**Chris Gammell:** Your whole life would just be inventory stuff, right?

**Dave Jones:** Well, I'd love to hear from anyone who actually takes that sort of thing seriously. I mean, well, I've just gotten some more parts bins, right, where I'm actually... I'm probably going to sit down one day when I've got some free time and go, right, these are, you know, linear regulators. And I'm going to put all my linear regulators in the linear regulator thing. At the moment, they're spread between different... I keep my components based on the project I worked on.

**Chris Gammell:** Right.

**Dave Jones:** Right. So all the parts for that particular project are in a box. And, you know, so I've got to remember, I've got to keep it up in the gray matter up here where, you know, oh, yeah, I used that switching reg over in that project three years ago and it should be in that box, you know.

**Chris Gammell:** That's good because you don't cannibalize your stock then, right? You won't necessarily be, oh, I want to build this. Now it's...

**Dave Jones:** So there's trade-offs both ways there. It's good that if you want to come back and work on that project, right, you've got all the parts in that one box. But it's bad if you're hacking something and you need that switching regulator chip and you know you've got one somewhere, but where the hell is it?

**Chris Gammell:** Yeah, right, exactly.

**Dave Jones:** You know? Okay. So, yeah, like I like to keep all of the parts for the current projects I'm working on in a box, right? That way, you know, they're all there and, you know, you're done with. But I think once a project's been set aside or it's no longer worked on, I should actually take all the parts out and then put those in my general inventory. Right.

**Chris Gammell:** Yeah.

**Dave Jones:** So, I don't know. It's a tough call.

**Chris Gammell:** Well, once you hire an intern or something, you get the first tax credit.

**Dave Jones:** Yeah. Yeah. There goes $100,000.

**Chris Gammell:** Interns don't cost $200,000. They cost a lot less. Right.

**Dave Jones:** They only cost $20,000 or $30,000, right? No, here, here, the minimum wage is like $30,000 or something, I think. Is it really? Wow. I'm not sure. Well, yeah. Don't quote me on that, but it's, you know, it's certainly, I don't think it's $20,000.

**Chris Gammell:** I mean, around in the U.S., I mean, some interns don't even get paid at all.

**Dave Jones:** Oh, wow.

**Chris Gammell:** See, that's illegal here. No. No, I didn't know. I don't know how they get away with it, actually. I've seen some articles about how that's kind of a crappy practice. I mean, a lot of engineering people, you know, like co-ops, a lot of times you'll get paid. Right. I think, I wouldn't have done a co-op if I didn't get paid, I'll tell you that. Yeah, yeah, of course. Yeah. But, you know, like it's pretty standard for a lot of, even in engineering sometimes, you know, like if it's like a summer internship, sometimes those aren't paid. Usually when they're shorter term kind of things. But a lot of other industries, they definitely don't get paid. You know, like to the point where like marketing interns, they'll go and live in New York, you know, like New York City. Right. Yeah, expensive, right? Right. And it's like, well, some of them take out loans. It's pretty, that's pretty crappy.

**Dave Jones:** Oh, they go and work nights at, you know.

**Chris Gammell:** I guess so, yeah.

**Dave Jones:** Some restaurant somewhere waiting tables. Right. But yeah, it's just seen as a right of... Pay for their free internship.

**Chris Gammell:** Right, exactly. It's just seen as a rite of passage and it's like, well, that's a crappy system. So, yeah.

**Dave Jones:** It's better to self-perpetuating system. Of course it is. Yeah, I do it for free.

**Chris Gammell:** Why don't you do it for free, right?

**Dave Jones:** Yeah, that's right. I pay my dues, you know.

**Chris Gammell:** Right, exactly.

**Dave Jones:** Yep. No, I think that's mostly stamped out here. It's illegal, I think, unless it's some very specific circumstance or something. Yeah, I don't think that's the norm here. Right. Certainly not. Yep. There are probably ways around it, right? If you really wanted to work for free, you probably could. Right, right. You know, yeah.

**Chris Gammell:** I guess it's not under the table if you're not paying, you don't have any taxes to pay. When you're, you just got to show up and be like, oh, what do I want to do today? Okay.

**Dave Jones:** Well, the tax-free threshold here in Australia, I think, is now up to, I think they're going to push it up to like $15,000 or something like that. So you can earn that much money a year and you don't have to even file a tax return.

**Chris Gammell:** Yeah, that's true. Yeah, no, they had that here, I guess, too. Because they used to know I have to when I was younger.

**Dave Jones:** Well, when I was a boy, it started out at like five grand was the tax-free threshold. Yeah. But now I think it's like tripled or something.

**Chris Gammell:** I don't know. Yeah. Kids these days, man. Right? Yeah, I know. Right? I've got these. I'm so old now, man.

**Dave Jones:** Yeah. Man. Jeez, you know, if they can earn 15 grand a year without paying any tax. Jeez, my first job was only 22 or 23,000 a year or something. Really?

**Chris Gammell:** They paid that much back in the Stone Age, huh?

**Dave Jones:** Yeah. Oh, yeah. Yeah, well, they paid me in tablets, you know. Right, of course. Of course. Yeah. Yeah. Stone tablet with, you know, something chiseled out in there.

**Chris Gammell:** Yeah.

**Dave Jones:** IOU, you know. No, they actually paid cash back then, you know. Really? I'm sure we talked about it before. Yes, we did. Yes, we did. Yeah, yeah. Somebody would go to the, somebody would ride shotgun with the secretary who would go to the, who would go to the bank and they'd pick up the, you know, the weekly, I think it was weekly. Yeah. They would pick up the weekly paychecks and it was, you know, cash already sorted by the bank into all the envelopes with your name on it. You know, that was, that was part of the, when banks actually, you know, did some service back then, you know. And, yeah, and you would get your little brown envelope with your pay slip and your cash.

**Chris Gammell:** Yep. Then you go to the bar. Yeah. Oh, boy.

**Dave Jones:** Yep. Those were the days.

**SPEAKER_01:** Mm-hmm.

**Chris Gammell:** Boy. So, we were speaking about parts before and did you see Octopart actually started, one of their interns actually, I think, they came up with a new thing. They have historical pricing now. So, you can see how much a part has cost over time. Nate. Greg, yeah, yeah, there we go. Greg Schickman, Schickman maybe? He said he's working at Octopart this summer as a software engineering intern. So, he actually is the one working on, you know, working on this, I think, maybe a trial thing. So, you can actually go and look at, you know, they use the Atmega324, which is, you know, use a lot of Arduinos. Yeah, I'm looking at that.

**Dave Jones:** And they can see, and you can see the price drop when the Japanese earthquake happened. Yeah. What? I thought the prices would go up.

**Chris Gammell:** I thought so too, but maybe, uh...

**Dave Jones:** What?

**Chris Gammell:** I don't know. Pricing doesn't have to make sense. I mean...

**Dave Jones:** They've got a Renesys part here, and there's a video which I watched the other week, which was the Renesys factory. It's on their YouTube account. And it showed what the aftermath of the earthquake was, and like all their fab lines, you know, and things, all these, you know, expensive machines just tipped over, you know, on the floor, and the roof caved in, and, you know, but they were back up and running in those fabs in like three months.

**Chris Gammell:** Right, yeah. They were a success story, because then it was offset by that thing we talk about two weeks ago with them getting bought and chopped up and everything.

**Dave Jones:** Yep.

**Chris Gammell:** Yeah.

**Dave Jones:** And, uh, boy. Oh, and I found out, by the way, um, it didn't affect their microcontroller being, you know, effectively bought out. Didn't affect their microcontroller division. It's all to do with other divisions. Apparently, the microcontroller one is completely safe. Okay, cool. They don't even know anything's happening, you know, so... Cool. But apparently, they're going to lay off a third of the workforce, but the microcontroller mobs just, you know... Yeah. Nah.

**Chris Gammell:** Well, that's probably their cash cow, right? I mean, that's probably whether... Yeah, yeah, well... Because that's... They're one of the biggest in the world, right?

**Dave Jones:** Uh, they are the biggest microcontroller manufacturer in the world. The biggest. Really? Yes. The biggest. Wow. Yeah, bigger, you know, everyone talks about Atmel and microchip. No, they're not the biggest, you know? Right.

**Chris Gammell:** TI, no. They're not the biggest. It's all volume. It's all in consumer devices and stuff.

**Dave Jones:** It's all in the automotive and the dishwashers and the fridges and, yeah, stuff like that. Yeah. So... Yeah, so this is pretty interesting, though, being able to see the prices.

**Chris Gammell:** I don't know if you'd actually be able to use it as a predictor. You know, like, maybe if you started seeing trends over years and, oh, well, prices start to drop in, you know, March because people are, you know, maybe, you know, because certain products don't do well. But either way, it's interesting. You know, you see... You can see a band that you could really use it as an error band of how much it might go up total, you know, like, really, you'd think prices would go down over time, but that's not necessarily true because, I mean, you could have been using a Atmega 324 six years ago, right? You're like, oh, this is probably going to get cheaper. And then, you know, it's going to get cheaper than, you know, it's going to get cheaper. And, well, demand goes up a little bit.

**Dave Jones:** Is that index adjusted? Is all this stuff index adjusted? So it's, you know, like, it's actually not dollars from 10 years ago. It's actually in today's dollars, kind of. I don't know. You know, has it got that relative adjustment thing based on the CPI and all that?

**Chris Gammell:** Right. I don't think so. Maybe.

**Dave Jones:** Anyway, the price did go up, sorry, due to the Japanese earthquake. All I saw was the end of the graph, which is the big drop, whoosh, down. But, no, it ramped up immediately, like it was flat. And then the earthquake happened and it ramped up from, like, you know, $16 a chip to, you know, $30 a chip or something. And then it lasted for a couple of months and then plummeted. Right.

**Chris Gammell:** I remember I was upset on the show about that because the number one response to that was, you know, all the buyers being like, well, what's going to happen to our supply, right? It was a very predictable response from the buyers. But I was upset that it was very inhumane kind of response, right?

**Dave Jones:** Well, yeah, but, you know, you've got to keep the two separate. No, and I know. Right?

**Chris Gammell:** I've since come to terms with it, but, yeah.

**Dave Jones:** You know, yes.

**Chris Gammell:** I mean, some of the buyers I knew, they were scrambling. They were just, they were going bonkers. Oh, yeah. So. Yeah. Yeah, it's a huge part. You know, like we talk about electronics on the show, but buying the parts is sometimes the hardest thing of it. You know, it's crazy.

**Dave Jones:** And when you've got to, and unfortunately, as a one-man band designer, you've got to take that into account. You know, if you're looking to get on Kickstarter and, you know, following Mark's footsteps and getting, you know, even if you're looking at getting a thousand made, you've got to choose those parts wisely.

**SPEAKER_01:** Yep. Yeah.

**Dave Jones:** Because if you choose the wrong one and you're stuck with a, you know, you're single sourced and you can't second source that sucker and you're stuck with a three-month lead time, you are screwed. Right. You know, you'd have to, you'd almost have to re-spin your board. You'd have to re-spin your design just to get out of, out of the shit you're in.

**Chris Gammell:** Yeah. Are you seeing stuff? See, the thing is, like, I, you know, I've been, I've been talking to people about, you know, single sourcing, multi-sourcing parts lately for these designs I'm doing. And it's like, is it even possible anymore unless you actually degrade the performance of what you're working on? I mean, like, if you're using 7.4 series logic, then yeah, okay, you can get second sources. But, you know, if you're using any kind of A to D or any kind of, you know, like even op amps now, like they're just, they use different packaging.

**Dave Jones:** Well, no, see op amp, you know, well, there is. Yeah, if you go for the weird ass BGA ones or something like that. But, you know, if you're using like, you know, your standard SO8 or SO14 op amp or your, you know, and second source doesn't necessarily mean a different manufacturer, right? A different, you know. Yeah, you're right. There could be different versions. It can mean the same manufacturer, but they've got different performance parts, you know. And yeah, you may be able to get out of the shit by buying the higher performance part. You're paying more for it, but at least, you know, you don't have to wait three months for it because it's available. So you can look at that. Oh, yeah, there's a higher priced option available. I don't like it, but it would get me out of the shit if I had to.

**Chris Gammell:** That's true. Yeah, no, that's a good point. I mean, yeah, I guess, but even still, I mean, I always hear second source and I immediately think of, you know, like chip companies used to do it. They would just straight up copy each other. There was like no, there was no beans about it. It was just, yeah, oh, you're making that part. We're making that now too. We're second source, right? And you just don't see that as much anymore because of patents on footprint technology or on packaging technology and footprints are different. Oh, that's evil. Yeah, that's evil shit. Yeah, it's not going to be. Maybe there's a business opportunity for someone to like, like be the middleman, you know, like doing like a pad reversal of, you know, like just doing little crossover boards where you're just, you know, like rerouting pads. That'd be kind of cool, but I don't know.

**Dave Jones:** Well, that's the other way to do it, but then that sucks ass with SMD, you know?

**Chris Gammell:** That's true, yeah.

**Dave Jones:** But if you go for like a large SO package, say, then you can make an SMD adapter board where you have like the half moon pads on the side of the board and you can mount it flat on the SO footprint and then mount the little tiny pain in the ass BGA package on top, you know, if you had to.

**Chris Gammell:** Well, it seems like it's getting worse with, you know, as manufacturers go into smaller packages. I mean, I know there are standards, it's smaller ones, right? There's like SC70s and everything else and all the SOT23 dash whatever. And I know those are smaller, but it seems like as you get smaller geometries now on the pads, it's just because there's more research in it, it's just they're going non-standard. And I wish there was something we could do to try and force standardization, but I don't know what it is yet, you know, other than I whine at reps every time. I'm like, well, I'd love to see this in a standard pinout and they all chuckle and say, oh yeah, of course, right? Screw you! That's right. I know your game and I don't like it!

**Dave Jones:** Well, that's what you got, you know, that's all you can do is call them out on it and, you know, piss and moan and rant until the cows come home.

**Chris Gammell:** That's what we do around here.

**Dave Jones:** It's like, you know, Milton down, someone stole my stapler, my stapler, you know, but nobody's listening, nobody's listening to me. Oh boy. Yeah. Tragic.

**Chris Gammell:** Yeah. Well, speaking of chip makers, there's actually an interesting link I found on anysilicon.com, which is a new site I'd never heard of before, but actually, yeah, so, you know, like a lot of the people are going, a lot of companies are going to the fab model, right? And we talked about, I complained on here about analog devices going to the fab model. And actually, there's a video that I found of, shoot, what's his name? Bob Dobkin. No, Bob Dobkin. Bob Dobkin. CTO of Linear Tech, right? He's an awesome guy. He's in the same.

**Dave Jones:** And he does lots of videos. Lots of videos.

**Chris Gammell:** He does lots of, he still makes chips. I mean, like, he's awesome. I'd love to get him on the show. Oh, I'd love to get him on the show. But anyways, he talks about that too. And granted, like, you kind of have to read between the lines there because Linear Tech does have their own fab. So they're trying to push that as like, oh, well, we're different now. But he talks about, you know, the same thing of going to foundries now and like with the analog stuff and how that's kind of dicey. So I'm not off my rocker here. I got Bob Dobkin behind me. You know, I sort of kind of know what I'm talking about. But this anysilicon.com, right? The author of the site actually shows a chart of the different foundries out there, right? And there's actually a bunch. There's Cytara. There's Tower Jazz. There's UMC. There's TSMC. There's Dongbu Hitec, right? And then the newest one is actually... Kazuntac. Yeah, right? Is the Global Boundaries. That's actually was... I think that's a shared research base between like AMD and a couple other people, I think. I could be wrong about that. I know they have a new place up in upstate New York because one of my former co-workers works there now. So anyway, this is... You know, like you hear all these names, right? It's like, okay, well, there's foundries and there's foundries. And this thing, though, it's crazy. You look at like the relative business levels, right? Especially over time. And it's just... It's like, you know, you got the little ones and then you get Global Foundries, which is pretty big. And then you get UMC, which is out of... I think that's also out of Taiwan. And I think they might have some stuff in Shanghai. And then you have TSMC. And it's just like TSMC is probably 90% of the business. And it's like, holy crap. Oh, man. So it's a very interesting chart because, you know, you think about... We talked on this on past shows about if you did have to finally throw your design to someone. Well, the reason they're so big is because they're getting all the big boys, right? They're getting the apples and everybody else, right? But so you're never going to get in there. So you might have some luck, but it just shows just how big of a scale difference it is. You know, like, it's insane. It's honestly 90% of the business. So...

**Dave Jones:** Oh, boy.

**Chris Gammell:** But yeah, it's an interesting chart. People should check it out.

**Dave Jones:** You'd have to be mad to go into that business, I think. Semiconductor business. Oh, man.

**Chris Gammell:** Yeah.

**Dave Jones:** Why would you?

**Chris Gammell:** Call me when the garage chip printer's available, right, Dave? Right, yeah. I mean, honestly, like, even then, I mean, it would be like Marcus sitting in my garage printing for four days straight.

**Dave Jones:** You'll be filing each individual chip down, you know? Yeah. Looking through each one through a microscope.

**Chris Gammell:** Yeah, it's tough business, you know? Oh, man. It's not... I don't know why people do it either. I think because it must look good on paper. And, I mean, there is a lot of money to be made, right? Chips aren't going away anytime soon. But, yeah, it's not easy.

**Dave Jones:** Well, some people get off on that sort of thing, you know? They're managing huge, complex, you know, and it doesn't get much more complex than a, you know, than a chip fab, right? Yeah, that's true. In terms of, you know, scale. I mean, actually, what else rivals? Here's an interesting question. What else rivals a chip fab in terms of cost to set up the fab and just the sheer technology and the trickiness to maintain it and run it? You know, the only... Maybe you might talk about, you know, a car manufacturing plant with all their robots to... But it's, you know, I don't think they cost $10 billion to set up, do they?

**Chris Gammell:** No, I don't think so.

**Dave Jones:** To set up, you know, and they've got big, you know? You can walk in there with your big wrench and, you know, your monkey wrench and you can fix anything, right?

**Chris Gammell:** Right, you don't have to worry about dust falling on your car, right? Yeah, exactly. Yeah, you don't need air filtration and everything else.

**Dave Jones:** Yeah, it's probably the most complex business in the world, surely. Manufacturing silicon.

**Chris Gammell:** It's got to be. Yeah.

**Dave Jones:** I don't know anything that rivals it. I'm trying to think about it.

**Chris Gammell:** I mean, like, there's other... There's comparable stuff, right? I mean, like, you think about, like, certain surgeries or like that. I mean, like, healthcare could be said, but I mean...

**Dave Jones:** Well, no, but in the end, in a surgery, you know, you get a wise old guy with... Strokes his grey beard and cuts you open and fixes you, right? With basic, you know, 18th century tools, right? Effectively. Effectively, yeah. You've got a scalpel. You know, have you seen how they cut your chest open to do open heart surgery, right? It's a big sore. Yeah. That's true. Yeah, that's a good point. I mean, it's not some precision freaking laser.

**Chris Gammell:** And ship fabs are a lot cleaner than operating rooms, too, if you didn't know.

**Dave Jones:** Oh, of course. Yeah. You know? Anyone can walk into operating rooms as long as you've got a mask on, you know?

**Chris Gammell:** Right.

**Dave Jones:** Yeah.

**Chris Gammell:** I guess I can't think of any.

**Dave Jones:** I don't think anything rivals it.

**Chris Gammell:** I mean, yeah. Well, I've been there. I mean, I've been on the easier, quote-unquote, easier side of memory, right? I mean, not even on the logic side. And that's 300 steps. I mean, that's... Yeah. I'm really racking my brain. I can't think of it. If people start a thread and discuss forum, and we'll see if anyone knows. I mean, because maybe there's something. But I don't know. No.

**Dave Jones:** I'm betting there's not. Yeah. I'm shooting from the hip and betting there's not.

**Chris Gammell:** No, that's the only way you shoot.

**Dave Jones:** That's right. Yeah.

**Chris Gammell:** Well, speaking of fabs and components, actually, Wired had an article about HP Memoristers. And they're claiming that their Memorister is going to reinvent computer memory by 2014.

**Dave Jones:** That's kind of a tall order, I think. That's pretty close.

**Chris Gammell:** Yeah. It's...

**Dave Jones:** No, I'm sorry. It'll take you at least that long to sort out the production, any production issues, let alone... Right. I mean... Actually, you know, come on.

**Chris Gammell:** Well, they're saying they're two and a half years away. I mean, they're working with people like Global Founders. Tell them he's dreaming. Well, hey, I'd love to see it. But, I mean, the thing is, there's going to be all these entrenched players like the Samsungs with their Flash and the, you know, like, and, you know, magnetic memory, M-RAM and P-RAM and all those others. You know, like, all these Flash and D-RAM manufacturers, they're not going to give up without a fight. So, to the point where they'll even price themselves, they'll try and price the HP out of the market, right? I mean, so it's got to be really cheap. I mean, it's just like what the hard drive manufacturers have done. I mean, hard drives are still around, right? They're... They've been saying for years and years and years, oh, well, SSDs are going to take over, but hard drive manufacturers just keep figuring out. So, I'm sure the Memorister has a ways to go.

**Dave Jones:** Yeah. No, they've got a long way to go because, you know, you can't compete. How long have they been doing Flash RAM, for example? You know?

**Chris Gammell:** Oh, Flash has been around for 20 years, I think.

**Dave Jones:** You cannot compete with that sort of development and refinement. And I'm sure, you know, if they have to, you know, if their, you know, heels are under the fire, I'm sure they, you know, heels are under the fire, they have to, you know, they've got some tricks up their sleeves where they can lower cost, improve yield, yada, yada.

**Chris Gammell:** Yeah.

**Dave Jones:** So, you know, lower profit margins if you have to, as you said, to the death, you know? Oh, yeah.

**Chris Gammell:** Yeah, it's interesting. A quote from this says, development costs at least 10 times as much as research and commercialization costs 10 times as much as development. So, in the end, research, which we think is the most important part, is only 1% of the effort. And, yeah, I'm sure all our listeners feel that pretty hard, right? I mean, no one has the same marketing budget as they do engineering budget.

**Dave Jones:** Have they even produced these things on the scale required? Like, as in, you know, the 10 megabit kind of, you know, like the huge densities required? I mean, it's one thing to do it in the research lab and you've got your 2 kilobyte memory. Woo! But you're not going to take the world on, you know, you're not going to set the world on fire by selling 2 kilobyte chips.

**Chris Gammell:** Right, yeah, you're going to be a real, you know, niche kind of player. Yeah. But they're working, actually, it was Hynex, actually, not UMC or Global Foundries. But, yeah, I think they have some. I knew because it was 08 that they actually had the first ones. And then, you know, they've actually started, I think they've actually started making them. But they said the hardware is going to arrive in 2013. So, we'll see. Right. I don't know.

**Dave Jones:** The mythical engineering sample. Right, right. Yeah, exactly. Yeah. Right. If you've ever gotten engineering samples before. You know. I have not actually. Pre-production samples.

**Chris Gammell:** I have not actually gotten them before.

**Dave Jones:** No, I've used pre-production silicon.

**Chris Gammell:** Yeah? Yeah. For what kind of silicon, though? Like, are we talking, like, microchips or are we talking...

**Dave Jones:** We're talking, yeah, we're talking analog to digital...

**Speaker ?:** Like, linear stuff.

**Dave Jones:** ...analog to digital... Yeah, we're talking analog to digital converters. Okay.

**Chris Gammell:** So, nothing like where it's, uh... You're going to have an errata sheet, like, as long as you're... As long as you're late.

**Dave Jones:** Yeah, exactly. Yeah. I was finding, you know... Oh, you were? Oh, okay. You're used as the guinea pig to find the bugs, you know. Right. Well, I was just thinking logic, you'd have a lot more than... Here I am sitting down recording all the bugs in detail to...

**Chris Gammell:** Really? Why would you do that?

**Dave Jones:** Yeah. I'm just pumping this thing with random data to see what happens to the thing as well. You know, I got to a point where, well, you know, I'm going to force this thing to fail and figure out where it's going to...

**Chris Gammell:** So, I'm doing their job for them. Did you know you'd have to do that going in?

**Dave Jones:** No. It was like, you know... That's killer. ...you had a pre-production data sheet which listed all the nice specs and you think everything's hunky-dory and you get the part and, well, you know... Yeah, not so much. It doesn't quite work as expected. Right, yeah. You know?

**Chris Gammell:** Yeah. Past success is no indication of future success. Is that kind of thing?

**Dave Jones:** Yeah, exactly. Oh, boy.

**Chris Gammell:** Well, we should get running. We should tell people who's on next week. Oh, we should, yes. Speaking of Wired.com, we will be having Chris Anderson, the editor of Wired.com next week and he also runs 3D Robotics, which is the commercial arm of DIY drones and he's running and wrote a bunch of books and actually they just announced another book called 3D Robotics. It's called The Makers, The Next Revolution or something like that. Sweet. He's going to be an awesome guest, I think. I think so. I'm really looking forward. We're going to try... So, I've got to discuss for him.

**Dave Jones:** What did we ask him about?

**Chris Gammell:** Oh, I think electronics.

**Dave Jones:** We're looking to so many...

**Chris Gammell:** Yeah.

**Dave Jones:** Well, we're an electronic show, supposedly, so... Right. Yeah, makes sense.

**Chris Gammell:** And I posted that... I posted a new thread in the discuss forum just for an easy way to people to ask him questions and vote up other questions and stuff like that. But I did say in there, you know, like, yes, he's written all these books on the internet, but I don't think we'll have time to ask about that. You know what?

**Dave Jones:** No, I think we...

**Chris Gammell:** Right. I mean, he's in the maker scene and they run tons of boards, so... I think that's going to be the most interesting things we could ask him because he's done tons of other interviews about the other stuff, so...

**Dave Jones:** Yeah, it's like, you know, imagine if we had, say, the... had on the show the Was, right? Would you ask him about all the Apple stuff? No. Probably not. You know, he's done like a million interviews. Right, exactly. You would sort of ask him about, you know, the electronics.

**Chris Gammell:** Right, exactly. Hobby. What he's doing these days, right?

**Dave Jones:** Yeah. Yeah, exactly. Yeah.

**Chris Gammell:** Cool. So, yeah. Chris will be on next week. I'm really looking forward to that. In the meantime, people can follow us on Twitter, on Facebook, on Google+, and they can rate us on iTunes or any other of the other... Ooh. Yeah. We haven't asked that in a while. That's a new one? Rate us. Yeah, rate us and review us on iTunes. That's really helpful. We really appreciate that when people do that. It takes about two minutes. If you run iTunes... I don't run iTunes, but there's other platforms where you can, you know, rate shows as well if you use Stitcher or anything else like that. So, we really appreciate that when people do it.

**SPEAKER_01:** That's all I got. What about you, Dave? Nah. All right. I'm done. Cool. We'll talk to you next week. See ya.

**Speaker ?:** Bye.
