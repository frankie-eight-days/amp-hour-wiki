---
episode: 678
title: All About Antennas with Katerina Galitskaya
url: https://theamphour.com/678-all-about-antennas-with-katerina-galitskaya/
---

**Chris Gammell:** This is The Amp Hour Podcast. Released September 30th, 2024. Episode 678. All about antennas with Katarina Kalitska. Welcome to the Amp Hour. I'm Chris Gammell of Contextual Electronics.

**Katerina Galitskaya:** And I'm Katarina Kalitska, Senior Antenna Engineer and Just Antenna Enthusias.

**Chris Gammell:** Welcome, Katarina. Thank you for being here.

**Katerina Galitskaya:** Thank you for inviting me.

**Chris Gammell:** I have been following you on LinkedIn for a while, and you post some of the most intriguing and confusing and magical RF animations. I mean, I just had to reach out and ask you how you understand all this stuff. It's really great.

**Katerina Galitskaya:** I don't think I even fully understand now after 10 years working that. But I think I understand more than most of people. So I post these cool animations and do all the simulations.

**Chris Gammell:** Okay, so you post these really great animations. We're going to have links to follow Katarina on LinkedIn as well so that other people can follow along as she posts there. Is this how you kind of see the world as well? I mean, this is a visualization using simulation platforms. But when you look at an antenna on a cell phone, for instance, or a commercial product, do you see radiation patterns?

**Katerina Galitskaya:** Oh, yeah, totally. I mean, I have this superpower now. So, yeah, I mean, I don't see it, of course. But I mean, I often think about that. I often think about antennas around me. And if you think, like, for example, just to guess, how many antennas do you think every day, kind of like at any moment you interact with?

**Chris Gammell:** Well, my desk is full of cellular modems. So I might be outside the norm. But just as, you know, just normal walking around person, I don't know, 100, maybe. Just thinking about like my Wi-Fi antennas and commercial products and stuff like that.

**Katerina Galitskaya:** Yeah, I mean, if you walk around, then maybe. Yeah, yeah, yeah. Right. Walking down the street. You have at least 10. Then like all the cellular towers, right? On almost every building you have. Yeah. If you walk around, if you have a nice walk, you can encounter. And also you meet all the people that have antennas and smartwatches and everything. Everything that doesn't have cables and communicate in some way has antenna in it. Yeah.

**Chris Gammell:** So I just bought a commercial product, like an off-the-shelf product, like a security system, basically, that has local recording. I was very excited about that to not have to pay for a cloud service. But then I realized, so I have a smart doorbell that's now talking through this thing and it's not then getting piped up to Google like my old house. And instead it's just capturing it locally. But I thought it was going to like sit on my network on Ethernet and I would just tell it the address. But it's like, no, actually, you're going to route all your Wi-Fi traffic through this device as well. And that's actually how it operates. And I'm just like, is this, it just feels like it's so ubiquitous and it's so low cost that it's, I mean, is the spectrum just a mess these days? Yeah. Especially 2.4, 5 gigahertz?

**Katerina Galitskaya:** Yeah, exactly. 2.4 is quite a mess, especially, you don't only have Wi-Fi there, you only also have Bluetooth and also some other devices like IoT devices, they work on this, it's called free spectrum, right? Oh yeah, like threads in 2.4, right? Yeah, yeah. So 2.4, like it's free, everybody can use it. And yeah, so that's why it's good to have, and now you know, a lot of companies, they include Wi-Fi 6, Wi-Fi 6E, Wi-Fi 7, so it's broader bands, and also 5 gigahertz bands. So yeah, it's always good to have some diversity.

**Chris Gammell:** Yeah, it's getting overwhelming sometimes. I mean, it depends, I guess, on the day and whatever, but I've, you know, I have a board that I designed that has a ESP32C3 on it and it's got a 9160, an NRAF 9160, so like right there, that's GPS, LTE, and then 2.4 gigahertz. I don't think it does 5 gigahertz, so that's at least three bands and then associated antennas. Yeah. Yeah, that's, and to be completely honest, most of the time, I kind of just punt and I just say, well, someone else can do this and I put a, you know, an SMA connector or a UFL connector on there and I say, someone else has done the antenna stuff, I don't even want to touch that, right? So,

**Katerina Galitskaya:** but I actually think that's the smartest approach because usually you don't want to touch antenna if you don't understand what to do with that. Better to live into antenna design because then you will do some mistake and they will hate you.

**Chris Gammell:** Yeah, right. Exactly. Yeah. The iPhone 4, was it iPhone 4? Was that the one where it like coupled to people's skulls or their hands or something? I remember there was one.

**Katerina Galitskaya:** Yeah, I remember something like that. I think also iPhone 12 was a total disaster because it worked badly if you hold it in the wrong way, according to Apple, of course, but.

**Chris Gammell:** Right, right, right, right, right.

**Katerina Galitskaya:** But yeah, it's always user mistake, right? It's always user mistake.

**Chris Gammell:** Of course. And yeah, so that's a, you know, maybe a good focal point. I guess that's a very complex device, but something like that where it's multi-band, it's multi-radio, multi-protocol, where do you even start with something like that? How do you start to construct a simulation to even maximize the output there?

