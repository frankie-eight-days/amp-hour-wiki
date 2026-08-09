---
episode: 256
title: Is This A Show?
url: https://theamphour.com/256-is-this-a-show/
---

**Chris Gammell:** This is the M-Hour Podcast. Recorded July 1st, 2015. Episode 256. With Chris and Alicia White. Is this a show?

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the AEV blog.

**Chris Gammell:** And I'm Chris Gammell of Contextual Electronics.

**Alicia White:** I'm Alicia White of Embedded.fm.

**Chris Gammell:** And I'm Chris White, also of Embedded.fm. The competition is here, Dave. The competition is here.

**Dave Jones:** Should we just mute them now? We have the power, don't we?

**Chris Gammell:** That would be the best prank ever.

**Dave Jones:** Welcome to the show. Mute.

**Chris Gammell:** Yeah, Chris, Alicia, I don't hear any response. We can respond for you. So here we go. I'm recording on this end, so I've got a different copy. So I can make an alternative cut of the podcast. Podcasters!

**Alicia White:** It was the cut that I was worried about. If I start sounding like, and then software is stupid,

**Chris Gammell:** you know, that's not really me, right? Who needs firmware when hardware rocks? Hardware is awesome.

**Dave Jones:** Well, technically, this episode would not be possible if we're running on an 8-bit micro. If we had 8-bit memory, it just wouldn't work.

**Alicia White:** Congratulations on reaching the 9th bit.

**Dave Jones:** Thank you. 8th bit. Yeah, we flipped a bit. 8th bit. Well, it kind of depends on if you count 0 as a show. Technically, this is our 255th show, is it? Mm-hmm. Oh, no, no, it's too big. No, we started from 1, so it is the 256th.

**Chris Gammell:** See, it's always the off-by-one error.

**Dave Jones:** Yeah, it's like, eh. Yeah. I was reading it every time.

**Chris Gammell:** At least, I'm not sure if I was reading your book or Michael Barr's book or someone about, or no, no, there's another, what's the one with the fish on it? There's a C book with a fish on the cover, you know what I'm talking about? No. It might be embedded programming at C. I think, yeah, no, it is that one. And it was just talking about, like, the history of why it was 0 instead of 1. Like, someone had proposed, why not start at 1? But right when, like, when Richie and K... Carnegie. Who was it? Sorry. K and R? Yeah. Yes. Yeah. But, yeah, something about, like, the 0 versus the 1. I don't know. So. This was decided a long time ago, Dave. That's what I'm trying to get to.

**Dave Jones:** Right. Okay. So, what's the conclusion about all that?

**Chris Gammell:** Who cares? We have flipped a bit, right? You're going to pick the wrong thing no matter what. Right, exactly.

**Dave Jones:** Yep. Yep. Yep. Yep. Anyway, we have flipped a bit, I'm sure. Let's just so declare it.

**Chris Gammell:** Yeah. In 10 episodes, or 5 episodes, it won't even matter. So, yeah.

**Alicia White:** So, does this mean it's 5 years worth of episodes?

**Chris Gammell:** In August. In August it is.

**Dave Jones:** Right. We've skipped the odd week, haven't we? Here and there, you know, over Christmas time or something. We just go, ah, bugger it. Couldn't care less. Yep.

**Chris Gammell:** It's close enough. But you guys are pushing their, what, 2, 3 years? No? You guys getting up there?

**Alicia White:** Just over 2. Just over 2. We hit 100, and we do 50 a year. Right. We seem to take 2 weeks off a year.

**Dave Jones:** You must be pulling in the big bucks like we are.

**Alicia White:** Oh, yeah. After talking to Chris at Solid, definitely we're both pulling in about the same big bucks.

**Dave Jones:** Yeah. Podcast pay, folks. Get into the podcasting business.

**Chris Gammell:** Very, very large single dollar bill.

**Dave Jones:** You can make billions. Billions. As Carl Sagan would say.

**Chris Gammell:** We may be the only two podcasts not sponsored by Skr***s though. Right. Or Skr***s.

**Dave Jones:** Or Skr***s. Do you think we can now get them to pay us for that? We'll just mute them out.

**Chris Gammell:** Because we did say all the names. You know, guys, I actually did just get a sponsorship offer from Spatula City. I don't know if I...

**Dave Jones:** I saw the tweets. What's the deal there? I didn't get it. Spatula City! Spatula City! It's just one of these late night ads on TV.

**Chris Gammell:** It's from a movie that I'm surprised you haven't seen. Saddened. What is it? Saddened you haven't seen. Yeah. It's UHF. Oh, the vidiot from UHF.

**Dave Jones:** The vidiot from UHF. That's what it was called. What's the vidiot? I think it must have a different title here in Australia.

**Speaker ?:** Yeah.

**Dave Jones:** Really?

**Alicia White:** It all goes a different direction.

**Dave Jones:** I've always known... Maybe I'm wrong, but I've always known it as the vidiot from UHF. Is it Weird Al? It is the Weird Al movie. Ah, here we go. Internationally. Released internationally as, yes, the vidiot from UHF. So it's only in Yankee land there that's known as just UHF. There you go. Well, yeah.

**Chris Gammell:** You mean where they made the movie?

**Dave Jones:** Yeah, but there is a pretty big planet outside of the US. Yeah. Anyway, everywhere else in the world... Haven't heard of it. Yes, the vidiot from UHF. Ha! I'm right. Yay!

**Chris Gammell:** Do they switch from Spatula City to like Barbie Town?

**Dave Jones:** No, I don't think anything else has changed. No, I don't think any...

**Dave Jones:** Unlike some Australian movies, which are changed for you silly yanks who just don't get stuff. You know, we are... Like The Castle, for example. A classic Australian show. I think it's called The Castle over there as well. And we couldn't talk about our Holden cars, right? So we had to, you know, change the name of the cars in there. Otherwise, you wouldn't know what we're talking about. It's crazy. They actually dubbed in, you know, over the movie to make it more yank friendly.

**Chris Gammell:** Ford.

**Dave Jones:** Yeah, it was... And there's other little things in there that they had to change for you yanks who were scared that you wouldn't get it. So, you know, and it wouldn't be as funny.

**Alicia White:** What was the plot of Crocodile Dundee for you?

**Chris Gammell:** It's just a love story. Right. Just a movie about a knife. Completely normal and accurate drama.

**Dave Jones:** Right, yes. It's not fiction, I'm telling you. The guy is really Crocodile Dundee. I've got one of his knives here in the lab. I opened mail with it.

**Chris Gammell:** We've all seen it, yeah.

**Dave Jones:** Anyway, I think we can... Can we take a vote? The vidiot from UHF is a far better name than just UHF.

**Chris Gammell:** No. Not co-signing.

**Dave Jones:** Can we put that in the... No? Can we put that in the Ampour survey?

**Chris Gammell:** I mean, do you want to put that in the survey?

**Dave Jones:** Yeah.

**Speaker ?:** Why not?

**Chris Gammell:** I mean, I guess two years ago I did put in, you know, what is the chip printer outcome?

**Dave Jones:** Right. And what was the result of that? I can't actually remember.

**Chris Gammell:** It was pretty evenly spread across all levels of delirium. I'm surprised. It will be done in 20 years. Yeah. Yeah. The best thing about surveys is the outliers. Right. Yeah, exactly. Yeah, exactly. Open forms. That's the best thing. You just let people do their thing, and, you know, sometimes you get a page and a half in, like, a little Excel box. You're like, oh. Yeah. Okay.

**Alicia White:** Yes, indeed. People wanted more dance numbers on our show.

**Chris Gammell:** Really? Oh, and so I assume that's on the way?

**Alicia White:** I wondered about the word more. I didn't think there'd been any so far.

**Chris Gammell:** You know, you can hear the jazz hands in your voices. It's just... I'm dancing right now. It's the joy. It's the joy.

**Dave Jones:** Speaking of data, getting data like this, you want to know what I've just got? Every single comment ever posted on my YouTube channel in a spreadsheet. In a searchable, sortable spreadsheet. The data mining that can, you know, how many instances of the word... Good Lord. You know what I'm talking about. Yeah. But, you know, how many death threats did I get? You know, like... I couldn't get, like, all the... There were a couple of programs out there that claimed to download all the YouTube comments, but they're all broken. So I had my cohort here, David, to actually write a little software thing that sucked all the data from the YouTube, you know. And they actually shut him down. They actually shut him down because they thought it was a denial of service attack, you know. So... Oops.

**Chris Gammell:** So is this the sort of thing you... Is this the sort of thing that you read to yourself when you're feeling too good about yourself?

**Dave Jones:** Oh, dude. It's hilarious. When I need to laugh my head off, yeah, search the comments.

**Chris Gammell:** Endless, endless, mindless things from 12-year-olds.

**Speaker ?:** Exactly.

**Dave Jones:** Like, Dave, after he wrote the thing and downloaded all the data, right, we were sitting there looking through it and he went, I bet you nobody has said the word moose. So I searched for the word moose. Sure enough, there's like five people have said the word moose five times in my comments. Like, he just picked that out of random. Sure enough, it's there. So, yeah, I'm going to have fun mining the data for that. Yep.

**Alicia White:** This is a good use for a word cloud. Yeah. Oh, yeah.

**Dave Jones:** Yes, yes. Is there a word cloud, like software I can get where I can just, like, feed it a spreadsheet and it takes care of that for me?

**Alicia White:** You can feed it a word doc, I know, for Word. Right. So you just cut and paste all of your text.

**Chris Gammell:** Okay. That's interesting.

**Alicia White:** I'll send you the link. I'm pretty sure that's what it's called.

**Dave Jones:** Thank you.

**Chris Gammell:** Yeah, we can flatten all The Amp Hour stuff, too.

**Alicia White:** We went to the comments, but you didn't mention, I mean, we talked about the survey, but you didn't actually say that you have a survey going on. This is really hard because, you know, on my show, I have to control all this stuff and make sure we get back to, we have to go through there and make sure we talk about the things we're going to talk about, not just mention and go on. No, no, no.

**Dave Jones:** In the media, in social media, this is called call to action. We must do a call to action, okay? This is the technical term.

