---
layout: post
title: Microformats zijn mijn eerste winst op IndieWebCamp
date: 2018-10-20 11:26:19 +2h
excerpt: 
published: true
header:
categories: webtech
tags: microformats webtech internet indieweb
---
Slechts 25 minuten in de eerste sessie op het IndieWebCamp en ik heb al mijn eerste winstpunt te pakken. [Martijn van der Ven](https://vanderven.se/martijn/) geeft een sessie rondom microformats. Deze HTML markup maakt het eenvoudig voor computers en machines (en robot overlords) om data van mijn site te lezen. Hier zat een kleine fout in, de titel van mijn blogposts werden niet goed uitgelezen door de microformats. Je kunt dat zelf testen met een [online parser](https://php.microformats.io/?url=https%3A%2F%2Fdiggingthedigital.com%2Fteam-human%2F). Nadat ik de [documentatie](http://microformats.org/wiki/h-entry#Core_Properties) checkte was de code zo [aangepast](https://github.com/frankmeeuwsen/DTD-Blog/commit/91ced098fd6b2a8ccb3913c1bea2751d963b6bf0) en wordt de titel nu in elk geval netjes weergegeven. Leuk!