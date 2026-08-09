---
episode: 708
title: All the Connectors with Davide Andrea
url: https://theamphour.com/708-all-the-connectors-with-davide-andrea/
---

**Davide Andrea:** This is the F-R Podcast. Released November 1st, 2025. Episode 708. Sponsored by Blues. All the connectors with Davide Andrea. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Davide Andrea:** And I'm Davide Andrea. I'm in La Moncolaoaro. I'm an engineer. I've been an engineer for more than 50 years. And I'm the author of a couple of books and some utilities online that we'll be talking about today.

**Davide Andrea:** That's right. Welcome, Davide. Good to talk to you. Thank you for sending me this book. This is a book I think our audience is going to be very interested in. It's the Electronic Connector book. The newer ones, obviously you said you've had a couple in your career. This one is particularly interesting. My friend Ben at DigiKey had recommended it to me. And I've been really enjoying it as a reference tome on my desk. I'm so glad. Yeah. Let's talk a little bit about books and your history with books, I suppose, right? You were an editor to start with. And then you said, what, there was no connector book out there? You thought it was the right thing? It was the time?

**Davide Andrea:** It started with a postcard. I have been the engineer for a lithium doing battery management systems for large lithium-ion batteries for a while. And I have been doing some presentations on battery conferences. And I got this postcard from Artec House, a publisher of technical books, saying, in our experience, when people talk about their subject in presentations, they already have all the materials they need for a book. So maybe you do too. And I said, oh, what the heck? Let me try. So I secretly wrote a book on lithium-ion battery management systems. And it took me three months. I sent it in. And it was pretty successful for their company because there were no books at the time on the subject. Well, I caught the bug. And although other authors I worked with were saying, usually you only write one book because it's so draining. You don't ever want to do it again. Instead, as it was, I was interested in writing more books. And the Artec House made me also a series editor, which allowed me to discuss with other possible authors whether they may want to write books.

**Davide Andrea:** It's like that version of, I'm not just the president of the company, I'm also a member or something like that, right? That's like the equivalent now as an editor, right?

**Davide Andrea:** Yeah, I suppose. But as they were asking me, what books do you think should be written? And I said, you know, the world needs a good book about connectors because there isn't one. Connectors are not sexy. Integrated circuits are. And radio frequency is sexy. But with all these things out there, there's not one book, a single book that talks about the entire gamut of connectors. Yes, there are books about connectors, but they're from the point of view of people who design the connectors, not from the people who use the connectors.

**Davide Andrea:** Yeah. And it does kind of bring up the idea of like, just thinking back to my own history about like, how do we all learn about connectors, right? I feel like it's, you know, you walk into a company, you have a, you know, wired to board solution. I really learned by doing things very poorly at first, right? It's like you learn about signal integrity. You learn about like corrosion on contacts and things like it by like being like, oh, yeah, no, maybe I shouldn't submerge that cable or have it exposed in a high humidity environment. And it's just like this kind of tribal knowledge that gets passed down, but not everybody has that.

**Davide Andrea:** It is ad hoc, not only at that, but it is also limited to a specific area. So if you are in broadcasting, you will know about XLR connectors, about BNC connectors, about high power RF connectors. If you are into gaming, you will know about USB connectors. You will know about hard drive connectors. But very few people have the full view of this very, very wide field. And I myself did not until I undertook this project five years ago.

**Davide Andrea:** Yeah. So let's just say the DigiKey catalog and all the connections that are on there. How do you start digging in and starting to understand all of the ones that are out there?

**Davide Andrea:** You said something correctly. In fact, DigiKey was extremely valuable in my research. But to a certain point, I had to extend past what DigiKey's offerings are in the writing of this book. Yes, absolutely. Going to the DigiKey catalog, there were things that I did not know about. For example, industrial heavy duty connectors. And yet there's people in the industry who use them a lot, and that's all they know.

**Davide Andrea:** What's an example of one of those? Like what? A use case perhaps?

**Davide Andrea:** They're using industry. They're very clunky. They were started by Harding. They have actually a history going back to the old cinch connector. If you may know about that one, it's the old disconnector still in production. They are very easy to connect because when you open them up, they have wire cages so you don't have to crimp or anything. They are very heavy duty, very sturdy, very reliable, very big with a metal shell and huge clamps for fastening. I knew very little about them before I started this, but then with the help of Phoenix Contact, I was able to learn a lot about them and write about them. I also found a person online in the PLC subreddit asking them if they would mind going through this chapter and seeing if I missed anything or if there's something wrong. And so I got the feedback from people who actually are using these connectors.

**Davide Andrea:** I had a similar kind of like diving down the rabbit hole. As all engineers do, at one point I said, well, how hard could this be? I can just design my own connector, right? It was like I had like a really tight space and I knew that I wanted to kind of look like this, but not like that. And I was like, well, I can just like make a custom. And boy, oh boy, was that a bad idea. Tell me why. Well, in that case, it was because crimping was something I had experienced before. I had used crimping machines and things like it, but I was putting it into an industrial scenario and I just didn't have the testing capability and just the longevity testing that would have really been required. So I had this really strong requirement around space and spacing, but I didn't have the, again, the tribal knowledge that like a Phoenix or a Wago or, you know, all the connector companies are out there. And so it ended up being this like back and forth with a mechanical engineer who just couldn't get the connector to like get the right plastic, the right, you know, injection shots, the, you know, just the stability and all of the things that we, you know, it looked really nice in the design, but the practical nature and like the longevity of it, that's where it really started to falter.

**Davide Andrea:** How did it end up? I left the company.

**Davide Andrea:** I see. Yeah. Yeah. If I had to guess, there was a terminal block, it was like a mated terminal block. So like the kind with the wire screw, the screwed down wires in the wire cage. And then, whereas we were going to make our own wire cage version and then have a male version of the receptacle on the board, I think they just ended up going with off the shelf, a wire cage version, basically. You know, it was even more clunky than it would have been otherwise. It was very space constrained. I think they ended up down specking otherwise, but it worked, but it just wasn't what we really wanted. You know?

**Davide Andrea:** I understand. A couple of points came up in my mind as you were saying that. And the first one is that through the Identicon, I am trying to offer a way for someone like you to see, okay, what else is out there? Maybe the reason I'm thinking about a custom connector is because I'm not aware of what all is out there. And so I'm trying to offer a palette from which people can select what works best for their application. And the second thought was that you hit it right on. People have no idea what is involved in designing a reliable connector. And that's why we really are best off letting the experts in the industry design it for us. Even if you want a custom connector, you're much better off going to a company that already makes a similar connector and say, can you modify it for me, please?

**Davide Andrea:** I think that is spot on. I think it's just, you know, there's a little bit of engineering ego and hubris in there. And it just like, of course, like how hard could it be? Of course, that's always kind of in the back of an engineer's mind. It's one of those things too, where if you have a hundred mating cycles and, you know, I don't think about that 99th cycle, if it's actually going to be, you know, if it's actually over specced or under specced or, you know, if corrosion is going to be in there. And it's going to be one of those things where an off the shelf connector might get a 30 year life out of connector and mine might get five years and it looks good enough, but it needed the 30 years, you know, and that's really where that capability is important.

**Davide Andrea:** Exactly. And people may not know about fretting. Do you know what fretting? Fretting, you said? Yeah. No, I don't know it. That's what my mother does all the time.

**Davide Andrea:** I was going to say, or a guitarist does as they shred on the fretboard.

