---
layout: post
title: GDPR en het Indieweb (deel 1)
date: 2018-05-08T090147CEST
excerpt: Als je je eigen weblog bijhoudt, wat moet je dan met de GDPR? En hoe zit dat met webmentions? Wat een vragen in deze eerste verkenning.
published: true
header: header-gdpr.jpeg
syndication: indienews
---
Bij Olisto zijn we al een tijdje bezig met de implementatie van de GDPR wetgeving. Deze nieuwe wet treedt eind mei in werking en ja, ook wij zijn in de "Last Minute Panic GDPR Mode" zoals vele anderen. Al valt het bij ons wel mee met die _panic_. We hebben een goed team er aan werken en wat er moet gebeuren is behoorlijk overzichtelijk. Ik ben er zijdelings bij betrokken, met name voor onze website.

Waar ik echter niet zo bij heb stil gestaan, is deze website. Ik weet dat het vreemd klinkt, omdat ik vaker schrijf over data-beveiliging en privacy, maar eerlijk gezegd had ik niet eerder het idee dat ik echt stappen moest ondernemen voor deze site rondom de GDPR. Ik sla geen reacties op, ik heb geen advertenties, ik vraag niet om jullie mailadressen voor een nieuwsbrief, niets van dit alles. Er zijn echter twee onderdelen die wel de aandacht verdienen: Statistieken en webmentions.

## Statistieken