**Katerina Galitskaya:** Yeah, so mobile phone is a good example for that, right? You need a lot of cellular antennas there and also you need diversity. So you cannot just put one cellular antenna because you need polarization diversity to connect with to base station antenna in every like position of your device. You can hold it in different ways, right? But yeah, in case something blocks one antenna, you really don't want to lose all the connection you want to have some backup antenna or something. And also to enable MIMO you need several antennas. And then you have, of course, Wi-Fi, then you have GPS, then you have ultra-wideband antennas now in new phones, and then you have NFC. Some people don't think that it's antenna because it's very low frequency, but it's still antenna kind of like principle, right? It works in a near field, but it still radiates. So yeah, usually you start with very simple design, imagining your phone as a kind of just like PCB metal block, right? You have just ground plane with the size of your phone, for example, 30 times 100 millimeters or something like that. I don't know. And you start to think first with the cellular antennas because they are the most challenging because they work on the lower frequencies. So for example, 600 megahertz, 700 megahertz, that is the lower band of cellular connection.

**Chris Gammell:** And lowers harder, you're saying?

**Katerina Galitskaya:** Yeah, harder. Interesting. Really harder because they require bigger ground plane to work to radiate efficiently. So antenna, this kind of antennas that we have in our devices, they never... So antenna is just like you can imagine it. I don't know how you imagine it, but probably like a wire, right? Like some wire. But this wire, it needs some feed point. And after this feed point, it also needs some ground plane. And that ground plane works as extension of antenna. You can imagine so if wire is a monopole, so this ground plane is also monopole and it makes dipole. And this is what works, this dipole that radiates, not only monopole. So, yeah.

**Chris Gammell:** Just to put a finer point on that. So if I visualize, actually, I always think about the little LoRa boards. Like I buy one from Adafruit and it doesn't have an antenna with it and it's just like, no, just solder like a roughly three-inch wire on here. Yeah, it's good enough. It's about 900 megahertz. That is my visualization of a monopole, right? Like the cheapest kind of crappiest version of that as I can.

**Katerina Galitskaya:** But you always need to connect it to something. You cannot radiate from thin air, right? You need to connect and that connection will have this extension of the other part of the antenna. Got it. That connection will have this other part. So in our, or before you were mentioning this PCB that you're working with, with the ESP modelers and on that you have antennas. These antennas, they don't work just because they put, they work because you connect them to your ground plane on your PCB. So if you didn't have a PCB there, like metal that antenna connected to this antenna just in the air, like in the vacuum, right? Like hanging in the air, it would never work.

**Chris Gammell:** Got it. Yeah. So when you visualize stuff, are you visualizing like a satellite in space because it is like a vacuum floating in, you know, floating in the void kind of thing? So you're saying though with a dipole, you just had two lengths of wire and you had like a center feed on it.

**Katerina Galitskaya:** Yeah.

**Chris Gammell:** That would work. But a monopole does not work.

**Katerina Galitskaya:** Yeah. The monopole, you need to feed it from somewhere. Monopole, it will radiate around it, but you need to feed point to that, of course. And also monopole is much, much bigger. So dipole is twice smaller than monopole. Got it. So all the antennas that we have in our consumer electronics, they usually, we tend to make it as small as possible, right? And for that, we need to kind of like make them like meandering or use just a fraction of a wavelength and construct antenna like on the very, very limited space. And that is just what I'm explaining now is just the antenna part. So basically the radiator that's kind of like focused the signal in itself, but it will never work without being connected to PCB or like ground plane. It, of course, depends a lot on antenna type. Different antennas require different, but if we're now talking about like really common, like some PCB antennas, right, or as well in our mobile phones, it's not PCB antennas there. It's most probably some 3D shapes antenna because we really need to use all the spaces, but they also connect it to ground plane. And returning back to why lower frequencies is harder because we want to keep devices as small as possible, but the lower the frequency, the longer the wavelength. And we always want to have our PCB size half of the wavelength on both antenna and ground plane. So on the ground plane, we need at least quarter wavelength then if we can just split it equally between antenna and ground plane. And then when you calculate that for lower frequencies, you need at least 180 millimeters or so. And if you don't have that, then you just decrease efficiency of your antenna. Like you cannot fix that. This is just physics. There is no way around that.

**Chris Gammell:** There's no like better antenna, fractal design, nothing like that.

**Katerina Galitskaya:** Nothing will help if you don't have enough PCB size.

**Chris Gammell:** Got it. I do think throughout this episode, it might be interesting to have just kind of easy rules, which are obviously meant to be broken and or confirmed with an expert such as yourself. But that PCB size is a really great one, right? So you said 180 millimeters. Was that for a specific wavelength or is that just a general?

**Katerina Galitskaya:** No, no, no. That is for, it comes from a wavelength. So it's better to remember it's like that. That's for, if you, if we are talking now about just some PCB antennas, right? For example, inverted F antenna, some, this is very popular, right? Inverted F antenna, you always see it on ESP. Low cost ESP boards. Yeah, exactly. ESP. It's all the best.

**Chris Gammell:** How do we make it lower cost? We make the antenna out of the copper that's on the PCB. Yes.

**Katerina Galitskaya:** So this PCB, PCB antennas, they need a quarter wavelength ground plane for 2.4 gigahertz. It's around 33 millimeters.

**Chris Gammell:** And this is just ground plane. That's measured at surface area or that is length?

**Katerina Galitskaya:** Length. So like you have antenna part and then down, down from the antenna, it's a length. That's why it's also very important to place your antenna so that you can have very efficient way of using this ground plane. For example, if you have PCB that is short on one side and long on another side, you want to place your antenna on the shorter side so you can use this long ground plane. Aha.

**Chris Gammell:** Interesting. Okay. That's another great. Okay. So these are kind of the tips that are coming out of here now. So it's obviously have a large enough PCB plane or ground plane rather, but then also place the antenna on the short side or take advantage of the length. Exactly.

**Katerina Galitskaya:** Always place the antenna on the shorter side of the PCB and better in the corner and always on the edge, never in the center of PCB. Yes. For the love of everything, I don't know how many times I need to suffer and see on some internet, some design where people place like ESP model with the E5 in the center of PCB.

