---
layout: post
title: Een lokaal Instagram archief. Indieweb style. 
excerpt: Hoe maak je een lokale kopie van je Instagram posts met gebruik van eigen scripts en open source diensten?
published: true
header: instagram.jpg
syndication: indienews
---
Als je deze blog volgt via RSS (laat het me even weten!) dan zul je de afgelopen dagen wat aparte berichten voorbij hebben zien komen. Mocht je hier toevallig via Google of op een andere wijze zijn gekomen, dan zie je wellicht wat opvallende berichten die je normaal elders verwacht. 

Tussen de Kerstgangen, oliebollen en vrije-dagen-met-kinderen door ben ik wat aan het klussen op de site. Omdat het kan. Omdat ik het leuk vind. Ik ben geen *webdeveloper* van origine, ik autodidact en [Stack Overflow][1] me een slag in de rondte. Ik leer steeds beter om in documentatie van programmeertalen snel het juiste te vinden zonder alle bagage van de complete taal mee te moeten nemen. Natuurlijk kan ik dit blog lekker veilig in WordPress maken, dat doe ik immers al jaren. Dan kan ik me richten op de inhoud. Op het geschrevene in plaats van het getoonde. Kies een theme, pak een aantal standaard plugins, next next finish en boem, de site staat. Uiteraard is daar niets mis mee. Maar het kriebelde dat er meer moest zijn. Mede gedreven door mijn interesse in het [Indieweb][2] de afgelopen maanden, merkte ik dat ik er liever op een andere manier mee bezig wilde zijn. 

De afgelopen dagen heb ik dan ook het volgende gedaan: 
* Een koppeling gemaakt tussen [mijn Instagram account][3] en deze site
* Een navigatie-item onderaan elke pagina gemaakt om het aantal blogposts per pagina terug te brengen
* Het template van elke pagina wat kleiner gemaakt zodat het beter laadt
* De CSS verbeterd voor zowel de Instagram als de reguliere pagina's
* Op Github de verschillende branches opgeschoond
* Tests gedaan rondom de implementatie van [Micropub][4] op deze site
* Een start gemaakt met syndicatie van Instagram reacties en likes naar de posts hier.

Tussendoor heb ik nog wel wat hardgelopen, lekker eten gemaakt, met Finnéan naar de film [Coco][5] geweest (ga die film zien!) en in huis opgeruimd. Man wat een drukte zo in de vakantie!

## Micropub? Instagram op je site?
In bovenstaande lijst vallen wellicht twee zaken op, Instagram posts op deze site en Micropub. Ze hebben met elkaar te maken. 
  
Eén van de principes van het Indieweb is "[Own your data][6]" (✊) waarbij het wordt aangemoedigd om vooral op je eigen site te publiceren en die content te distribueren naar andere silo's zoals Twitter en Facebook. Nu is dat in mijn ogen een principe wat weinig rekening houdt met de werkelijke wereld en hoe je dagelijks opereert op sociale netwerken. En niet elk netwerk staat dit toe. Zoals Instagram. Het is door de softwarematige structuur van Instagram niet mogelijk om iets op het netwerk te posten zonder gebruik te maken van hun app. Dat is een keuze die zij maken. Daar kun je het mee oneens zijn en dat een beknotting van je vrijheden vinden. Maar ja, ze zijn een private onderneming en ze mogen doen wat ze willen zolang het binnen de grenzen van de wet valt.  
Bevalt je dat niet? Dan zoek je een alternatief. 

Dus draai je het om. In plaats van eerst op je eigen site te posten en zo de controle over je data te houden, publiceer je lekker op Instagram en zorg je er voor dat je op een zo *DIY*-achtige wijze de foto en tekst tevens op je eigen site krijgt. Een van de manieren om dat te doen is via [OwnYourGram][7]. Met deze open source dienst van [Aaron Parecki][8](co-founder IndieWebCamp) kun je je eigen site aan Instagram koppelen. Als je vervolgens iets op het netwerk post zal na een poosje de foto en de tekst op je eigen blog beschikbaar zijn. Dit gebeurt door een protocol wat [Micropub][9] heet. Deze open standaard kun je integreren op je eigen site en zo posts maken op je site met gebruik van allerlei andere diensten.  
Om de vergelijking te maken met sociale netwerken, als je al wat langer gebruik maakt van Twitter dan ben je wel bekend met apps als Tweetdeck of Twitterific. Hiermee kun je je tweets plaatsen. Of de vele andere diensten die er voor zorgen dat je iets op Twitter kunt plaatsen zonder dat je echt op Twitter bent.  
Een Micropub Eindpunt werkt eigenlijk net zo, maar is niet gelimiteerd aan alleen een Twitter netwerk. Of alleen een Facebook netwerk. Via dat eindpunt kun je je identificeren voor allerlei netwerken en allerlei koppelingen maken.  
Het klinkt eenvoudig en als magie. Dat laatste is het voor mij nog wel, dat eerste is het zeker niet. De implementatie van zijn Micropub eindpunt is best een pittige klus, wat ik al eens eerder [heb uitgelegd in een blogpost][10]. 

