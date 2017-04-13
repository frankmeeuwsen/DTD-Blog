---
layout: post
title: Hoe werkt het volgen in de GNU Social universe?
excerpt: Van Mastodon tot Sealions.club. Eenmaal in de federatie kun je allerlei mensen volgen. Ongeacht waar je start
published: true
---

Een van de belangrijkste kenmerken van een sociaal netwerk is het kunnen volgen van andere accounts. Het is een heel normaal en logisch proces. Als je op Facebook zit, kun je ander Facebook-gebruikers volgen. Met je Twitter account volg je andere Twitteraars. Instagram? Idem!
Dat betekent dat ik één persoon op drie verschillende silo's volg. Ik kan niet met mijn Facebook account een Twitter account volgen. Of vice versa. 

Dat is logisch in de wereld van sociale netwerken en communities die we kennen. Je volgt elkaar op het netwerk waar je samen zit. Het netwerk heeft echter wel grenzen. De grenzen eindigen bij de domeinnaam van de eigenaar van het netwerk. Wellicht dat je met je Facebook account later nog wel Instagrammers kunt gaan volgen, aangezien het dezelfde eigenaar is. Maar Met je Linkedin account iemand op Snapchat volgen? vergeet het maar. En communiceren tussen twee verschillende accounts is al helemáál *out of the question*.

Maar op Mastodon en GNU/Social is dat geen probleem. En dat zorgt voor een *brainbender* voor veel mensen. Dat is niet zo vreemd. We zijn zó gewend om elkaar alleen te volgen op de silo waar we zitten. Maar in De Federatie kun je allerlei mensen volgen met elk account wat gebruik maakt van het onderliggende protocol oStatus.

Wat ik de afgelopen dagen vaak lees op Twitter is "Ik kom niet op Mastodon.social en hoe kan ik je dan volgen?" Hier zit volgens mij een aanname achter dat je op dezelfde instantie moet zitten als ik zit om me te kunnen volgen. De aanname is niet vreemd, want zie boven. Dat doen we al jaren. We weten niet beter. Maar joehoe! Dat hoeft dus niet! Want op Mastodon en GNU/Social bestaat zoiets als Remote Follow. Hiermee kun je vanaf [elke Mastodon instantie](https://instances.mastodon.xyz/) of [GNU/Social instantie](http://skilledtests.com/wiki/List_of_Independent_GNU_social_Instances) iemand anders volgen op een andere instantie.

Een voorbeeld: Recent is Digital City Groningen een eigen instantie gestart. Hier zitten Mastodon gebruikers uit Groningen, waaronder Lykle de Vries. Zijn adres is [https://mastodon.groningendigitalcity.com/@Lykle](https://mastodon.groningendigitalcity.com/@Lykle). Mijn adres is [https://mastodon.social/@frankmeeuwsen](https://mastodon.social/@frankmeeuwsen). In de situatie met Twitter en Facebook zouden Lykle en ik op verschillende netwerken zitten en elkaar dus *niet* kunnen volgen met deze adressen. 


## Hoe werkt Remote Follow
Maar Mastodon en GNU/Social is anders. De onderliggende technologie en protocol oStatus maakt het mogelijk dat Lykle en ik elkaar wel kunnen volgen met deze adressen en berichten kunnen sturen. Dit werkt via Remote Follow. Dit gaat als volgt. Stel ik wil het account van Bart Breij volgen. Hij zit eveneens bij Digital City Groningen: [https://mastodon.groningendigitalcity.com/@Scarbir](https://mastodon.groningendigitalcity.com/@Scarbir)

![<>](/images/scarbir.png "Scarbir")

Ik ben ingelogd op mijn account op Mastodon.social en klik op de knop Remote Follow die op zijn accountpagina staat.

![<>](/images/scrf.png "Remote Follow")

Op de volgende pagina is mijn Mastodon account al ingevuld maar het kan zijn dat je deze zelf nog even moet invullen. De schrijfwijze is username@domain.ext. Eigenlijk zoals een mailadres. Klik op *Proceed to Follow*

![<>](/images/follow.png "Remote Follow")

Ik krijg nogmaals een check dat ik zeker weet dat ik Bart ga volgen. Klik op *Follow*.

![<>](/images/Scarbirfollows.png "Done")

En dat is het. Nu volg ik met mijn Mastodon.social account Bart die op Digital City Groningen zit. 

## Aandachtspunten

Er zijn een paar zaken waar je rekening mee moet houden

1. Als je niet bent ingelogd op je eigen instantie zul je nog een tussenscherm krijgen waarbij je je loginnaam en wachtwoord moet geven. 
2. Als je de eerste en laatste schermafbeelding vergelijkt zie je dat het aantal toots, following en followers niet overeenkomen. Wat je ziet als je in je eigen instantie zit is het aantal posts wat voor jouw instantie zichtbaar is, het aantal personen die Bart volgt die op dezelfde instantie zitten als ik en het aantal mensen die Bart volgen van dezelfde instantie als ik zit. 
3. Er zijn servers die niet worden toegelaten op andere servers om te *federaten* ofwel om de toots te zien van die instantie. Dat betekent dat je personen op die andere instantie niet kunt volgen. Daar kom je snel genoeg achter. Het volgen werkt dan gewoon niet. Welke instances op een blacklist staan van de instance waar jij op zit is niet direct duidelijk. Er is geen publieke lijst van bekend. Tevens krijg je een typische server foutmelding als hierdoor het volgen niet werkt. Hier kan de gebruikerservaring nog wel worden verbeterd...
3. Dit werkt niet alleen met Mastodon-instanties maar ook met de "oudere" GNU/Social instanties zoals [Sealion.club](https://sealion.club) en de vele anderen die al jaren bestaan. Hier zie je wederom de Remote Follow knop.

Tot zover een eerste opzet hoe je mensen op andere instanties kunt volgen. Have fun! Kies [een instantie](https://instances.mastodon.xyz/) en toot! 
  