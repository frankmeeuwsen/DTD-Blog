---
author: frankmeeuwsen
comments: true
date: 2012-01-16 22:10:17+00:00
layout: post
slug: waarom-missen-weblogs-al-15-jaar-deze-manier-van-verspreiding
title: Waarom missen weblogs al 15 jaar deze manier van verspreiding?
wordpress_id: 1892
tags:
- api
- blogging
- ideetje
- wordpress
---

Eén van de grote krachten van het sociale internet is de mogelijkheid om je eigen platform te starten. Je eigen podium, waar je kunt zeggen wat je wilt. Niet gehinderd door een redactie, uitzendtijden of een zendfrequentie. Begin je eigen weblog en je kunt aan de slag. Eenmaal aan het schrijven kun je jezelf promoten op andere blogs, satellietmedia als Twitter, Facebook, LinkedIn of Hyves en offline via flyers, posters, shirts en stickers. Zo zijn er genoeg manieren te bedenken om je eigen podium te promoten. Eigenlijk ben je een mini-uitgever. Een _one-man band_ die alles zelf kan doen. Maar toch ontbreekt er een essentieel deel aan weblogs. Een nog grotere megafoon voor relevante content op andere sites. Blogs zouden een ingebouwde API moeten hebben. De mogelijkheid voor derden om geautomatiseerd geselecteerde artikelen en content te hergebruiken op een eigen platform. Ingebouwde API's in blogplatformen maken het écht mogelijk voor iedereen om uitgever te worden. Je creëert een ingang in je content die gedoseerd en context-gevoelig kan worden bediend door anderen. Het enige wat jij doet is goede stukken schrijven.

<!-- more -->


## Wat is een API?