**Davide Andrea:** Fretting is when a connector in a high vibration environment is constantly rubbing. The two contacts are constantly rubbing and they rub off the plating. It's called fretting. Got it.

**Davide Andrea:** Got it. Yeah. Yeah. And I think that's the thing, like even thinking about a young engineer coming into the industry, how would they possibly know that? These are hard won lessons that engineers have gotten over the years.

**Davide Andrea:** Yes. And speaking over the years, you know, I'm 68, almost 68 years old. I've had 50 years experience in electronics. I certainly have spent most of those years being a seat-of-the-pants connector designer like most people. But I felt for myself and hopefully for others that need to put it all on paper in one place. Now, a lot of this information is available here or there. Some of it I had to dig very hard, like trying to find some old build labs documents from the 1940s that apparently have disappeared. But most of the information is available online, but not in a single place. So I really wanted to have it in a single place. I also wanted to provide a free service with the Identicon so people could go and either identify a connector that they have in their hands or select a connector to fit the needs of their application. And that is, of course, a free utility that I've put out there in the world. Yes.

**Davide Andrea:** Yes. And that is connectorbook.com slash identification.html. We'll have links to that, of course. This, you know, it's almost reminiscent, you know, like the speed with which it loads. And it's almost like closer to like a McMaster, which is like very much appreciated. You know, just being able to just browse and like, don't get me wrong. I love DigiKey. I love Mauser. They're wonderful and they have huge catalogs. But like it is difficult to see, to kind of get your arms around everything at once. Right? Like how does that happen?

**Davide Andrea:** Yeah. Okay. Let me tell you something. There are some limitations due to the requirements of being a vendor that make DigiKey's search engine not perfectly aligned with the way the user thinks. So if you are looking for a wire-to-board connector, you're not going to find a wire-to-board connector section in DigiKey. Instead, you're going to find a section on housings, one on male headers, one on female headers, one on contacts, one on tools. So in their mind, and they have to do it this way. They divide it based on how the fields in a database can be set up. And because a contact has different fields than a housing, they have to be in different sections. But from the point of view, from my point of view, from your point of view, you're looking for a connector family, like the Molex KK.1 inch pitch connector. And to you and to me, they're all the one thing. Whether it's the female housing, the contact that goes inside of it, or the male that goes on the PC board, it's all one thing. Then, from the point of view of the manufacturer, in this case, Molex, it's even different. For example, they may group connectors based on the shape of the contact. And if they have a contact called the hotbox, they'll put all the hotbox connectors together, even though one is a circular connector, and one is a rectangular connector, and one is a industrial connector. But they'll put them together because they all were designed by a subsidiary that they bought 10 years ago, a company called Hotbox.

**Davide Andrea:** Oh, Hotbox is the brand? Is that what that is?

**Davide Andrea:** I'm making it up. Oh, okay, sure, sure. Okay, got it. There's a company called Hotbox. Molex buys it. And now they have a section on their website that is all the hotbox connectors. Here, a practical example, Doge connectors that TE bought. So, all the Doge connectors are together because they came from this one branch. And so, the way the manufacturer thinks about categorizing connectors, the way a vendor like DigiKey thinks about categorizing connectors are different, and they are different from the way us users think of them. So, the Identicon in the book is used as a taxonomy that is really derived from our needs as users of connectors.

**Davide Andrea:** One of my favorite days was when, like, the Samtech, you know, Samtech had the margin and the sales force to, like, stop by the office when I used to work at, like, Keithley. Those guys rock up with little suitcases full of connector boxes, and then you just dig through them like you're playing with Legos at the, you know, at a toy store. And that's what you need, though. You need that tactile, that ability to be like, oh, you know, if it was just like this, but maybe, you know, it's a 10 connector instead of an 8. And, of course, they're like, yeah, and we can do custom too. That's effectively what I need. But I really needed that cross-vendor. I didn't need just Samtech. I needed TE. I need Molex. I need them to come in and, like, fight for my business. Or really what I needed is I needed, like, the, you know, I used to watch the tours of, like, the Shenzhen markets and, like, just going to the connector floor in one of these buildings. Like, that's what I really need, but that is very impractical for most things, you know.

**Davide Andrea:** Yeah. That reminds me of a story, and I have it there in the preface of the book. I was in college, and my roommate says, my stepdad is a representative for AMP, which is now part of TE. And he's retired, and he's got a trunk full of samples. And he wants to get rid of it. So, he shipped this trunk. I mean, one of those shipping trunks that you, you know, from the old days. Like a steamer? Like a steamer trunk, exactly. Wow. Full of samples. And I wish I had kept all of them. I just kept a few. But to me, it was like being Christmas morning.

**Davide Andrea:** Oh, of course. Yeah, I mean, you open that thing up. It's got, like, the, you know, the light coming out of it, like the Ark of the Covenant and Indiana Jones. You know, the angels sing from on high. It's just like, I never will be without again.

**Davide Andrea:** Exactly. So, that was part of my love for connectors. But mostly, I think we all use them. And the fact is that we are not paying enough attention to their reliability. If you think about it, a lot of products break down, not because an IC breaks down, but because a connection, whether it is through a connector or maybe just a wire, breaks down. We really should be paying more attention to how we select connectors and how we maintain connectors. And we don't because we're so much more enamored with integrated circuits.

**Davide Andrea:** Yeah. I mean, again, I think it's one of those things where a lot of people design things, but it's the people who get them out into the world and get the returns and see the, you know, the brittle plastic that, you know, snapped off because some roughneck on an oil platform is just like trying to fit this thing together. It's like, oh, actually, I need to, you know, the next rev, this is going to get better or the corrosion or whatever it is. I mean, surely, you know, in your career, you've seen a wide range of issues like that. What are some of the ones that stick out to you?

**Davide Andrea:** In terms of reliability?

**Davide Andrea:** Yeah. Just, I guess, really things that went wrong, you know?

**Davide Andrea:** No, no. The classic one, and it happens once every three days on Ask Electronics. If somebody says, how come this FFC doesn't connect back into the socket? And the reason is because it was a ZIF, zero insertion force, and they had an actuator, and they pulled it out, yanked out the FFC, and the actuator broke off. And they say, how can I? It doesn't fit. I mean, I put it in there and just pops right back out. How can I fix it? And so then you have to be the bearer of bad news saying you really have to replace the whole socket. It happens every two or three days on Ask Electronics because people are not careful. They don't realize they have to lift or slide the actuator first and then pull out the cable, and they're yanking it out, and it breaks.

**Davide Andrea:** What is the common application of the space, like a PlayStation connector or like a Raspberry Pi?

**Davide Andrea:** Oh, absolutely, absolutely. They're used in pretty much every consumer electronic right now. There's one in my thermostat. There's one in the monitor I'm looking at right now. They're FFC connectors. FFC means flexible flat cable, by the way. And speaking of that, one thing that I constantly have to battle is people calling them ribbon connectors. What's the difference? Yes, a ribbon cable has round stranded wires in them. They're thick. Insulation is joined together to make this flat cable. But an FFC has very flat traces, not round stranded connectors.

**Davide Andrea:** FFC is like a flat flex connector, right? So that's like a polymide.

**Davide Andrea:** Yes. And then there's the flexible PC boards, which are really PC boards. They're custom PC boards, and they can take any shape. And sometimes they have a tail, and the tail may look like an FFC, but it's still a flexible PC board. Then there's the CIC, which is the conductive ink circuit, which looks like an FFC, flexible printed circuit. But it's done by drawing the circuit with ink. And you will, for example, find it in the keypad for a microwave oven. It ends up in this flexible tail, and it's hooked into an FFC connector. That's a CIC. There are multiple technologies, but please don't call it ribbon cable, because a ribbon cable is a very specific thing. Got it.