**Chris Gammell:** We did a cutout though. There's a cutout in the middle of the PCB.

**Katerina Galitskaya:** Yeah. I mean, this is actually good case if they have cutout.

**Chris Gammell:** Okay. Okay. So better than nothing, but not great.

**Katerina Galitskaya:** No, no. I mean, it's still very bad, but I think that it's not always that you see that people who place antenna in the middle of PCB, they also thought about cutout. Usually they don't think about antenna at all and they think that you can place it everywhere, like anywhere.

**Chris Gammell:** Right, right. They think it's easier routing for my signals, my low and slow signals if I turn this module 180 degrees and the antenna's in the middle of the board.

**Katerina Galitskaya:** Yeah. Yeah, exactly. Because it's easy, right, to place, I guess, to route and everything. But yes, always place it on the edge, always place it better on the shorter side and always have a good keep out area so no metal below antenna on any layer. On any layer.

**Chris Gammell:** Yep, yep. Yes.

**Katerina Galitskaya:** And usually if you work with this, like for example, ESP model, they always have guidelines, right? Just follow the guidelines for antenna, for like footprint because you usually want to have some bigger keep out area than antenna itself just to be on the safe side and don't place any metal components like big components. Sometimes you have some big capacitors. Sometimes you have like USB port, for example, or something like that.

**Chris Gammell:** Right.

**Katerina Galitskaya:** Just don't place it near the antenna. Choose some other place.

**Chris Gammell:** Yep. Yeah, actually, you have a recent post that we'll link in that's a really good example of kind of all the things not to do. It's pretty great. Yeah. Yeah. How often are people approaching you with this sort of thing? Like, I mean, I imagine you could look at something like this and just snap. That's not right. You know, like that sort of thing.

**Katerina Galitskaya:** Yeah, I usually spend like maybe 10 minutes per week just scrolling. I have several hashtags on LinkedIn like ESP32, PCB design, and just scrolling like people post their designs. And sometimes I just give some guidance because in 90% of the cases, people already know some generic guidelines and they just maybe need some recommendation. For example, if they have two antennas, what's the best way to place two antennas so they don't couple to each other. So the best way, right? Or maybe in this case, better to turn antenna 90 degrees and place it on the shorter side. But yeah, sometimes you see something like very, very outrageous. The antenna is placed in the middle of the PCB and there is no clearance area. There is metal below it and all the metal stuff around it. So yeah, that's sometimes it happens as well.

**Chris Gammell:** Yeah, I actually gave a talk back in 2019 when I was starting to do some of these my own designs but I actually followed a different talk from a past guest of the show, Mike Osman, who did the HackRF1 and he gave five rules for his stuff and I just follow that and I've been relatively successful from that but that's actually most of the time then I, like I said, I just kind of let someone else do the actual antenna piece and I'm just really designing the board to follow like it's basically like the guidelines you mentioned in the PCB or sorry in the data sheet I'm just kind of using these as a data sheet guideline for the PCB itself.

**Katerina Galitskaya:** Yeah, I think that for these 2.4 antennas they are quite forgiving if you just follow these guidelines, right? You have clearance and you don't design actual antenna yourself maybe because for that you need simulation but if you already have footprint for antenna if you have actually like radio antenna for example you have ESP32 model then you just follow the guidelines and you can place it yourself even if you are not antenna engineer for everything that is more complex than 2.4 IFA yeah, I would rather go to antenna engineer because then like so now I work mostly with the base station antennas but one year ago I worked with just customer electronics like all the wireless devices that you can imagine phones, headphones, routers, like everything I designed antennas for them for that and yeah it's how you can how you can understand if the project manager or is the owner of the business is good right? They come in the beginning to you and then in like maybe 30% cases people already come with the fail ones because they thought that they can manage this themselves they

**Chris Gammell:** how hard could it be right?

**Katerina Galitskaya:** yeah they didn't pass certification or they didn't even get any signal or something and then they ah okay so the antenna part maybe maybe it's not so easy and then they come to company that's like design antennas and then in this case it's always like okay you already have a device you cannot even change a lot of things right? because they really don't want to spend even more money on changing all the things but sometimes because you kind of left antenna apart on the very last you have very bad location you have very bad design PCB design you don't have enough space or whatever so if you come in the beginning if you think about antenna in the beginning you take that into account all the things needed for antenna

**Chris Gammell:** right I mean I can imagine even at the mechanical level like of you know leave this region just to go back to the phone example we're going to have someone holding this in their hand so like think about the hand we need to model you know a piece of meat on the back of this phone to that might be absorbing signals

**Katerina Galitskaya:** for sure it's always like next thing but it may be more advanced so we just gave some tips for for example PCB engineers right who want to just put for example ESP32 model to the antenna so for them these tips are enough just to keep antenna clearance keep it on the shorter side of the PCB and on the edge I think that will be enough and you will get good efficiency from

**Chris Gammell:** 80% of the way there right

**Katerina Galitskaya:** exactly exactly and you will at least have for 2.4 gigahertz it's quite forgiving so you will get signal but then if you like one step further then you think about where where your device will be because if it's underground that's one case if it's hanging in the air that's another thing if it's in your hand that's third thing if it's mounted on some metal plane it's another thing and that's called antenna environment and that is really important because it changed and in some cases significantly changed how antenna behaves and you cannot anymore use that antenna that was kind of you thought about it as it was like in the vacuum you know and then you take it in your hand and it's not the same antenna anymore

**Chris Gammell:** ! Could you rank easiest to hardest in terms of the antenna environment?

