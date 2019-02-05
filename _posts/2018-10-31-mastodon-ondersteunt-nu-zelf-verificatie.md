---
layout: post
title: Mastodon ondersteunt nu zelf-verificatie
date: 2018-10-31 23:03:59 +1h
excerpt: Gebruik je eigen domein om je online te verifieren. 
published: true
header:
category: indieweb
tags: webtech indieweb indieauth mastodon
---

OK, een korte check dan op wat er vandaag in de fediverse gebeurde. Of het open web. Het netwerk Mastodon ondersteunt met de laatste update de mogelijkheid om jezelf te verifieren. Dit hoeft niet via allerlei hoepels bij een centrale partij, zoals je gewend zou zijn bij een Twitter of Instagram. Je kunt relatief eenvoudig verifiëren dat jij bent wie je zegt dat je bent op het internet. Op je Mastodon account voeg je een link toe naar een website waar je zelf de controle over hebt. Zo heb ik op mijn Mastodon account een link naar deze site toegevoegd.

Op deze site plaats ik een link terug naar mijn Mastodon-account. Het subtiele verschil in deze links zit in de broncode. Hier staat niet alleen de link maar eveneens de toevoeging _rel=me_. Deze kleine toevoeging bewijst voor andere servers dat ik zeg wie ik ben op Mastodon. Ton legt het principe van rel=me prima uit [in deze blogpost](https://www.zylstra.org/blog/2018/10/mastodon-rel-me/).

### Wat voegt dit toe?
Met de toevoeging rel=me in de link naar een sociaal netwerk of Github, maak ik het mogelijk om mezelf te identificeren voor derde partijen. Als iemand op een andere Mastodon-server besluit zich als mij voor te doen (nee, ik zou ook niet weten waarom, maar even als voorbeeld…) dan kun je al snel zien dat ik het niet werkelijk ben, omdat de verificatie van de website mist. 

Een andere manier om dit te gebruiken is door je te identificeren bij andere services met je eigen site. We zijn gewend om in te loggen met een wachtwoord, of steeds vaker met een centrale service als je Twitter of Facebook account. Deze vorm van authenticatie (oAuth) is op zich prima, maar je bent afhankelijk van een derde partij waar je in principe minder controle over hebt. Dat heeft Facebook in het verleden wel bewezen door uitgebreide rechten te geven aan ontwikkelaars als je met je account inlogt om een kleine test te maken. 

Er is eveneens een meer onafhankelijke manier van inloggen, genaamd [indieAuth](https://indieauth.com). Hier kun je inloggen met je eigen domeinnaam. Als je dat doet, krijg je een overzicht van alle URL's die _jij_ op je site hebt gezet waar een rel=me toevoeging bij staat. Dit kan Github zijn, het was ooit Twitter, maar dat kan nu dus eveneens Mastodon zijn! Dit brengt nog meer controle in mijn eigen handen. En zoals Ton al aangeeft, verificatie van Mastodon instances kan interessant zijn om een netwerk te vinden van mogelijk interessante sites en mensen. 

![<>](https://diggingthedigital.com/images/mastorelme.jpg)

Maar helaas. Als ik bij IndieAuth mijn domein opgeef krijg ik de melding dat mijn Mastodon instance geen _supported authentication provider_ is, het wordt (nog?) niet ondersteund. Ik heb inmiddels mijn vraag weggelegd in de Indieweb chatkanalen, waar veel van de makers van deze diensten dagelijks rondhangen. Wel zo handig en het schakelt lekker snel. Dus ik hoop snel een antwoord te hebben op mijn vraag.  