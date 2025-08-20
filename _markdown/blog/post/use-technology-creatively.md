---
tags: post
title: "Use Technology Creatively"
---
_July 16, 2025_

# Email is magic

A good email client is like magic. As technologists, it's easy to lean into the world of the terminal and operating system, messing around with our Linux installations, Desktop Environments, or other things. It's easy to lean into this world and see this part as the "real world of computing", and then look at many of the more business and corporate tools such as email and Office Suites (like Microsoft Office or LibreOffice) as the boring technology, stripped of life. 

After all, look at your email inbox that you're forced to use for every service you sign up for. It's littered with corporate newsletters you didn't sign up for, advertisements from companies you don't even have an account with, and political updates from politicians who you thoughts you would care about when you signed up, but you've received over 25 messages in a row so far that have remained unread. (Well, that's my experience anyways).

It's easy to look at this and simply blame the corporate style of technology. But email isn't actually a bad technology, it's just that most people don't realize how good it can be if you simply take a few small proactive steps to improve your experience.

## Manage Your Subscriptions

Step number one to gain control is to manage how many new messages are coming in to your inbox. My preferred method for this is to maintain two email accounts. The first account you identify as _your email account_. It's the email you list on your website, and it's the one you give to contacts. You also will give it to any services for which you _actively want to recieve updates from_. Not weird marketing emails from a service you don't care to use for more than a week after signing up. Not sales ads from an online store you bought one thing from 2 months ago. Updates that you specifically, intentionally thought to yourself, "yeah, I think I want to get emails from these people, that would enrich my life or help me out in some way." For the other services, the ones that send you junk mail you don't care for, but which you still need an email to sign up with, you sign up through your second email. This inbox does not get checked unless they tell you to check it for something like a 2FA code or a password reset or something like that. 

The majority of services you use shouldn't get access to your "real" inbox, they get access to the secondary one. The one you don't check. This reduces the amount of messages you get in your first inbox, allowing you to actually read those few numbers of emails that actually _do matter_. It also means you can confidently hand your email out to contacts and not get stressed out to the prospect of having to check it once in a while so that you don't miss their message. Herman from Bearblogs mentions something along the lines of this strategy in his post about digital hygiene.
<br>
<br>
&emsp;&emsp;<https://herman.bearblog.dev/digital-hygiene-emails/>
<br>

This method can be further enhanced by using email filters to automatically sort emails into different folders of your inbox, though I personally don't receive enough emails in my "real" inbox to warrant that level of organization. The 4 emails a week I get are easy enough to handle without the extra tooling. That may change if I begin receiving more emails from contacts and real humans.

# It's Not Just Email

Fixing your email is a great move, it means you don't miss things. You come off to others as a more put together person. It reduces stress personally from your life. And the fact that it's such a simple move really is a major selling point on this idea. You don't need to do anything drastic, just make a new email (or clean up an existing one, unsubscribing from a few emails you're currently getting on it), and maybe apply some inbox filters if you plan on getting a lot of important messages. This idea is great, and it has a lot of room for further application. We can use the full potential of computing to become more efficient in as many ways as we feel creative, inspired, and compelled to explore. I'd like to detail some of these other tricks you can use. All of these are going to be 1) simple and 2) offer non-negligible payouts for minimal effort.

# Text Documents

Having a folder on your computer, just for general working notes is really important to me. I think anyone who works on a computer should have such a thing. Inside of it, you can include all kinds of things. There's of course your general todo lists (I do my day-to-day lists analog, keeping only big picture stuff digital), but then there's all the notes you need for remembering small details on a project you're handling, or for creative thinking while working through a fuzzy problem, or for keeping track of changing details regarding something as time goes by.

I personally advocate for using them as simple text files, using .txt or .md extensions. You don't need to use a Word Document file to do this. Text files are easy to open -- virtually any program will accept them -- and they don't obscure anything. Their pure simplicity is a factor of freedom, not constraint. The fact that it's just text, often rendered in a monospace font, means you are given a free canvas with which to format and organize your document. The simplicity is the point.