**Chris Gammell:** I think this is just Alicia being nice and taking care of us on our own show. Come on, Chris, where's your professionalism? I have none, Dave. Come on. We're having the embedded folks on. This is like a crazy cocktail party, you know? We're just, we're going to play Pictionary the whole time. Or something. But yes, we do have a survey, 2015. We'd love to hear from you. There are blank spaces. Please don't fill them with total garbage. Fill them with real opinions, even if your opinions are not very nice. We'd love to hear from everybody. And yeah, that'd be actually really nice because, you know, we use that just to kind of keep tabs and we can compare notes with the, and you guys did a survey as well, right? We did.

**Alicia White:** We did. It was pretty amusing.

**Chris Gammell:** Yeah.

**Alicia White:** The number of people who aren't hardware and software engineers was surprising. And the number of people who had really strong opinions about things.

**Dave Jones:** Hang on. They're not hardware people and they're not software people. Then why are they listening to an embedded podcast? Sorry. Don't get it.

**Alicia White:** Surely they must. A few were managers. A few were pure software instead of embedded software. But I had a good quarter that were retired. Or dentists. Okay. Or massage therapists. It was really kind of a broad spectrum. Those outliers on the book. I have no idea what it is.

**Chris Gammell:** Massage therapists. That's interesting. Okay. Okay.

**Dave Jones:** Well, actually, I was getting a massage the other day and the guy was so interested in my YouTube channel. He subscribed. So there you go. He knows nothing about engineering or electronics, but he liked my stuff. So he subscribed. He's watching.

**Alicia White:** He will soon. He'll know it at least a little bit.

**Chris Gammell:** Wow. We've had some guests outside the software hardware continuum and probably attracted people who listen to those episodes. Yeah. That's good, too. I mean, right? I mean, like, that's where you're going to find new people that are getting interested in firmware and software and hardware and stuff like that. So, yeah, that's real good. Yeah. So any other weird outliers from your survey, stuff like that? A lot of comments about not having cats back on. Oh, yeah. Yeah. Yeah.

**Alicia White:** It was only the once, but we interviewed our cat. I heard it. It was posted on April Fool's Day, which means it's at least six years before we can do it again.

**Dave Jones:** I was going to say, you've jumped the shark. Okay. But April Fool's, that's cool. Yeah.

**Alicia White:** And it was 20 minutes long. So it wasn't like we really shirked and did a five-minute thing.

**Chris Gammell:** It took only six hours to edit.

**Dave Jones:** Well, I had a really terrible idea for a, well, I think it was me or it might have been somebody else. I don't know, a really terrible idea for an April Fool's thing that I had outsourced the EEV blog to India. So I was going to get, like, an Indian guy to actually sit and do an entire episode and just take the piss completely out of outsourcing, you know. So, yeah. Oops. I don't know how that would have worked out, but it would have been hilarious.

**Chris Gammell:** It would have done something. I think you have to worry about that is if they outdo you. Right, right. So, okay. So we've gone through our craziness so far. What is new in the world of Embedded, guys? I mean, hopefully, if people don't know, Embedded is a podcast. Embedded.fm is a great podcast you guys run. Embedded.fm is a great podcast. And people should be listening. But if they aren't, what have they missed?

**Alicia White:** So many things. Well, we do. It's pretty funny because you have many listeners who listen to both shows. And that was partially because some of them came over after I talked to you a little over a year ago. And we tend to do more business and more art. And education. Education. Surrounding Embedded Hardware and Software. And it's usually, we almost always have a guest. Although we've decided we're going to do every five weeks, it's just going to be Chris and me talking about whatever we talk about.

**Chris Gammell:** Okay.

**Alicia White:** And our guests sometimes are really cool and sometimes are a little awkward. And generally, we want to have fun. So the laughter that you get on The Amp Hour, you'll see on Embedded.fm as well.

**Chris Gammell:** Periodically. All the time. Yeah, you guys. Yeah. And we've had. You guys are cracking up. Yeah. We've had guests. We do. It's a mix of very technical shows and not so technical shows. And that's sort of the way we like it, I think.

**Chris White:** Yeah.

**Chris Gammell:** Just kind of mixing things up. And, you know, we've had everywhere, everything from people talking about management to people talking about low power and microcontroller design.

**Alicia White:** Embedded keywords.

**Dave Jones:** So do you have the same problem that we have in terms of like being able to talk about stuff because it's radio and you want to demonstrate it? Like you want to, you know, you're flapping your arms around or you're holding something and you want to, you know, you're trying to talk about it on radio, on radio, in quote marks, you know, podcast. Yeah. But, you know, it's a visual thing and it just doesn't work.

**Chris Gammell:** Yeah. We've tried that a couple of times to not very much success, I think.

**Alicia White:** Oh, yeah. The time I unboxed the salier. Yes. I liked that, but you hated it.

**Dave Jones:** You unboxed it on the podcast.

**Alicia White:** And plugged it in and described the signals. But then I got lost in looking at the spy protocols.

**Chris Gammell:** Right.

**Alicia White:** It might not have been our best. Red line. I think it was like episode three. Green line.

**Dave Jones:** Now it's moving up. Now it's moving down. I guess it's great for visually impaired people, right? They, I could just listen.

**Chris Gammell:** I wish you guys could see this. I really do.

**Alicia White:** Well, at Solid, though, I got a question about magnetometers and calibrating them. And I wanted a whiteboard there. But on the show, since I know it's radio, we usually manage to skip stuff. And I always fling my hands about when I talk. So that was a different one.

**Chris Gammell:** I think the toughest one for that was we had a very technical episode about Kalman filters. Oh, yeah.

**Alicia White:** Oh, yeah. When Tony came on.

**Chris Gammell:** And that was like a graduate level course in an hour. Yeah.

**Speaker ?:** Yeah.

**Chris Gammell:** Very intense. And I'm not sure it came across that well because you did need kind of a blackboard or something.

**Dave Jones:** Right.

**Alicia White:** You needed to listen to that one two or three times.

**Dave Jones:** And you've got to visualize everything. You know, you've got to probably be experienced enough to visualize everything, too, which might be difficult.

**Alicia White:** Well, when I listen to podcasts, usually when I'm doing something else. Yes. So I try not to make it too, too technical because I, you know, kind of assume somebody's driving or doing chores or running. And I don't want to have to listen to it twice. Right.

**Dave Jones:** You don't want to distract them and cause a death. There's a huge pile up on Interstate 50. Reports on the engineering district. Listening to the Embedded FM podcast.

**Chris Gammell:** At least you can tell you how well I drive when I'm talking about physics or math.

**Alicia White:** We can get lost coming home.

**Dave Jones:** I had so, when I was doing like a drive time rant video, I had so many people actually, you know, tell me, don't do this. Don't do this. We don't want you to die. You know, like, we really care about you. You shouldn't be recording video while you're driving. You shouldn't be talking while you're driving. You should be concentrating, et cetera, et cetera. You know, the safety police come out every time. Yeah. Yeah. Without fail.

**Alicia White:** But driving's special. Driving's that time where you get to think.

**Dave Jones:** Exactly. And if you have someone in the car, you're talking to them anyway, or a song's on the radio, you're singing along. It's like, how's it different, really?

**Chris Gammell:** Yeah. So much of your senses are in autopilot. And to everyone listening right now, blah, blah, blah, blah, blah, blah. Oh, goodness. That was supposed to throw them off. I don't know if that came through. Sorry.

**Alicia White:** Great. Anybody crashes on Highway 85, it's your fault.

**Chris Gammell:** You'll find out on your survey. Right. Yeah. Right, right. Yes, exactly. Current age, dead. We'll get because of you. I really like the embedded show where you guys had the guy on from PayPal. That was a really unexpected show, actually, because it was PayPal. And he was talking about Go, I think, or similar language.

**Alicia White:** Josh.

**Chris Gammell:** Yeah.

**Alicia White:** Yes.

**Chris Gammell:** And Bluetooth, I think, right?

**Alicia White:** He did a really good intro to Bluetooth. Yeah. I didn't even understand how good that intro was until I started working with it myself. Yeah. And I went back and listened to it. And I'm like, oh, he hit all the high points.

**Chris Gammell:** Yeah. I was actually worried about that interview because it did seem like, oh, wait a minute. PayPal? What are we getting here?

**Alicia White:** Well, I need a handler.

**Chris Gammell:** Right. That was the first show we had where they had somebody come along with him and take notes.

**Dave Jones:** Oh, right. Like a corporate. That was a little strange. Yeah.

**Chris Gammell:** Mm-hmm.

**Alicia White:** And the PR person wouldn't let me talk to him directly. So I was like, screw it. He's got a Twitter account. Yeah, right. You could totally talk to him. I don't know why he won't forward my emails along.

**Dave Jones:** Have we had that, Chris? Have we ever approached somebody and like a CEO or something? I have a vague memory of something like that happening.

**Chris Gammell:** Yeah, but they haven't been on yet. So the journey continues. Right.

**Dave Jones:** And we had somebody, didn't we, who shall remain nameless, who wanted an appearance fee, didn't they? It was like, how much will you pay me to do it?

**Chris Gammell:** And it was surprisingly... Let's not name them. And sadly, someone quite classic, unfortunately. Yeah.

**Dave Jones:** Yes, it was somebody who you wouldn't have expected it from, I guess. Yeah, I was quite shocked.

**Chris Gammell:** Yeah, we've never had that one.

**Alicia White:** No, people are usually, either they say, no, I don't have time, or they're very generous with their time. I mean, most people have something they want to talk about, something, if not sell, at least be known for. Yeah. And that's usually enough.

**Chris Gammell:** One of the questions we ask before we start recording is usually, why are you on the show? And the answer is almost universally... We don't ask that, do we, Chris? ...because you asked.

**Dave Jones:** Because you asked, yeah, exactly.

**Alicia White:** I wasn't smart enough to say no. That was the other one.

**Chris Gammell:** I heard there would be punch and pie. No punch and pie? I was told there would be cake. Yeah.

**Alicia White:** Nate said that we wouldn't... That was the only way he could get us to feed him dinner, so that was sort of tough. No, I would have fed you anyway. This was all just fun.

**Chris Gammell:** In-house guests, do you make people dinner? Is that part of the deal? No, let's not start that rumor. Because I could be on your show anytime I'm in.