**Katerina Galitskaya:** The hardest is underwater I would think and think about this underwater communication you cannot communicate there water absorbs 99.99% of signal there is nothing you cannot that's why all these underwater things they try to invent some new things I don't know communicate with light or something like lasers I don't know but not radio frequencies right

**Chris Gammell:** yeah I think obviously a lot of sound right like low frequency stuff will travel through water right but it's still low bandwidth at that point it doesn't really help

**Katerina Galitskaya:** I to be honest I don't know I just recently read some article about some new approach that's testing for this submarine kind of communication but it's yeah it's not it's not radio frequencies and next one I would say human body human body because it's well we kind of come from 100% water now we come to 80% water so yeah it's very challenging and you always need to take into account your user case in this sense then a lot of things coming from that so first of all all people are different fat tissue different and between people and also between part of the body so if you have a head for example headphone you have one like structure that's close to your device and then if you have some device that is on the belt for example that's another environment

**Chris Gammell:** so it's like a fashion choice too if you on your belt or not

**Katerina Galitskaya:** GPS tracker or something like and I designed a device like that just it was something like GPS tracker I think for older people and they just put it on their belt you know like just sure sure yeah yeah and then for example smartwatching on the wrist then I don't know a lot of things then also implantable antennas it's inside the body so you have a lot of a lot of cases and you design your concept taking into account that so how usually you work with that is you start with a vacuum you start with just like very simplified design and you okay you at least like design something okay I choose this type of antenna so you make some very initial decisions about your future design and then after you kind of have the concept you really need as soon as possible start to work with the environment so for example if it's phone then primarily it will be in hand and near your head and then you include that part in the simulation and you simulate with that because human body will absorb and reflect depending on frequency a lot of signal and then it also can even change frequency of antenna so you really need to take into account ! After that you need to prototype and when you have your prototype you cannot measure it in vacuum because it's just hanging in the air because it's already not the same antenna you tune it to work on the body so you need human dummies there are a lot of things in the labs that kind of human head a bit kind of creepy Halloween-ish feelings you have hands you have heads you have the torso parts

**Chris Gammell:** yeah exactly

**Katerina Galitskaya:** and it's like they are very heavy because they have this liquid that imitates tissue right so and you just mount your prototype on that and hope for the best this is like one challenge right and the second challenge when it comes to humans we have a lot of safety regulations and we have a lot of certifications you cannot just blast signal towards humans with whatever power you want you need to it's called SAR so specific absorption rate and we have this limit that regulates for for example like for one like gram of tissue we have this power of signal maximum that can come to and then you need to of course adjust your device adjust your total power ready total radiated power for example or adjust efficiency of your antenna so you don't go over it and then when you kind of adjust for that you also need to pass certification for operators for example if you want to have cellular connection and for that you want to have more efficiency and you want to have more radiated power because they have limits and so you need to really balance between those you cannot have too much but you also cannot have too low and you need to be really in the sweet one

**Chris Gammell:** thing that seems difficult from just what I've seen the testing side of things too is that you only have one or two dimensionality in the testing capability too right so you have these wonderful visualizations that are from the simulation models but you don't get to see that unless you have multiple probe points in an area right what does it look

**Chris Gammell:** like

**Chris Gammell:** ! ! So

**Katerina Galitskaya:** this animations it's like fields we cannot see I mean now I think some companies at least I saw some advertisement that they have some scanners like field scanners that you can see the fields

**Chris Gammell:** but

**Katerina Galitskaya:** I don't know maybe something

**Chris Gammell:** that a CEO would buy but then it would be like this isn't that useful for us exactly

**Katerina Galitskaya:** that's what I wanted to say but I don't know that over there measuring so we have an echoic chamber if you ever seen this like small a lot of a lot of small kind of triangles pointy things yes yes pointy things so in an echoic chamber you can measure how antenna actually radiates and from that you get total radiated power and efficiency and you also can build cuts of radiation pattern and even you can have this 3D radiation pattern so it all depends on how how yeah it all depends on how long time you want to spend to measure these cuts because you need turn every degree or so and measure so yeah

**Chris Gammell:** because there's always like the rotating tables too right exactly the product or you got it yeah so that's kind of what I'm thinking about is we have these visualizations with the different field strengths that we're visualizing with different colors and shapes and lobes and all that stuff but then when you get into the lab you basically you have to then just step the antenna like one meter from the product and then 1.1 meter from the product right if you wanted to have the equivalent kind of remapping you would have to have multi-step tables or multi-step

**Chris Gammell:** Measurements and then reconstruct it from those correct I

**Katerina Galitskaya:** don't I don't quite understand what kind of product you mean like we have antenna and in an echoic chamber there is no product like antenna does not connect to anything it's just we have like default antennas there that's yeah well

**Chris Gammell:** it's a second antenna that's actually receiving second antenna that

**Katerina Galitskaya:** receives yeah yeah second antenna that's we have it measured we know how it works and we can judge by that antenna our antenna

**Chris Gammell:** yeah so what I was saying is to perfectly replicate a simulation like a visualization simulation type thing wouldn't you need infinite antennas !

**Katerina Galitskaya:** I guess and I know that there are these kind of scanners that do that but not for antennas because it kind of doesn't make sense you don't even need that but I know that there are these kind of scanners that scan PCBs for EMC issues right and then you can see kind of visually where you can have some potential EMC issue or something like that but for antenna it doesn't make sense like these metrics that I just described like VNA passive measurements and then over there measurements in an echolid chamber that's more than enough for antenna testing sometimes when we have cellular antennas we also have some active measurements so when actually our antenna receives signal and they send signals so actively working not passively working that's also but that's very rarely when it happens because like 99% you can do everything with the passive measurements and confirm that your antenna works