If you don't want to use a raw text file, don't. But if you're like me, and are comfortable editing files from raw text editors like vim, or on other operating systems, Notepad, I recommend doing it this way. 

(As a side note, if you happen to be looking for a better way to keep all of your endless notes organized, I recommend giving VimWiki a look. It's an easy to install extension for Vim, the terminal-based text editor. It allows you to put hyperlinks into your text documents that point to one another. It's also got a lot of quality of life features that are great, but I don't want to derail too far by going into depth about it. I'll let you look into it yourself.)
<br>
<br>
&emsp;&emsp;<https://vkc.sh/vimwiki-101/>
<br>
<br>
&emsp;&emsp;<https://tinkerbetter.tube/w/6hrXmYYNMjBGJnSE8iJ6NM>
<br>
<br>
&emsp;&emsp;<https://vimwiki.github.io/>
<br>

The use of these files is incredible. Not just for writing simple notes, but you can generate detailed logs which will be useful to you as a reference guide. Take, for instance, the idea of a Suspense File. This list is used in order to track not your own progress, but to track things you're waiting on others to do. It's not designed to track them in some controlling, "hurry up and stop making me wait" kind of way. It's more like "oh wow, me and Rachel were talking about doing xyz, but it's been 2 weeks since any news from her. She's probably too busy to make it all work out in time. Let's take a look. If she's making progress, it would be good to know about it, and if not, I'll give her an out and let her off the hook if she needs it." The idea is that people are busy, and the natural tendencies of people working together on a stagnant project is to just let it silently fall through. The point of the suspense file is to make sure if it does fall through, it's because you identified that one of you lacked in the time or resources necessary to make it work, and explicitly communicated that you wanted to drop the project.

That tends to be the more useful aspect of using lists. Lists don't help you know what to do, they help you decide what you _aren't_ going to do. Which projects you don't have time for, and need to ditch.

The suspense file works like this. Each line is a new entry. You can organize it however you like, but this is the method I use, and it's the one Cory Doctorow describes, which is where I learned of the concept in the first place. 

Each line starts with "`WAITING`", followed the category. After that, you describe who you're waiting on, and for what specifically. Finally, add a trailing string of dates for whenever a new development is made. If you communicate back and forth with someone for 3 weeks on a project, you might see over a dozen dates appended to the end of this line. The idea is that it gives you an idea of how long you've been trying to get the ball rolling on something, and how many interactions have taken place so far.
<br>
<br>
&emsp;&emsp;<https://pluralistic.net/2024/10/26/one-weird-trick/>
<br>

An example (fake) entry might look like this:

&emsp;&emsp;`WAITING Email from Prof. J on CS Club availability for advisorship 2/12, 2/16, 2/20`

After 3 separate interactions about it, I might decide that she's too busy and start looking into other options. On the other hand, she might have just been temporarily bogged down, but will be free again starting next week, and that fact just needs to be communicated. Either way, it helps me identify the progress or stagnation of a plan, and easily track whether I need to reach out.

Again, the point isn't to control anyone, or be an incessant nag (that would be weird). The point is to identify which projects are lagging behind secretly without being noticed, so I can communicate with others involved, and see if this is something that can be remedied somehow, or if we need to drop the project in pursuit of other aims that are demanding more of our time.

# Keeping Up With Updates

In our age of information overload, where we are often expected to stay up to date with a number of ever changing events at 400 words a second, it can be helpful to institute some simple practices that greatly help us to manage all that information we're expected to take in regularly. We want both to be able to quickly have access to that information without too much mental strain on actually _trying to find it_, as well as wanting a system in place that allows us to know which information sources we _still haven't looked at yet_.

