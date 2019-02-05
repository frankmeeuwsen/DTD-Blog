---
layout: post
title: A cabinet of bookmarks
date: 2018-10-26 19:35:00 +2h
excerpt: The blogpost where I talk about Kendrick Lamar and CSS grids.
published: true
header: 
category: webtech
tags: indieweb bookmarks pinboard rss
---
Sometimes all these things come together so why not chime in with my own thoughts and progress. The last couple of days you might have seen some more bookmarks on this blog insted of fully fleshed out blogposts.

It is my way of public experimenting. I just try stuff on this blog and see where it goes, both in terms of my own satisfaction and reactions of my readers. Since my wife is a bit behind on my blog and I haven't heard from my mum yet, I'm glad the other readers responded. Ton started his day with [some musings](https://www.zylstra.org/blog/2018/10/on-collecting-bookmarks/) on his bookmark-strategy (yes, that _is_ a thing for people like us) that resonated some of the talks we had last week. Peter responded with [his strategy](https://ruk.ca/content/how-i-save-bookmarks) on how to save bookmarks. 

BTW, if you're wondering why I am writing in English, it's my service to Peter to save him another trip to the machine-translator and get an idea what I am talking about ;-)

Let me share my thoughts, in no particular order.

My blog has always been [this _wunderkammer_](http://barnhard.nl/2005/07/27/weblog_als_de_moderne_wunderkammer/), a cabinet of curiosities where the categorical boundaries are yet to be defined. Ofcourse you can see some of the topics that are of interest, but I feel my blog should be some short of Frankopedia, where you get to know more about me, not just as a professional but also as a person. So I love to share links and pointers to all sorts of places on the web. Sometimes with some context, sometimes just a link. 

With my setup pre-[Indiewebcamp](https://diggingthedigital.com/tag/indiewebcamp/) it was quite a hassle to post a bookmark, so I refrained myself from doing so. But since I have my Micropub endpoint up and running, posting a bookmark has become much easier. Although not every app that supports Micropub bookmarking, does it in a very good way. The app [Indigenous](https://indieweb.org/Indigenous_for_iOS) (iOS) is one example. When I bookmark something with it, it just posts [the URL and a sort-of-summary](https://raw.githubusercontent.com/frankmeeuwsen/DTD-Blog/master/_posts/2018-10-25-50179.md) in a Markdown file and it's up to me to do something with it. 

This has led me down [another rabbithole](/webmentions-aan-jezelf/) for the past three evenings to try and come up with solutions on how to fix this. I would love my site to pick up the title and some basic information from this URL I bookmarked. This led me to [the Metainspector gem](https://github.com/jaimeiniesta/metainspector/), which led me to learning Ruby to write a Jekyll plugin I could use for myself...

You see where I was going with this? I just wanted to save some bookmarks and now I'm learning Ruby to write my own plugins. 

This blog is a hobby, I don't have to make money from it. So I don't mind spending some time and energy into it. I don't mind learning some basics of a program language. But today I asked myself why I would go this route? Why wouldn't I take the route I started a while ago and go back to Pinboard as my central place for bookmarks I'd like to share here? I like the service, even though it is not owned-and-operated as Peter suggested. 

But there's more then just Pinboard where I bookmark stuff. Here's a quick rundown on how I bookmark and why. 

### Why bookmark?

There are a few reasons for me to bookmark stuff from the web.

* Things that interest me to read later. One of the biggest categories and one that I'll never see the bottom of. This pile is huge since there is _always_ something interesting to read.
* Things for professional development. This can be more long-term or current stuff I'm working on and need quick access to. 
* Things for personal use. Interesting stuff for our house. Ideas for our holidays. 
* Things I'd like to share with others on my blog and/or social channels.
* Things I visit on a daily basis or I need available as part of a workflow .
* Random fun stuff I might do something with.

### Where bookmark?

I store my bookmarks on a few places, depending on the function of the bookmark. Remember it is not very binary. Sometimes a bookmark has multiple functions

* **Bookmark bar**. Very vintage, very low-tech. I have a lot of sites available from my fingertips ni the bookmarkbar in my browser. I don't bother syncing it with my mobile, since most of it is work- and desktopbased. 
* **Pinboard**. This is my current place to go and I am very happy with it. I use it to store all sorts of links for what I am working on. You'll find all sorts of links, ranging from the differences between [CSS frameworks](https://pinboard.in/u:frankmeeuwsen/b:8ab7b8e36855) to a brilliant mashup between [A-HA and Kendrick Lamar](https://pinboard.in/u:frankmeeuwsen/b:b2b6183e8d75). Some of these links are for current projects, some are to share later. Some are just there because I liked them. 
* **Evernote**. My Evernote notebooks are filled with local copies of articles, PDF's and ideas for projects and archived pages of things I worked on. This is also the place to store bookmarks and thoughts for our family. Like holiday ideas, inspiration for our interior, garden or other rooms and a lót of recipes I know will do well with our kids. 
* **Inoreader Stars**. Since RSS is back as part of my information-intake (I wouldn't call it a diet) I use [Inoreader](https://www.inoreader.com/) as my go-to reader. Every now and again I star individual messages, like Peter does as well. This are most of the time articles I need to get back to or might be of interest for this blog or social channels. 

### Where to go next?

I would love to have a better connection between my Inoreader Stars and Pinboard. Besides that, I'd love to work some more on an automation like [Brett Terpstra's Web Excursions](http://brettterpstra.com/2018/10/15/web-excursions-for-october-15-2018/) including the [amazing archive](http://brettterpstra.com/topic/bookmarks/). I think my first steps with Pinboard and NodeJS will help me with this, since I now know better how to post articles through automation and the Micropub services. I will stop my foray into Jekyll plugins and Ruby development, for now, and will work on a better service to post bookmarks from Pinboard to this blog on a regular basis. 

This was also posted to <a href="https://indieweb.xyz/en/indieweb" class="u-syndication">/en/indieweb</a> on [Indieweb.xyz](https://indieweb.xyz)