**Chris Gammell:** got it what does it look like on the flip side for the the people that work in a calibration lab called like a measurement like test engineers yeah I guess so what does it look like to make sure because you're saying that you're designing a custom antenna and then it is transmitting to a reference antenna

**Katerina Galitskaya:** yeah

**Chris Gammell:** how do they know that that is good yeah

**Katerina Galitskaya:** well yeah it's calibration and you buy it from so you buy it from good vendors that provide all the data about this antenna and then you calibrate it in your chamber in your environment and that's how you know like and sometimes you can also see it in your measurements when something is wrong for example you get efficiency more than 100% it's it's maybe I need to be a bit suspicious maybe I don't need to believe it even though I would want to just

**Chris Gammell:** ship off the report and say boss I deserve a raise yes

**Katerina Galitskaya:** and a Nobel prize

**Chris Gammell:** yeah right right right that's interesting so okay so we're at the point now so we've kind of walked through some of the guidelines around it and maybe some of the testing stuff here but I guess one question I had is aside from talking to an antenna engineer and putting a custom antenna on board is there a guideline for when I should even be considering to do that sort of thing do you have kind of high level guidance on when to go antenna down yeah yeah I

**Katerina Galitskaya:** understand your question so I would say that if you use for example cheap

**Katerina Galitskaya:** it always says what is the reference board for this antenna and then you also have a lot of plots all the efficiency all the nice things there but all of that only guaranteed on this reference board if you have anything and that reference board is exactly quarter wavelength so if you have anything that is significantly different from that I don't say like five millimeter different or like but significantly for example you have round shape of the PCB and or you have twice smaller PCB this antenna won't work like they show like 100% I guarantee that it will not work as they show in this data sheet and in this case I guess it also then depends on frequency if you want to work on the lower frequency or you have multiband antenna then I would really suggest to have some somebody who understands antenna I

**Chris Gammell:** looked at a GPS module and I was like what are the options for an antenna here and then I think it was just a little teeny tiny ceramic antenna there is no way this works

**Katerina Galitskaya:** quite good most of the GPS antenna they make in this ceramic because it's quite low frequency right if you think about it 1.5

**Chris Gammell:** I didn't but I'm just thinking the size of the antenna itself

**Katerina Galitskaya:** because ceramics is super high the electric constant and the higher the electric constant you have like substrate right so usually you use FR4 the cheapest one and it has 4.4 the electric constant epsilon so if you put your antenna on that so wavelength decrease in the proportion of this epsilon so the higher epsilon you have the smaller antenna you need but also efficiency suffers from that as well but it's like another story so if we go with the smaller we want like if we want the smallest antenna we would take the highest epsilon so highest the electric constant and those antennas those GPS antenna they have really high epsilon like 10 20

**Chris Gammell:** oh wow okay okay

**Katerina Galitskaya:** that's why they can put just some metal dot

**Chris Gammell:** and it works got it okay all right just off base like that's the thing like I'm basically you know like you said looking at reference platforms and kind of yeah but you're already

**Katerina Galitskaya:** doing more than some people because some people don't even look at this so yeah I would say if you just deal with a 2.4 antenna some kind of like PCB antenna probably you can do it yourself if you have experience in PCB design right you can read the guidelines you can understand the guidelines probably you will manage 2.4 is very forgiving yeah

**Chris Gammell:** so the real question then is am I going to try and build the antenna myself in the PCB that's so that's where you really should be asking yourself tough questions around that sort of thing versus buying

**Katerina Galitskaya:** I think I wouldn't do that if I were like PCB designer I've

**Chris Gammell:** actually been really surprised on the 2.4 so just to stick with the Espressif example I've been seeing a lot more designs go away from inverted F on a PCB and instead they follow with that bent metal it's still super low cost because it's just like a stamped metal piece that gets inserted but it's basically like a folded inverted F that gets soldered into the board that's lower you mean

**Katerina Galitskaya:** like 3D shape kind so there's no

**Chris Gammell:** inherent value there other than maybe allowing you to have a smaller board shape

**Katerina Galitskaya:** that sort of thing yeah I think you no you won't get any more benefits from that because it still comes from size of your ground plane but you can yeah maybe like use smaller PCB space on the antenna itself and thus you have smaller PCB size if you want to achieve that and also if anything on the PCB but you have space above PCB right so you can place something there it's all like sometimes it's quite beneficial to have some 3D printed it's also like this laser technology if you know it's called like LDS that you can print antenna on the for example plastic cover if you saw not this post but last week I posted about new airports and they have this LDS technology and antenna like I showed there how this antenna looks like so they basically printed it inside and it's some funny 3D shaped antenna that because this is such a small device right you really cannot don't have any place to put antenna and you need good antenna because it's human body you have a lot of challenges and they solved it by printing this unique 3D shape antenna

**Chris Gammell:** yeah I think that's the same one I don't know if you watched the Applied Science channel but Ben Krasno did some experiments where he was doing his own laser sintering and stuff like that to try and replicate that process but I think it is almost always targeted at those 3D antennas for these applications yeah

**Katerina Galitskaya:** what does

**Chris Gammell:** the feed look like for something like that you still have to !

**Katerina Galitskaya:** usually it's some like spring that goes from PCB and it usually has some pressure kind of you know so it's kind of like spring with the pressure and you then or it can be also pogo spring so there are options to feed that yeah

**Chris Gammell:** got it okay so you had mentioned some of the MIMO stuff and like multi some of the newer technologies are also doing beam forming and things like that so what should they be thinking of that have beam forming beam steering on board and things like that

**Katerina Galitskaya:** this is very advanced so

