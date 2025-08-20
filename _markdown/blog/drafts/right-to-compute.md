# Take back the right to compute

## Outline

- Computers are universal
	+ Data streams
	+ You can tell one PC to talk in the language of another PC
	+ You can run __any__ valid program on a computer.
		- For every 10ft digital wall, you can install a 12ft digital ladder
- What is DRM?
	+ A reaction to the Universality of Computers, attempting to remove this property
		- DRM attempts to stop evil software from building 12ft ladders. Subsequently, it also stops good software from doing just the same
		- List some examples --> Accessibility software that the original developers refuse to develop properly
		- A range of other legitimate uses of extending the functionality of a program, or reverse-engineering and re-building a program from scratch, but with a better experience --> more features, better interface, removing anti-features
	+ This is considered to be illegal --> "criminal contempt of business model" --> an individual might be able to get away with it, but a legitimate corporation can never be allowed to exist to provide services like this unless DMCA 1201 is repealed or otherwise updated.
	+ Not only this, it is also illegal to study the function of DRM modules for security flaws. The publishing of true facts about defects in digital products used by millions of Americans every single day in high-security environments is incredibly illegal --> freedom of speech concerns
- DRM isn't the problem, DMCA 1201 is the problem
	+ DRM is easy to break, and we shouldn't create laws to ban it. Companies should be free to do as they wish.
	+ But companies should not be able to use the apparatus of the state to punish its competitors, or to punish computer programmers who find a way to improve their products against the will of the company.

## Universality of Computing
The promise of computing is genuinely spectacular. Computers are general purpose computation device capable of performing any computation imaginable. Anybody who owns a computer can write themselves a program, and that program can do absolutely anything that the user wants it to do, provided they have enough technical know-how on how to create it. What if they aren't a technical user? Well, that's where the universality of computers comes in. A technical user who  _does_ know how to make the program can make it for their own computer, then share it across the internet, and all the non-technical users can run the SAME EXACT PROGRAM on their own computers.

Computers have a kind of unique ability to be work together with very little effort on the part of the developers. Computers only know the language of data. Data that is sent across the air using radio waves, or data sent from the RAM Stick to the CPU using electrical pulses, or data stored on a removable drive like a USB Stick. All computers know how to read data streams. Different computers might tend to write those data streams with different structures. For instance, Windows likes to read from the hard drive or from USB sticks in a format called FAT32. On the other hand, Linux uses the more updated EXT4 file system format.

Does that mean that Linux can't read data streams (in this case, file systems) that come from a Windows machine? Of course not! All it takes is for a clever programmer to create a program that allows a Linux machine to understand the FAT32 file system. Or the other way around, make a program that lets a Windows machine understand the EXT4 file system. There is no intrinsic difference between the computers that run the Windows operating system and the machines that run the Linux operating system. In fact, I personally run both Linux AND Windows on the same PC I have in my room. When I turn it on, I'm presented with a screen that allows me to choose which operating system I'd like to boot up.

The big picture I'm trying to share is this. Different machines might *by default* read and write data in different ways, to the point where they cannot understand one another, BUT! That does not mean that the computers cannot have additional software applied to them that allows them to communicate using the method of another machine, in order to allow these machines to work together. In fact, it goes even further than that, where the machines you're trying to communicate with won't even be able to know that you're of a different type than them, since the data you send to them is exactly identical to the data they would expect to receive from a machine that is the same kind as them.


## What is DRM?
As it turns out, a number of tech companies find the fact that computers are universal machines quite terrifying. In their view, computers would be improved if there were a way to prevent users from messing around inside their own device. They find it unsettling that you might be able to extend a mail program to also show you RSS feeds, or to enable you to create events that sync with your online calendars. They fear this largely because their profit model is based on you having a lack of choices.

Nearly every tech company that is dominating the market right now is doing so by trapping their users -- making it as difficult as possible to leave them for some other competitor. They are not keeping you by providing a good product, they're keeping you by making it hurt so much to leave that you just put up with the fact that their product is worse. [this claim needs evidence, but I fear it's going to derail the direction I'm trying to go with this, so idk]