**Davide Andrea:** Yeah. Like ribbon cable is like the kind that you might have like an IDC clamp go on to. Is that right? Yes. Yeah.

**Davide Andrea:** Yes, exactly. Yeah.

**Davide Andrea:** We used to use those at ABB, and we would have like a twisted pair ribbon cable. And then you'd have the clamp on the end, and it has like the tooling. And there's always that $150 hand tool that they want to sell you, and that you have one of. And then Bob was always stealing it and putting it in his desk drawer.

**Davide Andrea:** So let me tell you about that. The connector at the end of that ribbon cable does not have a name. Really?

**Davide Andrea:** Should we name it right now?

**Davide Andrea:** Well, I did. I tried to. So most people would call it an IDC connector. Okay. But IDC, which means insulation displacement connector. Is a general technology and is used by many, many different connectors. In some terminal blocks as well. So calling it an IDC connector is unfair to all the other IDC connectors out there. Additionally, the header that is on the PC board, the mail header, it is not an IDC connector because it does not use insulation displacement.

**Davide Andrea:** Yeah. So that would be like a 20 pin that's on like a J-Link, like that sort of thing?

**Davide Andrea:** I don't know about J-Link, but yeah, I think I know. Now, in Germany, they call it a bathtub connector because it's got this cavity in it. The industry needs a name that encompasses both the IDC plug that is on a ribbon cable and the header on the PC board. And I looked and looked for such a name and there is no such name. But there was one person who called them bump connectors because there's this keen block on the side of the plug that fits into a gap in the mail.

**Davide Andrea:** That's an optional key as well, right?

**Davide Andrea:** No, no. They always have it. Oh, I thought it was. They always have it. So I coined the term bump IDC connector and I keep on using it. And occasionally I see somebody else start using it as well. Is it arrogant of me? Possibly. I apologize if it is. But we really, really need a name for that connector.

**Davide Andrea:** I mean, at a certain point, you know, we make up words to describe new things. It's just all you need is a couple of people to understand what it is and you have a shared context and yeah, boom, a new thing's named.

**Davide Andrea:** And let me give you a different example of neologies in that coin. Great, great, great. You know, in a phone, like a smartphone, if you open it up, there's going to be flex cables or flex circuits with these very, very low profile connectors that snap into each other. Right?

**Davide Andrea:** Right. Like the ones like you watch like an iPhone tear down or something like a repair video, that sort of thing.

**Davide Andrea:** Exactly. Got it. What are they called? MMCs? Is that right? I don't know what that is.

**Davide Andrea:** No, I thought that was a, no.

**Davide Andrea:** Okay. So there's an example of a connector that everybody knows what it is. I know it when I see it, but I don't know what to call it.

**Davide Andrea:** So here's a question about all this stuff too, because like the naming idea. Is part of the problem that in the old days there would have been like some kind of standards body and these days it's like each vendor calls it something different. They all want to like call it their own proprietary thing.

**Davide Andrea:** If that, in fact, it's good if a vendor does call it something, but most often it's just the power number, the XYZ 100.

**Davide Andrea:** Oh, sure. So they don't give it a name. Yeah, good point.

**Davide Andrea:** Sometimes they do. So as far as the connectors I was just mentioning, which are surface mounted, very low profile, snapping together, genderless, two rows. I've called them dual beam. And it's because Samtech called them beam connectors. And I started from there. Beam is by itself is meaningless. So I ended up with calling them dual beam. And I hope the people will adopt it.

**Davide Andrea:** Yeah, I like it. You know, we're going to put all these terms in the amp hour show notes. So maybe we'll become a primary source here, you know. And of course, connectorbook.com slash identification as well. We'll link over to that. So, yeah, that's good. What do you call like those hundred pin DF 0.5 millimeter pitch Hiroshi connectors? Do you have a name for those or those beam style connectors?

**Davide Andrea:** I'm sorry. I'm going to look it up right now. What is it?

**Davide Andrea:** Yeah, look at the bottom of a compute module four. They were unobtainium coming out of the part shortage. They were harder to find than Raspberry Pi CM4s or CM5s. Well, CM5s were not yet. But I got an email on Christmas Eve that those connectors were available. And I left my family gathering to go and click purchase on DigiKey as a measure of how excited I was they were available.

**Davide Andrea:** So I have a picture up right now. There's a shroudless pin header in the middle. There's some FFC connectors around the edge. HDMI. I see a PCIe socket. I don't see anything particular.

**Davide Andrea:** Actually, maybe I can try and navigate the Identicon here as well. Right?

**Davide Andrea:** So like, why don't you share your screen?

**Davide Andrea:** Show me what it looks like.

**Davide Andrea:** Point it out to me and then we'll go from there. Yeah, that's a good idea. Okay.

**Davide Andrea:** Davide and I will be talking through this as well. But of course, you can follow along at home. We're just going to be going through. So there are QuickPix, navigate by type, browse by pictures, logos, find by term.

**Davide Andrea:** Good. Let's go through the process. So start by showing me the picture. Oh, yeah.

**Davide Andrea:** Okay. So CM4 connector. This is the actual CM4 style. These are by Hirose. I know that.

**Davide Andrea:** Okay. All right. So what you're showing me is a board-to-board connector, clearly. And it's genderless. It doesn't have pins and sockets. Instead, it has contacts that slide past each other.

**Davide Andrea:** Yeah.

**Davide Andrea:** And it has two rows. Right? And we can also count how many pins it has. How many terminals.

**Davide Andrea:** Yes. It's 50 per side. And I know it's a 0.5 millimeter pitch.

**Davide Andrea:** Wonderful. So it's 100 total, 0.5 millimeter pitch, board-to-board, genderless. Okay?

**Davide Andrea:** Yep. And I think it's a 1.6 millimeter. I think it's actually board height as well. So it's a very small gap between the full stacked height as well. I think it's 1.6 millimeter tall. Yeah.

**Davide Andrea:** It's the median height is what we call it. So now switch over to a tab of the identicon and navigate by type. Okay. And this is a rectangular connector. So number 14 there.

**Davide Andrea:** Yep.

**Davide Andrea:** And the first item is board-to-board connectors.

**Davide Andrea:** Uh-huh.

**Davide Andrea:** Right? And we see small genderless board-to-board connectors.

**Davide Andrea:** Okay. The one above it is low-profile mezzanine B2B connectors. How would I... You're right.

**Davide Andrea:** You're correct. How would you know? So hover over either one of them. Which one looks more like it?

**Davide Andrea:** Okay. It's like one of those eye tests at the optometrist. Absolutely. Is it number one or number two? Number one or number two? Which one does it? I think it's number one, actually, the B2B. Good for you. Yeah.

**Davide Andrea:** Yes. Okay.

**Davide Andrea:** Correct. This is kind of what was reminding me of the connector style that's on the end of the ribbon cable in an iPhone repair video as well. It's similar. Absolutely. It is. It is. Yeah. I see the beam. Oh, here we go. Dual beam. Yeah. Inner. Okay.

**Davide Andrea:** But now let's start using the filter.

**Davide Andrea:** Okay.

**Davide Andrea:** And if you go to click on off, now click on basic, I'm waiting pitch.

**Davide Andrea:** Oh, yeah. There it is. I think this has got to be one of these.