**Chris Gammell:** definitely call Katarina yeah

**Katerina Galitskaya:** this is very advanced so it's very how to say so with the beam forming you always have a lot of antennas so it's array of antennas right we cannot beam form from one antenna because you need some shift in phase between antennas to steer beam and also one antenna has very wide radiation pattern just radiate everywhere usually so for example if you imagine dipole or monopole it's just like around everywhere or omnidirectional so called that's what we want in our for example rotor we want it to radiate everywhere so we have good signal in the bedroom in bathroom everywhere then when we come into beam forming we want very narrow beam so we can point into direction and deliver signal very high concentrated signal only to this point not to other points that's maybe near it so if you can imagine just some beam that is focused for example laser it's focused beam of light and the same with the RF signal we can just focus it into one direction and transmit some very high power data to the person who received that signal or antenna who receives the signal and this is what all the base station antennas are doing they have beam forming because so the antennas are placed the base station antennas they are placed somewhere high on the buildings right and then you really don't you don't have people there like hanging in the skies so you don't need to transmit signal you really need to transmit signal towards the house for example that's there or towards street and that's how you have a lot of antennas there in this base station antenna and they all combine together and create one beam and then you steer it some antennas steer mechanically so actually turning mechanically but it's not so used nowadays it's usually like actually like old satellite beamforming yeah exactly so this is actually like actual beamforming that is used now so you can send your signal there when you know it will be used because you don't want to just blast the power to nowhere kinda

**Chris Gammell:** okay

**Chris Gammell:** okay all right and you said it's very advanced is that because usually it is more on like a base station side because you're serving multiple clients versus more on the device side so something like a starlink dish has beamforming

**Chris Gammell:** to try and hit different satellites in the sky

**Katerina Galitskaya:** yeah well I don't even think so for example yeah so it's always something it's more advanced because it's either radar beamforming they have on the right base station antennas so it's kind of like advanced if you go into that design you really need to understand what you're doing what you're doing so it's not consuming electronics I would say like okay in our mobile phones we have already some millimeter waves so millimeter waves are slowly coming now to you know we have now 5G and there are two types of 5G normal 5G that is just faster than 4G and then like super super 5G that is millimeter waves and several years ago when we were very hyped for this millimeter wave 5G everybody were talking about that everybody were like planning what we will do like we will stream our holocromes or whatever with this 5G but now nobody talks about that anymore because everybody it's completely different technology it's completely different frequencies it's wasn't it

**Chris Gammell:** also like you needed to have because of the distance of the millimeter frequencies and stuff like that you needed to have you basically needed to have a network and every light pole so that you're exactly exactly

**Katerina Galitskaya:** because why we use this low frequency now in in cellular communication because they go like they don't care about shit on their way like they go so yeah exactly they don't care they just go and go and go and millimeter wave they care about everything they care about rain fog walls of course everything and because it's such a high frequency so for example we are talking about 30 gigahertz compared to 600 megahertz right so it's scale differences there yeah it's scale difference and but what you can do it's this frequency is much faster and if you can have this mesh then you can get really big benefits from that but yeah it's very expensive that's why everybody were like buzzing about that but then people calculated what will it cost and everybody were like oh well actually maybe not

**Chris Gammell:** all the carriers are like well maybe we'll just lean on our existing infrastructure for another couple decades

**Katerina Galitskaya:** infrastructure because updating that's what I do now with my work updating from 4G to 5G easy

**Chris Gammell:** yeah

**Katerina Galitskaya:** well I mean of course you need to still but also it's still new frequencies some frequency bands you still need to update antennas but it's very comparable to what you have now if you want to update to millimeter waves it's completely everything is different cables are different

**Chris Gammell:** yeah

**Katerina Galitskaya:** cables everything it's not just antennas it's all network the whole network and yeah and then of course you also need to think that the obstacles they will destroy the signal but also just air just pure air will destroy signal so it will go like one meter and then nothing so you really need mesh of these base stations and then you maybe it's easier to just learn

**Chris Gammell:** how to change the weather maybe that would be the best way to do it

**Katerina Galitskaya:** yeah or like all the air and have vacuum it will make it a bit better to but still so yeah it's now everybody talking about 6G so that's that's the next big thing but well 6G it's even higher it's tetrahertz that we're talking about it's much much higher but of course it's not in the same sense so it's not nobody talking about like actually building base stations or whatever for that it's a bit different applications yeah

**Chris Gammell:** there's a lot of hype built into that stuff I feel like and I just kind of ignore I'm like I'm still using you know if I could still buy the modems and the towers are still turned on 2G is fine for most of the you know like sensor things except for the power needs on the device side 2G bandwidth wise is fine

**Katerina Galitskaya:** yeah true but for example here in Europe I don't know how it's over there but here in Europe they switch off all the 2G 3G networks so you don't even have now it's gone I think the only place

**Chris Gammell:** that 2G is still around is I think some places in Africa still have it because it's like really embedded in some of the infrastructure stuff there but often it's still fallback they have 4G but then 2G fallback is common on a lot of cell devices that I buy so yeah yeah it's it's it's no it is no more all those simcom modules they're dead in the water

**Katerina Galitskaya:** I mean from some point I kind of I like it kind of because I really like the technology and I maybe a bit sometimes I like this bit of harsh push because if you don't push then companies they will just prefer not to do anything just like being this very chill safe zone right yeah but if you push a bit like with these things I guess it can be really irritating and so in the beginning but then it usually leads to some good things

**Chris Gammell:** yeah I agree I agree okay so we mentioned multiple times on about your simulations that you share and things like that when should I start simulating when

