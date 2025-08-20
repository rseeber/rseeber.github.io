---
tags: post
title: "How I use VimWiki for note taking"
---

I made an earlier post where I tried my best to inspire folks to use simple tech solutions in strategically useful ways in order to get large gains out of the tech they already have. Among one of the things I discussed was the power of using simple text files to keep track of things. I'd like to expand on that point here and give some of my own technical details of what I use. Of course, any old text editor will work for the job. I'm going above and beyond so I can have extra features and efficiency.

## VimWiki

So we're going to be using VimWiki. It's an extension for the terminal-based text editor vim. So first, install vim. After that, the README for the VimWiki project tells you to simply git clone the project into a plugins folder, and run a special command to generate the help pages. It's all just copy paste into the terminal, super easy stuff. I'll link to their official website as well as a helpful blog post by Veronica Explains that tells you how to get it going in case you need extra help.

VimWiki:
&emsp;&emsp;<https://vimwiki.github.io/>
Veronica Explains:
&emsp;&emsp;<https://www.youtube.com/watch?v=RmEtH5FQs28>
&emsp;&emsp;<https://vkc.sh/vimwiki-101/>

## Using it

Okay, so now you've got it installed. Open vim, and type `\ww` to enter VimWiki. It will create a folder in your home directory called `~/vimwiki/` where all files will go by default. VimWiki is basically just vim with internal hyperlinks to other text files on your computer. When you create a link to a file, when you open it, it will automatically _create_ the file, if it doesn't already exist. You never need to leave the editor in order to add new files.

You can of course use nested directories for different types of notes. For instance, you might use `~/vimwiki/blog/` for writing up your blog posts, and `~/vimwiki/daily/` for all the notes you need at the beginning of your day. That kind of thing. All links are relative, so if you add an index page to `~/vimwiki/blog/`, you can refer to all posts as simply their filename without the full path.

## How I use it

A natural hierarchical order comes out of this system. You can begin at the top level index page, which lists sub-pages of different categories. Each sub-page lists either actual pages, or even more detailed categories, until finally you dig all the way down to a file where you're actually writing in, not just listing links. The hierarchy is saved entirely in your `~/vimwiki/` folder. It's all just files and folders. So if you ever want to switch to a different management system and ditch vimwiki, there's no conversion tool needed, everything is already is an easily readable format. There's no special vimwiki-specific metadata or databases or anything.

I have a few big categories, as well as a few that hold anything I didn't know where else to sort. I keep a 'Journals' folder all my big thinking. This can be of course actual note-taking and writing, or it could be simply collecting links of pieces of media I enjoyed or plan to enjoy in the future.

### Blog posts + static site generator

I also keep a blog folder. This site is self-hosted, and I use the static site generator eleventy to turn my markdown notes into html pages based on the template for the site. All I do is install the node package into `~/vimwiki/blog/` and have it generate my site whenever I finish a new post. I've got it configured to output files to a custom directory where I keep the git repo for the website. So when I run the command, it updates my website repo. When I like how it looks, I commit and push the changes, and they become public within a few moments.

Just for convenience sake, I also keep a `~/vimwiki/blog/drafts/` folder which I've instructed eleventy to ignore. Once I finish writing a draft, I move it into the parent folder where it can be seen by eleventy.

Of course, you'll probably want to configure your VimWiki to use `.md` files if you're doing this, rather than it's default `.wiki` files, which I'm unaware as to whether eleventy can support, but I'd guess there might be some problems.

## Cloud sync + mobile access

Okay, this is getting into perhaps the more technical, but still doable. You can actually sync your entire `~/vimwiki/` folder to _""the cloud""_ using git. Initialize the repo, and commit all changes. Pick a server you want to use for syncing. I use GitHub because it's what I know, but some may prefer to use GitLab, or even a VPS or something like that if you're hoping for some privacy from Big Tech services.

Anyhow, simply set up a _private_ git repo, set it as the remote, and git push. You'll need to of course authenticate first to prove you're allowed access, but after that it should all work. You want it to be this way, that way, nobody can read your notes or drafts unless they have access.

If you want to access it from somewhere else, simply git clone the folder to a separate device, edit the files, then commit and push. That's the benefit of simple text files instead of more advanced files like Word Documents. You can edit them from basically any device.

If you have an Android, you can install a terminal emulator like Termux, which enables you to install packages such as git and vim on your phone. That's what I do, I git pull my vimwiki folder from where I've got it cloned, and then I open it with vim. I even have the VimWiki plugin installed on it too. Of course, that's not your only option. All you need is a way push and pull a git repo to your phone, and any text editor. 

Then again, maybe you're trying to use something less technical. Either you have an iPhone and can't install UNIX tools, or you just would rather something easier. I can't vouch for any particular other method, since I haven't tried anything else, but you might find some luck in looking for other ways to sync your files online. You'll want something that automatically detects changes and uploads them, so you don't ever run into the issue where a change doesn't get uploaded and is then lost when you upload using a different device. As for text editor, this is going to be an app on literally any phone. You might need to download something, but it will definitely be available. You might not get all the fancy features of VimWiki doing this, but when you upload, the files will show up in VimWiki on your computer later for you to refine, in case you just needed to throw in a miniature little reminder for yourself next time you work on something you've got going on in your notes somewhere.
