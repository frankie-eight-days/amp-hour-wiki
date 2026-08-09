---
episode: 258
title: An Interview with Bertrand Irrisou and Gerald Friedland of Audeme
url: https://theamphour.com/258-an-interview-with-bertrand-and-gerald-of-audeme/
---

**Bertrand:** This is The Amp Hour Podcast. Recorded July 14th, 2015. Episode 258. An interview with Bertrand and Gerald of Audine.

**Dave Jones:** Welcome to the Amp Hour. I'm Dave Jones from the EEV blog. And I'm Chris Gammell of Contextual Electronics.

**Gerald Friedland:** I'm Gerald Friedland of Audine. And I'm Bertrand Irisu from Audine.

**Dave Jones:** Hey guys, thanks for joining us.

**Chris Gammell:** Thank you.

**Dave Jones:** Thank you. It's an interesting topic we've got today, voice recognition.

**Bertrand:** I'm pumped about this.

**Dave Jones:** Yeah, speaker independent voice recognition, which is even harder than regular voice recognition, is it not?

**Gerald Friedland:** Yeah, that's a good question. So speaker independent voice recognition these days is kind of the state of the art. So there are different ways of doing it. One way is to basically have acoustic models pre-trained with many, many speakers. So that if you sound similar to one of them, it just works. And different speakers can speak and you always sound similar to somebody else.

**Dave Jones:** Right, yeah.

**Chris Gammell:** It's also what everybody is used to these days. You know, Siri and Alexa and all these other systems that are becoming very popular are clearly speaker independent and continuous speech as well.

**Bertrand:** I would expect that if Dave was speaking to the same device as I was, that it would recognize his crazy Aussie accent at the same time as my beautiful Midwest stroll.

**Chris Gammell:** Well, as a matter of fact, you'd be really surprised. We have tried on a variety of accents in our system. And, you know, I have a light French accent. At least I'd like to think so. Gerald has a German accent. We've tried on Indian accents and all kinds of accents of English speakers. And it actually works really well. I don't know, mate.

**Dave Jones:** I reckon I could break it. No worries, mate. She'll be right.

**Chris Gammell:** Well, yeah, that might be an issue. There are some caveats.

**Bertrand:** Yeah. Another thing we should mention here is that, so, okay, so this is the audience and you guys are running a Kickstarter and we'll get into all the details of that. But the interesting thing to me, the most interesting thing is actually not the speaker independent, but actually the network independent. The fact that, you know, I'm used to having a phone. I talk to it. I say directions to 1234 Main Street, you know, Cleveland, Ohio. And it recognizes that. But it's doing that because it's passing that audio file up to the cloud, processing it, and then sending back basically like a JSON or a text file basically to the Maps program. Then, you know, it's sending back text. You guys are able to do a localized recognition of that kind of thing. So how the hell are you doing that? I mean, how are you separate from the massive cloud that does a lot of the processing that people are used to?

**Chris Gammell:** So let me just go back to this issue of cloudless, as we call it, before we go into the technical detail. Okay. You know, it's great to do things in the cloud. There's many reasons to go through that. But the reality is there's plenty of occasions where, first of all, you may not have a connection to the cloud. And we all know how well those Wi-Fi connections work. And I think the second issue, which is largely, you know, understated, is just privacy. I mean, we all know, you know, a lot of people don't seem to be terribly concerned, but I believe it's a real concern, privacy. And doing things local essentially get rid of this particular issue. You've got companies, I mean, a few months ago, Samsung got in trouble because their new TVs that essentially listen to voice commands, was using a third party and sending unencrypted text or speech, I'm sorry, to their third party for speech or text conversion, which basically anybody could have, you know, if dropped on.

**Gerald Friedland:** Right, right, right.

**Chris Gammell:** Yes, as a, you know, as a private citizen, it is of concern. So we really wanted a solution that was standalone. You know, there's nothing that goes out of that board except, hey, I recognize sentence number four that you told me to recognize. And that's what it does.

**Bertrand:** Yeah, that's powerful.

**Dave Jones:** Although I've got to say, Chris, you are a young whippersnapper because I used a voice, speaker independent voice recognition chip back in 1908, early 1980s.

**Bertrand:** And we all have seen your video. Yes, you did a video about this.

**Dave Jones:** You could buy the local Tandy store. Granted, it was pretty crap and it had like 10 words, go, stop, start. Right. But, hey, it worked. That's right. And it was, you know, no, there's cloud rubbish. Jeez, didn't even have the.

**Bertrand:** Right, right. Well, yeah, and you could also say that. It was very primitive. You could say that, like, oh, well, phones talk to you today, but then you could also say, well, the speak and spell was doing this. You know, they were also, it was electronics talking to you back in the day. You know, like it's.

**Chris Gammell:** Texas Instruments made a lot of money on that chip.

**Bertrand:** Yeah, right. Oh, they did. Yeah. But it's just the levels of how much of that stack is really working for you, right? Yeah. It's a different experience, I think.

**Gerald Friedland:** So the speak and spell is a synthesizer only, of course, right? So they were not recognizing, but we were basically spelling and then we'll speak, which is an awesome toy, by the way. We still have that here. And I don't know where it is, but we had it like at least for, it probably still worked last year. And anyway, the reason why we can make it work is because there's a combination of sort of, you know, newly available chips that make this happen. And also basically the combination. And I mean, I've been working in audio and multimedia for 15 years. And there's basically just a lot of tricks you can do because it's not a dictation application. It's basically voice commands. And so we can recognize full sentences. And it's also, it's, you know, speaker independent. And you can program your own sentences. And a lot of this is happening by basically smartly combining lots of the stuff that is out there, you know, and just making sure. And then timing is an issue. And there's a lot of things that just have to be right. And it's a lot of tinkering. But that's basically, you know, it was a lot of fun to basically put this together. And as definitely as an acceptance to a challenge. Because what happened here is that a lot of these companies were doing, you know, you know, Apple started and also smartphones. You know, even, and I usually say as a joke, the PlayStation 4 has a cloud-based speech recognizer. But the PlayStation 4 has like eight CPUs in them. It's basically as powerful as some of the compute clusters that we use to do speech recognition on a research basis.

**Dave Jones:** So what's the deal with that?

**Gerald Friedland:** That's nuts. And so they do it because then they have, you know, full control over all this training and can update the models for new words and so on. But what we wanted to do is we wanted to give that full control to the maker, to the, you know, person that builds an Arduino project. So that they can customize it the way they want and they have full control over it. So that was the goal. And it's actually, you know, again, I'm quite proud of that you can do that. You can totally program your own sentences, your own call sign. You can change all the timings. You can change, you know, the responses, all of this.

**Dave Jones:** And you can download those to the chip.

**Gerald Friedland:** And you can, yes, exactly. You can upload these to the board. And it's training, you know, basically the part that needs to be trained on board. And once you're done, you don't have to have an internet or a PC connection. It's just Arduino plus the shield. And you can build it into a robot, battery operated. And you may be somewhere in the wild where there's actually no internet. And, yeah, we've shown some of these demos on the website. And also we presented it at Maker Faire, so people in the Bay Area, so Maker Faire Bay Area, they could probably just basically try it out in life.

**Bertrand:** Right, which is where I saw it, actually.

**Dave Jones:** Yeah. All right. Yes, you've just seen the demo or heard the demo. Or no, you don't hear it. I enabled the demo with my voice. You controlled the demo. My radio voice. Please correct me if I'm wrong, but there are two types of speaker independent voice recognition. One is the trained version, which you have to train before it can really do anything useful. And there's the Holy Grail, which is the untrained one, right, which you can, you know, you don't have to do anything. You can, anyone can just walk up to it and, you know, do things like the Dragon, like a lot of people will be familiar with the Dragon software, right, which has been around since the 80s or something. That's been evolving. That's a trained-based system, isn't it? The more you train it, the better it gets at recognizing it and actually translating your voice into text. How does your one?

**Gerald Friedland:** Yes. So I want to, first of all, and this is not to be too professorial or too scholar, but we usually call it speech recognition because the voice recognition is what we don't want to recognize. We actually want to be independent of the voice because we want to recognize the words, right? So, hey. No, it's actually very common, including marketing people do that. And in fact, we also, our Facebook page calls it Arduino voice control. Right. But in reality, so the scientific term is speech recognition for that reason. Got it. So the question about Dragon. So if you have a dictation application like Dragon, this is much, much harder because you don't know whatever will be dictated, right? That's right. You're dictating full, maybe letters or full, like, papers even.

**Dave Jones:** And it has to be 100% accurate, too.

**Gerald Friedland:** Right.

**Dave Jones:** Otherwise, people get frustrated and don't use it.