**Katerina Galitskaya:** in all engineering area you always have some open source things but in this also we have some open source software that's been developing and currently supported by community so yeah you can try that and you don't need money to buy licenses and so well I don't know I think if you want to try

**Chris Gammell:** what are those two pieces of open source yeah I

**Katerina Galitskaya:** think that's a one called EMC so EMS oh

**Chris Gammell:** S-E-E yeah

**Katerina Galitskaya:** so not EMC like electromagnetic compatibility but EMS so yeah so yeah like visualizing

**Chris Gammell:** electromagnetics right like yeah yeah exactly yes yes yes

**Katerina Galitskaya:** so one it's called like that and just open source and another one some I don't remember now like off the top of my hand but some some strange name I remember the first one and yeah so it's like you know it's like key card it lives only by like support from the community kind so you solve everything together

**Chris Gammell:** yeah so yeah I feel like there's so much like of a graphical component so I use free key card the graphics are great and improving but they're that's feels like the hardest part like the the actual solvers like the mathematical solvers but then the visualization on top of it that feels like that's the that's the thing that people are often paying for yeah

**Katerina Galitskaya:** to be honest like in this antenna design this visualization it's mostly like a kind of playing around yeah with all the animation that I share I don't really need them like really interesting okay so maybe you can tell

**Chris Gammell:** us that what's that push-pull then so you share these visualizations which helps newbies like me in this scenario but how are you using it differently then in terms of your design work yeah I basically

**Katerina Galitskaya:** I simulate the same things the same metrics that I will test later

**Chris Gammell:** okay

**Katerina Galitskaya:** so I simulate this return loss matching to the impedance I try to optimize that and then I try to optimize the efficiency but sometimes of course you want to for example see how fields go especially in the beginning when you for example when you are a student you want to know okay but like fields go there and then maybe I like I need to put somewhere something there or like some shielding or whatever but when you already kind of know most type of antennas and then you already know what it will be and you don't like if I design by myself like actually my work actually my project I never plot these fields or

**Chris Gammell:** animations

**Katerina Galitskaya:** I don't do that well maybe like one case out of hundred when I'm really confused or troubleshooting or trying to understand what's the problem what's there like some resonance happening for example and I cannot understand so then it might help to plot some fields and see what's happening but usually it's all numbers it's much more boring than a show on LinkedIn

**Chris Gammell:** that's a great thing because like you said I mean I expect the antenna engineer is doing that visualization of fields but it's not as practical because like we were talking about with anechoic chambers you don't validate against that either right it's not like you can go and visualize and be like oh well look this lobe is over here it should be over there right it's like no that's not how it works yeah okay what about like the iteration so you get tasked to go redesign an antenna how do you know what to change like what are you tweaking in terms of geometry of the antenna or capabilities yeah

**Katerina Galitskaya:** so for example you kind of come it antenna so how can I solve it how can maybe my trace is too bad too narrow too wide maybe I don't have good grounding maybe I don't I have bad matching network for the antenna and so on so then if you have several antennas you can much more like challenges coming from that you can have coupling between these antennas then you also need to see how they couple to each other like how they affect each other and maybe separate them further maybe like put them further away maybe like turn one on ten and ninety degrees so they place so you have some like polarization diversity yeah it's just kind of you if you need to troubleshoot then you come from the you start from the problem

**Chris Gammell:** got it okay I had done some RF stuff I was starting to get into a little bit more I had an 8753 in my old lab and you know I'd be looking at Smith charts and moving my hands near an antenna and I'm just like I don't know it was always tough so one of our long time guests on the show Jeff he would be like well you got to go back to first principles and understand that sort of stuff and I'm just waving my hands and the Smith chart is bouncing all over the place

**Katerina Galitskaya:** human body as we talked before it's very harsh yeah so well Smith chart is the great tool if you understand what's !

**Chris Gammell:** yeah right so yeah and maybe that so you said troubleshooting so maybe could you lay out the tools that you use when you are in a situation where you're like this antenna isn't performing as expected and you have simulation at your disposal but maybe like other troubleshooting elements that you use to then back calculate what might be the problem

**Katerina Galitskaya:** so if it's already prototype and I see that it works not as I would expect then it's usually something with the matching

**Chris Gammell:** and

**Katerina Galitskaya:** then you usually I don't know like maybe for very simple antennas you don't even have some matching network but usually you always put at least like two components two three components of matching network

**Chris Gammell:** just put the shape and you're in good shape yeah

**Katerina Galitskaya:** so and you usually start looking into the matching network and try to match it better

**Chris Gammell:** okay so you're saying that you're starting from a prototype of an antenna and you know that that is working because you've done measurements on that in the lab and such but then I guess how do you know that the antenna was right in the first

**Katerina Galitskaya:** oh well so it's it's kind of feeling so you have of course you have all your metrics right you can see radiation pattern in the in the simulation so if we're talking about like first steps you can see the simulation pattern and based on that simulation pattern you want in the end for example like if you if you're talking about headphones we put it in our ear and we really don't want blast signal in the head what we want is to have signals outside the head and that's how you can think okay I need this kind of radiation pattern right so it goes like in this direction and not to that direction and because you know like different types of antennas you know which type of antenna will give you approximately that so you at least kind of yeah

**Chris Gammell:** that's like a topological choice of like yeah topological

**Katerina Galitskaya:** choice and also like the principle right so some antennas work differently some antennas like only directional some antennas are directional some antennas work over the ground plane some antennas doesn't need ground plane below it so you choose this and then of course you have restrictions of your environment so you start to put this antenna that you chose you know that this antenna like in ideal world for example it's like 100 millimeter straight wire this is this antenna like in its prime but then you need to put this like in such a shape that it will fit into your device yeah and then you have radiation pattern you have efficiency you have all the numbers right in the simulation that you are looking for so for example you know that you want 80% efficiency that you want this radiation pattern that radiates outside the body not towards the body you want to have good matching you want to have good return loss not no reflection back to the PCB yeah that's that's how you understand that this is an antenna that fits this application