**Davide Andrea:** That's the general style. Oh, no. I think you may have advanced in one extra step. Click on low, at the very top, low profile mezzanine BB2B connectors. Yeah. Okay. And it's CI or dual beam. I don't know which one it is, but if you go and search on the...

**Davide Andrea:** Oh, it's that one. Yeah. You see that inner, the intersection area? Yeah.

**Davide Andrea:** Try that.

**Davide Andrea:** Yeah. And those look, that looks awfully close, doesn't it?

**Davide Andrea:** It does look very close. Yeah. Yeah. That's it. That's it. Right there. DF23. Yep. That's the one. And now, a word from this week's sponsor. Building connected products shouldn't mean fighting with carriers, contracts, or SIM cards. With Blue's, you skip all that. The Blue's note card includes 500 megabytes of prepaid global cellular data with no monthly fees, roaming headaches, or carrier certifications. Just power it up and start sending your data to the cloud. When coverage gets spotty, Blue's star note can take over, switching to satellite so your device stays connected. If cellular or satellite aren't a fit, you can switch to a pin-compatible LoRa or Wi-Fi module, all using the same radioagnostic APIs. Integrate any note card with your product using Blue's note carrier, or add an M.2 edge connector to your own board. To top it off, NoteHub, the Blue's cloud service, securely routes data from the field to your cloud. No brokers, VPNs, or custom infrastructure required. Plus, it supports full device management and OTA firmware updates for STM32, ESP32, and NRF52 hosts. From prototype to production, Blue's makes wireless connectivity simple, scalable, and resilient. Learn more at blues.com, or take 10% off your first cellular, satellite, or LoRaWAN starter kit with the code AMPHOUR at shop.blues.com. And now, back to the show.

**Davide Andrea:** Okay, so we've gone through the process. Of course, the fact that I am familiar with the website made it easier. If you're just starting, unfortunately, just because of the complexity of connectors, it can take some time.

**Davide Andrea:** If you already know the part, I would say the best thing to do is to go and search for, like, I know it's CM4. I would go search for, like, CM4 connector and probably find a schematic. That's an easier, faster way to do it in the short term. But there's a bunch of things out there. You're not going to have that, right? You don't have... We're looking for the classification of this general arena of parts versus, like, knowing the exact part number or having it available.

**Davide Andrea:** One thing that I struggle the most, and I never resolved to my own satisfaction, is the terminology for a connector that fits inside another one. The gender of connectors is set by the gender of the context. If it has a pin, it's a male connector. If it has a socket, it's a female connector. If it has both, it's a hermaphrodite connector. If it has neither, it's a genderless connector. Many people will look at a male PCP header and call it a female because the housing encompasses its mate. And this is what's so confusing, is that we are confronted with two different mechanical genders. The gender of the metal pin and the gender of the plastic housing. We use the same terms for both, and it just confuses the heck out of us, out of the industry. Amphenol handled that by saying it has a male contact gender and a female housing gender. And that's a good solution.

**Davide Andrea:** Right. So, if we go back to that not called an IDC connector, right? There's a shrouded... So, say, like a standard 10-pin, what I would call an IDC, but you called a IDC... Bump IDC. A bump IDC. The thing that's on the board...

**Davide Andrea:** Is a male, but it has an outer shroud in the plastic. That's right.

**Davide Andrea:** Female shroud. Right. Exactly.

**Davide Andrea:** And the plug that goes into it is a female, but fits inside the shroud.

**Davide Andrea:** Yeah, right.

**Davide Andrea:** So, we had clear terminology for the pins, male and female, but we don't have terminology for the plastic.

**Davide Andrea:** Yeah.

**Davide Andrea:** And what do we use? And I struggled for years on this. I asked mechanical engineers. I've come up with some terms that apply to carpentry, but they're really obscure. Oh, yeah. Like joints and stuff like that? Yes, exactly. But people don't really know these terms. And I looked at what's out there, and the closest I came up to what was out there is shrouded. So, in the example of the Bump IDC, the header on the PC board, the male, is shrouded. But what do you call the one that fits inside of it? In the preview edition of the book, which I published 12 months, 18 months ago, I came up with the term gazinta. G-A-Z-I-N-T-A. I didn't coin it. It came up in a poem from the 1800s. It was the first use of that term. But it's like two gazinta, ten, five times.

**Davide Andrea:** I love it. This is right up my alley. I love coming up with obscure names. Like every time I name a board, I spend about a day and a half naming the new board. Yeah. So, this is great.

**Davide Andrea:** Absolutely. So, I used gazinta in the preview book, but I didn't think the industry was going to accept it.

**Davide Andrea:** The industry is not ready for 1800s poetry, huh? Exactly.

**Davide Andrea:** So, in the first edition, I went to enshrouded, E-N-shrouded. So, for genders, we have a male and female based on the context, and we have a shrouded and enshrouded based on the plastic.

**Davide Andrea:** Yeah. I think that's pretty-

**Davide Andrea:** Or the metal.

**Davide Andrea:** Yeah.

**Davide Andrea:** That feels right. Feels right. Good. I'm glad because I've asked battery experts, people in the industry, and they all said, well, let me think about it, and just, we don't have these words, and it's hard to communicate if you don't have terminology that we share.

**Davide Andrea:** So, within the book now, is there a glossary for these sort of terms that we can just point people directly to?

**Davide Andrea:** Yes. If you don't mind flipping it, and I think it's like 40 pages long.

**Davide Andrea:** Sure. That's great. Yeah. I think that's the thing. Like, but it's, again, just thinking about like our listeners and thinking about the, you know, the people that are going to be picking this book up. There's going to be some experts out there, but there's going to be a bunch that aren't. And it's like, I think the other thing is that, you know, this book is fantastic. I've seen a lot of these things. I've wondered about a lot of these things, but I have some experience of thinking about the people that don't have the experience. You know, where do they go? Where do they start, you know, flipping back and forth to start learning these terms? You know what I mean?

**Davide Andrea:** What I advise is to read a chapter one and two. One is terminology, and two is basic concepts. And the rest of the book is that it's covering a particular type of connector. So if you're interested in circular connectors, just go look at the circular connector chapter. You don't have to read the other chapters.

**Davide Andrea:** Yeah. Terminology is 2.2. And yeah, this is where it really, really gets, gets into all the details of what we were just saying as well. And I think it's, yeah, it's, it's great. I mean,

**Davide Andrea:** Let me ask you, USB connectors type A, what do you call the two genders?

**Davide Andrea:** Uh, the pluggy part and then the thing that you plug it into part. I don't, I don't know. Yeah. Uh, and also type A, doesn't type A also have, oh no, type A is, is the, the flat rectangular one with the four con four contacts. Yeah.

**Davide Andrea:** It's a rectangular one that is, that is available on, on, uh, on USB adapters and on, in the front of computers on the side of laptops.

**Davide Andrea:** I don't know what I would call them. I would just say the plug and the receptacle, I guess.

**Davide Andrea:** Perfect.

**Davide Andrea:** Yeah.

**Davide Andrea:** Perfect. And I would too. Okay. But I, you won't believe how many times there will be people who will argue strenuously and understand why that the plug is the male and the receptacle is the female. And I will not hear any other arguments because, you know, the plug is going into the receptacle. So the plug must be the male. Huh. But if you go from the definition that the gender of connectors based on the contacts, and you look at the contacts, they are not pins. They are not socket. They just slide past each other. So they are neither male nor female. They're genderless. Therefore, with USB connectors and similar connectors, we can't use the gender to distinguish one from the other. We can't use plug and the receptacle either because, as you know, they make extension cords for USB type A, which has one gender on one side, one gender on the other side. So how you distinguish them. And at the point, the only thing you can use to distinguish them is the shrouding. So the plug is in shrouded. The receptacle on the computer is shrouded. And the plug at the other end of the extension cord is also shrouded.