**Gerald Friedland:** Right. So it will never be 100%, but it has to be quite accurate so that you actually save work compared to typing it. Correct. And so that's why they do speaker adaptation. So that means they have models for speech recognition in there, but they will adapt to your voice and make sure that the similarities they are matching are actually really, really similar to your own voice. So the good news is that in our application case, we do voice control, right? So you cannot build a full dictation application with what we do. Right. Got it. What you can do, though, is you can give it hundreds of sentences and sort of build a Siri type of application where you basically say, okay, like, I mean, we have these examples where we have Eliza, for example, or we have an adventure game, well, an early, early 1980s adventure game. Eliza.

**Dave Jones:** Oh, that brings back memories.

**Bertrand:** Wait, hold on. Young person here. Can we give us a hug? Young whippersnapper alert. Whippersnapper alert. Can we explain this?

**Gerald Friedland:** Okay. So Eliza was like, oh, my God, was it 70s or 80s? No, 70s.

**Dave Jones:** 70s, yeah.

**Gerald Friedland:** You can Wikipedia. Weizenbaum basically came up with a thing where you would type natural sentences, a natural English sentence, you know, and then it would react to it based on some keyword that spotted it. And it would basically emulate sort of a passive therapist, you know, not a very good therapist.

**Dave Jones:** Yeah, it would talk to you and answer your questions. And right. And Eliza, I'm depressed.

**Gerald Friedland:** Right. Pretty much. And the funny thing was that with very little AI, really, you could almost fool people into it. You could. And of course, yeah. Yeah. And of course, since the 70s, this has evolved to, I mean, some Elizas are really amazing at this point. It's like, oh, my God, this is reacting to everything I say. And so it was really interesting for us to say, well, I don't like the typing. I actually want the real voice interaction. And so I did this with Movi. And there's a video on the Kickstarter page that shows that. And the other one is the Hunter Bumpus game. So basically, it's a little adventure where you go through caves and you're trying to find this creature that is going to try to eat you. And so if you run into the cave with a creature, it's eating you and it's game over. But if you manage to shoot it first, then you win.

**Chris Gammell:** But the real purpose of these examples really was to share interaction, real dialogue interaction where you recommend either keywords or full commands, essentially. And that's really key. And Eliza, I mean, was essentially 40 lines of basic back in those days.

**Dave Jones:** Yeah, I learned a lot of programming basic. Yeah, it's great.

**Chris Gammell:** That's right. It was running into a 16K Apple computer, at least in my days, which is far less than any Arduino that you buy today. Right. And we just wanted to demonstrate that you could do all this just voice control using the setup. And it's trivial to program. That's really the idea. Right.

**Gerald Friedland:** And that's the point. It's like all of this can be done even if you basically pre-specify the sentences and the vocabulary that is to be recognized, which helps the recognizer tremendously. Right. Because that's what you cannot do in a dictation application. That's the big difference.

**Bertrand:** Got it. Right. And it's almost like that the, you know, a lot of this stuff I think about in the sci-fi terms, you know, this is the promise of the future is voice commands, not necessarily full, you know, like at least all of the sci-fi stuff is always commands of like, okay, Earl Gray hot. Right. Like it wasn't like, well, I wanted to taste, you know, a little bit water today and I want it to be like a couple degrees warm. It was always just a command. It wasn't necessarily a full, you know, recognition type of thing.

**Chris Gammell:** It wasn't like going to Starbucks and really have a full range of options when you were ordering your latte. Or even if it wasn't, it was still pretty good. Yeah. I wish I was going to tell.

**Dave Jones:** Come on.

**Chris Gammell:** You just gave me an idea for an application here. We should have the Starbucks voice control.

**Bertrand:** Yeah. Well, yeah.

**Chris Gammell:** Which actually would work really well. Right.

**Bertrand:** I mean, you have all these K-Cups. You have these, there was another K-Cups thing where it was like a bartender. I mean, like all of these things, like it's not, you know, it's amazing when you think about it. When you move outside of natural language processing type stuff, really what we were really doing with, even with computers these days and apps and all these other things, it is still command based. It's still, you know, click a button. A button is a single command. And in this case of, you know, if you can recognize a single sentence, as long as it matches that sentence, it's what you want to end up with the output. It's a digital one or zero output kind of thing.

**Chris Gammell:** And that was exactly the intent that we had when we started this. I mean, you know, you think of software programming as layers of programming. A lot of people don't think of hardware as a layer of hardware, but that's really what we're trying to do here. It's like, here's a board, give it a bunch of sentences, you know, and it's just going to recognize them for you. And whenever it gets one, it just flags it and you do something with it. It's, you know, it's, that's really the intent of this particular project.

**Dave Jones:** Right. So when, when somebody programs this with the sentence, is that just programmed to them or is it a, or does it try and be speaker independent for that sentence? How does that work?

**Gerald Friedland:** Yeah. So you program the sentence by typing it. So you say in the...

**Dave Jones:** Oh, okay. Yeah. All right. Oh, okay. That's clever. Now we're getting fancy pantsy. Okay. Right. Definitely.

**Gerald Friedland:** So that's why, so, so that was a complication we had because, you know, English spelling and English pronunciation really don't match. Yeah. Right. So. Yeah. It's a pretty smart language. Yeah. Yeah. Right. So, so what you need to do there is there's, we included a two gigabyte and that's the two gigabyte dictionary. Many people ask us about this. What does this do? So the two gigabyte dictionary is actually giving you, you type the word and internally it's taking the word and, and mapping it to pronunciation. And this way the, the movie board knows what to expect when you say the sentence. So. And so that's what, that's also how it's speaker independent because it doesn't know anything about the speaker anyway. Okay.

**Dave Jones:** That's a massive amount of data though.

**Gerald Friedland:** Yeah. Yeah.

**Dave Jones:** How did you compile that sort of database?

**Gerald Friedland:** These databases are online. Oh, they're actually available.

**Speaker ?:** Right.

**Dave Jones:** Somebody, these have evolved over the decades, have they? Yes.

**Gerald Friedland:** Right. Okay. This is where you need the speech research experience.

**Bertrand:** So when a user is using this board, does that mean that they're typing in something into like an online? So can you just walk us through the process here? Is it like the user types something? I mean, there's, there's the Arduino sketch that I saw on the site, but does that mean that it's going out to the cloud and actually grabbing these various pronunciations and downloading that whole thing to the board?

**Chris Gammell:** No. So the, so the board has a, you know, the, the, the board has a four gig SD card on which two gig is the dictionary. So the, the method through which we program the board essentially, uh, if you take an Arduino sketch, basically you have a setup, you know, and in there you would essentially tell it, uh, learn, you know, sentence one, I want to turn on the light, learn sentence two, turn all the lights off, learn sentence four, three, four, five, et cetera. You can have as many as you want. Then you have a, you know, once you're done with a setup, basically the, the board will go through its own learning phase where basically it, it breaks down all these sentences into phonemes through the dictionary and, and, and figures out, you know, what to do with it. But that's completely, that dot part is completely transparent to the user and it's only done once if you change any of the sentences. And then all you have to do is in the main loop that you have, uh, you know, the main, uh, execution loop of the Arduino program, uh, you just pull them on a regular basis and you, you know, and you check to see if a sentence was recognized. And if it, if you did, it'll tell you, Hey, I recognize sentence number four and sentence number four was, you know, dim the lights 50%. Who knows? I mean, whatever you've programmed. And then you take that information and you go do something with it, uh, on your board. So there is, you know, it's, it's all, uh, you know, I mean, literally, I think we, we, we, we figured the absolute minimum number of line of codes you needed to add was like five. Yeah.

**Dave Jones:** That's about as high level as you can get.

**Chris Gammell:** That's about as high level. And, um, you know, that's just to recognize a couple of sentences basically, and then do something with it. Wow. Really, really simple. Uh, I mean, it's, it's, it's, it's extremely abstracted if you will, but it, I think it, it becomes extremely intuitive to a user. Uh, you know, and a lot of users, uh, on Arduino, I mean, you know, they're, they don't have 20 years of programming experience and then it's certainly not speech experts. So, um, and I'm not a speech expert either myself. So I really wanted something that was actually easy for me to use.

**Dave Jones:** Well, that's why even back in the eighties when we, like the speak and spell and the, uh, famous SBO two five six, um, speech allophone chip, right. Which would actually talk, right. It was not voice recognition here, but you know, it was actually difficult to use that chip because you had to know all about phenomes, right. And you had to know how to concatenate them together to form a speech. So that's why they came out with this companion chip that would just take serial ASCII in and then it would figure out all the, all the allophones for you and generate the speech. Exactly.

**Chris Gammell:** And, and for us, so the, the, the board also has a built-in synthesizer as well, uh, with both male and female voice, although the male sounds a little bit like Stephen Hawkins. Uh, but the idea there, um, is, you know, there's a say command and you just type in plain English what you want the synthesizer to say. Uh, and again, we use the same dictionary to phonetize and make it, you know, go through sound. So trivial to build dialogue, basically.