**Alicia White:** There's only one person, and he was coming to dinner first.

**Chris Gammell:** Okay. Okay. Fine. No dinner.

**Alicia White:** I make pizza, and that's really all.

**Chris Gammell:** Sleepy for a and pillow thoughts? Stay up till 2.30 in the morning talking about it.

**Alicia White:** No, thanks. I sleep in.

**Chris Gammell:** So is this the show?

**Alicia White:** Yeah, this is the show. Oh, okay.

**Dave Jones:** It is. This right here? Aren't we supposed to be arguing about switch debouncing? We are.

**Alicia White:** This right here. Yes, switch debouncing should be done in hardware. My processor has better things to do than to fix your stupid broken hardware.

**Chris Gammell:** Ah, but what if you don't want to go back to the hardware engineer and say, I don't like the way you're doing it? Screw switch debouncing.

**Dave Jones:** It's too overrated.

**Chris Gammell:** Screw it. I like that. Why don't they build it into the switch? That's what I want to know.

**Alicia White:** That'll look great on a keyboard.

**Dave Jones:** Oh, God, we can have, yes, we'll have an Internet of Things switch that, you know, debounces via the cloud. What do you think?

**Chris White:** Are you stealing my joke, man?

**Chris Gammell:** I think there's records of that joke. I think there are. There's Twitter records.

**Alicia White:** There's no records of what time this recorded.

**Chris Gammell:** Right, that's true.

**Dave Jones:** Really?

**Chris Gammell:** Yeah.

**Dave Jones:** Okay, right. So I'm not the first to, I'm just devastated. I'm not the first to think of a cloud bounce, a cloud switch debouncer. That's so wrong. That could have been the next April Fool's joke video. We could have made a, you know, build it into a little surface mount tactile switch, you know?

**Alicia White:** There are still lots of Internet of Things you can make fun of. You know, the 555 of Internet-based cloud thing.

**Chris Gammell:** Wait, is that really a thing?

**Dave Jones:** I haven't seen that. Is that a thing?

**Alicia White:** I just made it up.

**Dave Jones:** Oh, it should be a thing. Can I invest in this somehow?

**Chris Gammell:** It oscillates on the Internet?

**Alicia White:** Kickstarter going up today.

**Chris Gammell:** So, speaking of the Internet of Things and at the risk of changing topics to something serious. Okay. No, please do. I'm sorry. This is a show, right? Yeah. This is not the free recording. This is just... You were critical at Solid. Yes. Is that it? Solid Con.

**Alicia White:** Solid Con. O'Reilly, San Francisco, last week.

**Chris Gammell:** You guys talk about it. Alicia, is this what having a producer is like? I met him there last year. Where it's just like the producer just says, how about you talk about?

**Dave Jones:** Sometimes he tells me things like that.

**Chris Gammell:** Okay.

**Dave Jones:** I love this. Like, slip your note.

**Chris Gammell:** Usually it's over IM.

**Dave Jones:** Right.

**Alicia White:** You guys made fun of me because you thought I was telling Christopher what to do. Now you know which way it really goes. He's trying not to laugh. He's really trying not to laugh. I wish I had timed that for when he was taking a drink.

**Chris Gammell:** Yeah, spit take. But yeah, so we got to see each other. It was solid.

**Dave Jones:** And that was great. Yeah, come on. So what happened?

**Chris Gammell:** Oh, go ahead.

**Dave Jones:** What is Solid Con for those who don't know? And I don't really know what's there. I don't know.

**Alicia White:** I haven't the faintest. Not really. I mean, it was...

**Dave Jones:** Even though you went.

**Alicia White:** Nominally, the Conference for Hardware Software and the Internet of Things, which doesn't explain why one of the keynotes was a race car driver. Another of the keynotes was a chemist from Wrigley about how to do bubble gum. And there was a whole track on biology.

**Chris Gammell:** Yeah, of course.

**Alicia White:** It was sort of a random conference.

**Chris Gammell:** Wasn't there an Internet-connected pot plant?

**Alicia White:** That was the thing. I went up and said, so BLE and plants is becoming really, really popular and sort of ubiquitous. How is your startup? Because they were in a little startup competition thing. How is yours different? And he said, we focus only on cannabis.

**Chris Gammell:** Future's weird.

**Dave Jones:** This is like the TED conference of the hardware world, is it? Is that what it... Yes. You know, it's just like completely random stuff.

**Alicia White:** It is. I mean, there's manufacturing and there's... But it's all sort of slick and glossier than I expected. From like an engineering conference.

**Dave Jones:** Yeah. So do they have like booths and like a trade show and like... Yes. Is there like a floor where, you know, people, you know, spruik their wares?

**Alicia White:** There's an expert floor and Chris would know more about his wares than I do.

**Dave Jones:** Yes, I was. Oh, that's right. I saw a photo of you on the stand.

**Chris Gammell:** Yes. I was hawking... I was hawking software wares for the hardware folks. So, yeah.

**Dave Jones:** Right.

**Chris Gammell:** It was interesting. I mean, you know, you get people coming by, but... Yeah, it was... I mean, like Lucy said, it was just... It was boring. Admit it, Chris. It was boring. No, it wasn't boring. It was just such a weird mix, you know? Like, and so it was nice. I mean, so there's a lot of great stuff, right? So I got to see a lot of people that I already knew. Like people have been on the show and get to see them again. Like Noah from AKA Media Systems and obviously Alicia. And, you know, a certain person was at home sick, so that wasn't as cool. But he'll be forgiven for that. Sorry. Yeah. And so it was...

**Dave Jones:** Come on. Just admit it. You were sitting there on the stand going, please, somebody come and talk to me. Please. I've got really cool shit. Please. Come on.

**Alicia White:** Mubit wasn't empty all the time. No. I worked by a lot.

**Chris Gammell:** Yeah.

**Alicia White:** I did.

**Chris Gammell:** It was okay. And I mean, like... Giving him the evil eyes. She wants us. Like talking to the startups and everything was fun. I mean, that was cool. And like the... So Seed Studio was there and they were doing some cool stuff. They actually were... They had a pick and place on hand. All right. Yep. It was just eclectic. You know? Okay. Like it was just... There was a bunch of disjointed stuff. But that's kind of the feeling that it all is right now anyways, right? There's platforms everywhere. Like everybody's like, oh, I want to be a platform for the data of Internet of Things. And someone else says, I want to be the software that goes on the platform of the Internet of Things. And then I turn around and I go, and where the hell is the hardware? And no one knew. So... It's out there somewhere though. Hardware.

**Alicia White:** They were like, oh, aren't you just going to like 3D print that?

**Dave Jones:** Yeah. Hardware is just commodity. You know? It's just...

**Chris White:** You just buy a module and, you know, you plug the power in and you're done.

**Alicia White:** Use an Arduino IDE to program it in like Node.js or something.

**Chris White:** Yeah. Wait, what? Yeah.

**Alicia White:** I don't know. There was a guy who wrote a book about, I think, Node.js. Is that a thing?

**Chris Gammell:** It is a thing.

**Alicia White:** It is a thing. He was very excited to tell me about it. Yeah. This is how much I remember.

**Speaker ?:** He was nice.

**Chris Gammell:** Yeah, but I do feel like a lot of the hardware has gone to these little modules, right? Yeah. Yeah. And there's incentive for the hardware sellers to keep doing that, right?

**Dave Jones:** Like, people pay big money to go to this conference?

**Alicia White:** No, most of us spoke there in order to get to go to the conference.

**Dave Jones:** I didn't get a free ticket. Didn't you say, Chris, that it was like a couple of grand or somebody said it was a couple of grand to go?

**Alicia White:** It was. It was like $2,000, $2,500 the day of. There were cheaper tickets earlier. Wow. It was sort of like the Maker Faire for grownups. If you took out all the kids and made it just slightly more professional, but you kept it sort of frantic and crazy and all the weird stuff that might or might not be useful in five years. That was more like Maker Faire without kids than anything else.

**Chris Gammell:** Do you think it'll settle down in a few years? I mean, it's only been around for two years.

**Dave Jones:** I'm sure there was no fire and shit blowing up and stuff like that, right? Right.

**Alicia White:** Well, I mean, there might have been at that booth with the Internet of Things and plants.

**Dave Jones:** Stilt walkers and... Right, right.

**Alicia White:** Well, there was a giant robotic music thing.

**Dave Jones:** Oh, I'm sorry, but you're not selling it to me, you know. I am not sold. Sorry, I'm not going to jump on a plane and pay $2,500 to go to SolidCon.

**Chris Gammell:** Well, maybe that's a better question, though. I mean, like...

**Alicia White:** I had to wonder how many people actually paid to be there. I mean, all the sponsors did.

**Chris Gammell:** Like, well, what are people going to anyways these days, right? Like, what are conferences that people are really into? I just... With the Internet, you know, the Internet has replaced a lot, and I think... I don't think they care. It's a junket. We've replaced a lot of this.

**Dave Jones:** It's a junket. That's it. People aren't going to pay this out of their own pocket, right? It's mostly companies.

**Chris Gammell:** They price it that way because it's companies, yeah.

**Dave Jones:** Yeah, exactly. Companies pay it. It comes out of their educational budget or whatever, you know?

**Chris Gammell:** But who has that anymore?

**Alicia White:** And a week in San Francisco when it was... I mean, I got sunburned. It was really quite warm.

**Chris Gammell:** Yeah.

**Alicia White:** It was nice. And it was beautiful, and it was interesting. I felt like there were a couple of talks I got good information out of.

**Chris Gammell:** Hey, I got dev kits, and I didn't go.

**Dave Jones:** But you didn't get $2,500 worth of value. If you spent your own dosh on this, would you be talking it up as much?

**Alicia White:** No, but that's... I mean, that's the thing. With O'Reilly conferences, the deal is you get a speaker passed. That's the way you go. Of course.

**Dave Jones:** Otherwise, you wouldn't give a toss.

**Alicia White:** It compares to the Embedded Systems Conference, and that's $1,800.

**Dave Jones:** Oh, okay.

**Alicia White:** So it's not totally outrageous.