**Davide Andrea:** Wow. Yeah, that's wild.

**Davide Andrea:** And you know how much time I had to spend to understand that? There are things that are so clear to me today after years of looking at it.

**Davide Andrea:** Yeah.

**Davide Andrea:** But I started like most people and possibly like you. I did not know the difference between a hermaphrodite and self mating. Do you know what the difference is?

**Davide Andrea:** I don't know. Wait, no. So you said hermaphrodite has both male and female style contacts, right? Pins. Yes.

**Davide Andrea:** Yes. And self mate?

**Davide Andrea:** I don't know that.

**Davide Andrea:** The very same connector mates to itself. For example, Anderson connectors.

**Davide Andrea:** Is that like the one I asked you about the APC7? That one?

**Davide Andrea:** Yes. The APC7 is a circular connector that has a flush front face. The two mates look exactly identical. They both have locking rings. They're used in high precision RF electronic equipment.

**Davide Andrea:** That was my exposure to this as I had the HP 8537, the VNA that now resides with Jeff Kaiser. Yeah. It had these connections. I had no idea what they were, but they basically like you screw them in one direction and it has like threads and then you screw it. You screw the connector in the other direction and it has receptacles for those threads. I don't even know. How do you talk about threads then too?

**Davide Andrea:** Yes, exactly. So each one of them has a locking ring. You only use one of them to lock the two together. Why don't you explain to the listeners what VNA is?

**Davide Andrea:** VNA is a vector network analyzer. And in this case, it was because, so usually a lot of them have like a type N connector, which is an RF connector. All of these are available on the Identicon. You can go look at them. And this one is because it has this, because it has like a measurable distance between the coupling conductor between the two connectors, right? That's really why you wanted that. So it was a very precise way to, to couple two conductors together without, without having like variable spacing and.

**Davide Andrea:** Without introducing reflections.

**Davide Andrea:** Without reflections. Yeah. There you go. Yeah.

**Davide Andrea:** And that is a self-made in connector. Both sides look exactly the same. And, but it's not a hermaphrodite because it doesn't have male and female pins.

**Davide Andrea:** Right. Yeah. They just kind of smoosh the two contacts together effectively, right?

**Davide Andrea:** It's another example is the Anderson connector used in large batteries, like four forklifts because they're identical and they're genderless. Then we have self-mating that are hermaphrodites that have pins and sockets, like two pins and two sockets on each mate. And you mate them. They have non-self-mating hermaphrodites. That's a very common one where you will have, for example, a motor has a circular connector which has pins and sockets on one end. And it's mate does not look the same because one has a hood, the other one doesn't. One is right and one isn't. And finally you have hermaphrodites that are self-mating. So, they're all four permutations and people conflate self-mating and hermaphrodite, but they're really different things. I did not understand that when I started writing this book.

**Davide Andrea:** I can't imagine the conversations that like, again, like I think back to the salespeople from a connector company, what they have to do. And like, they probably have to have like, I'm sure they're going to be carrying this book around and handing it over to their customers and being like, well, go read this and then come back to me with what you really need. You know?

**Davide Andrea:** Manufacturers are the worst. You will see how many times they will, they have a self-mating connector and they call it hermaphrodite, but it isn't.

**Davide Andrea:** Oh, interesting. Yeah.

**Davide Andrea:** I'll tell you what else. The reverse female. Can you imagine somebody calling something? I'm not a reverse female, I'm a male. So, you have a RF connector, such as a TNC, and normally it has a pin in it, but if you have, they have the opposite direction or the SMA, RF connector, they swap the pin and the socket. When they do that, it's reverse polarity, okay? Which is fine. But instead of saying that now this has gone from a male to a female, they say it's gone from a male to a reverse male. And that is such twisted thinking.

**Davide Andrea:** Well, so like, okay, so actually I have a thing back up on the screen again, and I'll link this in. It's actually the default view on find by term on Identicon. Okay. So, we're looking at a RF connector here that I think someone would refer to in this case as a reverse male, right? It's basically accepting a pin, the one on the right side here.

**Davide Andrea:** That one you're showing is a enshrouded female. Go to TNC and you will see that the regular TNC has a shrouded male. You see there's a pin and there's a locking ring on the right there. So, that's a standard polarity, which I call shrouded male. Now, go back. Click one back. And now do the RP TNC, reverse polarity TNC. If you look at that, the shrouded is now a female. So, that's a female, but they will call it a reverse male.

**Speaker ?:** Oh, my God.

**Davide Andrea:** That's so dumb. So, how did you deal with this then? Like on the site here, there are going to be these references to reverse male, reverse female, whatever.

**Davide Andrea:** I don't on the side. I talk about it in the book though.

**Davide Andrea:** You leave it off. Okay. Cool. Cool. Cool. Cool. On a BNC connector, right? So, the constant, yeah, what is the white stuff? I mean, that's just dielectric. What do they call that? Are there names for like different parts? It's Teflon.

**Davide Andrea:** Yeah, it's a dielectric.

**Davide Andrea:** It's dielectric, but is it like, is there a name for that class of material? I mean, I know it's usually Teflon, but.

**Davide Andrea:** P-F, I'm not a chemist, P-F-F-E, I believe. Okay. I talk about it in the book, but I don't remember what it's called. If you go to the navigate by type, you will see that there are a total. Yeah, go to home, excuse me. Home. Yep.

**Davide Andrea:** Yep.

**Davide Andrea:** There are total 21 classes. And one of the hardest things for me to do was to classify this taxonomy. Sure, sure. Of where do I put particular connectors? I'll give you an example. Plugable terminal blocks. Yeah. The European type.

**Davide Andrea:** Yeah, that's like the cage like we talked about before, right? Exactly. So, like a Phoenix connector where you have a wire that goes into this wire cage, you call it, with the wire gets fastened down, and then that whole thing plugs into a.

**Speaker ?:** In the plug.

**Davide Andrea:** Yeah, and then the whole plugs in a receptacle.

**Davide Andrea:** Into a header. Where would you put those? Because on the one hand, they're terminal blocks, right?

**Davide Andrea:** Yeah. Yeah, yeah, yeah, yeah.

**Davide Andrea:** But on the other hand, there are rectangular connectors. Of course. Right. Yeah. And so, if you look at Phoenix Contact, the inventor of such connectors, they call them connectors. They don't call them terminal blocks. Yeah, this is our thing. Where would you look for them?

**Davide Andrea:** Where would I? I mean, when I go to like a digi-key and I go for terminal blocks, usually I go for, I search for terminal blocks on the search first, first and foremost. And then I just take a guess, you know?

**Davide Andrea:** Yes, exactly. Which is why, after a long struggle, where do I put them? Logically, they're connectors that happen to have a wire termination that uses wire cages. There are other rectangular connectors that use wire cages. But these, just because you and I would think of them as terminal blocks, I ended up putting them with terminal blocks. That taxonomy took a long, long time.

**Davide Andrea:** You ever seen the Pixar movie, WALL-E? Yes. And then WALL-E's like, he like finds a spork and he's holding up to the fork. He's like, he's collecting stuff, holds up the fork, the spoon, and he just puts it in the middle. It's like, how many times can we subdivide into the middle, you know? And that's his own problem of like, now you have a new category and then you have to classify that and do other things fit into that new category too, you know?

