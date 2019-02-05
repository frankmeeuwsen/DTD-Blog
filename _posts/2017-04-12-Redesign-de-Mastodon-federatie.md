---
layout: post
title: Redesign de Mastodon federatie!
excerpt: Het zoeken van de juiste instantie is niet heel makkelijk. En de software maakt het nog ingewikkelder...
published: true
header: header-federation.jpg
tags: mastodon
category: 
    - indieweb
---
Yep. Deel 3 in mijn Mastodon avonturen. Zoals ik in [deel 1](/Mastodon) al schreef, ik heb meerdere invalshoeken en ideetjes waar ik het hier over wil hebben. Vandaag wat gedachtenkronkels over het design van Mastodon. Niet over de al veelbesproken driekolom structuur die van Tweetdeck is geleend. Maar juist wat je ziet als je nog *niet* bent ingelogd in Mastodon. 

## It's all in the brand...

Mastodon kun je op je eigen server installeren. Mastodon is niet een centraal geleid netwerk zoals Facebook en Twitter waar je op één plaats je inschrijft en inlogt. Iedereen die er wat tijd en *elbow grease* in steekt kan een eigen Mastodon server opzetten. Er is inmiddels al een aardig stappenplan hoe je dat kunt doen.

Echter, na die installatie zit je met een standaard vormgeving van Mastodon. Niet alleen in de drie kolommen voor je posts, maar eveneens bij het eerste contact wat je bezoekers hebben met de site. Een voorbeeld?

Zie hier de startpagina van het vlaggeschip [Mastodon.social](http://mastodon.social/)

![<>](/images/groningen.png "Groningen")

Hier de startpagina van een instantie die [Groningen](https://mastodon.groningendigitalcity.com/) heeft geinstalleerd.

![<>](/images/mssocial.png "MS Social")

En hier de startpagina van de instantie van podcast [No Agenda](https://noagendasocial.com/). 

![<>](/images/nosocial.png "MS Social")


Zie je de verschillen? Die zijn er inderdaad niet. Waar het grootste verschil zit is achter deze link.

![<>](/images/about.png "about link")

Op de vervolgpagina kun je als beheerder van de instantie meer vertellen over het hoe en waarom en wat de richtlijnen zijn van de instantie. Wederom even de screenshots

Mastodon.social

![<>](/images/over-mss.png "about link")

Groningen

![<>](/images/over-groningen.png "about link")

No Agenda

![<>](/images/over-noagenda.png "about link")

Je snapt al waar ik heen wil denk ik. Als een argeloze bezoeker heb ik geen idee wáarom ik voor welke instantie zou moeten kiezen. Wat is het voordeel van bv Groningen ten opzichte van een andere instantie? Is MS.social sneller dan No Agenda? Welke onderwerpen worden er besproken? 

Kortom, het merkdenken is (begrijpelijk) nog niet echt doorgedrongen bij de software ontwikkelaars. Ik vind dat geen ramp, laat alles zijn eigen tijd krijgen. Maar ik zou het wel interessant vinden in dit open source project ([Github broncode](https://github.com/tootsuite/mastodon)) als er een *fork* komt waarin je je eigen startpagina kunt maken. Een betere *onboarding* om nieuwe gebruikers te begeleiden in deze federatie van instanties. 

## Publieke tijdlijn

Wat hier goed kan helpen is een publieke tijdlijn per instantie. Ik heb een schreeuwende onwetendheid wat betreft de installatie van Mastodon maar het zou interessant zijn om de lokale tijdlijn publiek te zetten voor niet-ingelogde gebruikers. Zo kunnen ze een idee krijgen wat er op de instantie gebeurt en of het de moeite waard is om je bij aan te sluiten. Twitter had in de begindagen een publieke tijdlijn en dat werkte wel om duidelijk te maken wat de waarde van Twitter kan zijn voor je. 


## Open source

Het mooie is dat Mastodon open source is. Elke team van design en tech kan de broncode pakken en bovenstaande mogelijk maken. Ik ben geen designer noch een begenadigd programmeur. Ik heb wel ideeën hoe zo'n volgende stap zou kunnen zijn voor de software. Of in elk geval een *fork* er van. Wil je hierover meedenken en kijken wat mogelijk is? Laat het me weten op [Mastodon](https://mastodon.social/@frankmeeuwsen/) of [Twitter](https://twitter.com/frankmeeuwsen/). Whatever your flavor is...