**Dave Jones:** I was going to say, so you almost got that for free. You almost got the capabilities for free. That's right. Right. Nice.

**Bertrand:** Can you guys explain the, the phonemes a little bit more for, for uninitiated like myself, um, just like what they are and how, how that ends up affecting some of this stuff. Obviously Dave made a video about this and I'll link that in as well, but, um, just kind of how all this stuff fits together with the, the segments and breaking up speech.

**Gerald Friedland:** Yes. So pretty much what it is, is, uh, all words in all the languages, but let's keep it to English are composed of. So like we have 26, uh, um, letters letters in the alphabet. Uh, we have sort of a set of, uh, phones and phonemes, uh, in each language. So the letters in the alphabet, especially in English, only roughly correspond to the phonemes. Um, and so, uh, what you have to do is you basically, there's also there's phonetized alphabet and so on. So the point is phonemes are basically like the letters of the language, except they're really corresponding to how we pronounce the language. So like a is a phoneme, right? And this, uh, is of course repeated in so many words, right? So it's like some, some unit that, that is like the minimum unit that is repeated.

**Bertrand:** So you mean a, a being not the letter, but the sound like a, y, if you were spelling it, right?

**Gerald Friedland:** Exactly. So a and a is different, right? While the spelling would be made probably the same in English, you never know, but it would probably be the same. Yeah. Yeah. But these, these, these are also, you know, meaning bearing. Uh, and, and so that's, so when they have me, when they bear meaning, that's when they called phoneme. And when they're just basically a random sound, it's called a phone. So there's also, it's, it gets tricky at some point.

**Dave Jones:** And it's not just a matter of joining them together. You also have to add a little delays here and there, right? As, as well.

**Gerald Friedland:** Right. So, and also then in depending on the language you're using, there is, uh, of course, like sometimes it makes a difference whether the, the, the stresses on different syllables, right? And stuff like this in English, we don't have that that much. Um, and then of course, if you would ever do Mandarin, there's tonality in there. So it, it, it becomes tricky.

**Bertrand:** Oh, right. Like ups and downs and diphthongs and all that other stuff, right?

**Gerald Friedland:** So, so exactly. So that's why for now, by the way, people often ask this, is there, how easy it is to do other languages? It's not that easy. Right now we keep it to English and, um, you know, if there's enough demand, we might actually take on the championship.

**Bertrand:** Do you guys do Esperanto? Any Esperanto? No, we don't speak, we don't speak minions.

**Chris Gammell:** I'm sorry. Right. Not yet. Not yet. You'll get there. Yeah. Not yet. You'll get there. No, we, and you know, and the, the, the one thing we really tried really hard to do, we wanted to do a really, really good quality, you know, uh, project board, because there are so many things that are really just average out there. We really wanted to kind of up the, up the ante on, on the result. And as soon as we start focusing on multiple, I mean, there's, it's only two guys right now. It's Gerald and myself, uh, doing this. And we just don't have the resources to go, you know, to do more. Uh, if there's an interest, we'll definitely look at other languages. We've actually had lots of requests for, you know, German, uh, uh, there's some interest for Spanish and, and, and French as well. These are sort of the easy European languages, if you will. Uh, I'm sure there's plenty of opportunities for others, but again, let's do the first one really well. And then we'll do the other ones afterwards. Yeah.

**Bertrand:** That's smart. Yeah. That's good.

**Dave Jones:** Now you guys actually, we should talk about this. It's a custom chip, right?

**Chris Gammell:** No, no, no. It's not a custom. It's not a custom chip. It's a, no, it's not. It's a company called All Winner. It's a, it's a Chinese. Oh, right.

**Dave Jones:** I thought you actually used them as a, as a, uh, like to actually do the custom chip for you. Oh, okay.

**Chris Gammell:** It's a general. Oh no God. I, that, that would require a different amount of financing. This would be a major Kickstarter campaign there.

**Dave Jones:** Exactly. This is a million dollar Kickstarter. I was going to ask about this. Yes. Like, you know, how has this come about? Right, right, right. So you're, so you're using this off the shelf chip from All Winner.

**Chris Gammell:** Is that right? It's actually, that, that chip is using a lot of, of, um, tablets and portable electronics on, uh, well, I guess non-Apple and non-Seption products. And, uh, what does the chip do?

**Gerald Friedland:** Well, the goodness about this chip is that it's initially designed for tablets. So it has a whole CPU in there, you know? So first of all, and then second, it also has audio input and audio output because tablets usually have that. Yeah. And that makes it very, very convenient, uh, to use.

**Chris Gammell:** So it's low, it's low power. It's, it's fairly inexpensive. Uh, it's an ARM Cortex, uh, eight, eight inside. So it's, it's quite a, quite a powerful, uh, CPU.

**Bertrand:** Oh, I see it now. Yep. Yeah. And that's the, that's the same company that, that, uh, that, that was used in the chip, the CHIP, that a $9 quote unquote board that was being, that's on Kickstarter right now as well. Is it the same one? That's right. Yeah. That, that we're having, let's not get into this. I think that we're here. No, of course, of course. Yeah. But, but it's the same company at least. And that's, and that's, that's basically how I'm trying to get it. So. Yeah.

**Chris Gammell:** They're actually a major, they're actually a major player. They're actually one of the largest, uh, well, I don't know if I should say that, but largest, uh, customer of ARM.

**Bertrand:** Yeah. No, no, no. I mean, yeah, it's, it's in lots of, uh, consumer level devices. I know that.

**Chris Gammell:** Oh, very, very, very reputable company. Actually. It's not very well known by consumers, but, uh, people, people on the hardware know them.

**Bertrand:** We had a, we had an article on, on our subreddit where we keep our links this week about, uh, cause all winter just came out with an eight or a, so you guys are using the 813, correct? Yeah. Uh, they also just recently released a 20, I think, or they announced the 20, something like that. So yeah, it's, it's very interesting to see this stuff. Cause it seems like, especially with all winter and these kinds of similar consumer level chips, these are the ones that are just moving super, super fast. Um, and I, I guess tied to that, does that end up affecting you guys because you, you know, you're using this chip. Is it going to be here in six months? I mean, or does that even matter?

**Chris Gammell:** So the answer is, uh, yeah, the chip is going to be there in six months. Uh, we've actually had discussions about this. Uh, actually that particular chip is used all over the place. So there's, uh, it's actually made, I think by TSMC and basically as long as there's demand, they will keep, uh, as long as there's demand and as long as they're, the process is available at TSMC. Uh, it will get manufactured. Uh, you know, you might have to go, you might have to go and buy 35,000 at a time, but, uh, it's definitely available. Now the, the good, the really good news, if you look at the architecture that we're using, you know, the, the underlying of what we're doing is, is really a Linux, you know, we're running a Debian on it. Uh, we did a whole bunch of things to have it boot in a couple seconds. Uh, so really if, you know, at some point, uh, it's very certain that this chip will not be available, but we'll have to go and use one of its, uh, you know, future brother. Um, you know, it will probably end up with a redesign of the board on the next generation, uh, and, you know, recompile and keep going. Yeah.

**Bertrand:** So that's not really a showstopper. That's the benefit of doing high level, like programming like that. That's great actually. Yeah.

**Chris Gammell:** And it's, and it's, and it's really a hybrid of, of low level and high level. If you think about it, I mean, it's high level in a sense that, yeah, we are programming at higher level. It's low level in a sense that we kind of control the hardware. So, and we like the idea of having just that running on that board. Um, it helps us control timing. It helps us control, uh, all kinds of things. I mean, you're doing real time speech recognition. You know, you want your system to react in 300 to 500 milliseconds. Uh, so you don't want, you know, all of a sudden, you know, a service interrupt, you know, servicing your screen. Right. Or you're dizzy. And also, again, the system become unresponsive. So that's one of the advantages of controlling the hardware. Definitely.

**Dave Jones:** Is there any, um, would your ultimate goal be a custom processor? Like I say, there are other speech, uh, recognition, uh, voice recognition chips out there, like the, you know, the HM2007 or whatever it is. Um, ones like that. Would you want to go for a custom if you could? Is there any huge advantage to that?

**Chris Gammell:** I have 25 years of, of doing chip design and custom chip designs.

**Dave Jones:** Yeah. Right.

**Chris Gammell:** And the answer is absolutely not. Unless, unless, unless, unless you're going to be selling millions of systems. Right. So there's, there's, there's a, there's a threshold doing a custom chip of something like this is a multimillion dollar undertaking. Uh, if somebody shows one, you know, if someone shows us, uh, that there is a 50 to a hundred million dollar opportunity out there for doing this and is willing to, you know, uh, finance us, Hey, I'll, we'll gladly take their money and go and run with it. But we're not there today. And, you know, we, you know, we're taking it one stride at a time.