**Dave Jones:** Right. I mean, usually at these sort of things, like the floor is free. Like if you want to go visit the thing, like over the three days or whatever, it's free. You can just wander around or whatever. But if you want to go to the talks, then usually you've got to buy a package or something. That's how the ones I've been to work.

**Chris Gammell:** This is the same.

**Alicia White:** I don't know if the Expo Hall was free. I guess they had door guards, so... Yeah, it was $45.

**Chris Gammell:** If you shared it on Facebook, it was quote-unquote free. You know, like if you gave them your info, you were worth $45 to them.

**Dave Jones:** Facebook. Fail right there. Anyone who's on Facebook has instantly failed. Facebook is bullshit. And yet companies have to tick it off their KPI, right? Key performance indicate every month. Oh, how much social interaction did we get on Facebook? How many people could we pay? How much money did we have to spend to get people to like our crap on Facebook? It's ridiculous.

**Alicia White:** You know what this is telling me? Stop it, people. We can host and amp our Facebook page. We can have whatever we want on there.

**Chris Gammell:** We have one. It's very...

**Alicia White:** No, you've already got like a Facebook page.

**Dave Jones:** Yeah. Well, I've got a Facebook page for the EEV blog, but I never visit it or read it. I've got a bot that automatically posts to it and posts my videos to there because some people like to get it in there. Facebook feed. Okay. Well, fair enough. But don't comment on there because I don't read it. Sorry, I hate Facebook.

**Alicia White:** I can't stand it. Really? I could never have guessed.

**Dave Jones:** Come on. Somebody back me up.

**Chris Gammell:** I hate Facebook. I hate Facebook. I never go there. Thank you. Somebody once said to me that Facebook is where you go to find out you hate your family and friends. And Twitter is where you go to find out that you like people you don't know.

**Dave Jones:** Oh, that's interesting. Okay. Yep. It actually works out pretty well.

**Alicia White:** Yeah.

**Chris Gammell:** Yeah. Although Twitter has been edging more toward hating people for me.

**Alicia White:** That's what the unfollow button is for.

**Dave Jones:** That's right. Yeah. Right. Yeah. And the block button. Yeah. If people start, you know, spamming your thread thingy, your window thingy with, don't even know what the bloody terms are for these things. It doesn't matter. Your feed or whatever it is. I don't know. Anyway, people start, you know, like 10 posts in a row to your feed and that's all you're seeing is this person on your block. You know, it's great. Problem solved.

**Alicia White:** That's what I do. I unfollow more people than I follow. Soon I will have negative people I follow.

**Speaker ?:** You're right.

**Chris Gammell:** So you guys are, you mentioned you're going to ESC. I heard that on your last show too, but where do people go? I mean, that's the thing. Like I don't, that's what I don't get still. I don't get where our conferences like just not worth it anymore for everything or?

**Chris White:** Yeah. The major ones are, I don't, I don't know.

**Chris Gammell:** ESC, there's ESC, there's solid and there's the smaller ones like Arm Tech Con. Design Con. Design Con. You know, Randy's got a design one too.

**Speaker ?:** Design Con.

**Dave Jones:** Design Con.

**Chris Gammell:** Yep. Yeah. I am going to, I'm going to XOXO this year, I think, up in Portland. What's that? It's like actually an art and technology together. That's more of a cultural. Yeah. This is kind of like South by Southwest except in Portland, right? Right. Yeah. Yeah. So I'm kind of excited about that. I'm not sure.

**Alicia White:** Well, South by Southwest has been, everybody seems to go. I've been wondering if we should.

**Chris Gammell:** It's a, it's like. Is it worth the airfare? A week of, yeah, it's like a week of insanity down there. So I'm not, I don't know personally, but I love Austin. So I used to live there. But I don't necessarily want to go back now. We're during South by. That's the main thing, you know?

**Dave Jones:** Sorry. All this stuff is foreign to me being in Australia. We don't have any of this.

**Chris Gammell:** It's literally foreign to you.

**Dave Jones:** Well, we, well, we have a make affair coming up, you know, mini make affair. It's kind of exciting. You know, that's about as exciting as it gets around here. Oh, we have our logo. You know, we have our yearly show. We have our yearly tech show, but, you know, that's, yeah. It's not huge. It's pretty tiny. If you've seen video of me walking around it. But I have had my own stand, which is kind of exciting. But that won't happen again this year, because this year it's Melbourne. So it alternates between Sydney and Melbourne. There's no way I'm lugging all my crap to Melbourne, you know. So, well, I wouldn't be able to go by plane. And I'd have to, like, load up the car or hire a van or something and, you know, take everything with me and drive to Melbourne. No thanks.

**Alicia White:** But to answer your question, Chris, I don't know that there's a tech conference that I would go to Boston for. Let alone pay $3,000 for. I mean, I don't like to travel. So going somewhere to a conference would be, it'd have to be a good conference.

**Dave Jones:** Yeah.

**Chris Gammell:** Okay. Well, that's good to know.

**Dave Jones:** For example, the only reason I'm going to go to the Melbourne one again this year is because it's the only one. I mean, it's the only thing in Australia. So, you know, why not, right? It's, you know.

**Chris Gammell:** I mean, it's surprising to me that the fact that, like, we're all online, right, and people are hungry to meet the people that they, you know, interact with on Twitter or, you know, podcasts or wherever people do. Facebook, you know, three out of the four people here don't want to. But, you know, most people on Facebook and, yeah, I mean, like, so I don't, that's the thing that I don't understand is, like, there must be a real world place that people want to meet. Burning Man?

**Dave Jones:** Even, like, you know, so, like, anti-social nerds like me. Yeah, like, I actually do like going to these things and actually meeting people and, you know. And fans actually coming up is really good. It's always good.

**Chris Gammell:** Yeah.

**Alicia White:** But I don't feel like I get a lot of knowledge from it. I mean, I've been speaking at them, so I feel like I'm handing knowledge out, but I don't feel like I'm gaining a lot.

**Dave Jones:** No, same here. I don't gain anything from it. It's just a fun thing to do and hang out, you know, and sort of, yeah. No, I don't think I've ever learnt anything going to any of these conferences or, you know, trade shows, really. You know, there's occasional thing I might see, you know, gadget I might see that I haven't seen before and go, oh, that's pretty cool, you know. But, yeah, like, as far as doing it as a, like, financial and time investment for learning, it's, you know, just that aspect is fairly poor, I think.

**Alicia White:** When I switched from software to embedded, I did go to the embedded systems conference sponsored by my company and went to as many sessions as I could. And that was the last time I learned a lot there. Now, mostly, I go and beg for dev kits, which even that I'm not going to do this year.

**Chris Gammell:** Well, and I think a lot of people go to these things because they want to make deals or they're working on a product and they want to go on the show floor and talk to a bunch of people. And that's not, I mean, that's not the business that we're necessarily in.

**Dave Jones:** Right.

**Alicia White:** That's true. The times I've gone with a plan, like, the year I needed these parts.

**Chris Gammell:** So, embedded crew. I mean, like, where are you guys learning stuff these days? I mean, when you're, I mean, obviously, both of you both consult, you both consult still, right? You're both doing projects. What are your main resources these days? I think I learned, me personally, I learned better by doing. So, you know, when I was younger, I learned a lot from books and, you know, school. But afterward, I don't know. I mean, I learned everything by on-the-job training almost after that.

**Alicia White:** Well, and I'd read magazines, Circuit Cellar usually.

**Chris Gammell:** So, trying to keep up now, you know.

**Alicia White:** I don't even read those.

**Chris Gammell:** Follow stuff on the internet. You know, if a new dev kit arrives, I usually spend a few hours messing around with it.

**Alicia White:** Well, the horrible part is sometimes I do my learning by inviting guests on the show. I mean, why do you really think Andreas from At Metal King on the show? Right. I needed to know more about how he was doing his power monitoring.

**Dave Jones:** Yeah. Yeah. The annoying thing about learning is that it takes time, right? And if you're too busy actually doing stuff or producing stuff, like, you just don't have time to learn.

**Chris Gammell:** Well, that's why I try to occasionally do stuff or make something that I wasn't expecting to or just push the boundaries a little bit. So, I do have to learn something while I do my job.

**Alicia White:** See, this is actually convincing me that Solid wasn't that strange and bad. Because I did learn things I didn't expect to. I didn't learn the technologies that I wanted. There was a session about security and Bluetooth and medical. And I was like, okay, this will just solve all sorts of problems for me. And it turned out to have nothing to do with any of those, I think.

**Chris Gammell:** Oh.

**Alicia White:** And it was more of an advertisement for their business. So, it wasn't what I wanted. I wanted something technical. But then listening to Noah Frehant's listening table and how he built this really cool thing. And then he went on to talk about how it works in the real world and how that's a part of his New York Times job. And that was neat. And it made me think of outside the box and outside of the technology into more, I don't want to say humanitarian things, but more applied. More social-oriented things. Real-world type application. And then I went to a session about monitoring the power grid. And that was cool.

**Dave Jones:** I've got to say that I'm, every day, I'm learning something new, actually. Because, you know, I'm, like, reading comments, like, I'm on the forums, there's always something, people are sending me things. And I always see something and learn something almost practically every day. I don't think a day goes by. Just, you know, bumming around the internet, you learn stuff. You know? It's, like, always something new. Yeah, but there's cursory knowledge like that. But in terms of, like, formal learning, like, yeah, and formal learning, right? Like, oh, I'm going to learn how to program in VHDL, right? And, yeah, right, you've got to go spend, you know, weeks and weeks at it, right? To actually do that. Rather than, you know, but, yeah, there's lots of little, you know, but you're always learning little snippets, like, every day. And it's, like, a lot of people ask me that. They go, how do I get my knowledge, you know, how did I get my knowledge in engineering? You know, did you learn, how did you learn all this? And I go, I just, it's my hobby and my job. I've done it every day for the last, you know, well over 30 years. And, yeah, you just pick up stuff every day and you continue to learn every day.

**Alicia White:** I like Twitter for that. I do get, you know, links to blog posts that I wouldn't otherwise see.

**Dave Jones:** Yep. Yep, totally. And then if I see, you know, if I see a real, you know, if I see a crappy product, I'll go and debunk it. And I'll learn a hell of a lot doing that, you know, just going through the process and things like that. And, yeah, almost every video I do, I learn something.

