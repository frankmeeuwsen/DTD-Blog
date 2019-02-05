---
layout: post
title: Public Folder, host je website lokaal en bij Amazon.
date: 2018-06-05 08:39:33 +2h
excerpt: Hoe je makkelijk je statische site van Github Pages kunt verplaatsen naar Amazon S3.
published: true
header: publicfolder.png
syndication: indienews
category: webtech
tags: nodejs cheatsheet code bloggen
---
Ik was vanochtend eigenlijk op zoek in mijn Programma's map of ik nog een offline RSS-lezer had. Zover kwam ik niet, want mijn oog viel op het programma [PublicFolder](http://this.how/publicFolder/). Ik wist eerst even niet wat het was maar nadat ik het opende zag ik al snel dat het een projectje van Dave Winer was. Een relatief kleine NodeJS applicatie die als losstaand programma kan fungeren. Wat doet het? Het fungeert als een soort privé Dropbox. Als het programma is gestart kun je bestanden in een zelf gekozen map plaatsen. Vervolgens, na wat configuratie, gaat PublicFolder deze bestanden automatisch kopieren naar Amazon S3, een [online opslagplaats](https://www.wat-betekent.nl/wat-betekent-s3/) (**S**imple **S**torage **S**ervice)voor vanalles en nog wat.

Op Amazon S3 kun je instellen dat een specifieke map als website beschikbaar is. Zo kun je dus heel snel en eenvoudig een website hosten die je lokaal beheert. Deze website staat volledig lokaal op mijn laptop, en ik schrijf alle blogposts lokaal. Als ik tevreden ben kan ik met 1 druk nu de site via Github online zetten. Maar in de toekomst zou ik dat dus net zo makkelijk bij Amazon S3 kunnen doen. Ik betaal dan alleen voor de schijfruimte die ik daadwerkelijk gebruik en de site blijft razendsnel beschikbaar. Met de mogelijke veranderingen bij Github kan het geen kwaad om de alternatieven eens te bekijken voor de hosting van mijn site. 

De code van PublicFolder is [vrij in te zien](https://github.com/scripting/publicfolder/blob/master/publicfolder.js) op Github en Dave Winer heeft op zijn eigen traditionele manier de [how-to geschreven](http://this.how/publicFolder/) die eigenlijk net te weinig informatie geven. Je moet dus zelf wat knutselen. Mijn belangrijkste tip: Zet in het config-bestand je S3Folder tussen slashes. Dus niet 

    "s3Folder": "publicfolderfm"

maar

    "s3Folder": "/publicfolderfm/",

Oh en je kunt deze site als (voorlopige) mirror eveneens op [deze prachtige URL](http://publicfolderfm.s3-website-us-east-1.amazonaws.com/) vinden. Extern geladen afbeeldingen doen het niet, maar verder werkt alles prima! Ik moet [deze stappen nog doorlopen](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html) om er een domein aan te plakken, dat volgt later wel. Als een snelle test in plusminus 10 minuten vind ik dit best geslaagd...