The first is simple, we want some database of all our sources like blogs, news sites, product updates, etc in a singular place where we can quickly check all of them. The second goal is a little more nuanced. Perhaps we spent the first 15 minutes of the day checking through our updates, but get cut off before checking the last one. Or, for instance, perhaps we're following a large number of publication sources, but each source only puts out a small number of articles per month. Many times we check, there will be nothing new. It would be worth having a kind of system that keeps track of which source has received updates lately, and which ones we don't need to bother checking in on yet.

Lucky for us, a tool for this already exists that covers both of our needs at once. It's called RSS feeds (or sometimes "Atom feeds". I think there's a nuanced difference between them, but from the perspective of a user, they function exactly the same). You can follow the RSS feed of a publication source online, such as a blog or many news sites. You will store these feed links into an application called an RSS Reader. There's a lot of apps to choose from, but I personally like to use Mozilla Thunderbird for it. That way, it's stored in a folder right next to my emails inside of the same program. You can use something else if you like, there's plenty of options to choose from if you just care to do a quick search online.

When you subscribe to a particular feed through your app, it shows up as a little folder of updates. When you click on the folder, it shows you any recent posts from that source. Unread posts are highlighted a different color so you know you haven't seen them yet. You can read the title of each post and decide if it's worth your time or not. I'm currently following over a dozen feeds, though checking through them often only takes a little bit of time each day. Some days, I use it to keep up with light, enjoyable reading from popular posts on the Bearblogs blogging platform.
<br>
<br>
&emsp;&emsp;<https://bearblog.dev/discover/>
<br>

I also use it to keep up with the news, dev updates relating to Arch Linux, or other projects I'm following, podcasts I listen to, and noteworthy blogs I follow outside of the Bearblogs trending page.

Most sites that post regular articles will have an RSS feed you can follow somewhere. Heck, even YouTube provides one for each channel, even if they don't necessarily advertise about it, or make it easy to find. I use an online tool to convert channel links into RSS feeds.
<br>
<br>
&emsp;&emsp;<https://ytrss.pesky.moe/>
<br>

## Without RSS

If you don't have an RSS feed for a site, you get two options. Either don't follow their updates, or find a way to follow it anyways. An easy way to do the second option is to create a basic "startup" bookmarks folder in your web browser. Every time you check your RSS feeds, you'll also open that startup folder, comb through if anything demands your attention, closing each tab once you're finished. This should take usually take a few minutes each day, unless you're putting a bunch of news sources into this folder, which I would not recommend.

You can also use these folders to check up on special pages that require you to log in to your account to view. If you're trying to follow the shipping on a particular product you've purchased, or check if some important lab result from your hospital has been posted to your account yet, rather than stressing about it, you can just right click your folder and "Open All Bookmarks". Comb through if an update has been posted, and be done in less than 5 minutes. Once you've received the update you were waiting on, you can delete the bookmark if you no longer need to check it regularly. You can always add it back again later if you get more labs done, or buy another product.

# Conclusion

The point is that each of these tricks are _dead simple_. They each provide moderate to high payouts for realistically small effort required to institute them. They utilize the power of computing to solve problems that computers are uniquely capable of solving efficiently.

This article has largely been inspired by the general principles laid out in Cory Doctorow's post on Suspense Files (linked above), as well as his Lifehacking liveblog he links to at the beginning of that post. The idea that people who are keen with technology can use that technology in ways beyond just what everyone else is already doing (often without much thinking on the matter). To actually think critically about the tools at your disposal and find clever ways to use them that makes you accomplish more, it's a simple idea but it's also incredibly powerful.
<br>
<br>
&emsp;&emsp;<https://craphound.com/lifehacksetcon04.txt>
<br>

I'm only really just starting down the path of experimenting with and discovering creative ideas like the ones I've laid out in this post. If you've got any of your own that I didn't mention and you think I'd like it, I'd be happy to hear from you. You can feel free to shoot me an [email](https://rseeber.github.io/about.html) telling me all about it. I love getting emails from real people -- it's the explicit reason that I ever went about cleaning my inbox in the first place.