**Chris Gammell:** One of the things I found was that teaching is a really great way to learn because you're really forced to understand things if you're going to tell somebody else how to do it. And mentoring folks and companies.

**Alicia White:** Even writing these blog posts.

**Chris Gammell:** Teaching while in grad school. I understood things after doing that that I realized later I really hadn't understood until I had to teach it to somebody else. So I think, you know, doing the EV blog stuff and contextual electronics, I think you guys have to have honed your knowledge just to prepare for that, right? Yeah, and, I mean, when you're learning, when you're teaching people, I think that, you know, that kind of solidifies it mostly out of social pressure, right? And there is a lot of social pressure on a lot of these things, even on Twitter and everything else, right? This is a pressure, I think, that's pretty ubiquitous kind of in the social age. It's just like I see what you guys are doing, right, on Embedded. I see what Dave's doing because he posts his videos all the time. And I look at, like, Ben Krasnow, I look at, you know, everybody who's doing videos, Alan, everybody who's doing videos online and talking online and all these other things. And it always feels like it's not enough. And that's a separate issue, I think. Because you think you should be doing all of those things. Right, exactly. I mean, like, why am I not better at Embedded stuff, guys? I mean, come on, I need to learn this stuff, right? Why can't I fix my own car?

**Dave Jones:** This sort of thing kills me. Every day I go, geez, I'd love to do a video on that. But, like, I just can't. I can't produce 10 videos a week. It's physically impossible, you know? Yeah. It just, it takes time to produce content. I'd love to be able to just, you know, rattle. I should just, you know, leave the live camera on 24 hours a day and just have a live, you know, Truman Show type channel or something where I just keep talking, you know? But it's, yeah, no, it's a very poor way to disseminate, you know, information. And stuff. But, yeah, I see so much stuff I want to try and not teach.

**Chris Gammell:** I think all these years, too, like, you just got to try. I mean, some of this stuff, you just got to try it, right? I mean, like, I think that's true a lot of program language is, personally, I just did a reflow in my home lab for the first time ever. I don't know if you guys have ever done that on, like, a hot plate. It turned out to be pretty simple. But once you do it, you know, it's scary until you do it. So you got to just kind of jump in.

**Alicia White:** That's very true. Yeah. We had a listener offer to help us learn Altium, Philip. And it was a very nice offer. And it made me had to admit that I have lots of things I want to learn. And that isn't highest on my list this week. Right.

**Chris Gammell:** And I would only learn that if I needed it for something. I can't just learn tools. That's the thing. I mean, it's like, oh, go learn a programming language. Why? Yeah. Yeah. Right. Yeah. Yeah. You need a project, really. I mean, so what is on your list? I mean, because, like, let's come on. Let's get the, let's do, come on, Dave. Let's do an interview here. Alicia, Chris, what is on your list of things that you want to be learning here? Yeah. I would like to get better at electronics. Although, as I play with more dev kits and things, I wonder why. Because it really is becoming just this plug a module together thing. Yeah. But I don't really have a good fundamental understanding of it. So when I get into trouble with things like 3.3 versus 5, you know, I don't, I don't know what to do. God, this needs 5 volts. Well, I guess I can stick a transistor here, but I don't really understand what that means. Yeah. So fundamentals like that I'd like to get better at. But, you know, I have so many things I want to do that it becomes overwhelming and I end up doing nothing. Because I used to do, just outside of software and things, I used to do a lot of astrophotography and telescope stuff. I do a ton of music. So it's very hard for me to focus. And yet I do feel this pressure that I should be getting better at everything. Yeah. But, you know, I have some little projects. I picked up one of the Photon Dev kits from SolidCon and I turned it into an internet connected garage door opener in just a few hours, which was both cool and discouraging in a way because it was so easy that it didn't feel like I'd done anything.

**Dave Jones:** Yeah. Right. Well, that's the problem with the communications revolution these days is that you just see so many things that you want to do and learn. It's overwhelming.

**Alicia White:** Well, Chris Gamow was saying about how that can make you feel bad. I try to fight that. Because you do, because you hear everybody's, I don't know, was it Mythbuster or Adam Savage who said, that's everybody's billboards. You're seeing their highlight reel. You're not seeing their whole movie. It's a documentary and all you're seeing are the good stuff.

**Dave Jones:** Yeah. Right.

**Alicia White:** And, you know, I've had people say, how do you get so much done? And I'm like, by telling you only the good stuff. Right. Okay. Yeah.

**Chris Gammell:** I've got a pile of deadboards in my lab. Yeah. And Jerry did a really good video about that too, where she just kind of showed all the broken stuff. It was just, it was great. I mean, just like, yeah, you learn by failing.

**Dave Jones:** Yeah. Yeah. How do you make your own transistor? She said, look, it took me five years and all this, you know, failures to make my own transistor. You know, like, you know, and she makes it look easy. Right. And then.

**Chris Gammell:** Yeah. And that's even more accelerated in software because we'll fail 260 times a day. Right. Until we get something that's right.

**Dave Jones:** Until it gets up and it compiles. Yeah.

**Chris Gammell:** So it's a little bit twisted because in hardware, you have to, you do have to plan ahead unless you want to burn through a lot of, a lot of gear. Yeah.

**Alicia White:** I'm really sorry. I blew up that nine volt battery. I didn't think it would work that way.

**Chris Gammell:** I used to like when, I used to have an embedded guy I work with and he would, he would give me these amazing phrases where he'd be like, uh, Chris, there's noise. And I'd be like, uh, you mean it's not working? He's like, yeah, that's what I mean. Or, uh, it's, it's not working today. And I'm like, you mean you burned out the power supply? He's like, yeah, that's what I mean. It's always code words of like, like it's like an abstraction of like ways that he broke things. And it was, uh, you know, he was brilliant. I mean, like like one of the best engineers I've ever worked with, but like, just, I'm just like, dude, let's say things like they are. Well, when I put this piece of code. I never felt worse than when I broke hardware. Yeah. No, no coming back from that one.

**Dave Jones:** Oh, dear ID.

**Chris Gammell:** Alicia, what is, what's on, what's on your list? I mean, what, what are you, what are you looking to learn?

**Alicia White:** That's kind of tough. Um, cause I'm, you know, kind of all over the place and getting over a cold, which makes me even more frantic.

**Chris Gammell:** Um, we can go to like a six month timeline if you really feel comfortable, you know, like it's not like quick. Where would you like to be in five years? What are you looking to do in the next five minutes?

**Alicia White:** Um, I'm doing more and more low power stuff and I've been doing it for a while and all the software isn't a mystery. Optimizing is fun. Um, that is even assembly language optimization is fun, far more fun than useful, but far

**Dave Jones:** more fun than use. There's a great t-shirt quote, assembly language, far more fun than useful.

**Alicia White:** Um, but I've been doing like measuring power for different boards and I wrote an element 14 blog post about it and it was while I was still feverish. So there are a whole bunch of errors in it and reading back, I realized that there are things that I don't truly understand about the low level, why you need this power rated resistor and under what circumstances you need stuff. I even got one of Dave's, uh, microcurrents.

**Dave Jones:** Microcurrents, right. Nice.

**Alicia White:** And, um.

**Dave Jones:** Well, you don't necessarily need it. You can shove a resistor in there. You can build your own. It's just a resistor at a times 100 amplifier.

**Alicia White:** Yeah. That's what I thought it should be. It didn't show me what the resistor showed me. And the different resistors didn't show me what I expected them to show me. And this TI board I have doesn't show me the same thing either.

**Dave Jones:** Right. So you're putting a shunt resistor in, in series with your supply of your product and it wasn't showing what you thought it was showing.

**Alicia White:** And there are lots of tweaky bits about that. And that goes back to teaching is, is a way to figure out that you don't know something very well. Um, because I can say, oh yeah, you get a 10 ohm resistor. I mean, you look at how much amp you expect, probably using a DMM and then you, you get a 10 or a hundred ohm resistor and you make sure it can handle lots of power. And then you use that and then you can use an oscilloscope. And so these things I can like talk through, but when you get down to, well, how much power does this resistor need? And under what conditions does it matter that you're doing other things?

**Dave Jones:** And, and how much role is decoupling playing and all sorts of stuff like that?

**Alicia White:** Like right now, that's a very solvable problem. And I suspect by the end of the week, I will be totally golden on that particular subject. But all those little things of the electronics at a level beyond where I need it for software.

**Dave Jones:** Yeah.

**Alicia White:** And I keep masquerading that with, um, confusing that with doing schematic capture. And those are not the same things. So I keep saying, I want to do schematic capture. What I really want to do is understand the electronics.

**Chris Gammell:** Yeah. And some of that's vernacular it seems like too, right? Cause it's, you know, Dave's, Dave quickly jumped into like, oh, like a hundred X amplifier and a, you know, a resistor, a sensor resistor and stuff like that. And like, I can imagine that being very, uh, off-putting at the beginning. Just like if someone came in and started talking about, uh, pointers and oaring stuff in and that kind of thing.

**Dave Jones:** Have, have you guys been, uh, you know, public face professionals, you know, like easily found on the interwebs, um, have you ever had lawyers approach you, like asking you to be an expert witness in any court case? Cause I've, I've had it like two or three times now and I just got another one last night.

**Alicia White:** I haven't. Nope. Um, I think everybody here would go with Michael Barr instead because he actually has that as part of his business.

**Dave Jones:** Yeah. I think Jack does too. Who's Michael Barr? Sorry.

**Alicia White:** Um, he wrote the first O'Reilly embedded software book. Um, and yeah, Jack Ansell. If I, if I had to prove software, I would go with Jack.

**Chris Gammell:** Yeah. Yeah. Michael. Oh, right. Okay. Right. He was involved in the Toyota. Yeah. Oh, was he?

**Dave Jones:** Oh, okay. Oh, I didn't know that. Okay. They got him in as an expert witness. Okay. Fair enough. Yeah.

**Chris Gammell:** But I think that's a big enough, uh, time commitment that has to be kind of part of your gig. I think.

**Dave Jones:** Oh, that's why I told him to bug. I've told him to bugger off every time. It's like, why? What's in it for me? And, and they always say, but, but we will, you know, give you a retainer and pay you a professional rate. It's like, no, I have better things to do. You know?