[explain the process of enshittification, maybe don't name it specifically, maybe call it Platform Decay. Give specific examples, but don't make it too much of a strong thesis on the article. We're talking about DRM primarily, but DRM does relate to enshittification.]
--> * <--

[talk through the pretext of DRM, and then the truth. Give proof through the W3C commission to standardize DRM, and the admissions made therein. Link to the EFF article.]
---> * <---

[this bit needs to be re-written or removed]
--->
Now, the supposed pretext for which companies lie and pretend they use DRM is that they're trying to "prevent copyright infringement" or piracy. They want to use DRM to impose restrictions on media players that make it impossible for you to clone that media and share it with your friends who didn't pay for it. This is not why DRM is __actually__ used. The W3C commission to standardize DRM and the behavior of the pro-DRM caucus demonstrates that quite clearly.
<---

They fear this because they're worried that if you can create a program that can extend an email client, then you will realize you can also create a program that modifies Netflix or Hulu in some way that allows you to commit piracy by sharing copyrighted materials. It's just an extension of the Napster wars. So to ease these fears, they've invented a special kind of technological measure called "Digital Rights Management", or just DRM. DRM is basically any module of a program that uses so-called "technological measure" to "effectively control access" to a copyrighted work. In the USA, and in most countries around the world, we've made it a crime to bypass DRM. So problem solved, right? It's illegal to create or use software that bypasses a technological measure that's used to control access to copyrighted work. So now, it's a crime to download and share those movies without permission.

Except that it was already illegal to share pirated movies. We've just decided to criminalize it again, while also scooping up a bunch of legitimate use cases in there and outlaw those as well. You see, "copyrighted work" doesn't just apply to the usual candidates -- music, movies, TV shows, video games, etc. -- it also includes the code for a program, or encryption keys used to prevent a user from accessing their own digital media.

Corporations have used this loophole to make it a crime to modify programs like Instagram to remove annoying features. For instance, suppose I'm a developer who wants to make an alternative app to connect to Instagram. I just want to make the app show me only the people I follow's content, not all this endless junk from random accounts that it thinks I want to see posts from. In order to build this, I need to know how Instagram communicates with the server. Well, lucky for me, I've got the Instagram app. I download the program, and begin work reverse engineering what it does. I'm allowed to do this for a while, until I hit the DRM module on it. If I begin investigating the inner workings of this portion of the Instagram app, I am committing a federal crime. If I publish an app that plugs into the Instagram ecosystem, ostensibly improving the Instagram experience for users of my app, Instagram will notice me and very quickly slap a lawsuit on me, forcing me to pull my app off of the app store, and disappear forever. The crime I would be committing in this theoretical situation has been referred to by [who?] as "Criminal Contempt of Business Model". The law I would be punished under would be the anti-DRM law. But somehow, I've committed absolutely zero acts of any real copyright infringement. I'm not enabling anyone else to commit copyright infringement. I'm giving the users a Right to Computation. I've communicated a bit of math to them, and some numbers. I've wrapped that information up in a program nearly identical to the one that Instagram provided them with, but not officially sanctioned by Instagram, and that is what makes it a crime.

Companies believe that it is in their right to sue you for creating and running certain programs on your device, or to sue competing companies that allow you to run certain programs on your computer.




They're right, you __can__ do that. You totally __could__ make a program that commits piracy.

[this paragraph needs to be re-written] 
--->
So what we've covered is that computers can be made to talk to one another. And it only really requires *one* of those computers to be in on it. The other computer can be blissfully unaware of the interoperability between them. The other computer is simply responding according to its programming, reading and writing in a format that it knows. But beyond just that, you can take advantage of this property of computers when trying to make programs behave a certain way together ON THE SAME PC. So I can be running an email program that came with my Operating System, and on top of that, I've got a program that talks to the mail program in some way, or perhaps modifies it while it's running, extending its functionality in some way. Depending on what that extended functionality is, you would call this program either an extension, or, if it was installed with ill-intents behind the back of the PC owner, you would call it malware.
<---

[go talk abt DMCA 1201, legal saran wrap, etc]

## Freedom of Speech, Ownership