Dankzij dat Micropub Eindpunt op mijn site ([kijk in de code op Github][11]) kan ik nu inloggen bij een dienst as OwnYourGram en me verifiëren als eigenaar van mijn eigen Instagram account. Vanaf dat moment zijn mijn site en Instagram aan elkaar gekoppeld. Nu wordt elke Instagram post automatisch op mijn site geplaatst. Ik zou nog een Whitelist of een Blacklist kunnen opstellen. Waarbij foto's met een specifieke term respectievelijk worden geplaatst of overgeslagen. Ik kijk het een tijdje aan hoe dit me bevalt en misschien pas ik die lijst nog wel aan. 

## Wat is het voordeel?
Mijn Instagram account is iets anders dan Twitter en Facebook. Laatstgenoemde kan me werkelijk gestolen worden. Er is op mijn Facebook account weinig van waarde wat ik tot het einde der tijden zou willen bewaren én wat uniek op Facebook is te vinden. Alles wat op Facebook staat van enige waarde (foto's of een specifieke post) heb ik ook elders opgeslagen. Online of offline. Voor Twitter heb ik al [een archief][12] wat dagelijks wordt bijgehouden én wat ik in eigen beheer heb. Voor Instagram had ik dat nog niet. Ik heb een tijdje een koppeling gehad via If This Then That om Instagram posts in Evernote op te slaan, maar dit maakte geen kopie van de foto. Natuurlijk heb ik de foto nog op mijn telefoon, maar de combinatie van foto, onderschrift én de reacties maken het een compleet pakketje voor mij. 
Ik heb vanaf nu een publiek archief van mijn Instagram foto's op mijn eigen site. Het is op zo'n manier opgeslagen dat ik het vrij eenvoudig naar andere diensten of sites kan transporteren als ik dat zou willen.  
Wat ik nog wil doen met deze koppeling is de reacties en hartjes van elke Instagram post lokaal op deze site opslaan. Dit zou via de dienst [Brid.gy][13] kunnen maar wederom is dat vooral abracadabra voor me. Ik weet nog niet exact hoe ik de [webmentions][14] kan koppelen aan de juiste foto op deze site.  Wat ik eveneens nog moet doen is de RSS-feed van deze blog aanpassen zodat niet alleen het onderschrift wordt getoond maar tevens de foto. Tenslotte zou ik de vormgeving van Instagram posts nog wat explicieter willen maken, passend bij de bron. Maar dat zie ik dit jaar niet meer gebeuren...

## Doe mij ook zo'n lokaal Instagram archief!
Mja, dat is makkelijker gezegd dan gedaan. Ik zal er nog eens een uitgebreide post aan wijden hoe ik nu exact te werk ben gegaan en welke stappen je moet zetten. Maar ik waarschuw je, het is verre van eenvoudig en het vereist wel wat meer technische kennis dan een plugin installeren of een WordPress theme configureren. Er zijn weinig vinkboxen en keuzemogelijkheden, veel is zelf uitdokteren en leren terwijl je werkt. Heb je daar geen trek in, begin er dan niet aan. Heb je er wel trek in , begin dan met het concept van [Micropub][15]. Vanuit daar kun je alle kanten op...
<a href="https://news.indieweb.org/nl" class="u-syndication"></a>

[1]:	https://stackoverflow.com/
[2]:	/Indieweb
[3]:	http://instagram.com/frankmeeuwsen
[4]:	/Micropub
[5]:	https://screenrant.com/pixar-coco-movie-easter-egg-secrets/
[6]:	https://indieweb.org/own_your_data
[7]:	https://ownyourgram.com/
[8]:	https://aaronparecki.com/
[9]:	https://indieweb.org/Micropub
[10]:	/Micropub
[11]:	https://github.com/frankmeeuwsen/DTD-Blog/commit/f23b143dbd2f56e503e222dc3d964a96c2fe1b3d
[12]:	http://twitter.frankmeeuwsen.com/
[13]:	https://brid.gy/instagram/frankmeeuwsen
[14]:	/webmentions
[15]:	https://indieweb.org/Micropub