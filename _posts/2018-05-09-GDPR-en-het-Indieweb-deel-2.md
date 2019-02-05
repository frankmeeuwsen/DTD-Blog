---
layout: post
title: GDPR en het Indieweb (deel 2)
date: 2018-05-09T214044CEST
excerpt:
published: true
category: indieweb
tags: gdpr indieweb
---

_Dit is het tweede deel in een serie van drie artikelen. In [deel 1](/GDPR-en-het-Indieweb/) maak ik een eerste overzicht wat er zou moeten gebeuren, [deel 3](/GDPR-en-het-Indieweb-deel-3-Webmentions/) gaat over webmentions en reacties._

In het [eerste deel van deze serie](/GDPR-en-het-Indieweb/) heb ik voor mezelf op een rij gezet waar ik met deze site mogelijk aan moet voldoen voor de komst van de GDPR. Belangrijk voor mij zijn de statistieken en de webmentions. In dit artikel grijp ik terug op de wetgeving en of de GDPR wel voor mij van toepassing is en kijk ik naar de ontwikkelingen bij Matomo, de statistieken software die ik gebruik. 

## GDPR en persoonlijke sites

De GDPR of AVG is opgesteld omdat de oude privacywetgeving niet meer aansloot bij de huidige digitale wereld. De opslag-, verzamel- en deeldrift van veel online organisaties begint de spuigaten uit te lopen en het werd tijd om de wetgeving op Europees niveau gelijk te trekken. Het doel van de wetgeving is om de burger beter te beschermen en data-misbruik te voorkomen. Met name online klanten, gebruikers, lezers, surfers, _cybernauten_, krijgen er een hoop rechten en bescherming bij. De nieuwe wetgeving is voornamelijk relevant voor commerciele sites, verenigingen, stichtingen, overheden en soortgelijke online diensten. Zoals ik de artikelen in de wet interpreteer, lijkt het alsof persoonlijke sites zijn vrijgesteld van deze nieuwe regels. Ik baseer dit op de volgende artikelen in de wet:

* In [artikel 2](http://www.privacy-regulation.eu/nl/artikel-2-materieel-toepassingsgebied-EU-AVG.htm) lees je: "Deze verordening is niet van toepassing op de verwerking van persoonsgegevens...door een natuurlijke persoon bij de uitoefening van een zuiver persoonlijke of huishoudelijke activiteit". 
* [Artikel 9.2e](http://www.privacy-regulation.eu/nl/artikel-9-verwerking-van-bijzondere-categorieen-van-persoonsgegevens-EU-AVG.htm) geeft aan dat de data is vrijgesteld als "de verwerking betrekking heeft op persoonsgegevens die kennelijk door de betrokkene openbaar zijn gemaakt." (Zoals ik dat lees: via een sociaal netwerk als Twitter)
* [Grond 18](http://www.privacy-regulation.eu/nl/r18.htm) meldt: "Deze verordening is niet van toepassing op de verwerking van persoonsgegevens door een natuurlijke persoon in het kader van een louter persoonlijke of huishoudelijke activiteit die als zodanig geen enkel verband houdt met een beroeps- of handelsactiviteit." 

Aangezien dit een persoonlijke site is zonder winstoogmerk en ik de komende tijd die ambitie niet heb, denk ik dat ik me redelijk veilig hoef te voelen wat betreft de GDPR. Daarnaast verwacht ik dat de Autoriteit Persoonsgegevens zijn pijlen eerst zal richten op allerlei grote partijen voor ze bij mij aankloppen. Als ze al [genoeg mensen](http://customerfirst.nl/nieuws/2018/05/autoriteit-persoonsgegevens-niet-paraat-voor-gdpr/index.xml) hebben.

Desalniettemin vind ik het geen slecht idee om meer duidelijkheid en transparantie te geven wat ik op mijn site opsla en met welke reden. Te beginnen met de statistieken.

## Statistieken
Omdat ik wil weten hoe mijn site wordt bezocht en welke pagina's worden bezocht vanaf welke andere site, hou ik statistieken bij. Hiervoor gebruik ik de open source software [Matomo](https://matomo.org/). Deze software draait op mijn eigen domein op een eigen server, in tegenstelling tot andere (populaire) statistiekensoftware die bij een andere partij in beheer is. Om de software te laten werken draait er een script op deze site die een cookie zet op jouw computer of telefoon. De informatie die hiermee wordt verkregen, wordt verwerkt door Matomo. In de software heb ik de volgende maatregelen getroffen om de data zo anoniem mogelijk te maken zonder verlies aan functionaliteit. Hierbij maak ik gebruik van de lijst die Matomo [zelf aanreikt](https://matomo.org/docs/privacy/).

* IP anonimisatie. De laatste 2 bytes van je IP adres worden geanonimiseerd. Ik zie dus niet het IP adres 192.168.100.42, maar 192.168.xxx.xxx
* Bezoekersdata ouder dan 180 dagen wordt automatisch verwijderd. Tevens hou ik hier geen archieven of copieen van bij. 
* Ik respecteer je [Do Not Track](https://www.eff.org/issues/do-not-track) keuze in je browser. 

Ondanks dat ik niet *wettelijk verplicht* ben om dit allemaal te doen, voel ik me wel moreel verplicht om dit te doen. Ik heb het al eerder betoogd, ik gebruik zelf extensies als Privacy Badger en Adblock, dus waarom zou ik de bezoekers op mijn eigen domein lastig vallen met dit soort zaken? Omdat ik geen belang heb bij het bewaren van al die data en al helemáál niet om deze met andere partijen te delen, wil ik de beste mix van functionaliteit die mij helpt met inzicht in het bezoek en zo min mogelijk inbreuk in de data die wordt achtergelaten door jullie, de bezoekers. 

In de volgende post ga ik verder in op het gebruik van webmentions. Wat zijn ze en hoe werken ze? En is de GDPR op ze van toepassing? Tevens werk ik aan een privacypagina waar bovenstaande eveneens in wordt uitgelegd, plus de mogelijkheid om je eigen bezoek aan mijn site te verwijderen uit de statistieken.