**Alicia White:** I don't know. Some of my coworkers at ShotSpotter, um, had to do the professional or had to do the expert witness thing to explain ShotSpotter. And they said it was really fascinating. I mean, it was, it was not something they wanted to do regularly. I think it would be. Yeah. But once. Yeah.

**Dave Jones:** I've always wanted to do the jury thing. I got called up once, but then they canceled it. I've never had to do it. I, yeah, I think it would be fascinating, but you know, I'm not going to, you know, um, yeah, I don't want to wait. I've got better things to do. We see a lawyer in its native element. Here it is peering through the court stands. In this case, in this case, they wanted me to come to Malaysia to, you know, appear in court in defense of some dude who I won't tell you what he's accused of. But anyway, it's, it relates to one directly to one of my videos and they wanted to use one of my videos as evidence and also have me as an expert witness. So I told them to bugger off, but I said, oh, you know, look, you're free to use the video. And then they came back and, and said, oh, for us to use the video, we really need a letter from, you know, statutory declaration thing from you signed, signed in blood by 20 JPs or something. Um, anyway, we need something like that saying that you're the owner of the video and it is you who are appearing in the video. It's like, are you shitting me? Bugger off. You know, it's like, God, why? What's in it for me? No, go away.

**Alicia White:** You didn't ask for cash at that point? Cause I figured lawyers, they always have plenty of cash.

**Dave Jones:** Well, I, I, I could have like, yeah, they will pay. Well, they, yeah, they said, yeah, we will, how much to write a, and they wanted me to write a report too. Um, and they said, you know, like how much, you know, quote, please, how much to write a report? And it's like, no, sorry. You know, no, I don't want to be dragged down the rabbit hole. I got better things to do with my time than, you know.

**Chris Gammell:** Yeah. If you want to be involved in the legal system, it's probably better to become a patent lawyer with your technical expertise at this point.

**Dave Jones:** Oh, my brother-in-law is a, um, he's a PhD in laser physics and he's a patent attorney. And, uh, he tried to convince me that when he changed careers, right. And became a patent attorney cause he never wanted to be, but there, there's not that many jobs in laser physics here in Australia. So, you know, yeah, the wife made him go out and get a real job and he retrained as a patent attorney. And he tried to drag me into it. Come on, look, you know, with your engineering expertise, you know, you can be a shit hot, you know, patent attorney. Oh my, ah, a fate worse than death. Pass.

**Alicia White:** It sounds lucrative, but not much fun. At least not to me. I want to build stuff.

**Dave Jones:** Yep. Yeah. Charging per five minutes. You know, they, they, they actually have like a timer on their desk where they actually have to bill per five minutes. Yeah. You know, God, I, I hate weekly time sheets, you know, let alone five minutes, you know.

**Chris Gammell:** Yeah. So Al, what do you, what do you guys, uh, what do you guys, you said you want to build stuff. What are you guys building these days?

**Alicia White:** Uh, that one I can't talk about.

**Chris Gammell:** Oh, I can't talk about what I'm being paid to build.

**Alicia White:** Uh, well, I gave that inertial talk and I built the little LED inertial widget that I'm trying to convince everybody is like a hello world for sensors.

**Chris Gammell:** That one I can talk about. The shaking to blinky. Is that the, uh, you can shake to blinky.

**Alicia White:** It's got three modes in an accelerometer mode. It, it shows you which way is down. It's red, green, blue LED and X, Y, Z. And then, I mean, that lets you say acceleration is almost always gravity. And then the gyro in that mode, it's usually dark because gyros are boring unless you're moving. And then you can talk about how gyros, um, are about motion and gestures. And if you can give that to a designer who wants to do gesture recognition and say, okay, what colors do you see? It gets easier.

**Chris Gammell:** Well, what am I on right now?

**Alicia White:** And then it does a little light compass.

**Chris Gammell:** Oh, cool.

**Alicia White:** And so people, people get so freaked out by sensors. It's like, it's not that hard. I mean, sure. Once you get to Kelman's and Quaternian's, it gets a little more difficult, but just the sensors. They're more, they're totally worth it. They're fun.

**Chris Gammell:** What do people get freaked out about?

**Alicia White:** Um, well, when you are doing a light compass, you do have to do a bit of trigonometry.

**Chris Gammell:** Ooh. Ugh. Ooh. Yeah.

**Dave Jones:** What's that? That's that, like, Pythagoras thing, right? With, like, yeah, that I learned in, like, primary school. Signs. Cosigns. Ugh.

**Chris Gammell:** Mathematician over here is crying. In his chair.

**Alicia White:** Arch tangents, man. Arch tangents everywhere. It's fun.

**Chris Gammell:** Really, guys? Lookup. Wait, do you guys do that? Do you do that in lookup tables, or what?

**Alicia White:** Oh, I'm, I'm, I'm running Cortex things, so I'm just going, using the math library and letting it fake floating point.

**Chris Gammell:** I do not do that. I don't do that. I generally have lookup tables. Yeah. Well, it depends on how accurate you need to be. Oh, yeah. You know, it can get by with.

**Dave Jones:** And for the late books. And how much RAM you've got, how much embedded RAM and stuff, you know. Yeah.

**Chris Gammell:** I'm constantly frustrated in my paid work by this whole embedded thing. I didn't start out as embedded. You know, I started at Cisco, and we had plenty of resources. And, you know. Memory as far as the eye could see, kids. Yeah. And then I went to work for a couple of medical startups. And, you know, they're a PC architecture base. So it was like gigs of RAM and this. And then I, you know, got into the embedded world. I'm like, what do you mean I have 128K of RAM? There's a typo here. That K should be an M.

**Dave Jones:** 128K? Luxury, man. Luxury.

**Alicia White:** You sent that email where you meant to say 256 byte array. I filed a bug.

**Chris Gammell:** Yeah, no, I filed a bug. And I said 256K everywhere because my brain couldn't manage to say 256 bytes. I can't be that small. That doesn't make any sense. What am I going to do with this? 256. Come on. That's nothing.

**Alicia White:** Yeah. So that project I did for the inertial talk for Solid. And then I have an ESC talk about something. About makers. Maker to maker. Yeah. Yeah. Why? Why? What was I thinking? I heard this.

**Chris Gammell:** You can't diss your own talk before you give it.

**Alicia White:** Right. No, it would be great. There's a picture of a cephalopod. Maybe two. There you go.

**Chris Gammell:** Winning.

**Alicia White:** But I don't have any neat gadgets for that. Although I may break down the talk and look at other people's neat gadgets.

**Chris Gammell:** So I've heard on your show before, and I agree with it. You guys talk about, or at least Alicia, I'm not sure about Chris if you agree as well, but talk about robots and that's the best way to get started. But I have a more probing, distant question. If you could go back in time and talk to your former selves, would you still recommend Embedded?

**Alicia White:** Yes.

**Chris Gammell:** Yes, definitely.

**Alicia White:** It was great for me. It is great. There are things I would like to do differently with my education, but this was where I belong.

**Chris Gammell:** This may come out wrong, but I'm glad I ended up Embedded because had I continued where I was, I think I would have bored myself to tears. Yeah.

**Dave Jones:** But is this because you've been successful in Embedded? And of course you want to go back and tell yourself, yes, do Embedded because I was successful.

**Chris Gammell:** No, I was successful in regular software. Okay. It's just somehow making stuff move and turning lights on, not lights, 25 watt lasers. Shaking, blinking.

**Alicia White:** The physicality of it.

**Chris Gammell:** Yeah. And trying to solve problems that aren't about, can I make this, compute this faster? Can I figure out a way to move these bits from this memory to this memory faster? More like, well, how do I figure out that this motor is in the right position? And how do I get it to move here without maybe shaking the whole system apart? It's just real stuff. And that just caught my interest a lot more after having started doing that than moving bits.

**Alicia White:** Well, there's the application part too. When you're moving big bits around, it's hard. Lots of little bits. Right. Lots of little bits. It's hard to know what you're doing makes a difference. The application of, okay, I made a database. Anybody can use the database. It's very cool. That's great. But what is it being used for? A shot spotter or children's toys or DNA scanners or even Bluetooth wearable things. I can look at it and say.

**Dave Jones:** Oh, can I talk about Bluetooth wearable things? Please, please, please. Later, let me talk about Bluetooth wearable things.

**Chris Gammell:** We'll put a pin in that for you.

**Alicia White:** All right. That was it, actually. I mean, just the embedded allows you to be application focused. And I don't think I'd have gotten that from any other software.

**Chris Gammell:** Hmm. I like it. A rousing advertisement for embedded.

**Alicia White:** And now, Dave, are you going to rant about Bluetooth? Yes.

**Dave Jones:** Thank you. Can I get everyone's opinion on this, right? I did a video unboxing. And it wasn't really a review. It was like a first impressions. Like, it was unboxing first impressions of the new Pebble Time smartwatch. And that's exactly what it was. An unboxing first impressions. I gave, you know, my raw first impressions of out of the box. Here it is. And, wow, did I cop a lot of flack for this. Now, the reason I copped a lot of flack for it is because I, silly me, expected it to actually do something useful out of the box. Like, maybe for me to, like, turn it on and be able to play with it and maybe set the time and look at the clock display because, you know, it's a watch. And apparently, and I got attacked from every man and his dog for saying, you can't expect that. It's a smart watch. They don't work out of the box. You've got to do everything. You've got to set it up, program it, update the firmware, do everything, you know. And connect it to your Bluetooth phone and download the apps before you could do anything useful. It's a smart watch, Dave. Do you guys agree? Like, I think, like, and they go in. You have to, you expect that. We expect this from a smart watch. And my response is, why? Why can't it do something useful out of the box?

**Chris Gammell:** I have to be careful here.

**Alicia White:** Talk about that one, though.

**Chris Gammell:** Well, I will say one thing in general, and this is kind of dry and boring, but one of the reasons that you have to often have to update the firmware right out of the box is because the product isn't finished when they manufacture it.

**Alicia White:** This is like when they ship those empty boxes as a software? That is their problem.

**Chris Gammell:** I'm not saying it's not their problem. I'm just saying that's the reason.