**Dave Jones:** It just seems a shame that everything goes high level. Oh yeah. Let's just do it in a Linux. Let's just do it in an ARM processor running Linux, you know, you're, you know, Well, but there's good company there though. I know there is.

**Bertrand:** So my, my, my cell phone actually, I think it was one of the first ones doing it. Maybe not, but I know that the Moto X, I have a Moto X and it runs a coprocessor just sitting there listening for voice commands. And it's the same thing where it's a high level. It's just, they just, they don't like have a custom processor. I think they just doubled up the processor.

**Gerald Friedland:** Right.

**Bertrand:** I could be wrong about that, but.

**Gerald Friedland:** So, so, so I, to be frank though, that, that, that is the appeal for makers too. Right. I mean, what I like is when I saw this first, that really reminded me of the Commodore 64 really, where you have, you know, your basic, you had your basic, but then you had the peaks and pokes where you actually could actually directly access, access the hardware. And in some way it's the same thing where right now you have GPIOs and you can actually, you know, turn on and off individual lines. And, and I mean, you could, some of the chip, for example, is double, two or three functions on the same output pins. And so you can actually switch those functions, which is kind of interesting. We actually had to do this. It's part of the development. And, and then, and then you could create a costume kernel, you know, for in our case, for example, there's no TCP stack in it because we can, don't have internet on the board again. And so on and so forth. So you go very, very low level. And at the same time, you can run a bash script or a Python thing on it. So you have the full range of, of, of capabilities there. And you really, you own it, which is really interesting. And as far as I know, also the ACE 13 itself allows bare metal programming. So you could actually do it without Linux. Right. So that's killer.

**Dave Jones:** But it's still not power and size optimized for the task though. But to do that requires full custom and millions of dollars, as you said.

**Chris Gammell:** Yeah. It's a, it's a million dollar undertaking basically that, that can be justified if you're targeting particular markets. And I think it's, it's going to be really interesting. I mean, you know, I think one of the outcome of what we, you know, what Joel and I did is we're showing it. You really can do it and you can actually do a pretty good product out of this that, you know, I mean, could literally be in a lot of devices. Right. Cost is, cost is an issue. When you look at the kind of bill of material, you know, raw bill of material, and I'm counting everything, you're talking 10, 12 dollars, you know, of, of stuff in medium quantity. Might be 20% cheaper, 30% cheaper if you're building millions. But, you know, even if it's $10, you really, you know, it's, it's hard to justify that, that additional cost to a toaster. Now that I won't necessarily talk to my toaster. But so at $10, it's going to be adequate for some applications. But it's going to be way too expensive for other things. I think that's the reality. So at some points, once people realize, oh my God, we can actually do this. You know, if there are people out there who want to come talk to us, hey, we'll gladly listen and work with them to do something like this. But, you know, the first step was really to show people, first, it can be done, and it can be pretty cost effective for a lot of solutions. And yeah, I'm sure we can make it a lot cheaper. But yeah, $10 is killer.

**Bertrand:** I mean, that's, that's a really, I mean, like, $10 for a robotics project is nothing, right? I mean, that's, that's a server.

**Chris Gammell:** You know, that's, that's the bomb. That's the bomb. That wouldn't be how much, you know, the thing is sold for. Oh, I know, but even still, I mean, like, yeah. You still have to do everything else. But that's, I mean, the incremental bomb, bill of material for somebody who's already doing a board and the assembly and everything else would be of that order.

**Bertrand:** Right.

**Chris Gammell:** So, yeah, it's, it's a pretty cheap add-on, really.

**Bertrand:** Yeah.

**Dave Jones:** So is this all open source? Is this open source hardware or are you guys actually starting a company and the technology is proprietary?

**Chris Gammell:** So we're actually using a lot of open source software to do all this. Yeah. Yeah.

**Dave Jones:** I'm more talking about like the, the algorithms and everything else.

**Chris Gammell:** So all the algorithms are open source. There's, I mean, there's a lot of, a lot of packages we're using. We're actually going to put everything on the site once, once we actually release the product, because first of all, we have to, and we want to give credit to where it's due. A lot of the know-how is really how you put all these things together and getting it to work. We're not entirely decided yet how much of it we want to, to share at this point. You know, and the hardware itself is fairly straightforward. I mean, you know, it's, it's basically a credit card. It's a big ass processor with a half a gig, half a gig of memory and a four gigabyte, you know, SD card. Okay. Well, there you have it. As I mean, you know, we're attending, we're going to a conference next week and we're showing, you know, what, what it is exactly. So there's really no secret there. Right.

**Bertrand:** And that will be ESC we should mention because some of our listeners may be going. All right. Yep.

**Chris Gammell:** That's right. Yeah. In Santa Clara, California. And so at this point, we're not, at this point, we're not open sourcing the actual flow. That's, that's the one limitation we're doing.

**Bertrand:** Right. That's okay. I mean, like, yeah, I mean, like where you, everybody's going to make the decision about where, where you're going to make the money, where you're going to make the decision to be open or closed. It's fine with me. I mean, like you guys put a lot of work into this, so, and, and so like, so when, when you say open or close though, like, so when, when you think about this into the future and we talked about the bomb costs as well, do you envision this being always, like, do you envision licensing this out as a, you know, like buy this processor, have the software stack, you're good to go. You basically pay a license fee type thing or, or how do you envision it working?

**Chris Gammell:** So, you know, the, yes, that's, that's the next step for us in some respect. I mean, some people, there's really two types of, of, of users in, in, at least in our experience. The one that just want, you know, here's the board, you know, they're, they're, I call them the system integrator, basically. It's like, oh, I've got this great idea and I just want to buy a board that does this. And they don't really care about, you know, saving money there really, if you will. So there's, I can, but the, obviously the other, the other model is to license essentially the stack and, you know, basically have people talk to us. We'll, we'll show them exactly, you know, how it's done, what it takes, how to implement it on whatever platform you have.

**Bertrand:** Put this process on your board, put those other stuff and install this, right?

**Chris Gammell:** Exactly. I mean, basically we'll be holding their hands. Because, you know, we, we have the expertise and, and literally in a few days we can get this up and running on, on your particular Linux distribution or on a core of your, you know, a Snapdragon from Qualcomm or something like that. There's plenty of ways you can, you can do that.

**Dave Jones:** How much processor grunt do you actually need? Do you actually need a big, um, Cortex I8 or whatever it is and, you know, working at gigahertz or hundreds of megahertz? Can, can this be done like lower end? What's actually driving the response time there?

**Bertrand:** A couple op amps and like some TTL on it? Or what are we talking about?

**Gerald Friedland:** So, so, so, so the answer is, the answer is yes, but at what quality? And so the way I did this. What are quality? Someone is speaking. We know this much.

**Bertrand:** There is definitely sound going on. Or is it a dog barking? I'm not sure.

**Gerald Friedland:** So, so, so, I mean, you can build a board that just like to, let's say, discriminate between yes and no, you know, that would, that would be not hard. Maybe not even, uh, maybe even speaker independently, that will be not that hard. But we do really, I mean, we can do hundreds of sentences and, um, we, we give the soft limit. There are 200 sentences, which is our limit. Like, this is where we stop testing. Um, you know, if people manage to put on more, we have no restriction on there. Um, and the major point is that we not just. We have a lot of models in there. So we have the, again, the acoustic model, which is basically matching these phonemes. But then there's also a language model in there. So basically, we, we built the language model based on the sentences so that when you recognize a sentence, um, when, when you say a sentence, um, that it's, it's, it's similar to another sentence based on the similarity. You know, we can still match it, for example. But then also the point is that if it doesn't get it a hundred percent, it will try to match it against the sentences it has. And so there's, there's this acoustic model, a language model as a matcher. And if you combine all these two, then you get the quality up. And of course, the more you add models and the more you add algorithms to make it better, the more you need CPU. And right.

**Dave Jones:** Because it's a brute force type approach. Like if you've put in 200, uh, sentence commands in there, it's got to search all 200 until it finds a match. Or is it more advanced than that? Can it narrow down the options? Yes. Yes. Which ones to search?

**Gerald Friedland:** So there are two ways. Uh, actually we give two options to the, to the programmers. Um, one option is to do the raw recognition. So for example, if you train it to recognize one, two, three, then, uh, you can recognize two, three, one or two, two, three or one, one, three as well. Right. Um, but the language model will favor two, two, three, uh, in some way, because if you, if it basically says two, two, um, uh, it sounds like three, then it's going to be two, two, three. Um, and so the other thing though, is this, this is the first model we call this raw output. It's very, very useful for passwords. For example, if you actually want to ask for a password, you do it this way. The other mode that we have is you say, no, I actually want an exact match. And that means we'll, for all the sentences you put in, if you say two, two, four, and the only other sentences that has two, two, send it is two, two, three, then we'll force match it to two, two, three. Um, because you say that's the closest one, right?

