---
layout: post
title: PhantomJS. Browsen zonder browser
date: 2018-05-06T113242CEST
excerpt:
published: true
category: 
    - webtech
---

Bij Olisto hebben we te maken met de GDPR wetgeving die eind deze maand in werking treedt. Dat is nogal logisch, aangezien we best wat (persoonlijke) data ontvangen en versturen via onze dienst. Vanaf de start van de app zijn we al behoorlijk *privacy-aware* maar het kan altijd beter. Met een team werken we al een tijdje aan het vernieuwen van de privacy policy, verbeteren we de manieren waarop je je data kunt downloaden en je account kunt verwijderen en nog meer.

Een van de klussen die ik kreeg is het verzamelen van de cookies die we op [de site](https://olisto.com) verzamelen. Nu is onze site al niet zo cookie-hungry. De site is voornamelijk een etalage voor onze app en [ons blog](https://olisto.com/blog) is er te vinden. We tracken de bezoekers op minimale wijze met statistiek software en dat is het wel. Maar een lijstje van de cookies is altijd handig. 

Ik wist zo snel niet hoe ik dat handig voor elkaar kon krijgen maar al na één zoekopdracht ontdekte ik [PhantomJS](http://phantomjs.org/) met een [mooi voorbeeld](https://www.iubenda.com/en/help/262-come-identificare-quali-cookie-sono-installati-dal-tuo-sitoapp) hoe dat script met 1 regel de cookies voor je site netjes in een lijst zet.

![](/images/cookies.png)

Uiteindelijk was ik in 5 minuten klaar met deze klus. Dankzij een [open source](https://github.com/ariya/phantomjs) terminal script met duidelijke voorbeelden. Dat niet alleen, het script biedt tevens meer mogelijkheden om zonder een browser allerlei slimme web-kunstjes uit te halen. Zoals het maken van [screenshots](http://phantomjs.org/screen-capture.html), [automatisch testen](http://phantomjs.org/headless-testing.html) en inspectie van [je netwerk](http://phantomjs.org/network-monitoring.html). Een gratis script met zoveel mogelijkheden. Wat is het internet soms toch fijn!