**Dave Jones:** Yeah, no, I totally understand that. But I still think it's not a valid reason for people to think that things shouldn't work out of the box. I agree with that. And people are talking about all smart watches, not just Kickstarter projects. Right? Yeah, no, I can see that. Totally, totally agree.

**Alicia White:** So what was the iWatch unboxing like?

**Chris Gammell:** The iWatch, the Apple Watch unboxing. So with this, I did have to pair it with my phone. It didn't do squat out of the box. But they led you through it very nicely. And it was kind of cool because they had a weird pattern on the screen that you held your phone up to and it did some pattern recognition to do the pairing. So that was interesting, but I would rather not have done it.

**Dave Jones:** But do you agree that it should do something useful out of the box? Why can't it? Why should we expect modern gadgets like this not to do anything when you take them out of the box? Is that normal?

**Alicia White:** Well, the software, embedded software engineering in me is like, well, sure, as long as you're getting a Gen 2 or 3 of that product, no problem. Yes, it should work. But Gen 1, it ships before my software is done. So all I can put in there is a bootloader and pray that it all still works when you open it.

**Dave Jones:** Should it ship before it's done?

**Chris Gammell:** It has to. It has to because the hardware has to go to manufacturing. Why does it have to? The hardware goes to manufacturing way early in the schedule now compared to where the firmware is.

**Alicia White:** Well, then I do need production hardware in order to finish something. Right. So, yeah.

**Chris Gammell:** Yeah. I think it's because it's consumer, right? I mean, just the timelines are so compressed these days.

**Dave Jones:** But that's more reason for it to do something out of the box because it's consumer. But the risk is so high that it will sit on shelves.

**Chris Gammell:** Yeah. Right. It's a survival thing. The inconvenience that you're feeling as a consumer is nothing compared to cash flow. That's what I think it is.

**Alicia White:** Right. Well, there's also, in order to finish the firmware, you have to have the production units. Yep. And you can't start a production run and then stop and wait two weeks for the software to get their ass in gear.

**Chris Gammell:** But, you know, going back to Dave's side here, this didn't used to be the case.

**Alicia White:** No, this is just...

**Chris Gammell:** It's not that there's a universal truth that this has to happen. But it didn't used to be a six-month cycle either. Yeah. Yeah. Right.

**Alicia White:** So, did you buy the Pebble or did they send it to you for free?

**Dave Jones:** No, I bought it. I was a backer. I was a backer on their Kickstarter thing.

**Alicia White:** This is one of the cool things about having a business and with the podcast. And for us, the podcast is loosely advertising for our business. But everything's a business expense. Apple iWatches, business expense.

**Dave Jones:** Oh, yeah. Totally. No, I certainly claim the Pebble smartwatch on business. Yeah.

**Alicia White:** So, we say we don't make any money off these things. Well, and you did it for the video. So, that is your business.

**Dave Jones:** Well, I saved 28% of that whatever it costs, $190 or $200 it costs. Yeah. So, I got 20% of that back.

**Alicia White:** Woo-hoo! Woo-hoo! I'm totally in favor of that because Chris would have bought the Apple Watch anyway.

**Chris White:** It's competitive research. Yeah.

**Dave Jones:** Right.

**Chris Gammell:** Yep.

**Dave Jones:** Anyway, I was just really, like, I didn't even think about it beforehand. I just sort of opened the box and I went, okay, it's turned off. I expected it to be turned off. But then when I turned it on, I expected to be able to play with it. Like, because it had firmware in there, right, to actually do, like, to, you know, to sync to your smartphone and everything. Why couldn't it just have a simple, you know, a demo app to at least play with the gadget you've just bought? I don't, I just thought it was silly and I said so. And, yeah, everyone seemed to, no, it bought out all the smartwatch fanboys, you know. But, jeez, I found a new crowd of...

**Chris Gammell:** I don't understand, yeah, I don't understand getting on your case about that. That seems...

**Dave Jones:** Yeah, it just seems silly. Yeah. It's like, yeah, I don't get it either.

**Alicia White:** No, when the software updates, then the next time people get those watches, it will be fine. They will have a demo.

**Chris Gammell:** Right, right.

**Dave Jones:** Well, apparently, right, they were saying that, like, the previous Pebble watch, when they first got it from the Kickstarter, had multiple clock faces, for example. This one has one. And it's analog. And it doesn't even have Roman numerals on it. It's just crap. Right? So they've actually gone backwards from the previous one to what they install in there in default. And by default, and everyone's... Well, a lot of people on the comments, their excuse is, or their reason behind that is, well, you shouldn't include different things in there by default, because that's just bloatware then.

**Chris White:** But, you know, it's temporary bloatware. You guys don't make hardware that you ship out to people that they have to attach a bunch of blue wires before it works?

**Dave Jones:** Yeah, they're called kits. And you sell them as kits. You know, like... I mean... It's appetized as a kit.

**Chris Gammell:** You expect it not to work out of the box. In my past, it's never been... I mean, but the timelines are just different, right? I mean, there's... So, you know, industrial products, 18-month, 24-month cycles, you know? If that, maybe more. Dave was in military. You know, like, that... Yeah, five years. It is finished, and you're going to be able to make it for 20 years. Like, that's just what you do. So I think that's just the difference here. I think... And I think the expectation is raised by, you know, the Apples and the Samsungs of the world. But, I don't know. Yeah, because they could turn that wheel so much faster. Right.

**Dave Jones:** But I think it's a poor direction we're headed in. If people expect things not to be polished and work out of the box, and you have to set them up and go all techie and know how to, you know, Bluetooth connect your phone to your gadget. Like, I just... I'm surprised by that view by YouTube. You're the thin edge of the wedge, you know? Yeah, I know, right? You think, like, if anyone would understand it, it'd be me, right? But, no. When I buy a watch and I take it out of the box, I want it to tell the freaking time. I don't expect the time to be correct, of course.

**Chris White:** But you didn't buy a watch.

**Dave Jones:** I did. It's called the Pebble Time Smartwatch.

**Chris Gammell:** No, you bought a Pebble Time. Those words don't mean what they said, they mean. Right. You bought a dev platform. An early back of that platform. Silly me. You bought a Bluetooth gadget. You bought a computer with a Bluetooth attached.

**Dave Jones:** That's what everyone's saying. I didn't buy a watch. I bought a phone gadget.

**Chris Gammell:** You bought a Cortex-based timepiece, eventually. But this is one of the complaints that you've had about the Internet of Things all along, Alicia, is the techie requirement of, oh, you have to connect this to something. You have to know how to provision something. Connect it to your Wi-Fi. Connect it to your phone. And it hasn't gotten any better, I don't think.

**Alicia White:** It doesn't seem like it now.

**Chris Gammell:** And yet the market is exploding. No, I don't think it has.

**Dave Jones:** No, I expected it to. You know, it's been, how many years has it been since the whole Internet of Things?

**Chris Gammell:** Three or four minutes. At least. Like, yeah. Okay, so I have one new data point on all this stuff, which is now having worked on web stuff, where the assumption is someone comes in, you can't explain them anything, or else they're going to go somewhere else. That's, like, the absolute minimum of time. I think there's still a balance between that, though, and, like, having a product where you still have to set it up. You have, like, a guide to set it up. I think there's still always going to be that, just because, like you guys alluded to, the Pebble time team doesn't have a thousand engineers like Samsung does. You know, there is no problem.

**Dave Jones:** They sold a million smartwatches over the last year or a half. At what margin, Dave? They sold a million smartwatches. Who cares? A million is nothing to me. You're telling me they don't have the resources. No. Oh, come on. What is their margin? They're a couple hundred million dollar company, and you're telling me they don't have the resources. They're a Kickstarter company. No, they're not. They're a couple hundred million dollar company. They're huge.

**Chris Gammell:** You want to find out how many employees I have? Right, exactly. Money does not buy you faster software. It doesn't change space time, right? Chris, Alicia, come on. Software people, help me out here. Often the more people you buy onto a project, the slower it goes. Exactly.

**Alicia White:** Well, yeah, because somebody there said, we have to localize this, and so now we can put even less in the initial install base, because the first time you download stuff, you're going to have to download all the character set you need. And so now, instead of having four watch faces, you have one watch face because it doesn't have any localization needs. It's the dumbest, simplest face you can give.

**Chris Gammell:** Or a month before shipping, Apple releases iOS 8.4, and they've got to scramble to understand that SDK and change all their code around that talks to something because they changed the Bluetooth API. Yeah, but you can still upgrade later. It's just all this stuff that happens that they have no control over.

**Dave Jones:** No, I'm sorry. It's just poor upfront design to not have a good out-of-the-box experience. You can design that in, and sure, okay, if you need to change the firmware later, okay, well, you, you know, that's part of the update procedure. But that's no reason to ruin a good out-of-box experience.

**Chris Gammell:** I think the reason you got attacked and the reason you're getting attacked here, because I am attacking if there's any clarity. If there's any misconception here. It's because this is Dave Consumer versus Dave Engineer, I think.

**Dave Jones:** And that's how I did the unboxing. I bought a watch, and I expected, I wasn't expecting, I didn't buy a kit, right? I didn't buy a development platform. I didn't buy a phone gadget. I bought a watch. And I could not turn it on and play with it out-of-the-box. I was disappointed.

**Chris Gammell:** This is the reality of Kickstarter. Right? It's not the end of the world, right?

**Dave Jones:** It's not the end of the world, but I'm just saying, I'm disappointed. And it's a poor direction the industry's headed if people take this as, like, expected. Then everyone's going to just do piss-ball products right out-of-the-box. Oh, we can fix it later in firmware. I think it's a dangerous direction.

**Alicia White:** I think a more dangerous direction is how secure and how private is that data? Yeah. I would rather people be talking about whether or not I can hack your watch by walking by a few times. Oh, totally, yeah. Whether or not your initial experience was great.

**Dave Jones:** A totally different argument. That's a non-sequitur, though. That was totally a non-sequitur. I wonder if you read about something else. Teeing you up.

**Chris Gammell:** Next time on The Amp Hour. Yes. Are you guys focused on security a lot in your work? Not these days.

**Alicia White:** Not a lot.

