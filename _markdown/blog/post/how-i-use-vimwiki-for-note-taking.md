---
title: How I use VimWiki for note taking
tags: post
date: 2025-08-10
---
_August 10, 2025_

I made an earlier post where I tried my best to inspire folks to use simple tech solutions in strategically useful ways in order to get large gains out of the tech they already have. Among one of the things I discussed was the power of using simple text files to keep track of things. I'd like to expand on that point here and give some of my own technical details of what I use. Of course, any old text editor will work for the job. I'm going above and beyond so I can have extra features and efficiency.
<br>
<br>
&emsp;&emsp;<https://rseeber.github.io/blog/post/use-technology-creatively/>
<br>
<br>

# VimWiki

So we're going to be using VimWiki. It's an extension for the terminal-based text editor vim. First, install vim. After that, the README for the VimWiki project tells you to simply git clone the project into a plugins folder, and run a special command to generate the help pages. It's all just copy paste into the terminal, super easy stuff.
<br>
<br>
&emsp;&emsp;<https://github.com/vimwiki/vimwiki?tab=readme-ov-file#installation>
<br>
<br>

Veronica Explains did a pretty good blog post and video tutorial about using VimWiki, which you can take a look at if the official documentation isn't enough for you. My post is mostly going to be about what you can _do with it_, not necessarily a tutorial on the details.
<br>
<br>
&emsp;&emsp;<https://vkc.sh/vimwiki-101/>
<br>
<br>
&emsp;&emsp;<https://www.youtube.com/watch?v=RmEtH5FQs28>
<br>
<br>

# Using it

Okay, so now you've got it installed. Open vim, and type "`\ww`" to enter VimWiki. It will create a folder in your home directory called `~/vimwiki/` where all files will go by default. VimWiki is basically just vim with internal hyperlinks to other text files on your computer. When you create a link to a file and open it, it will automatically _create_ the file, if it doesn't already exist. You never need to leave the editor in order to add new files.

You can of course use nested directories for different types of notes. For instance, you might use `~/vimwiki/blog/` for writing up your blog posts, and `~/vimwiki/daily/` for all the notes you need at the beginning of your day. That kind of thing. All links are relative, so if you add an index page to `~/vimwiki/blog/`, you can refer to all posts as simply their filename without the full path.

# How I use it

A natural hierarchical order comes out of this system. You can begin at the top level index page, which lists sub-pages of different categories. Each sub-page lists either actual pages, or even more detailed categories, until finally you dig all the way down to a file where you're actually writing in, not just listing links. The hierarchy is saved entirely in your `~/vimwiki/` folder. It's all just files and folders. So if you ever want to switch to a different management system and ditch vimwiki, there's no conversion tool needed, everything is already is an easily readable format. There's no special vimwiki-specific metadata or databases or anything.

I have a few big category pages, including "Journals", "Writing", "Blog", and some for different projects I'm working on, like school clubs or things.

I use the journals folder to keep all my generic notes. There's your typical examples of just brief ideas or little details I need to record for later, but I also like to keep links to or names of media I've enjoyed, or that I plan to take a look at later when I have time. I also keep a todo list and a suspense file.
<br>
<br>
&emsp;&emsp;<https://pluralistic.net/2024/10/26/one-weird-trick/>
<br>
<br>


## Blog posts + static site generator

Next, I also have the blog folder. This site is self-run using a static site hosting service (GitHub pages currently), and I use the static site generator eleventy to turn my markdown files into html pages based on the template for the site. All I do is install the node package into `~/vimwiki/blog/` and have it generate my site whenever I finish a new post. I've got it configured to output files to a custom directory where I keep the git repo for the website. So when I run the command, it updates my website repo. When I like how it looks, I commit and push the changes, and they become public within a few moments.

Just for convenience sake, I also keep a `~/vimwiki/blog/drafts/` folder which I've instructed eleventy to ignore. Once I finish writing a draft, I move it into the parent folder where it can be seen by eleventy.

Of course, you'll probably want to configure your VimWiki to use markdown files if you're doing this, rather than it's default `.wiki` files, which I'm unaware as to whether eleventy can support, but I would assume markdown has better support in any case. You also don't necessarily need to use eleventy -- any static site generator that is comfortable for you will do.
<br>
<br>
&emsp;&emsp;<https://www.11ty.dev/>
<br>

The idea to this whole system is that all your external tools for memory are stored into a singular place. Rather than having to think about where you keep movie suggestions, read later list, todo lists, favorite quotes, and notes on different projects, you can just know that everything is in your VimWiki folder. Just start following links down your category until you land on what you're looking for. It eases the friction for getting started on a task, and it also makes it easier to transition from one task to another, since your notes are going to be all stored in the same place.

# Cloud sync + mobile access

Okay, this is getting into perhaps the more technical, but still doable. You can actually sync your entire `~/vimwiki/` folder to the so-called _""cloud""_ using git. Initialize the repo, and commit all changes. Pick a server you want to use for syncing. I use GitHub because it's what I know, but some may prefer to use GitLab, or even a VPS or something like that if you're hoping for some privacy from Big Tech services.

Anyhow, simply set up a _private_ git repo and push your changes. You'll need to of course authenticate first to prove you're allowed access, but after that it should all work. You want it to be this way so that nobody can read your notes or drafts unless they have access.

If you want to access it from somewhere else, simply git clone the folder to a separate device, edit the files, then commit and push. The benefit of using simple text files instead of more advanced files like Word Documents is that you can edit them from basically any device, even a phone. A lot of file managers for your phone will come with a text editor pre-installed.

You can get even fancier than that though. If you have an Android, you can install a terminal emulator like Termux, which enables you to install packages such as git and vim on your phone. That's what I do, I git pull my vimwiki folder to get the latest version, and then I open it with vim. I even have the VimWiki plugin installed on it too. I make my edits, then commit and push back up. Of course, that's not your only option. All you need is a way to push and pull a git repo to your phone, and some kind of generic text editor. 

# Closing

I really enjoy my experience with VimWiki, creating a hierarchical note system. I try not to get carried away with the data structure of it all, instead focusing on just keeping notes on important stuff. If you have any other tricks how to make the most out of this tool, feel free to let me know about it! I love endlessly tweaking with my workflow on my laptop to optimize efficiency (or often just coolness factor).
