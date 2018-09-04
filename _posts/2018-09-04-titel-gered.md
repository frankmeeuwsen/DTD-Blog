---
layout: post
title: ''
date: 2018-09-04 08:06:23 +2h
published: true
---
De titel is gered. In moderne CMS systemen zijn dit soort rand-problemen vaak al afgevangen met plugins en code, maar omdat ik zo nodig alles zelf wil maken en aanpassen naar mijn gewenste situatie, moet ik dit soort problemen zelf oplossen.

Wat was er aan de hand? Ik schrijf dit blog voor 99% via textbestanden die ik op mijn laptop opsla en automatisch naar Github stuur. Daar wordt de site samengesteld met alle blogposts die je hier ziet. Dat is vooralsnog een prima methode. Maar er komen steeds meer mogelijkheden om blogposts te maken op mijn onderliggende systeem (Ruby, Jekyll en Github) waarbij met name het protocol Micropub interessant is. Omdat ik hier ondersteuning voor heb ingebouwd, kan ik via andere editors eveneens blogposts maken, of interessante bookmarks opslaan. Ik ben daar zelf mee bezig geweest via Pinboard, maar dat project lag wat stil. Nu heb ik via Quill een [fijne oplossing gevonden](/prima-dit-lijkt-te-werken/) die soort-van-werkt. Het is nog niet ideaal en ik zou zeker in de gebruikersinterface en mobiele mogelijkheden wat veranderingen doorvoeren. Maar goed, er is iets om weer mee te testen.

Als ik echter een korte notitie maak via Quill om hier te posten, dan kan ik daar geen titel aan meegeven. Voor die uitzondering had ik nog geen oplossing. Het was immers een uitzondering die nog niet eerder was voorgekomen. Omdat ik alles zelf schrijf, zorgde ik er altijd voor dat ik een titel had voor mijn post. Nu werd dat dus anders. Het missen van de titel breekt zowel de navigatie naar de permalink-pagina van de post alsmede de titel in de RSS-feed. Tijd om mijn Wickie de Viking helm op te zetten en een oplossing te bedenken.

![<>](/images/wickiedeviking.gif)

Een veelgebruikte oplossing is om de eerste woorden of aantal karakters van de blogpost als titel te gebruiken. Gelukkig heeft Jekyll en de opmaaktaal Liquid hier een prima oplossing voor die snel was te implementeren.

In het template voor de voorpagina heb ik een conditie gemaakt die checkt of het titel-veld leeg is. Als dat zo is, dan laat ik de eerste 4 woorden van de tekst zien. Dit is een eenvoudige oplossing:
{% raw %}
    {% elsif post.title == '' %}
    <h1>{{post.excerpt | strip_html |truncatewords: 4}}</h1>
{% endraw %}

Dezelfde code kon ik direct gebruiken in de template voor de RSS feed en in de template voor de artikelpagina zelf. Een kleine wijziging, die me wel wat tijd heeft gekost om uit te vogelen en vooral goed te testen. Uiteindelijk ben ik blij met het resultaat en dat is wat telt.