**Bertrand:** Um, does, does this mean that the, uh, the higher likelihood of success for, for programming this as a user? Would not be to sing, have single words, but instead to have sentences because there'd just be more matching criteria against the sentence versus a single word.

**Gerald Friedland:** Yes. And that is the beauty of language models. So in fact, you know, if you say light on, light off, you, because it's just on and off, you know, these two words are very, very similar. There's really just one phoneme different differentiating it. It's way harder. But if you say, you know, make it bright versus I want to sleep, it's going to be, you know, basically accurate. Yeah. And that's, that's the beauty of language models.

**Chris Gammell:** There's one thing I want to touch on. Uh, you were talking just earlier, cause I'm not sure we quite answered your question regarding the, the CPU power. There is one very important thing, which is the overall response time. So we don't use a hundred percent of the CPU obviously, but when we do recognition, we want a quick answer. So if you're actually having a dialogue with you or you're talking to the, the, to the board and you want to answer, you know, we expect a, you know, half a second response time, basically. You know, if you have to wait five seconds for the board to decide what it heard, it's unbearable. And it's, it's completely, I mean, the human interaction is, is horrible. So we need that amount of power to essentially get that response time, which is within a very acceptable, um, human interaction, uh, expectation.

**Bertrand:** Right. If you had a, if you had a butler, you'd expect about a half second as well. Right. Yeah, exactly.

**Chris Gammell:** I mean, you don't want to feel like you're talking to somebody who's on the moon and have a six second, you know, response time.

**Dave Jones:** Where is at what, you know, is there a, is there something that's a real bottleneck in the software to the process in time? Um, or is it just a whole combination of a whole bunch of things?

**Gerald Friedland:** Um, it's a whole combination of a bunch of things. Um, but also we, since we allow training, you know, when you pass it 200 sentences right now, you have to wait, you know, 20 to 30 seconds. So that training process is, takes long, but again, the training process is only done once sort of, you know, when you change the sentences, um, basically once per project sort of, right. Um, or if you update the project. Um, but, um, uh, in reality. It's, it's, it's, we want to have a smooth response and like everything else. Like for example, if there's more noise, um, you know, you have to take care of the processing takes a little longer and so on. If you want to just basically be, be able to smooth to respond, uh, to whatever comes in there.

**Dave Jones:** Um, how do you deal with, um, echo and things like that? Like if, you know, you've got an omnidirectional mic on the board and somebody's, you know, all the way on the other side of the room shouting and rooms, there's not much furniture. It's echoing like battery.

**Bertrand:** Podcast you're talking here.

**Dave Jones:** We need to be easy.

**Chris Gammell:** Yeah. You guys are audio guys. I can tell. Um, so echo is an issue. So what we did is actually, we, we put a lot of care. The, the, the, the board we're doing is more than just, uh, a computer board that we spend a lot of time on the audio front end as well. Uh, we want a system. You can actually talk from, you know, a distance that would work from literally a few inches away to about 12 feet or so. Um, it really depends on the room condition. Now, ideally you don't have echo. We don't do echo cancellation. Um, the onboard microphone is just an electric microphone. It's, you know, it's, it's fairly broad in terms of its pickup. It's omnidirectional. Uh, there's no, we don't, we don't do echo cancellation. So if somebody had an application where there is echo, one of, one of several things is going to happen. Either it's going to reduce the range at which they can talk considerably. Literally, they might have to be just a couple feet away when you talk to it. That's, that's, that's a real issue. Alternatively, we, we offer, you know, they can actually put a, uh, we have, uh, you can put an external microphone and bypass the internal one. Uh, and then you could put a, uh, you know, uh, an array of microphone that, that does echo cancellation basically. Right. But this becomes, this becomes very project specific. And so, you know, we can't solve every single problem. We, we can't have went for, for, you know, I would call the most common case there. Uh, we think it's going to work. It's going to actually, we know we've tried it in a lot of condition. It works really well. Uh, there's cases, for instance, where loud environment, when we were at maker fair, uh, the average, the average, yeah, we had a db meter that recorded an average of, uh, 82 db.

**Dave Jones:** Oh, wow. Constantly.

**Chris Gammell:** So there was absolutely no way you could talk to it, you know, at 12 feet. And here we had to use, uh, a headset, but with a headset, it worked, it worked perfectly. I mean, actually, to tell you the truth, we were, we were a little skeptical at first, and then we're actually, uh, very pleased how well, um, the audio front end responded to that. And, uh, I mean, Chris, I'm not sure if you got a chance to try it there, but.

**Bertrand:** I did. Yeah, yeah, yeah. I did. So can you tell us a little bit about the front end? I mean, is it all built into the silicon, uh, on the A13 or is there external op amps? No, no, it's external.

**Chris Gammell:** It's external op amps, basically doing, doing good, uh, automatic gain control and, and other things as well.

**Bertrand:** So what, what kind of op amps, I mean, like what, what's on board? I mean, is it just an ADC or the AGC auto control op amp? Exactly.

**Chris Gammell:** We're using a good quality AGC to essentially, I mean, the idea is you want to be able to, to pick up something that's in a quiet environment. You want to be, you know, pick up the sound. So the basic principle there, you know, when it comes to audio, especially speech recognition is, you know, garbage in, garbage out. If, if the signal that you're getting in is, is terrible, your speech recognizer is not going to do anything, say anything good. So you have to get good, uh, good audio, uh, input, uh, and try to essentially normalize it. Um, the advantage of doing it in analog, if you will, is that, um, uh, you get a very, very fast response time. So if somebody starts shouting, you, you adjust, you know, immediately. Uh, a lot of the, uh, ADCs that, that these built-in, uh, CPUs have are fairly low quality. You know, they can do one or two bit adjustment. But it is 12 bit, it's not going to give you any, you know, if you had a 24 bit, you know, ADC in there. Yeah. You might be able to, you probably would be able to do it digitally, but that's not the type of, of, um, of what we have.

**Bertrand:** So are you, are you willing to, uh, tell us what the part number is or do we have to wait for Dave to do a teardown for this?

**Chris Gammell:** Uh, no, you'll have to wait till we get the board out. Ah, come on. Yeah, I know, I know.

**Bertrand:** We're going to get there. We'll get there.

**Chris Gammell:** Well, you'll, you'll get there. You'll, you'll get them. You'll get it soon enough.

**Bertrand:** Okay. Okay. So some, some, some form of, uh, the audio AGC. Exactly. Exactly. You know, I've had bad experience. So Dave knows this as well. So we, but both Dave and I have an, uh, H1, um, uh, recorder for audio stuff. And the auto gain on that thing is terrible. I don't know if it's just the, I think it might be a digital algorithm type of thing where it's, it's so discreet. It just steps it up and it's like, it's like, you can, you like hear it when you, when you listen back to the recording, it's like, it's like, hello, this is Chris. And I'm now in a bathroom and blah, blah, blah. You know, and it's just like, it's terrible. It's just like, it steps up like that. So how do you, how do you deal with that? I mean, is it, is it gradual?

**Gerald Friedland:** Yeah. So the issue here was that was actually quite some work to figure this out. Um, especially against the closed circuit that we don't know from A13 because A13 has a, has a microphone input. And we didn't know anything about it. I mean, if you find something out of work, please tell me. Right. You can't, you can't just go listen to it. Right. So I, I remember, uh, several oscilloscope sessions, um, that we had on this. And we also, uh, also like trying this and see the other problem that we have, um, um, is that, so now you distort the signal. Right. Um, because while it sounds good to humans, speech recognizer might not pick this up so well. Right. So, um, we, there was a lot of testing involved. Um, and this is partly why we're trying to say let's wait a little bit because we're kind of proud of the solution. Um, so it's, it, that was actually hard. Um, that was, that was a hard part. Um, a couple of months of testing until we got this right, but it was totally worth it. So, I mean, um, the, the robot example, for example, that you see on the video that we just posted with, uh, Romibo would not have been possible, uh, without, uh, that part. Because, you know, when, when we have, in this case, like the microphone is inside the robot and there's a fur around it. Yeah. Yeah. Right.

**Dave Jones:** And the person that's a nice windshield. Yeah, exactly. It's a high-pass filter. It really is. It's a high-pass filter. Yeah, that's true. Yeah. It's a totally, totally excellent dead cat built in, you know. Yeah.