**Chris Gammell:** Bluetooth security comes up occasionally. Because it's so bad. Because it's a brave new world. Well, that too. I always feel like with all this stuff, it's just... I understand that all the data can be back-calculated. I understand where I've been, what I've been doing, all these other things. But it's just like, I don't care what my Bluetooth earpiece has been doing. I know that there are all these crazy hacks. Like Sammy. What's his... I forget Sammy's last name. But you know, like that one where he was sniffing packets off a keyboard in the... Oh, yeah. Yeah. So you're hard.

**Dave Jones:** Well, there was... Talk about this on the forum the other day. The new Altium Circuit Maker software, right? Somebody in the forum realized that there's huge security vulnerability in it. And it looks like you can actually download files to people's machines through some, you know, back channel or something. That through some security labs in the Altium. Because it's not encrypted or something. I don't know.

**Chris Gammell:** And who at Altium is going to think hard about securing a tool? Yeah. There's so many... There's just so many vectors for this kind of stuff that...

**Dave Jones:** Yeah. So, yeah, I'm not necessarily blaming them. But, you know, like, yeah, apparently there is a big security... Or there's a security vulnerability there. And, you know, apparently this guy says, yeah, I can dump files on your machine. Well, all these things, it feels like...

**Chris Gammell:** It just feels like a lot of it's... With the security in mind, it's just... Or everything we've been talking about, even the software updates, stuff like that. It's like everybody's being asked to do more with less. And when do you have time to focus on these things, right? Security or out-of-the-box type stuff. If you don't have big teams or resources. Yeah, and it's not part of the plan.

**Dave Jones:** You don't need a big team or resources. You just need to have that as a focus.

**Alicia White:** I think what you need is the person. The person who says, no, we are not compromising. This is not a group project. This is not mediocrity.

**Dave Jones:** You need some ass-kicky. You need some, you know, someone to come along and say, this must be right. And we're going to make sure this is right.

**Chris Gammell:** Yeah.

**Dave Jones:** And then they make it happen. And otherwise, you know, like, you know, engineers and programmers like us, we just go, oh, yeah. You know, who cares if, you know, we'll just do whatever we think, you know, if there's nobody driving us, we'll do whatever we want. And go, oh, yeah. If we need a firmware update out of the box and it doesn't work, who cares?

**Alicia White:** A lot of engineers don't really appreciate what a product manager can do. But if you've ever worked with a really great product person, it's worth it. Because the product ends up being, having all these sanded, these edges sanded off and it just feels nice.

**Chris Gammell:** Well, what about the engineers who know what we should be doing but can't because they're not making the decision?

**Dave Jones:** They're not listened to. I mean, there's plenty of us who know what the right thing is. Sometimes you scream. Yeah, yeah. Yeah. I mean, I've encountered that, you know, because I'm always, this may come as a shock to people, but I'm always the guy within the company who puts his hand up and goes, hey, I think we should do this. I think it's really important. Here's why. And, you know, yeah, go away, Dave. Like, shut up. That just, you know, screws up something. Just go away.

**Alicia White:** So demoralizing when that happens. I don't even think the managers understand that those are the incidents that make us leave jobs.

**Chris Gammell:** Yeah. Right. Exactly. It's not like, it's not the, oh, I didn't get a 3% raise. I only got a 2% raise. No, no. It doesn't matter. Yeah, yeah. You're totally right.

**Dave Jones:** It's not that.

**Alicia White:** It's all those times when I had a good idea or a really important thing and you just said, nah.

**Chris Gammell:** Right.

**Dave Jones:** Yes.

**Chris Gammell:** We don't have time.

**Dave Jones:** Not necessarily saying no. I don't mind that. But not giving a crap. Right. Like, not caring and not listening and trying to understand and then going no. I don't mind that if they listen to it and listen to all my explanation and my reasoning behind it and they go, okay, yeah, I've carefully considered it. You know, no. And here's why. You know, and fair enough. You know, but when they just ignore you and tell you to shut up and go in the corner, you know, and don't rock the boat. That's, yeah. Yeah. That's when you want to go, yeah, this company's not really great to work for. I think I'll go elsewhere.

**Chris Gammell:** I had the opposite experience at a couple of companies. I was Mr. No. They would always, the thought leaders would come up with, oh, we have this great idea for doing this. And I'd say, no, you can't do that. Because at these places it was either illegal or impossible. Pick on it. Right. But, you know, that felt bad too because I felt like I was continually saying, no, you can't do that. Your idea is just something you can't do. Guys. Physics. Guys.

**Dave Jones:** I get that reputation all the time. I get accused of that all the time. You're just a naysayer, Dave. Yep. You're just a naysayer. You know.

**Chris Gammell:** Dave, you are a naysayer.

**Dave Jones:** I'm a bloody engineer. I'm a practical design engineer. I know when things are going to work and when they're not. Have a gut feel for it, you know. And then I can prove it to you, you know. Right. And, yeah. Yet, I'm always a naysayer, you know.

**Alicia White:** Saying no is important. Especially those kinds of things. Sorry? But that's another instance where you can get steamrolled and somebody will say, do it anyway. Or it's critical. And you're like. Yep. Yeah, that's nice. Could you type it in? Because I don't want to go to jail.

**Dave Jones:** Right. Yep. Yep. Yeah. Yeah.

**Alicia White:** And.

**Dave Jones:** I've had to do that except the jail part. I've, you know. Like, I've had to have them, like, send me a formal email telling me to do it. Because I know shit's going to come back on me. You know.

**Alicia White:** Well, this is depressing. I think we should just go to the job. And to think, I was thinking recently that I sort of miss a team and a real job. But now not so much.

**Chris Gammell:** Yeah, right.

**Dave Jones:** Yeah, right. Yeah, yeah, yeah.

**Chris Gammell:** This is like a team. This is like a four-person crazy team right here.

**Chris White:** Yeah. We should make smartwatches with great out-of-the-box experiences.

**Chris Gammell:** Yes. I know.

**Alicia White:** On the outside, we'll say open at noon. And we'll just put a cardboard thing in there. It'll be really pretty. But it will be fixed. Yeah.

**Chris Gammell:** What about, like, the plastic covering that has the fixed time on it? Like, that's a great out-of-the-box experience, right? That's how watches used to do it. You peel it off and you just turn it on, right?

**Dave Jones:** Oh, goodness. Have you noticed that when you do work for companies like that, you always tend to gravitate towards the groups where, you know, a similar mindset to you. Oh, yeah. You know, it's not that you're going to hang out with those no-managers, you know. Yeah.

**Chris Gammell:** You have to because otherwise you'd go crazy. Yeah. You can't find anybody like mine. That's the places that you don't last long at.

**Dave Jones:** Yep. Exactly. And that's why I've often stayed at a job for so long. And I look back and say, well, why did I stay there? That was just a batshit crazy company, you know. And it was because, yeah, I enjoyed the people that I hung around with, you know, and worked with.

**Chris Gammell:** We have it on tape, folks. Dave enjoys some people.

**Dave Jones:** I do enjoy some social interaction. Yeah. Now I just sit in a windowless office all on my own every day. Yep.

**Alicia White:** It is funny how a lot of times engineers, even I will say, I don't want to really interact with people. And yet that is the part I miss about working in a team or the people. I remember once I was in a job interview and they said, can you describe your perfect job? And I said, well, I would have a huge library. You would shove pieces of paper with problems under the door, puzzles or information questions. And I would have a time limit and give it back to you. This, by the way, is not the correct answer to that question.

**Chris Gammell:** The answer is always this exact job you just described to me. Yes.

**Chris White:** So basically you said, I'd like to be put in a cell for eight hours a day. I would like to be a turning machine.

**Chris Gammell:** You can't have that now. Open offices are everywhere. They can't find you a cell.

**Alicia White:** So awful. That's another thing that will keep me from going back to a full job.

**Dave Jones:** A death for an engineer. Open plan offices.

**Chris Gammell:** Well, we do have a lot of listeners that are on their own. And we salute. I'm thinking of surveys past. And I salute the solos out there. It can be tough. Hopefully the Embedded podcast. Hopefully The Amp Hour Podcast. Hopefully we seem like the annoying coworkers that are on the other side of your cubicle. Just for a little bit.

**Alicia White:** We'll keep you company at lunch. Yeah, once a week.

**Chris Gammell:** I'll never use the conference call feature on my phone. Yeah, right. Every outro is just, yeah, yeah, no, we should go fishing this weekend. No, no, no. We'll take my boat this time. No, no, no. How's the wife? Can you hear me? Yeah. I think I lost you. Can you hear me? No, I'm going to lunch later. I'm going to lunch later. Don't worry. Don't worry, Morty. Yeah. Okay.

**Dave Jones:** Yeah, I sat next to that guy. We're not. No, we've lost it. It's all right.

**Chris Gammell:** What I did want to say is that, first off, thanks to you guys for being on the show. We've got to wrap up. Second off, fill out the listener survey. Was this the show?

**Alicia White:** We're not done yet. There's still outro. No, I think we're not done yet. The whole previous time was the show?

**Chris Gammell:** We're on the way out, Chris. Come on, man. Oh. This is the process. Yeah, we are.

**Speaker ?:** Okay.

**Chris Gammell:** Okay. All right. When did you think it was starting? I didn't think we had started. One, two, three.

**Dave Jones:** Bet you laughed at me before when we were trying to re-sync the damn show for doing a countdown time sync.

**Chris Gammell:** Yeah. Okay. Well, Alicia, Chris, thanks for being back on. Thank you for having us.

**Alicia White:** And congratulations. This is a great show. Thank you.

**Chris Gammell:** We love you guys. Thank you very much. We do have a great show as well. All right, guys. Bye. Bye. Bye. Bye. Bye. Bye. Bye.

**Speaker ?:** Bye.

**Dave Jones:** Are you back? Okay. Are we in sync? I'm back. Can everyone count down with me? Three. Three. two, one Chris, where are you? Wait a minute, I didn't have to do this last time too

**Dave Jones:** You did this last time too

**Chris White:** Yeah, what?

**Chris Gammell:** Alright, let's just start counting What the hell is going on here?

**Dave Jones:** What? Counting confuses you? You need to watch Sesame Street, dude Apparently I was so confused I was just like, what are we supposed to do? Countdown! 3, 2, 1 Go! We're all in sync!

**Chris Gammell:** What the hell were we talking about?
