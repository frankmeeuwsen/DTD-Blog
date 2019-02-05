---
layout: post
title: "Werk handiger in Google Sheets met Google Translate"
date: 2018-07-03 12:28:35 +2h
excerpt: "Met de functie =GOOGLETRANSLATE kan ik zo'n 50% op mijn werk besparen." 
published: true
category: webtech
---

Een basishouding die ik probeer na te streven in mijn werk is: "Hoe kan ik dit handiger of sneller doen?" Ofwel, hoe kan ik iets zo ver mogelijk automatiseren? Dit resulteert in een uitbundig gebruik van sneltoetsen en shortcuts in allerlei programma's, al dan niet zelf gemaakt via een app als [Keyboard Maestro](https://www.keyboardmaestro.com/main/). 

Maar eveneens in dagelijks werk wat ik doe, zitten soms wat werkzaamheden die ik te saai vind om vaker dan één keer te doen. Zoals het vertalen van teksten. Op [onze site](https://olisto.com) hebben we kanaalpagina's met voorbeeld-triggs, de regels die via onze app iets kunnen automatiseren of vergemakkelijken voor je. Zijsprong: Snap je nu trouwens waarom ik geloof in een app als Olisto? Het lost mijn eigen problemen op!
De site is tweetalig, wat betekent dat de Nederlandse triggs van onze junior marketeer moesten worden vertaald naar het Engels. Vanwege vakanties, drukte en volle agenda's besloot ik de vertaal klus voor nu op me te nemen, anders zou het nooit gebeuren. Niet dat ik overloop van de tijd, maar ik had een vermoeden dat dit makkelijk te automatiseren was. 

De oorspronkelijke Nederlandse teksten staan namelijk in Google Sheets. Ik had een idee dat er wel eens een koppeling kon zijn met Google API's in de functies van Sheets, waarmee een vertaling relatief eenvoudig is te starten. Een zoekopdracht verder en voila...

![<>](/images/translate.jpg)

Met de functie `=GOOGLETRANSLATE(text, [source_language, target_language])` kun je eenvoudig al 50% van het werk laten doen door de vertaalservice van Google die steeds beter wordt. Toegegeven, de Engelse teksten zijn nog niet perfect en ik moet ze nog handmatig controleren en corrigeren waar nodig. Maar er is in elk geval een begin. Ik hoef niet bij elke cel na te denken over de complete vertaling of de tekst kopiëren en plakken op de website van Google Translate. Dit is al een hele verbetering!

Heb je een vertaalklus en heb je toegang tot Google Sheets? Denk dan eens aan de functie `=GOOGLETRANSLATE` om je werk weer net wat eenvoudiger te maken. Meer informatie vind je in [de Help bestanden](https://support.google.com/docs/answer/3093331?hl=nl&authuser=1) van Google Docs. Er is eveneens [een Excel versie](https://technitya.com/), die heb ik verder niet getest.