**Chris Gammell:** got it yeah yeah and I guess like you said I mean we're really talking about like a almost like a spec sheet that you would have been handed or working collaboratively with a mechanical engineer to do that sort of thing and then

**Katerina Galitskaya:** well yeah usually you have you almost always you have some specification for example how much gain you need how much efficiency you need what size restrictions it's always some size restriction unfortunately yeah and then like weight

**Chris Gammell:** so if you if you had your choice you would have like just a car sized PCB that sort of thing

**Katerina Galitskaya:** yeah just in the vacuum like no people around nothing around just antenna like yeah

**Chris Gammell:** it's the easiest yeah easiest and just

**Katerina Galitskaya:** blasting in all directions yes

**Chris Gammell:** yeah totally totally yeah wait so is satellite design easier or harder than I don't know ground

**Katerina Galitskaya:** satellite design is well we have a lot of a lot of antennas on satellites so it's very different they also have they also now they have like millimeter waves they have

**Chris Gammell:** oh sure

**Katerina Galitskaya:** higher frequency like lower frequency higher frequencies and also they have this dish that's very high gain because you need very high gain to reach longer distances it is like as an antenna design it might be not so complicated but it's such a harsh environment imagine all the vibrations imagine all the risk there like weight restrictions you cannot just like take 10 20 30 kilograms like of the metal and just shoot it up the space they have very harsh weight restrictions they have very harsh temperature so requirements right it needs to work perfectly at minus 100 and plus 100 degrees and so it's very harsh environment and that's why you only kind of use only like restricted amount of antenna types that can survive this

**Chris Gammell:** yeah that that seems like that would be and then of course all the radiation coming from the sun I'm sure is also not great yeah yeah you really

**Katerina Galitskaya:** need very like very robust like very robust very antennas that you like you can trust that they will work a long time and in this very harsh environment yeah in all the radiation and because there are a lot of satellites there and a lot of kind of like signal pollution as well so yeah it's very it's very harsh in this sense like to actually get your antenna work in the environment I don't

**Chris Gammell:** think I have any chance of designing a satellite antenna anytime soon so I'm probably going to stick to more of the when I think about this sort of stuff that the designs I'm personally I'm gonna go personal here the stuff I usually do like I said is usually you know offloading to someone else using a UFL connector something like that maybe putting antennas on the PCB once in a while for 2.4 not really I don't really plan to do anything and then like probably the extreme low cost would be adding a coiled antenna to like a LoRa chip or something like that or a wire that's about as far as I'm gonna go and I have very low expectations like that's like that's just to try it out and then like I expect it to go across my desk as opposed to operate in the field in harsh environments that sort of thing

**Katerina Galitskaya:** yeah but I actually think that's to have this connector for an antenna it's usually if you can afford that right if your device can afford to have antenna outside of the device that's always better than to have PCB antenna

**Chris Gammell:** okay that's yeah that's another good good rule to have there does it matter then you still the ground plane size still matters though as well right

**Katerina Galitskaya:** it's more forgiving

**Katerina Galitskaya:** that antenna that embedded in the PCB

**Chris Gammell:** okay all right yeah I've used a lot of those like flex antennas in the past as well they're okay but it does also seem like sometimes it's directionality like if I try and shove it inside a plastic case with all the other stuff that's going on in there it's maybe not the best idea sort of thing

**Katerina Galitskaya:** yeah a flex antenna can be good but they also you can break them very easy

**Chris Gammell:** so

**Katerina Galitskaya:** the antenna itself okay is supposed to use like that in this way that it's bent one time and you just keep it like that's this way yeah exactly exactly exactly flex and flex and all these things and it can get broken then of course the connection to this antenna as well like how to feed antenna it also can be a bit tricky and then you really need to think in this case about the material of your case because antenna is flash to that case and that case is the electric and this electric has the electric constant usually it's some plastic so the electric constant not so high like 2.4 or something like that but sometimes you have some resin in plastic sometimes you have some fancy 3D printed

**Chris Gammell:** enclosures yeah exactly

**Katerina Galitskaya:** and then the electric constant can get really high and if you remember we discussed that before the electric constant change the antenna working frequency so that can also affect antenna a lot so you need to think about that that also works for PCB antenna that works for all like everything that is in the near field of the antenna kind of affects antenna so the enclosure of your PCB antenna also affects antenna but usually we don't maybe spend too much time on that because it's already you have so much challenges people are already tired from that so you try to maybe at least to minimize that but if we are honest that also should be taken into account but if we're talking about most common plastics they are not so high in the electric constant ! you see that your antenna doesn't work as you thought even though you have good clearance you have good PCB size you have everything but then you put it into your case and it doesn't work anymore because the electric in the case shifted the working frequency yeah

**Chris Gammell:** well and then people need to give you a call and help fix it up but that's probably where we should leave it because I've already you it's also a little frustrating maybe but then I get to talk to brilliant people like you and learn from that so where can people follow you online and see all these simulations I've been talking about

**Katerina Galitskaya:** yeah it's my LinkedIn I guess they can find me by my name or by some links that you can provide just Katarina Galitskaya on LinkedIn I think that's it's quite easy to find

**Chris Gammell:** great yeah we'll definitely

**Chris Gammell:** link that in Katarina thank you so much for being here and explaining this stuff I'd love to love to chat again with you in the future thank

**Katerina Galitskaya:** you very much for having me bye bye x