**Davide Andrea:** Sometimes, most times I will fit it in one of the two categories. But in the identicon, which you will see, is also a see also. Therefore, if something could have fit into different categories, I will have a also see these other categories because they may be similar. For example, pogo pins and magnetic connectors. Magnetic connectors use pogo pins. So, you may be looking at magnetic connectors, but you say, you know, I'm not looking for the plastic part, I'm looking just for the pins. And that's where you say, see also pogo pins. And that jumps you to the completely different section of the identicon where the pogo pins are. And as you were in the pogo pins-

**Davide Andrea:** Sorry, can you explain the magnetic using pogo pins, the magnetic connectors? Like, is that like the Apple laptop connector thingy? Exactly.

**Davide Andrea:** The pins have a spring-loaded retractable pin. That is a pogo pin. Because when you are joining the two connectors, you're having a flush surface on one side and a retractable pin on the other side. And as they mate, as they are attracted by the magnets, then the pins go against the flat target and they retract to fit the difference in spacing of where they start and where they end. So, they are built out of pogo pins. And so, you may start in your mind from one such connector, or maybe if I have servers, you start from pogo pins and say, but I don't want just the pin, I want the entire connector. So, that's why when you go to pogo pins, there's that connection. So, go to compression interconnects number 12. Okay. And you'll see spring-loaded interconnects. It's the first selection. Oh, yeah, yeah, yeah. Pogo pins. And below you see, oh, here's a test fixture probes. There's an also. I suppose I didn't tell you the story correctly because there was no reference to the magnetic connectors. I know. Go back.

**Davide Andrea:** Well, you went the other direction, I think, in that case, right? We went straight to pogo pins instead of... Fine.

**Davide Andrea:** Go back one step, please. Okay. Spring-loaded? Yes. And do pogo pin headers, number five.

**Davide Andrea:** Uh-huh.

**Davide Andrea:** Okay. So, down there, at the very last item, pogo rectangular connectors. That's the C also.

**Davide Andrea:** Perfect. Yeah.

**Davide Andrea:** See, that's how it jumps back and forth because I know that the user may be going about it in a direction that is not the most logical way, but I want them to find it anyway. And that's why I have all these cross-references throughout the Identicon.

**Davide Andrea:** Yeah. I mean, this is the thing. Like, I've wanted, you know, MagSafe is a really interesting innovation and, you know, Apple's obviously great at that sort of thing. So, now I want to go, no offense DigiKey or Mauser, but I want to go source it from Ali Express or Alibaba. And I need to, like, be able to talk across the language barrier and maybe just search directly for it. You know, like, I could just search for MagSafe and shoot the breeze on Alibaba and, like, try and find something similar. But instead, finding an actual part number and being able to, like, be like, oh, no, no, no. I'm going to start from HTTP, HTTP, CON, M413 or whatever it is and just say, that's the one I want. Like, that is a way better starting point.

**Davide Andrea:** Yes. And then, as you see, there's a link to the actual company. Uh-huh. So, it takes you directly to the company that I've linked to.

**Davide Andrea:** Got it. Yeah. I just lost my screen share. I'll bring that back up for us. But, I mean, what about, you know, I bring up China. What about China, lookalikes, similar type of things? I mean, this is height.pro, H-Y-T-E.pro. We'll link that in, too, just so we have it in here. But, like, what about now, lookalikes, low-cost replacements, Alibaba, AliExpress, that sort of thing? Like, how did you treat that in this similar kind of scenario?

**Davide Andrea:** Well, take the case of the PH connector from JST, which is made by many other companies.

**Davide Andrea:** Yeah.

**Davide Andrea:** Super generic. Yeah. Super generic. Let's see if I could find it again.

**Davide Andrea:** Even more so, the PicoBlate by Molex, which Molex finally gave up and stopped making because so many other people were making it instead. If you go to the page where the PH, JST PH, is listed, it will also list other companies that will do the same connector. So, under a return. Let's go for the Quick Pick. The Quick Pick is a way that allows you to look for a connector just from a picture. So, if you scroll down. Yes. Right on the left. There you go. That's the PicoBlate. Oh, yeah. I see it.

**Davide Andrea:** Yeah.

**Davide Andrea:** Okay. Yeah. But if you go one step back on low profile W wire to board connectors, if you were to enter the pitch and other characteristics like no latch for the PH, you will find that there are other companies as well who will produce that connector. Huh.

**Davide Andrea:** Interesting.

**Davide Andrea:** Pitch is two millimeters.

**Davide Andrea:** Two millimeters. Thank you. Okay. And then.

**Davide Andrea:** And for fasten method down near the bottom.

**Davide Andrea:** Uh-huh.

**Davide Andrea:** Do none. No latch any type. Okay. The PH is going to be listed in there. But do one row. Number of rows. One row. Number of rows. One row. You see the PH there is on the list towards the end. Yes. Of course.

**Davide Andrea:** Yeah.

**Davide Andrea:** Yep. Okay. But you will see similar looking connectors. Like if you go further up, you will have other brands. Yeah.

**Davide Andrea:** This DL two zero zero three three. Yeah.

**Davide Andrea:** Yes. Yeah. It's the same connectors. Just that it made by DLL.

**Davide Andrea:** It's taller. Looks like there's taller.

**Davide Andrea:** And in the notes, it says taller than the PH.

**Davide Andrea:** How do you maintain all this stuff? Like this is a labor of love. I have to imagine. It is.

**Davide Andrea:** Yeah. I worked in spurts. And so when I start working on circular connectors and start researching them, and then I start entering data. Right now, I'm at a 75, 7,500 families in there. Wow. And I add one or two every week or so. Wow. But at times I will go on spurts and let's say I find a new manufacturer, enter all their offerings. Yeah. And then I will be entering another extra 100 components in there.

**Davide Andrea:** Got it. Yeah. I mean, I'm sure some are added in anger and some are added in, you know, like, oh, this isn't in here yet. That sort of thing. Yeah.

**Davide Andrea:** Yeah. Because somebody says, wait, what's this connector? And I don't know. And somebody else says, oh, it's an XYZ. I said, oh, geez, I didn't have that one in there. I better add it.

**Davide Andrea:** Yeah, exactly. Oh, wow. There's a bunch of crimping stuff in here. A lot of these are crimping based. How do you advise people on that?

**Davide Andrea:** Do you know that crimp connectors were invented in the 50s? Before then, connectors had permanent contacts.

**Davide Andrea:** I did not know that. So, because the crimping machines were like, they come out of like post-war period?

**Davide Andrea:** No, nobody thought of it. Everybody, like they would mold the contacts inside the plastic. They never thought that the idea of, hey, let's separate the contact so that it can be crimped to a wire. And then you snap the contact into the housing.

**Davide Andrea:** Yeah, yeah, yeah. Yeah, I mean, it does seem so natural these days, but it's been around my whole life, right? Exactly. Yeah, of course. My first job at AudioPack way back in the day, it was like an audio company. And so, it was a lot of wire to board type stuff. It was like, you know, speakers and microphones and all these different assemblies. But there was these nice little ladies that would work the crimping machine. They'd let stupid Chris co-op come in and do it once in a while to like learn it. And, you know, also they would make sure I didn't stamp my finger off.

**Davide Andrea:** The connector industry is a mature industry. So, one thing that one would think is if you write a book about ASICs, in five years, the book is going to be obsolete.

