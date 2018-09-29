---
layout: post
title: Een extra abonnee mogelijkheid op deze site
excerpt: Je kunt artikelen hier op de site lezen. Of in je eigen leesmap-software. Met RSS of JSON. 
published: true
header: jsonfeed.jpg
categories: 
    - webtech
---
## RSS, kent u die term nog?
Elke blogger die begin deze eeuw actief was kan zich nog herinneren dat er ineens zoiets was als RSS. Een blog had een klein oranje knopje waarmee je je kon abonneren en automatisch nieuwe posts ontvangen in eigen lees-software.    
Internet-weetje: RSS is mede ontwikkeld door Aaron Swartz, "The Internet's Own Boy" en een held. (Check zijn levensverhaal in [tekst][1] of [video][2])  

De meest bekende lezer is Google Reader, waarmee je je eenvoudig kon abonneren op sites en ze makkelijk kon organiseren.  Dit had als voordeel dat je niet per se dagelijks allerlei sites hoefde door te klikken of ze iets nieuws hadden gemeld. RSS zorgt er voor dat je je eigen leesmap kan maken van persoonlijke blogs, landelijke nieuwssites en alles wat maar de inhoud van zijn site beschikbaar stelde in dat formaat.  
Helaas is RSS nooit doorgebroken naar een groot publiek. Het had te kampen met technische struikelblokken om een abonnement te nemen op een site, er waren verschillende kampen die steggelden om de juiste standaard en vervolgens hield Google Reader er mee op, waardoor ineens een zwart gat leek te ontstaan voor RSS. 

Gelukkig is RSS altijd in de marge blijven bestaan en zijn er nog voldoende onafhankelijke software ontwikkelaars die fantastisch werk verrichten met zowel online als offline feed-readers. Naast RSS is er nu zelfs een alternatief ontstaan: JSON Feed

## Nu is er JSON-feed?
Ineens waren er [twee software ontwikkelaars][3] die het opviel dat binnen de software community een voorkeur ontstond voor het formaat JSON. De twee ontwikkelaars besloten een nieuwe standaard voor feeds te maken: JSONfeed. Inderdaad, dat doet wat aan onderstaande denken...

![][image-1]

Want volgens andere ontwikkelaars, onder andere van RSS lezers, is er niets moeilijk aan het bewerken of uitlezen van RSS. Er is eigenlijk geen probleem met RSS. Soms kan een webfeed niet goed worden uigelezen, maar eerlijk gezegd kom ik dat probleem niet zo heel vaak tegen als lezer. Maar de makers zeggen:
> For most developers, JSON is far easier to read and write than XML. Developers may groan at picking up an XML parser, but decoding JSON is often just a single line of code. 

## Waarom zou *ik* dat gebruiken?
Er is geen verschil tussen RSS en JSON voor de lezer. Je krijgt in je leesmap-software (Inoreader, Feedly etc) nog steeds je artikelen te lezen op de manier zoals jij wilt. Ongeacht op welke manier het in jouw leesmap is gekomen.   
Voor software ontwikkelaars maakt het eigenlijk niet zo heel veel uit. 

## Heb jij een JSON feed van je site?
Jazeker! Op [http://diggingthedigital.com/feed.json][4] is de JSON versie van mijn posts te lezen. Het kostte me letterlijk 5 minuten om dit mogelijk te maken aan de hand van [dit voorbeeld][5]. Lekker makkelijk!

## Ja maar Twitter en Facebook dan? Die geven toch ook mijn nieuws?
... ['Tuurlijk][6]...

## Kan ik een JSONfeed op mijn site krijgen?
Waarschijnlijk wel, check [de mogelijkheden][7] voor plugins en eigen scripts.


### Headerbeeld
<a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px;" href="https://unsplash.com/@mikeack?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Mike Ackerman"><span style="display:inline-block;padding:2px 3px;"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-1px;fill:white;" viewBox="0 0 32 32"><title>unsplash-logo</title><path d="M20.8 18.1c0 2.7-2.2 4.8-4.8 4.8s-4.8-2.1-4.8-4.8c0-2.7 2.2-4.8 4.8-4.8 2.7.1 4.8 2.2 4.8 4.8zm11.2-7.4v14.9c0 2.3-1.9 4.3-4.3 4.3h-23.4c-2.4 0-4.3-1.9-4.3-4.3v-15c0-2.3 1.9-4.3 4.3-4.3h3.7l.8-2.3c.4-1.1 1.7-2 2.9-2h8.6c1.2 0 2.5.9 2.9 2l.8 2.4h3.7c2.4 0 4.3 1.9 4.3 4.3zm-8.6 7.5c0-4.1-3.3-7.5-7.5-7.5-4.1 0-7.5 3.4-7.5 7.5s3.3 7.5 7.5 7.5c4.2-.1 7.5-3.4 7.5-7.5z"></path></svg></span><span style="display:inline-block;padding:2px 3px;">Mike Ackerman</span></a>

[1]:	https://en.wikipedia.org/wiki/Aaron_Swartz
[2]:	https://www.youtube.com/watch?v=9vz06QO3UkQ
[3]:	https://jsonfeed.org/
[4]:	http://diggingthedigital.com/feed.json
[5]:	https://natelandau.com/a-json-feed-for-jekyll/
[6]:	http://fieldguide.gizmodo.com/why-rss-feeds-still-beat-facebook-and-twitter-for-track-1800722740
[7]:	https://jsonfeed.org/

[image-1]:	https://imgs.xkcd.com/comics/standards.png