**Gerald Friedland:** Well, that is kind of true. The thing is, you don't really need a windshield when, when you're inside and you're actually, you're just sort of 12, 12 to 12, 12 feet away, pretty much, uh, what it was. And just said, you know, Romibo come here and it just works. And, you know, in some ways I'm, I'm always surprised myself that how well that worked. Um, but it was basically the result. And I, I totally texted this to Patron. It was totally the result of, you know, us fiddling with it until we got a nice, uh, audio front end.

**Dave Jones:** That's, yeah. So what frequency response do you need for speech? Yeah. That's a good question. Recognition. Yeah. Like, is it, is it, is it the classic, you know, 300 Hertz to three kilohertz phone? No, 10K. You need, you need those, those hard consonants, Dave.

**Gerald Friedland:** Oh, tell us. Come on. I tell you, no, so no, I mean, uh, yeah. So that was basically telephone speech a long time ago. Um, the three Hertz to, uh, no, what we have is, uh, we usually, for, first of all, we sample at full rate, which is 40, 40, 44, 100 or so. Basically city rate. Because we can, right. Because we can. Right.

**Dave Jones:** Of course. Right. But we're talking about what is the minimum requirement.

**Gerald Friedland:** Yeah. All the models and everything is usually in speech recognition is now trained at 16 kilohertz sample rate. That gives you, that gives you like a, sort of a 50 to, to eight kilohertz, uh, you know, sampling, um, uh, frequencies that you basically can pick up. And you need those higher frequencies for S for distinguishing of S and T and so on and F, you know. And actually F is so important. Turn off, you know, you really need that. Right. The trailing stuff, right?

**Bertrand:** Or start. It's very important. Start. Instead of start, it's start. Yeah. Right?

**Dave Jones:** And for guys like me with a high pitch voice. Yeah. Well, yeah.

**Speaker ?:** Right.

**Chris Gammell:** Yeah. So actually you're bringing pitch, which is really interesting. Um, so the models, the models were, the models we're using for training are actually all adults. I mean, we're trained by adults. And so what, what we've, um, realized, and it's interesting because, you know, we're trying, we're targeting at least the maker community and there's a lot of kids there. Uh, and it's a, it's a great, uh, it's the, the board is really great, uh, you know, telling boys ages because essentially, um, if they haven't hit puberty, it's, it doesn't do anything. It doesn't do anything very well for, for boys. They really have to get that lower voice, uh, to really get things to work. So it seems to not work very well for boys under the age of 12. Uh, after, after 12, it works right. But for girls, it works at much younger ages. So girls usually eight years old and older seems to work without a problem. It's very interesting. And, and it's just, and it's not that, that the, uh, it really has to do with training more than anything else. Because the, the sampling is adult voices for all kinds of legal reasons.

**Bertrand:** So one thing I also wanted to ask about is the, uh, so you mentioned response time previously, and you said about 300 to 500 milliseconds. What, what actually is that stack up? Can you tell us about the, the, you know, okay. So from the time when that five, 50 Hertz to 16 kilohertz hits the, hits the microphone, goes to the AGC, very minimal delays from there. It gets into the ADC. What happens then? Like all the way up to the top level. Um, well, yeah.

**Gerald Friedland:** So, I mean, basically we, the, the kernel of the operating system sends us the sound data and packets, right? Okay. So.

**Dave Jones:** Oh, so, so is it as, as, is, is it as the person is speaking or does it wait until a pause at the end of a sentence? No, as the person is speaking.

**Gerald Friedland:** No, it's sending packets constantly, right? So you have to practice packets all the time. And then, yeah. And then the first thing you need to figure out is the person speaking. Okay. Um, so, um, in, in our case, what we'll do is we do this energy based and there is a, a fixed threshold built in, but you can also modify that threshold. Okay. And, and it's actually, uh, it's sort of tries to be a little intelligent because we know we have a model in there that knows how language typically works. So we, for example, know that if it's something super short, like it won't be a word, right? Did you hear that actually? Yeah. Okay, good. Okay. Um, or, or if it's like, uh, ongoing, never changing for 10 seconds, that's not a word either. Right. So there's some, there's some intelligence in there. Actually, that's yet another model that needs to be calculated. Usually don't even mention that.

**Bertrand:** So can you, can you give things? So like an example be like someone saying no, like currently saying no, or someone saying like, like screaming, like, ah, like, is that like kind of the difference you're talking about or what?

**Gerald Friedland:** That's the difference I'm talking about. Yes. So, because usually words are like sort of half second or a good of a, like half a second long to like two seconds long. Right. Depending on the long word. Germans have very long words, but we're English. Yeah. Right. Um, and, and then also there's, there's some short pauses and then there's longer pauses. And these longer pauses really usually indicate somebody's done with speaking.

**Bertrand:** Okay.

**Gerald Friedland:** And, and so you have to catch up to typically how dialogue works. Um, and, um, this is also something we can do in contrast to when you have systems that are trying to transcribe stuff because we talk to the machine. And, and in fact, there's always a little bit of an adaptation going on with the human towards the machine. Um, but this works pretty well. I mean, you know, you see all the examples that, you know, they work with that. And so once we have figured out, okay, so that's likely some speech, um, we'll basically, uh, need to recognize this. And in order to recognize this, we, we, uh, extract features. And then we use acoustic model to try all combinations of phonemes that this spectral envelope could represent.

**Dave Jones:** Right. I was going to say, is this done in a spectral form? Do you like FFT this and then you look at the spectral density in each frequency band? How does that work?

**Gerald Friedland:** Sort of. So what we use is what everybody uses these days is MFCC features. MFCC features stand for mal frequency capsule coefficients. And capstrom is an interesting word that is actually like spectrum, except not, right? This is kind of a word, right? And if you look that up, actually, that's, that's very interesting. That's exactly what that is. So what it is, is, um, you do, uh, uh, basically you take the logarithm, then you do an, uh, DCT. And then you do, um, uh, what's called a mal spacing. That means you do, you weight the frequencies according to typical hearing. So like lower frequencies, uh, are perceived differently than higher frequencies. And so you basically do this weighting. And then, and that's the interesting part. You do a DCT again. So you take a DCT off the DCT and this is a total hack, right?

**Bertrand:** So DCT, we should also mention, sorry, we should also mention DCT is district cosine transform, which is similar to an FFT, basically binning frequencies, right?

**Gerald Friedland:** Yes. Then the more important part is that you don't come up with complex space. If you have an FFT, you have a complex values and non-complex and real values, and you don't want the complex values because it's just so much data. We want to do data reduction. Um, so you do that. And what you end up with is, is basically an interesting hack. So the reason I, what you actually want to do is you want to look at this, at the spectrum, but the reason we use Capstrom is because it is even less data. And you basically look at, so what are the peaks in the spectrum, right? Because basically now you're fitting, uh, again, cosine curves to, to the, uh, to the spectrum. So you find out what are the peaks in, in the spectrum. And so you look at way less values. And I don't want to explain this trick here because it's really old. It's like, I think 60s or something. And that's what, what everybody does. And as an academic, I could tell you how bad it is, but the point is, it's what, it works. It works and it's what everybody does. And so I'm, I'm, while we've, we've been trying and I have publications on this to replace those features. Um, you know, it's just work. It's really just what everybody does. And so you have these. We don't judge you here.

**Bertrand:** Dave and I use things that work all the time.

**Gerald Friedland:** So that's basically the point. So you have these features, MFCCs, and then with those features, usually you match them against these phoneme models. So you try to find out your sort of, you know, this, this capsule feature, it could that be that phoneme or that phoneme. And so you come up with a whole combination of phonemes for that particular region that had high energy. And then you take the language model and say, okay, which of these combinations is the most likely? Because we know the sentences that are most likely in there.

**Bertrand:** Yeah. It's almost like a paint by, at least in my head, the way it seems like is like you already programmed in. All right. The, the, the sentences, Chris is better than Dave. That's, you know, that's, that's a set of 20 phonemes. Like it's like 20 or it's, there's like, you know, and they're all coded, right? Each of the phonemes is coded as, you know, A, F, G, H, I, E, whatever it is. Right. And then you go and match against that model. Is that, is that sound right?

**Gerald Friedland:** Yeah. That, that's pretty much sound right. So that's the point. And then, and then, um, you, you, you come up with all these sentences and then, so we do this on a phoneme level and come up with words, right? So as I said before, you could have one, two, three as a training. And if you said two, two, three, we would actually recognize two, two, three. So that's the first output. And then the second output would be to match two to three. If you basically ask for that to forcibly match it to one of the sentences that you were trained in. So that's the whole process.

**Dave Jones:** Got it. So would it, because you're continuously, um, listening, like there's no, like a button that you push and go, right, I'm going to recognize, I'm sure your job would be much easier if you got the user to push a button and then speak and then know that's the start of a thing. What is your, um, false detection rate? Like have you programmed in, you know, a few dozen sentences and then just left it running all day to see. And in like in an office where people are talking all the time to see if there's any false output.

