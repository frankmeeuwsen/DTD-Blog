---
layout: post
title: Het plan voor de IndieWebCamp hack-sessies
date: 2018-10-21 7:22:41 +2h
excerpt:
published: true
header:
category: indieweb
tags: indiewebcamp indieweb webtech
---

De tweede dag van het [IndieWebCamp Nurnberg](https://indieweb.org/2018/Nuremberg) staat in het teken van je eigen web-problemen oplossen. Elke aanwezige heeft een eigen site of is bezig met een specifiek project waar altijd wel iets aan te doen is. De dag begint met een korte presentatie van iedereen wat hij of zij wil aanpakken. Daar worden groepen uit gevormd en gaan we aan de slag tot het einde van de dag, alleen onderbroken door de lunch.

Het is lang geleden dat ik bijna een hele dag ongestoord kan werken aan eigen projecten, veelal is het een verloren uurtje in een weekend of in de avond. Dat heeft het gevolg dat ik vaak opnieuw begin, weer de documentatie van iets lees, weer dezelfde scripts probeer en weer dezelfde fouten maakt. Dus ik zie wel uit naar deze dag. Ik heb voor mezelf al een plannetje gemaakt wat ik vandaag wil oppakken.

## Webmentions

Gedurende de sessies op zaterdag werd me duidelijk dat ik me voorlopig op drie onderwerpen moet concentreren: Microformats, Webmentions en Micropub. Dit zijn achtereenvolgens nieuwe protocollen en afspraken rondom de weergave van data voor machines, een nieuwe wijze van reageren en communiceren via blogs en sociale netwerken en Micropub brengt het publiceren op je eigen blog naar een open protocol, waarbij je niet afhankelijk bent van de instrumenten die je blogsoftware of sociaal netwerk je aanreikt. 

Mijn plan is om vandaag in elk geval het volgende voor elkaar te krijgen

1. [Microformats](https://diggingthedigital.com/indiewebcamp-microformats/) helemaal goed werkend op mijn site, zowel voor mijn _h-card_ als de _h-entry_ optie
2. Vervolgens wil ik een opzet maken om webmentions lokaal en online goed te kunnen testen. Ik vind het niet fijn om steeds op liveblogs allerlei tests te moeten doen. 
3. Het [versturen](https://diggingthedigital.com/indieweb-webmention-client-ruby-a-ruby-gem-for/) van webmentions. Ik heb dit nu in een ruwe versie voor elkaar, maar ik wil dit nog uitwerken naar een degelijke oplossing. Dit betekent dat ik het webmention script goed moet configureren, de server in orde maken, de trigger voor het versturen van de webmention testen en configureren en tenslotte een feedback-loop of het versturen goed is gegaan.

Als ik dit vandaag voor elkaar krijg zou dat al mooi zijn. Op de wat langere termijn wil ik de volgende onderdelen op mijn blog verbeteren

1. Ontvangen [webmentions](https://diggingthedigital.com/tag/webmentions/) en notificaties. Ik ontvang nu wel webmentions, maar dat is alleen op individuele blogposts. Ik weet dat er ook wordt gelinkt naar mijn homepage. Die moet dus eveneens webmentions krijgen. Daarnaast wil ik notificaties krijgen (mail, telefoon) als er een webmention binnenkomt.
2. Weergave en beheer webmentions. De weergave van de webmentions mag nog beter, evenals het eigen beheer, zoals het verwijderen van test-webmentions.
3. Syndicatie naar Twitter verbeteren. Middels een Zapier-script heb ik het inmiddels voor elkaar dat elke blogpost automagisch op Twitter verschijnt. Dat is meer een lapmiddel dan een duurzame oplossing. Daar moet ik dus nog aan werken, evenals de presentatie van de tweet. Nu pakt de webmention de eerste 280 karakters en een permalink. Dat wil ik anders. Hoe exact weet ik nog niet, dat zien we gaandeweg wel.
4. Micropub. Ik kan inmiddels met [Omnibear](https://omnibear.com/) goed posten vanaf elke pagina naar mijn site. Maar in de weergave op mijn site zitten nog wat onhebbelijkheden en ik wil de mogelijkheden van dergelijke tools verder uitdiepen en mogelijk verbeteren.

Kortom, genoeg te doen. Maar nu eerst ontbijt!