**Davide Andrea:** Yeah, yeah.

**Davide Andrea:** But connectors are a mature industry. And yes, new connectors do come out every year. But in proportion to how many connectors have been developed over the past 150 years, it's a small part. Right. And so, that's why I feel comfortable that this book is going to be applicable for the next 20 years without becoming too obsolete.

**Davide Andrea:** What I imagine too with like the rise of, you know, just like electrification of everything as well, right? I mean, the time for insanely massive battery connectors for EVs and, you know, just even in the home with heat pumps and just everything being electrical, I suppose, these days. It's just more important than ever, especially to ensure efficient connection between them.

**Davide Andrea:** Which brings the question is why are there so many damn connectors?

**Davide Andrea:** Great question. Why are there so many damn connectors? I assume capitalism is one reason?

**Davide Andrea:** One reason, yes. Actually, more than capitalism is imperialism.

**Davide Andrea:** Really? Okay. Let's go there. Let's do it.

**Davide Andrea:** All right. So, you're the imperial country. Let's say, for example, Britain. Okay.

**Davide Andrea:** The classic example.

**Davide Andrea:** The classic example. And you go to India and you impose your sockets onto India. Oh, my gosh. Then you go back to your own country. They kick your butt out. Uh-huh. And they say, but you know what? The connector we give to India is really no good. We really need a better one. So, they design a better one. Today, you still find the original imperial connector in India, but in the UK, you don't see it anymore because it's not that reliable.

**Davide Andrea:** What's an example of like one that they kind of left for the ages that's still? So, it's still active in certain parts of the world though?

**Davide Andrea:** That's an example. But here's another example. You go to Tahiti and they use the French connectors, which are the ones that have two holes in one pin sticking out. Next door, the next country over in Fiji or in New Zealand, which is pretty close, they will use British connectors.

**Davide Andrea:** Sorry, are we talking about the wall sockets as well?

**Davide Andrea:** Yes, I'm talking about DC power outlets.

**Davide Andrea:** Okay, great, great, great. Yeah, and there's that wonderful map too that shows like connectors and power line frequency and voltage. Why isn't that all one as well, right?

**Davide Andrea:** So, you import a bunch of consumer products to New Zealand. It'd be very easy to transport them over to Tahiti or to Fiji, but they won't work there because of imperialism, because of which empire had conquered them at the time.

**Davide Andrea:** I see, got it, yeah. Yeah, and that is why you would have said South America, right? And you see like country to country, it is both, right? There are regional things, but there's also…

**Davide Andrea:** Yes, regional and in South America tends to be the American plugs because of the imperialism of the… It was not a military one, but it was a commercial one of the Americas.

**Davide Andrea:** Right, yeah. Easier to ship short distances, that sort of thing, yeah. Yeah.

**Davide Andrea:** And now go back to 1940 and you have a small company that's building radios. You have absolutely no commercial connection to the United States. You're in Poland. When you're building radios in Poland, you're going to put an outlet on it, a plug on it that works for European outlets. Yes, you're not going to be worried about this plug working in America because you're never going to export there and vice versa. Right, right, of course. So, that's why…

**Davide Andrea:** There's no auto transformers at the time either, right? They're going straight…

**Davide Andrea:** You're talking about voltage, but I'm talking about the shape of the plug. And there was no need to have a unified AC power connector back then. Today there is, but for historical reasons, we're stuck with at least seven different types of AC power outlets around the world. And it's a headache.

**Davide Andrea:** Yeah, yeah. Well, thank goodness for auto transformers though. And like, I mean, like when I travel, I just bring my laptop brick and a converter plug, a converter that like kind of plugs in anything. And then like everything gets powered off the computer basically. Like that's the move, you know?

**Davide Andrea:** Because USB was developed by an international consortium.

**Davide Andrea:** That's right. Yep.

**Davide Andrea:** And that's why we all use it. And that's why no matter where you are in the world, there's a USB connector and it doesn't matter.

**Davide Andrea:** Right, right, right, right.

**Davide Andrea:** So, historically, that's why we have so many different connectors when we shouldn't. On the other hand, if we only had one connector, we couldn't charge our car with a USB connector because it doesn't carry enough current. We couldn't connect the antenna to your TV with a USB because it doesn't have the high frequency response and constant impedance. So, that's why we have to have multiple connectors.

**Davide Andrea:** Just to go back to that male, reverse male, female, reverse female thing as well with regards to RF, why do some antennas swap it around like that? I just always expect everything's an SMA. You know, the antenna is always a male. Receptacle is always female, that sort of thing.

**Davide Andrea:** Okay. This is how it started. They built modems and they went to the FCC in the United States to get a license. FCC says you got a problem here because you are using an external antenna with a connector. What's keeping the consumer from removing your antenna and putting a Yagi antenna there with the same connector? And suddenly, their Wi-Fi, instead of covering their home, covers the neighborhood. I can't let you do that.

**Davide Andrea:** Yeah, exactly. That's what we want to do as consumers.

**Davide Andrea:** That's what we want to do as consumers. So, the industry building modems said, I'll tell you what, we'll do a custom connector. They go to the company that makes the SMA connector and say, can you make us a custom? And the company that makes the SMA RF connector, Quack's connector, says, well, we can just swap the pin in the socket and they won't fit. So, they do that. And that's how the reverse SMA appeared. Well, the next thing you know, companies started making reverse SMA connectors for the consumer with antennas. And so, the problem was defeated.

**Davide Andrea:** Right, right. Can get kicked down the road.

**Davide Andrea:** Yeah. And it's the same reason why they did all the various reverse Quack's connectors was trying to make them incompatible and people get around it.

**Davide Andrea:** Right. This is like also when, I mean, obviously, an adjacent industry, but like, you know, you see these repair kits from iFixit and stuff like that. And they've got 150 screw types on there. It's like, you know, Apple is going to release a new screw type to try and like be a security screw. But yeah, somebody is going to make a tool eventually because consumers want to get at their stuff because they paid for it. Exactly. They bought it. And it's their right. Yeah, right. Exactly. Yeah.

**Davide Andrea:** Absolutely. That's exactly what it's like. Yeah.

**Davide Andrea:** Okay. Well, that's nice of them to make that more confusing. So, that's called reverse SMA though.

**Davide Andrea:** Yes. RP means reverse polarity. Aha.

**Davide Andrea:** RP. I see. Okay. So, if I, again, go to Identicon and I go in the SMA section, I will find a SMA and a reverse SMA.

**Davide Andrea:** Yes. Let me tell you what else I'm working on, if you don't mind.

**Davide Andrea:** Please, please do. I think this is great.

**Davide Andrea:** My passion for the last 20 years has been lithium ion batteries. That's why I ended up doing battery management systems for them. And I wrote three books about lithium ion. The thing that is coming out now is a sodium ion.

**Davide Andrea:** Yeah. So, what is a sodium ion battery? So, that's like a different chemistry entirely? Or is that the anodes that differ? Or what's...

**Davide Andrea:** It's very, very, very similar to lithium ion. Instead of having lithium, we have sodium. And they use a lot of the same technology and the same materials inside of them. There are no books about them. So, I'm writing a book on sodium ion batteries.

**Davide Andrea:** When is that coming out?

**Davide Andrea:** A couple months. Okay. Great. I finished it. I'm just now doing the proofreading.

**Davide Andrea:** Yeah. We should also call out... I mean, on the connector book, these are all self-published, which is amazing, right? So, you do these on-demand printing?