**Gerald Friedland:** Yes. So, um, there's a couple things to say here. Um, first of all, you can do push to talk if you want to. So we, we program the API in such a way that you can either call a call, uh, put in a call sign or you can put in no call sign. Um, then it will react to any noise, you know, as soon as you raise your voice, it will say, Oh, that's, that's me. Or you can, you can not do this at all. And you can basically, uh, just say, don't do any recognition at all unless I tell you. Right. And, and that means that if you install a button to the Arduino board and then you basically question that button and the button is on, you say, okay, now, now do recognition. So you can actually do a push to talk. But, but, but the call sign is.

**Bertrand:** Well, in your example, you also show like the videos that you guys have on the Kickstarter page, you have like a thing that says computer or, you know, what if. Yeah.

**Dave Jones:** That's the thing I was going to say, like the, like the Siri, like you say Siri, because that's the trigger keyword. So you don't have to search everything else.

**Chris Gammell:** It's exactly that. So the call sign really helps you get the false triggering down to hardly anything. It's actually, so in our case, the call sign is programmable. Uh, you, you can pretty much use anything, but there are some sort of, if you wish guidelines and the guidelines there typically is, uh, try to avoid like the five most, you know, 500 most common English words because otherwise it'll get triggered by just standard conversation because it's actually really good at picking up the call sign. Um, typically three syllables tend to work really well. So actually Siri, when you use it, it's actually, Hey Siri or Amazon use Alexa, which are words, you know, that are really nowhere near close to anything else. Right. Uh, when we did the robot, um, uh,

**Dave Jones:** So you can go like, Hey stupid robot.

**Chris Gammell:** Well, so actually though. Yeah. With the robot example, we actually just posted, uh, it's called Romibo. So we actually program Romibo in there and Romibo really doesn't sound like anything else. And it picks it up just every single time. It's, it's, it works really well.

**Bertrand:** What if someone was reciting Shakespeare and they're like, Romibo, Romibo, where's the Ratho Romibo?

**Gerald Friedland:** You screwed. Then you have that problem. So, so, and that's why, so in terms of the second question with measuring the accuracy is so, I mean, you can definitely get into, uh, human accuracies with the system. Um, of course though, you can also screw it up. I mean, that's the point of being a maker. It can fail. Um, so, I mean, again, if you make the call sign like, uh, two or a, or some of these words that we use all the time, then guess what? It's going to react to it all the time. Um, and also if you basically program it with 200 sentences, but they're all distinguished in one syllable. Well, good luck. I mean, that's just fine.

**Bertrand:** I command that you blank. I command that you blank. I command that you blank.

**Gerald Friedland:** Exactly. Exactly. Exactly. That's it. And the point is though, I challenge you then if you do that and you complain to actually try that with a human because a human actually is not a hundred percent either.

**Dave Jones:** No. No.

**Gerald Friedland:** Right. And, and, and of course the typical things make it worse. If you have heavy accent, you know, it makes it worse. And if you have a lot of noise in the room, it makes it worse. Um, you know.

**Dave Jones:** Or if people aren't paying attention properly, they're not, you know, they're thinking about the next thing they're going to say. Like we often have that here on the amp hour because we're, you know, constantly trying to communicate to people and we're trying to, you know, we might miss things and, you know, because we're thinking about some question we're going to ask next.

**Bertrand:** Dave, I have never missed a sandwich before. That's what you said, right? Sandwich? It was something about sandwiches?

**Dave Jones:** Sorry? What? What's that? Chris, I was too busy thinking about what I was going to talk about next. Yeah, exactly.

**Bertrand:** Sandwiches. So I was actually, I was wondering about this. So what about like, so, so obviously it's sitting there monitoring all the time. What kind of like power consumption? I don't really know. I don't know much about the A13 itself, but what kind of power consumption is it just to sit there monitoring and listening? Because I would think that's a, there's no sleep mode. It sounds very active. Even if you are just listening for a certain keyword or call sign. So, so.

**Gerald Friedland:** What does it take? We, we usually say it's three Watts power consumption. In general.

**Dave Jones:** Three Watts. You can fly to the moon on three, three Watts. Yes.

**Gerald Friedland:** But. But can you, can you tell the rocket to go there, Dave? No. Yeah. Well, no. But the point is that it is in fact taking less energy if, if it's just listening versus, for example, if you're training it. And we actually could actually, that's something we actually might do just actually release an energy profile of, of this thing, which we haven't done. But we have internally looked at it and it's actually interesting. It's something that I learned in this project is that it, you can actually, you know, usually you know, when you study computer science, we tell students to like, you know, runtime is important. Well, runtime is important, but when you do small devices, energy consumption is also important. So you can, based on the algorithm you're implementing, the, the, the energy consumption changes. And so we actually took this into account a little bit when we created this. And so actually that's something to do. It's a good, good hint for us to actually release the energy profile for it. One, one.

**Dave Jones:** Can people slow it down and trade off response time versus power consumption?

**Chris Gammell:** It's a good question. Good question. Not yet. No, and this is not the way, this is probably not the way you want it. You would want to do it. It's a stretch goal. It's a stretch goal.

**Speaker ?:** That's right.

**Bertrand:** If we hit $50,000 on Kickstarter.

**Chris Gammell:** We will have the power consumption. No, but there, I, I agree with you, Dave. There's definitely applications where, I mean, if let's say you wanted something like this that's going to be battery operated and you want to change the battery once a year type of thing, then essentially you'd have to, you know, essentially you would, you know, stop the CPU, put it in deep sleep, if you will. And then you just keep your analog front end and whenever you get the right energy. You wake up immediately, you do some processing and you shut back down. So these are techniques that can be done. We haven't, you know, this is another level in terms of complexity. We haven't gotten there yet.

**Dave Jones:** I was going to say, is there, could you implement like a two processor solution where you have a smaller, lower power processor just hooked onto the front end, which recognizes your keyword and then it wakes up the heavy duty processor to process the, you know, main sentence and things like that? No, there's no advantage to it.

**Chris Gammell:** Because essentially you'd be duplicating, you'd be duplicating everything twice. You'd be duplicating the effort. Right. I think just looking at energy level and whenever you get a spike in thing.

**Dave Jones:** Unless you had a fixed keyword, right? Maybe if you had like a fixed keyword, you could program that into a low power micro. Possibly.

**Gerald Friedland:** I think the reason, the real way to do this quickly is push to talk, right? So you basically.

**Dave Jones:** Of course. Oh, that solves everything. Yeah, exactly. Yeah, right. Right.

**Chris Gammell:** But I mean, these processors have sleep modes. So I'm sure there are ways of doing it. You know, we've been in the process of solving a lot of other problems so far. Yeah, that's a lazy problem. I think that this will be sort of the next generation afterwards. Or if someone comes with a particular application, we'll be glad to work with them and do that specifically. But I think what's interesting is, you know, once people realize, oh my God, you can actually do this on something that's the size of a credit card, you know, then you start thinking about all the other things you can do with it. And, you know, that's, I think, what makes it really, really interesting. And for us, it's, you know, we're finishing the first leg of the journey and we have a lot of ideas afterwards. Well, that's okay.

**Dave Jones:** So you guys are aware, you've reached your goal, right? Yes. But you're, everyone's, of course, secretly hoping, is there like a secret goal that you're hoping for? Oh, like we really, we asked for 12 grand, but we really need 50 otherwise, you know. No.

**Chris Gammell:** So otherwise, you know, that's, so I'm going to tell it as it is at $12,000. We will be losing money in the process.

**Dave Jones:** Okay. Yeah.

**Chris Gammell:** We really would like, we really would like to be at 20,000. You know, I mean, to us, this is, this really was, the goal of the Kickstarter campaign was really to engage the maker community to see what the response was. We've been, we've been really getting a lot of really good feedback, questions from people. I mean, we had someone come back to us and say, Hey, my, my cousin is paraplegic. He can only make sounds, you know, with this work, you know, and sadly enough, the answer is probably not, but we actually have been working on sound recognition. So it's actually a problem that we know well, and there might be a way for people like this, but this is, this is for us a way to engage the community and make sure that we come up with something that, you know, people think, first of all, Hey, it's pretty cool. And I could actually use this, uh, that, you know, and we want to engage them. So part of it is, you know, engaging the community, part of this marketing, getting our name out, uh, you know, getting to people to realize that this kind of stuff can be done. Uh, and now you can start thinking about, you know, what you're going to do with it. We're not in there to make, you know, end product. I mean, this is, and this is always a difficult part of Kickstarter campaigns, which is not, you know, an end product where people can just buy it and put them around, right. You know, we're, we're selling a board, which in itself will do nothing unless you're a maker and you're actually going to do something with it. One thing I want to mention by the way, is that, you know, we picked Arduino as a platform because there's millions of them out there. It's a great platform, but the basic way the Arduino talks to the shield is actually via an RS 232 interface. So for people who actually know a little bit of that serial communications, and I'm sure there's a lot of people out there, there's no reason why you can just use the board and, you know, talk to any other system. So you could connect to Raspberry Pi, you can connect to your PC for like here, or these the RS 232 is not as common. Uh, but it's, it's very easy to use on other, uh, platform and we will be releasing kind of the low level, um, serial, uh, commands, uh, you know, uh, to be able to do all these things at a low level as well. I said the library you're saying, right? So right now you're in the library. Yeah, the library provides a really nice way, you know, a higher level, uh, you know, to interact with the board, but you know, all the low level commands will be, will be made, uh, will make that available. So people can really, I mean, I don't want to call it hack it with hack the board because you're not going to be able to go change the software inside, but you'll be able to do some, some very cool stuff with it that you may not necessarily be able to do with the, the higher level. Yes.

