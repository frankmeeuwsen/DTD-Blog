---
layout: post
title: Het juiste zijpad kiezen
date: 2019-01-23 14:48:30 +1h
excerpt: Hoe zorg ik voor de beste oplossing voor mijn wensen met deze site en het beheer er van?
published: true
header:
categories: indieweb
tags: 
- indieweb
- code
- github
- statische site
---
Ken je dat gevoel? Je bent lekker op weg met een project, het gaat de goede kant op. De hobbels die je onderweg tegenkwam heb je weten te overwinnen. Sommigen heb je nog even links laten liggen tot een later moment. Je denk dat het allemaal goed gaat. 

En dan gaat het toch niet goed.

Dat overkwam mij de afgelopen dagen met de verhuizing van mijn blog. Mijn doel (lees [hier](/verhuizing-in-de-planning/) en [hier](/verhuisupdate/) meer) is om dit blog nog meer zelfvoorzienend te maken. Nog minder afhankelijkheid van derde partijen en _(wo)men in the middle_. Dat doel zou een losse server zijn, waar ik zelf de software op installeer, zelf de scripts onderhoud, zelf de boel koppel aan mijn lokale bestanden en zorg dat alles netjes draait.

Helaas mag het niet zo zijn. Op dit moment zijn er beperkingen omdat ik dit blog gratis onderbreng bij Github Pages. Een puike plek en het werkt prima met Github. Maar helaas zorgen de technologische beperkingen dat ik allerlei omwegen moet bedenken en maken om mijn groeiende archief goed te beheren. Een simpel voorbeeld zijn de tags en tagpagina's. Omdat Github Pages geen Jekyll plugins ondersteunt die dit snel en efficient kunnen realiseren, moet ik het met een omweg doen. Dat lukt wel, maar het is foutgevoelig en de opbouwtijd van de site gaat er enorm op achteruit. 

Na de verhuisupdate van eind vorige week ben ik best wat verder gekomen. Ik heb het voor elkaar om een blog op een server te draaien zoals ik wil. Zonder tussenkomst van Github, met versiebeheer op de server zelf en met een snelle bouw- en laadtijd. Hiervoor ben ik afgestapt van de kant-en-klare bouwpakketten die [Digital Ocean](https://m.do.co/c/c3654dd40a00) aanbiedt, zoals een server met Ruby en Rails al geïnstalleerd. Dat bracht weer andere beperkingen met zich mee. Ik heb uiteindelijk een losse server genomen, daar zelf Ruby en alle nodige pakketten op geïnstalleerd (wat vooral héél veel wachttijd is) en toen draaide alles als een zonnetje. Zoals ik wil.

Maar natuurlijk kwam hier weer een kink in de kabel. Ik ga proberen het niet té technisch te maken (succes Frankie...)
Eén van de interessante ontwikkelingen in het Indieweb is de ontwikkeling van [Micropub](/Micropub/). Dit is een protocol dat het mogelijk maakt om met diverse schrijfcliënts te posten op je eigen site. Het is een open protocol in tegenstelling tot bijvoorbeeld WordPress of Medium. Wat MicroPub doet is datgene wat jij ergens schrijft (bijvoorbeeld in [Quill](http://quill.p3k.io/) of [Micropublish.net](https://micropublish.net/)) in een algemeen format aanbieden bij je site, waarna de software van je site er mee kan doen wat nodig is. 

Veel van de kant-en-klare scripts en open source apps die dit mogelijk maken op je eigen site, maken gebruik van de koppeling met Github. Eigenlijk doen ze dat allemaal wel. En laat ik die nu net hebben ontkoppeld. Dus dan kan ik twee richtingen op:

1. Ik ga de open source scripts zelf omschrijven naar een manier waarop andere git-servers dan alleen Github wordt ondersteund
2. Ik kies weer voor een koppeling met Github en ga op zoek hoe ik zonder gebruik van Github Pages mijn site kan hosten. Want dan heb ik meer vrijheid in Jekyll plugins en minder hoepels.

Ik heb twee dagen mijn tanden stuk gebeten op de eerste mogelijkheid. Maar mijn beperkte kennis van zowel de interne werking van git als van programmeertalen als Node of Ruby gaven me hoofdpijn. De hoeveelheid nieuwe kennis die op me afkomt is overweldigend. Enorm interessant, maar tegelijkertijd een stap te ver voor me. Ik wil graag bijdragen aan open source projecten en nieuwe mogelijkheden verkennen. Maar ik ben geen programmeur _pur sang_ en heb niet de ambitie om allerlei randgevallen, unieke _usecases_ en updatevraagstukken te gaan ondersteunen. 

Dus heb ik een stapje terug gedaan. Ik kies er voor om de broncode van deze site bij Github onder te brengen. Maar de uiteindelijke site, waar je dit leest, die moet ergens anders worden ondergebracht. Dat brengt me weer op een volgende zoektocht. Ga ik dat doen via diensten als [Travis CI](http://travis-ci.com/), of kies ik voor een oplossing als [Netlify](http://netlify.com/)? Of een van de vele andere [statische site hosting oplossingen](https://www.slant.co/topics/2256/~best-static-website-hosting-provider)? En wat heeft dat voor gevolgen? 

Soms vraag ik me wel eens af waarom ik het mezelf zo moeilijk maak. Maar goed, het blijft een hobby. Soort van.