**Davide Andrea:** The previous three books were by Arctic House. Okay. The last two books were not promoted sufficiently. And they just didn't sell. So, that's why this time I decided to try the self-publishing route. And it has been nice. It's worked.

**Davide Andrea:** Yeah.

**Davide Andrea:** There's more control over the book, which helps me produce what I want. And there's the fact that I can collect higher royalties. Instead of making $5 a book, I make a bit more. That's great.

**Davide Andrea:** I think one thing that we kind of get into is just like the... Yeah, this is a niche industry. This is somewhat niche. Obviously, connectors are very broad, but there's not a ton of people doing sodium ion yet. Fine. You know, higher price for the book. Higher knowledge. Right. Yeah. And so, then you can still recoup some of the investment you've made time-wise, which makes sense.

**Davide Andrea:** Oh, never. I mean... No, no. I mean, I'd be working for 50 cents an hour. Got it. Got it. Got it. Yeah. Okay. And I'm not exaggerating. Yeah. Okay. Okay. It is a labor of love.

**Davide Andrea:** That's great. Well, we really appreciate that. So, tell me about sodium ion. So, like, where would I expect to see them? I mean, is it going to be car batteries? Is it going to be consumer products? Where are they going to be?

**Davide Andrea:** Probably everywhere. Their claim, which is not really true, their claim is that they're safer than lithium ion. The fact is that they both use the same electrolyte. And it's the electrolyte that burns when a cell goes on fire. And in some cases, they even use the same electrode material. So, it is not totally true. They're somewhat safer because of a higher temperature, which they self-ignite. So, that part is true. But there are other reasons why they're not as safe as lithium ion. The idea actually is more of an economical one because sodium is from salt. And salt is everywhere. You're not beholden to any country that has lithium.

**Davide Andrea:** I was going to wonder about the geopolitics kind of thing. They call lithium like new gold, that sort of thing. And, you know, there are a lot of stores, but there are some places.

**Davide Andrea:** And peak lithium, you've heard of that?

**Davide Andrea:** What is it? Peak lithium?

**Davide Andrea:** Yeah, but like peak oil.

**Davide Andrea:** Oh, no, I've not heard that term.

**Davide Andrea:** We're going to run out of oil. People are afraid of running out of lithium.

**Davide Andrea:** Okay.

**Davide Andrea:** Lithium is very abundant, but the lithium that you can extract easily is not.

**Davide Andrea:** Well, salt. Yeah. Sodium is everywhere. You got it. I've got it. We're, you know, it's, yeah. Well, first off, I should just say when this new book comes out, please come back. We want you back for that too. But how much does it take in terms of like manufacturing to refine it down?

**Davide Andrea:** So I am not a chemist. So I don't really know. Pulling the sodium out of salt is extremely easy, of course, compared to pulling lithium ion of whatever the compound is that you find it in. But the big problem with sodium ion cells is that our voltage is all over the place. Lithium ion cells, the voltage is relatively constant as you discharge them. But sodium ion goes from four volts to two volts, approximately, depending upon the chemistry, as you discharge them. So you have to have electronic products that can handle the high voltage swing without giving up.

**Davide Andrea:** That feels like that's doable, though. I mean, like, you know, just thinking about the circuits that are out there for, obviously, the charge controllers for, you know, recharging, discharging, that sort of thing. It's better.

**Davide Andrea:** But you cannot do a one for one swap.

**Davide Andrea:** Oh, sure. I see. Got it. Yeah. So you have to have like a check or you need to know what your chemistry is before you plug it into a different controller, that sort of thing.

**Davide Andrea:** So that's all I wanted to say about sodium ion. If you want to go back to connectors.

**Davide Andrea:** Okay. Well, once you come back and talk about it, I think that's great. And we can talk about connectors on sodium ion batteries as well. I think that's very interesting. The lithium books, I mean, those are all available. We'll have those linked in as well. How wide is the coverage of the arena of lithium ion batteries? Is it around BMS mostly? Or is it usage? You know, like who's the target audience for this?

**Davide Andrea:** It's from the point of view of the battery designer and user. So it tells you connecting cells in series in parallel. It tells you the gotchas to avoid. High voltage applications such as traction batteries for vehicles or house batteries, which may also be in vehicles, but they don't move the vehicle. High voltage grid batteries. The details of having a voltage high enough to be able to produce 240 volts a C out of a given voltage DC. Off-grid and on-grid inverters. And the fact that they behave differently. One is a follower. One is a leader. All these things. So it really is looking at the big picture as opposed to just the details of the cell. Got it.

**Davide Andrea:** Got it. One thing we've talked about, we've called Yehu, I think, Garcia, one of the guys and YouTubers. He does like kind of DIY house battery builds, stuff like that. And I look at like his builds and I'm just amazed. Like I get very scared thinking about that and thinking about like powering my house like that. Is that something that you've done as well where you've built these kind of systems for yourself or professionally?

**Davide Andrea:** No, no, no, no. I've worked with customers and they're the ones building the batteries. I just get in the electronics to monitor the batteries. So, yes, I have built some batteries myself, but not in a great scale.

**Davide Andrea:** It makes me very nervous because of all the inherent dangers, right? Everything can be monitored and there are safety precautions you can take. But that's what I have done myself, I think.

**Davide Andrea:** Absolutely. And I'm telling you, the number one cause of fires that I have experienced has been loose lugs. Really?

**Davide Andrea:** Oh, interesting. Well, that ties back to connectors.

**Davide Andrea:** Yeah, it does. The heat of a soft connection through when carrying high current, it gets hot and it starts a fire. And then it's just a consequence of that. The lithium then catches on fire and creates.

**Davide Andrea:** And the loose lugs is because of vibrational environments and stuff like that as well?

**Davide Andrea:** It was because of poor design and poor QA at the factory.

**Davide Andrea:** Got it. Got it. Okay. Yeah, that's really interesting. I mean, like, yeah, you do think about how that all ties back with, you know, the QA being, I guess that's not even something we talked about here. But like, it's not just about how you crimp a connector on and screw it down. But it's like how you check it, how you do checking over time, you know, that sort of thing. Yeah. Well, this has been very fascinating. Where can people find you and find your books and find your work online, Davide?

**Davide Andrea:** Just search online for connector book and it pops right back. Okay, great. Search for my name and the first one that comes up, Davide Andrea. Davide is, by the way, Davide is an Italian name. I was born in Italy. Nice. That's great. Andrea is just like Andrea. Yeah.

**Davide Andrea:** Great. Yeah. And we'll have links in there as well. I saw you, like we were talking about before the show, but you were just featured on Hackaday as well recently. So people might have seen you on there as well.

**Davide Andrea:** Yes, I saw a spike in book sales in the last two days. I really appreciate the person who wrote about it. There was a mention on Twitter some time back and that resulted in a few hundred sales on the book. I post on LinkedIn once a week. That has not resulted in many sales, but it has resulted in what I hope is a lot of education concepts like the difference between a pogo pin and a test fixture probe. That was my last post from Monday.

**Davide Andrea:** If I could give the listening audience some homework, one would be get this book, of course, but two would be show it to your local connector rep so they also can start speaking with the same terminology and pass the good word along. Because I think this, you know, like shared language, you know, shared knowledge, I think this will really benefit the industry. So thank you for being here, Davide. I really appreciate it. And I'm looking forward to hearing more about sodium ion batteries in the future as well.

**Davide Andrea:** Thank you so much, Chris. Talk to you later.

**Speaker ?:** Bye.