**Bertrand:** As one last question about software. So, I mean, like, so all this stuff, I mean, you, you guys had mentioned, let me just look at my notes here. You had mentioned, uh, this MFCC, but like, what is all this written? I mean, like, so the, and you said, this is all in a Debian system, but like, is this all Python based or what is, what is the main languages this stuff is written in? Is it all custom or what?

**Gerald Friedland:** I, you know, I like this question because I get this question all the time and I'm, I always tell also, you know, to my students, I tell them, look, a real system is composed of whatever you can take. Right. So there's like when people buy a robot at the first, it's sort of MacGyverism really. Um, yeah, yeah.

**Bertrand:** It's made of hot glue and popsicle sticks.

**Gerald Friedland:** I mean, when you, when you build a robot, you have to take whatever part fits and this is the same way. So, um, this is, uh, there is, uh, you know, again, he's going to say it's Fortran, Dave. No. Okay. Good. No. That is about the only language that is not in there. But it's, it's made mostly, uh, uh, C for all its thing that's low level. Again, there's a costume kernel and so on. So I needed to go into sound drivers and so on. And then, um, there's a lot of Python to glue things together. Um, which is usually a good way to glue things together. Yeah, definitely. Yeah. And, and there's a lot of shell scripting too. Um, so the other thing is, for example, a board like this needs to start up, uh, a little faster than let's say, you know, your typical Linux boot of a minute. Um, so you need to do a lot of scripting and optimize scripts, uh, in this regard. Um, so there's from basically, honestly, from very low level C programming, uh, up to, uh, very high level shell scripting and Python and C and C plus plus. And of course, you know, you have your Arduino code that I, that you create a C plus plus for library. Yeah. And it's sort of this Arduino ish dialect for Arduino. So it's all in there. It's, it's, it's, uh, it's multi-language, multi-cultural.

**Bertrand:** So, so, but what you're mostly saying is that the, the user won't really have access to nor will they need to have, uh, this kind of access to the, to the lower level programming stuff or even the high level programming stuff on, on board. It's kind of just a standalone solution and you kind of throw it chunk commands through RSDW2.

**Gerald Friedland:** Well, so, I mean, basically I'm saying two things. First of all, all the Arduino stuff is going to be completely open because all the Arduino stuff is open anyway. So on the Arduino side. Um, but then also again, all the open source stuff is open because, uh, not only do we have to do that, but it also is absolutely sort of in, uh, my intention to always keep open what needs to be open. But what I'm saying though, is it's not that easy for somebody to go just in there and change it because it's such a pottery of, I mean, the real work here is to integrate it in a smart way. Right.

**Bertrand:** It's interdependencies and stuff, right?

**Gerald Friedland:** Right. Interdependencies. So if you look into it, it's not easy to, it's not like, actually that's the thing that it might be open source, but it might not be helpful to be open source because you're like in there, it's like, Oh, I need to know how to configure a speech organizer, a Linux kernel at this and this and this and this. And there's a lot of work. Um, and so that's basically our work. That's basically what it is, is we have, we, we basically create a solution where all this configuration complexity is hidden and just basically all you need to do is do it with an Arduino. You know, and that is basically the, the, the, the magic here. Right.

**Bertrand:** Got it. Cool. Nice. Well, uh, this, so how soon is this thing coming out? Because we should probably wrap up here, but I, I, I really want to get my first thing that I want Dave to go into these so I can find out what this AGC chip is. And the other thing is I want one of these, I'm building a robotic product project right now and I want one of these for my robotics project. So how long until we can get one of these things?

**Chris Gammell:** So, um, right now we're, uh, our early backers will get boards in December, the production boards in December. We will get our own, we'll get our own prototypes probably in September. Uh, then we get a, you know, call, you know, call and do all kinds of great thing to make sure it's all, uh, all good. But the, uh, the first 120 backers will get their board in December and then the rest will be available, uh, probably in February, uh, 2016.

**Bertrand:** Nice.

**Chris Gammell:** But, uh, the, the, the engineering, I mean, the, the hardware design is, is done at this point. Uh, you know, we're, we're done with it. We're, we're still, we're still doing the, the, um, you know, some of the Arduino sketch basically is being, uh, is being programmed at this point. The low level stuff is already in there. Uh, so, you know, as far as risk is concerned, we feel that it's, uh, it's, it's very much into control. Uh, very, uh, I mean, it's, it's, you know, we're on target basically.

**Bertrand:** Yeah. And as of this recording, uh, it's 45 left of one 24. So 45 lucky people can still get that December board. And I might be, I might be one of them. There we go. Well, this is exciting.

**Dave Jones:** Thank you very much for, yeah. Thank you very much for joining us guys. I hope your project goes well. We'll definitely link it in. Great. Where can people follow you? So on Facebook. Are you regularly tweeting all this? Yes. So we have a fabulous fountain of knowledge to do with voice recognition.

**Gerald Friedland:** So I, we have a Facebook page where we kind of update.

**Dave Jones:** Oh, boo. We hate Facebook here on the air, Bill.

**Gerald Friedland:** Yeah. Well, you know, you have to use something. Um, I can tell you a lot of things about Twitter. Um, um, you know, um, you, you don't, this is another, this is another podcast. If I start talking about Twitter, um, I, I have a whole project on, it's called teaching privacy.org. So we'll talk about that later.

**Bertrand:** Um, Facebook is, is stellar on their privacy stuff. Oh yeah. Yeah. Yeah.

**Gerald Friedland:** Um, I'm not commenting on that either. I agree. Okay. But the point, the point is, the point is, uh, we, you know, I have to choose some, something and we chose Facebook. Um, and so we have a Facebook page where we basically, this is the first source of information because we put in a lot of personal stuff on there too. Like, you know, we, when we did the Kickstarter video, we showed some photos of the prep for this and so on. So people see the early stuff, like as it's developing on that Facebook page.

**Chris Gammell:** And the link is, yes, our shield slash ASR shield all in one word. Yeah. Uh, which wasn't the most obvious name. So let's actually go.

**Dave Jones:** You can also find, so I had trouble finding that. Yeah.

**Gerald Friedland:** So ASR shield is the project name because when we started, we didn't have a fancy movie. Uh, we had an ASR shield, which ASR stands for automatic speech recognition and then shield. Right. So ASR is actually the scientific term for the whole, all of this. This is automatic speech recognition. So ASR shield is what it was, you know, before we came up with that name movie.

**Chris Gammell:** But you can find us on Kickstarter. Uh, if you search for Arduino movie, M O V I, uh, you know, maybe you can put speech in there.

**Bertrand:** And we will of course have tons of links for the users. Yep. Thank you. Okay.

**Dave Jones:** Awesome. Thank you very much, guys.

**Bertrand:** I'm very, I'm looking forward to this for robotics and everything else. I mean, I mean, uh, I, I've always wanted, uh, uh, what's the guy's name in Iron Man? The, the house thing.

**Dave Jones:** Oh, um, uh, uh, uh, J. Is that a question? Jarvis.

**Bertrand:** I want a Jarvis in my house. Jarvis. Yeah. So if this can give me a Jarvis or even something close, I'm happy.

**Gerald Friedland:** So, so by the way, just on that, I tried that call sign and it worked pretty well.

**Bertrand:** Okay. All right. Good. Good. Great.

**Gerald Friedland:** There you go.

**Bertrand:** Jarvis for the home.

**Gerald Friedland:** All right.

**Bertrand:** Well, thanks guys. Thanks for telling us all about this, uh, speech stuff and we'll, we'll definitely be checking it out.

**Chris Gammell:** Yeah. Thank you. Thank you very much. See ya. Bye. Bye. Bye.

**Bertrand:** Bye. Bye.

**Bertrand:** Bye.

**Speaker ?:** Bye. Bye. Bye. x x x