Sinds enige tijd heb ik [weer statistieken software](/piwik) op deze website. Ik maak gebruik van [Matomo](https://matomo.org/), een open-source oplossing die ik op een eigen (gehuurde) server heb geinstalleerd en daar onderhoud. Aangezien alles op een eigen domein en eigen server draait ligt het voor mij vermoedelijk anders dan als ik Google Analytics zou gebruiken. Gelukkig heeft Matomo een [GDPR overzicht](https://matomo.org/docs/gdpr/) waar ik in kan duiken en waar ik hopelijk meer informatie kan vinden over mijn specifieke situatie. Ik verwacht dat ik sowieso een privacy policy zal moeten opstellen. Al is deze nog zo simpel en klein, misschien is het overkill, maar het kan nooit kwaad. 

Ik zie dat er [GDPR-opties zijn](https://matomo.org/changelog/matomo-3-4-0/) in de nieuwe versie van Matomo. Die ga ik eveneens een verder onderzoeken. 

## Webmentions
De webmentions op deze site zijn een ander verhaal. Ik worstel al sinds het begin van dit blog met het concept van de [Webmentions](/webmentions/) en het is er niet beter op geworden. Op zich werken ze wel, ik krijg netjes jullie Twitter hartjes binnen en als iemand reageert via Twitter op een tweet waarin mijn blogpost is vermeld dan krijg ik dat netjes te zien onder de betreffende blogpost. Waar ik echter voor mijn statistieken een oplossing heb die op mijn eigen server draait, heb ik dat voor webmentions nog niet. Ik gebruik hiervoor [een dienst](https://webmention.herokuapp.com/) die gratis is aangeboden door [Pelle Wessman](https://voxpelli.com/), een van de voorvechters van het open internet. Onder elke pagina haalt een stukje script de likes en berichten van Twitter op en laat deze zien. Dat script vind je [hier](https://webmention.herokuapp.com/api/embed?version=cutting-edge&url=http://diggingthedigital.com/fietsenstalling/) voor een van mijn eerdere blogposts. Als je helemaal naar beneden scrollt zie je een lijst met Twitter berichten inclusief naam en link naar de avatar van de maker. Wat ik me nu afvraag is ten eerste, wordt deze lijst elke keer opnieuw real-time gegenereerd? (Lijkt mij niet) en waar wordt deze lijst opgeslagen? En moet ik er iets mee? Moet ik ergens melding maken dat je reacties op Twitter op mijn blogposts mogelijk onder de blogpost worden getoond? Of is dat iets wat Twitter al dekt in de eigen privacy-statement? En hoe verwijder ik webmentions van blogposts?

## Wetgeving

Dat de GDPR impact heeft op het grote sociale web, dat mag geen verrassing zijn. Facebook, Twitter, Instagram, Pinterest, allemaal zijn ze druk bezig om te voldoen aan de wetgeving die eind mei in werking treedt. Je hebt inmiddels al genoeg mails ontvangen dat je je afvraagt of alle juristen op een "Herschrijf Je Algemene Voorwaarden"-kamp zijn geweest en nu hun eindopdracht doen. Maar het internet is juist bedoeld voor de individuele expressie. Iedereen heeft de vrijheid om zijn eigen website te starten en te doen en laten wat hij wil. Dat is de grote kracht van het internet. Het Indieweb-gedachtengoed is hier een goed voorbeeld van. Het kost je wat zweet en doorzettingsvermogen, maar het is mogelijk om onafhankelijk een eigen plek op het web op te bouwen, zonder al te veel afhankelijkheid van derde partijen. Hoe de wetgeving hier mee om gaat is niet zo duidelijk omschreven in alle artikelen. Binnen de Indieweb community zijn er wel veel discussies over de geldigheid van de GDPR voor persoonlijke websites. 

Artikel 18 van de GDPR stelt: "Deze verordening is *niet van toepassing* op de verwerking van persoonsgegevens door een natuurlijke persoon in het kader van een louter persoonlijke of huishoudelijke activiteit die als zodanig geen enkel verband houdt met
een beroeps- of handelsactiviteit. Tot persoonlijke of huishoudelijke activiteiten kunnen behoren het voeren van correspondentie of het houden van adresbestanden, *het sociaal netwerken en online-activiteiten* in de context van dergelijke activiteiten." (Bron: [Officiele tekst in PDF](http://eur-lex.europa.eu/legal-content/NL/TXT/PDF/?uri=CELEX:32016R0679&rid=1))

Dit is een cruciaal punt waar nu discussie over is. Kun je webmentions zien als het voeren van correspondentie of het sociaal netwerken? Ik ben er nog niet over uit.

## Lees meer over GDPR en het Indieweb
Wil je meer weten over het Indieweb en GDPR, dan kan ik je de volgende artikelen ten zeerste aanraden

* Sebastian Greger - [The Indieweb privacy challenge (Webmentions, silo backfeeds, and the GDPR)](https://sebastiangreger.net/2018/05/indieweb-privacy-challenge-webmentions-backfeeds-gdpr/): Dit artikel gaf mij het inzicht dat ik nog eens goed naar mijn eigen situatie moest kijken. Het gaf tevens een startsein voor meer artikelen in het domein...
* Dries Buytaert - [The data protection challenges of a decentralized, social web](https://dri.es/the-data-protection-challenges-of-a-decentralized-social-web)
* Chris Aldrich - [A reply to Sebastian Greger](https://boffosocko.com/2018/05/03/brief-reply-to-the-indieweb-privacy-challenge-webmentions-silo-backfeeds-and-the-gdpr-by-sebastian-greger/). Check de tongue-in-cheek disclaimer onder aan zijn artikel...
* Daniel Goldsmith - [A reply to Sebastian Greger](https://ascraeus.org/micro/1525556293/). Daniel geeft Sebastian wat interessante tegenargumenten in het debat. 

Ik heb dit artikel met opzet (deel 1) meegegeven om dat ik verwacht dat er meer delen zullen komen. Zie dit als mijn eerste stappen om deze site netjes volgens de nieuwe AVG/GDPR wet te laten werken. Hopelijk haal je er zelf goede informatie uit die je in je eigen situatie kunt gebruiken. Als dat zo is, laat het me weten via Twitter of schrijf een blogpost met een verwijzing naar mijn post. Als je webmentions gebruikt zou het moeten werken dat hieronder een verwijzing wordt geplaatst. Gebruik je geen webmentions, dan kun je met [deze tool](https://indiewebify.me/send-webmentions/) je webmention sturen. Hoop ik...

Headerbeeld 
	<a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px;" href="https://www.pexels.com/photo/architecture-bungalow-cabin-clouds-277696/" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos"><span style="display:inline-block;padding:2px 3px;"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-1px;fill:white;" viewBox="0 0 32 32"><title></title><path d="M20.8 18.1c0 2.7-2.2 4.8-4.8 4.8s-4.8-2.1-4.8-4.8c0-2.7 2.2-4.8 4.8-4.8 2.7.1 4.8 2.2 4.8 4.8zm11.2-7.4v14.9c0 2.3-1.9 4.3-4.3 4.3h-23.4c-2.4 0-4.3-1.9-4.3-4.3v-15c0-2.3 1.9-4.3 4.3-4.3h3.7l.8-2.3c.4-1.1 1.7-2 2.9-2h8.6c1.2 0 2.5.9 2.9 2l.8 2.4h3.7c2.4 0 4.3 1.9 4.3 4.3zm-8.6 7.5c0-4.1-3.3-7.5-7.5-7.5-4.1 0-7.5 3.4-7.5 7.5s3.3 7.5 7.5 7.5c4.2-.1 7.5-3.4 7.5-7.5z"></path></svg></span><span style="display:inline-block;padding:2px 3px;">Pexels/Pixabay</span></a>