Even een paar stappen terug. Wat is een API? De letters API staan voor Application Programming Interface. Een API zorgt ervoor dat je een ander stuk software als een blackbox kan gebruiken. Een API is een set aan definities waarmee softwareprogramma's onderling kunnen communiceren. Het dient als een interface tussen verschillende softwareapplicaties waardoor de gebruikte code automatisch elkaar toegang tot informatie en/of functionaliteit geeft, zonder dat ontwikkelaars hoeven te weten hoe het andere programma exact werkt. API's bestaan voor (web)applicaties, softwarebibiliotheken en besturingssystemen en kunnen voor allerlei doeleinden worden ingezet. Zo gebruikt een besturingssysteem een API om softwareprogramma's in de gelegenheid te stellen om bijvoorbeeld te kunnen printen en kun je via een API van een internetapplicatie bijvoorbeeld teksten, foto's en video over de hele wereld binnenhalen en/of versturen. Bekende voorbeelden van API's zijn bijvoorbeeld de [Twitter API](https://dev.twitter.com/docs) waarmee je Twitter kunt gebruiken op een veelheid van andere programma's en websites. De Google Maps API geeft de mogelijkheid om een laag op Maps te leggen waarmee je weer andere functionaliteiten kunt maken zoals een overzicht van geldautomaten in de buurt. Met de Funda API zou je een applicatie kunnen maken die op basis van locatie het aanbod laat zien. Amazon heeft een API waarmee je product- en prijsinformatie kunt ophalen en hergebruiken in andere sites en applicaties. Sinds vandaag heeft Bol.com [een API](http://www.emerce.nl/nieuws/bolcom-publiceert-open-api) waarmee je actuele productinformatie kunt opvragen in je eigen applicaties. Zoals een [Zoek&Scan mobiele app](http://developers.bol.com/showcases/zoek-scan-op-iphone-ipad/) om direct te zien of een product bij Bol.com goedkoper is. Pijnlijk voor winkeliers, maar het is dus mogelijk...


## Waarom zouden blogs dat moeten hebben?


Welnu, een krant als The Guardian heeft een API. Met hun [Open Platform](http://www.guardian.co.uk/open-platform) kun je je eigen apps bouwen op de data van de krant. Ze hebben enorme datasets vrijgegeven voor het publiek, waarmee iedereen weer zijn eigen applicatie kan bouwen of kan aanvullen met relevante data. In hun [API Explorer](http://explorer.content.guardianapis.com/#/?format=json&order-by=newest) zie je al wat een veelheid aan data ze hebben. De [Apps gallery](http://www.guardian.co.uk/open-platform/apps) laat zien wat je zoal kunt maken met de data. Erg interessant met grote hoeveelheden data. Data en inzichten, dat is waar kranten op draaien. Ongeacht het medium en frequentie. Die data maakt The Guardian beschikbaar voor het publiek. En voor andere kranten en uitgevers.

[![](../images/uploadimages/2012-01-16_2307-e1326751714331.png)](../images/uploadimages/2012-01-16_2307.png)



Je kunt je afvragen waarom andere online contentplatformen dit niet hebben. Zoals blogs. Waarom hebben blogs geen ingebouwde Explorer zoals The Guardian? Met de mogelijkheid om een specifieke output te krijgen zoals alle berichten uit 2011 over Griekenland die _niet_ over de eurocrisis gingen en zijn geschreven door een specifieke journalist. Dat zou voor blogs mooi zijn. Een blog met een flinke dagelijkse stroom berichten zou deze content opnieuw beschikbaar kunnen stellen. Sites als iPhoneclub.nl en  Retecool.com kunnen zo volgens mij een relevante nieuwe stroom bezoekers trekken. Of in elk geval de data beschikbaar stellen voor anderen.


## Maar we hebben toch RSS?


Klopt. Sinds de start van blogs (nou ja, bijna...) hebben ze een RSS-feed. Maar dat is een rudimentaire stroom met data. Eigenlijk is een RSS feed een brandslang met data terwijl je slechts een klein stroompje nodig hebt. Maar je bent gedwongen om die hele stroom te nemen omdat er nu eenmaal niets anders is. Er zijn wel tussenoplossingen als [Yahoo Pipes](http://pipes.yahoo.com) waarmee je complexe queries op feeds en andere data kunt doen en daar weer [je eigen feed](http://lifehacking.nl/web20/maak-je-eigen-rss-feed-met-aiderss-en-yahoo-pipes/) van kunt maken. Maar het is een tussenoplossing. Als Yahoo besluit de stekker uit Pipes te trekken ben je alles kwijt. Waarom zou je een tussenoplossing als Pipes nodig hebben als het ook vanuit de bron zelf kan, namelijk het blogplatform.


## Waarom moeten we dit willen?


Je moet niks van me. Maar zie het als een extra service aan je lezers en andere geïnteresseerden. Een dienst die je aan en uit kunt zetten in het beheer van je blog. Maar met de API kunnen anderen geautomatiseerd inpluggen op de database met jouw content en daar hun eigen relevante content uithalen en wellicht hergebruiken. Ik zie er wel betaalmodellen voor ontstaan. Tevens kun je met intellectuele en auteursrechten heel precies omgaan. Eigenlijk zoals The Guardian het doet. Maar dan in het klein, als je dat zou willen.


## Kan het al?


ik ben nog weinig voorbeelden tegengekomen waarbij een weblogplatform een API-achtige omgeving aanbiedt voor derden. Op de plugin markt van Wordpress heb ik de  [JSON API](http://wordpress.org/extend/plugins/json-api/) gevonden. Een interessante plugin die het inderdaad mogelijk maakt om hele specifieke content terug te krijgen uit een Wordpress blog. Zo kun je nu bijvoorbeeld alleen de blogposts van mijn blog halen met de tag "[privacy](http://incredibleadventure.nl/api/get_tag_posts/?tag_slug=privacy)". Gooi de URL van voorgaande link even door de [JSON Formatter](http://jsonformatter.curiousconcept.com/) om wat duidelijker output te krijgen.

Natuurlijk kan dat al met een RSS feed op de tag "[privacy](http://incredibleadventure.nl/tag/privacy/feed/)" maar een plugin als de JSON API kun je verder uitbouwen om bv op meerdere tags te zoeken, van een specifieke auteur, in een bepaalde periode. Bijvoorbeeld op iPhoneclub alle geruchten rondom de komst van de iPad in 2007, geschreven door Gonny. Kijk wederom naar het Open Platform van The Guardian. De data is er al, waarom die niet op meerdere manieren beschikbaar stellen? Met een API zou dat kunnen. En wederom, de schrijver hoeft er niets voor te doen. Je zou als weblogauteur er voor kunnen kiezen om paywalls achter de API toegang te zetten. Er is een andere Wordpress plugin genaamd [WP-RESTful](http://www.joseairosa.com/2010/06/29/wp-restful-wordpress-plugin/) die dergelijke mogelijkheden heeft ingebouwd. Helaas kreeg ik hem op mijn server niet goed geactiveerd en werkend. Maar het is dus wel mogelijk!

Een behoorlijk ontwikkelde plugin is [Kickpress](http://kickpress.org). Deze plugin biedt zeer veel mogelijkheden voor Wordpress blogs, waaronder een uitgebreide API. Ik heb helaas nog niet de mogelijkheid gehad om deze te testen.


## Hoe nu verder?


Ik hoop dat bovenstaande plugins verder worden ontwikkeld. Ik ben geen programmeur, maar zou er als blogger zeker gebruik van maken naast RSS. Met name projecten als Kickpress zijn hoopgevend en bieden voor bloguitgevers nieuwe manieren om mogelijk op _long tail content_ nog extra bezoekers te krijgen. Door het aan andere platformen aan te bieden via een geautomatiseerd proces. Wellicht dat deze blogpost voor een (hernieuwde) interesse zorgt bij programmeurs om het grootste blogplatform Wordpress uit te breiden met een API die voor de eindgebruiker relevant is. En mogelijk volgen andere blogplatformen snel...


