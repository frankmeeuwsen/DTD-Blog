---
layout: post
title: Waarom mijn post als reactie onder dezelfde post staat
date: 2018-10-24 8:38:20 +2h
excerpt: Een verhaal over open source, de losse kralen van het internet en eigen technisch inzicht.
published: true
header:
categories: webtech
tags: webmentions indieweb 
---
Oh de hoepels waar je door springt als je je eigen oplossingen aan elkaar wilt rijgen als een kralenketting. Sinds dit weekend kan ik eindelijk webmentions versturen vanaf mijn site. Nu bestaan webmentions uit twee onderdelen: Versturen en ontvangen. 

Het principe is best simpel: Na publicatie van een nieuwe blogpost checkt het verstuur-script in de post welke links hij kan vinden en gaat webmentions versturen. Als de ontvangende site geen webmentions-ontvangstdienst heeft, dan is dat geen probleem. De webmention wordt dan niet verstuurd. Is er wel een ontvangstdienst op de ontvangende pagina, dan verstuur ik automagisch de webmention. Of nou ja, ik niet, een klein robotje ergens op een server.

### Webmentions aan jezelf
Volgens de W3C specificaties is het aan de ontvangende dienst om de webmentions te checken. [Een van de specificaties](https://www.w3.org/TR/webmention/#request-verification) is:

> The receiver MUST reject the request if the source URL is the same as the target URL.

Dus als je een webmention naar je eigen pagina stuurt, dan zou de ontvangende site - mijn eigen site dus - moeten zeggen "OK supersympathiek, maar die hoef ik niet te hebben want die komt van mijn eigen site." Klinkt logisch toch?

Nu gebruik ik voor de ontvangende dienst weer [een andere service](https://webmention.herokuapp.com/), die destijds makkelijk was op te zetten voor mijn site. Die service heeft nu alle webmentions van het afgelopen jaar. Helaas checkt die dienst niet of de bron en doel URL gelijk zijn. Dit is een bug die al [meer dan een jaar open](https://github.com/voxpelli/webpage-webmentions/issues/43) staat, maar helaas heeft de maker geen tijd om het te fixen. Dat is begrijpelijk, dit soort services zijn _labors of love_ en de kachel moet wel blijven branden. 

### Volgende stappen

Dus wat kan ik nu het beste doen? Er zijn een paar mogelijkheden die ik de komende tijd verder evalueer

1. De dienst die ik nu in gebruik heb in eigen beheer hosten en zelf het script aanpassen. Omdat de Webmention dienst open source is, kan ik het script zelf [downloaden](https://github.com/voxpelli/webpage-webmentions) en eventueel zelf aanpassingen doen. Dit vereist echter wel dat ik mijn NodeJS skills weer wat opkrik én dat ik een goede lokale testomgeving heb. Een goede oplossing kan ik natuurlijk weer teruggeven aan de community. 
2. Een andere dienst kiezen. Er zijn meer diensten die het mogelijk maken om webmentions te ontvangen en weer te geven. Hiervoor hoef ik in theorie één regel aan te passen, het adres van de ontvangende dienst en de code om de webmentions weer te geven om te leiden. Echter, [alle bestaande webmentions](https://webmention.herokuapp.com/user/sites/diggingthedigital.com) wil ik dan wel importeren bij de nieuwe dienst zodat ik geen verleden kwijt ben. 
3. Zelf iets in elkaar brouwen. Dat is mogelijk een lange termijn doel. Afgelopen weekend zijn de verschillende protocollen rondom het open web gedemystificeerd voor me. Zeker sinds ik [Aaron Parecki](https://aaronparecki.com/) aan het werk zag en in [een paar minuten](https://www.zylstra.org/blog/2018/10/micropubiwcnuremberg/) een werkende ontvangende dienst zag maken in een demo. Het is voor mij nu nog iets te hoog gegrepen, zeker als het om de beschikbare tijd gaat. Misschien is dat een project voor een volgende IndieWebCamp. 

Al met al is het probleem nú nog niet opgelost, anders dan dat de maker van de Webmention dienst [heeft aangeboden](https://github.com/voxpelli/webpage-webmentions/issues/43#issuecomment-432535847) om de doublures handmatig uit de database te halen. 

To be continued!