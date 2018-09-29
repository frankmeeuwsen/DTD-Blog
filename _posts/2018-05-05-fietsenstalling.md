---
layout: post
title: De fietsenstalling als testgebied voor je app
date: 2018-05-05T082757CEST
excerpt: 
published: true
header: header-stalling.png
categories: 
    - random
---
"But what about the fish? The fish?"

Het is een klassieke episode uit de Seinfeld serie. De [aflevering](https://en.wikipedia.org/wiki/The_Parking_Garage) waar de vier hoofdrolspelers verdwalen in een parkeergarage, op zoek naar de auto. Cosmo Kramer is vergeten waar hij de auto heeft geparkeerd wat uiteraard compleet in de stijl van de serie resulteert in 30 minuten praten over niets terwijl vanalles gebeurt.

Ik moest aan de show denken toen ik weer in de fietsenstalling bij Utrecht Centraal liep. Deze nieuwe stalling claimt de grootste ter wereld te worden als hij helemaal af is. Zelfs met nu een halve fietsenstalling open is het al een wirwar van rekken, gangen en verdiepingen. Ik kom er vrijwel dagelijks en zoals vele anderen, heb je dan toch een eigen plek in zo'n grote stalling. Ik probeer mijn fiets altijd in dezelfde gang te zetten (67), in een bovenste rek, ergens in het midden links. Zo hoef ik niet eindeloos te zoeken en niet heel hard te onthouden waar *exact* mijn fiets staat. Door een paar voor mij opvallende kenmerken kan ik hem redelijk snel uit een volle rij stalen rossen pikken. Met een vage richting waar hij kan staan, heb ik hem redelijk snel gevonden.

Door de bouw van het nieuwe Hoog Catherijne sluiten de fietsenstallingen buiten het stationsgebied en zijn fietsers gedwongen om gebruik te maken van de nieuwe fietsenstalling. De stalling is gratis en je fiets staat er goed, dus is het logisch dat het aantal fietsen wat er dagelijks staat zienderogen toeneemt. Met als gevolg dat het steeds vaker gebeurt dat mijn "vaste" plek al is vergeven aan een ander vehikel. Natuurlijk is het geen probleem om mijn fiets ergens anders te parkeren, maar wat extra hersenhulp kan geen kwaad. Ik ga niet onthouden waar mijn fiets exact staat en ik heb geen zin om als een Jerry Seinfeld panisch door de fietsenstalling te rennen. Gelukkig schiet de techniek me ter hulp!

## QR code voor je fiets

Elk rek heeft een eigen QR code met een nummer. Ik ben benieuwd en ik scan de QR code met mijn telefoon. Onmiddelijk opent de website [Waarstaatmijnfiets](https://waarstaatmijnfiets.ledspark.nl/). Om de locatie van mijn fiets op te slaan moet ik een account aanmaken. Natuurlijk. Na een snelle registratie zie ik een plattegrond met de plek waar mijn fiets staat, rij 64 plek 48. Is mijn fiets nu opgeslagen? Ik denk het wel. Moet ik nog ergens een mailadres verifieren? Of kan ik nu gewoon gaan? Het is me wat onduidelijk...

![](/images/fiets.png)

Terwijl ik naar het station loop vraag ik me toch een paar dingen af. Ik moet er namelijk zelf aan denken om deze pagina als bladwijzer op te slaan in mijn mobiele browser. Als ik vanavond terug kom heb ik geen idee wat het internetadres van deze digitale plattegrond is. Maar er valt me meer op. Als ik mijn fiets heb opgehaald moet ik zelf op een knop "Fiets gevonden" klikken. Dan komt die plaats weer vrij in de app. Maar wat als ik dat niet doe? Je ziet in het bovenstaande screenshot dat mijn fiets er al schijnbaar sinds 1 mei staat. Ik kan je zeggen, inmiddels ben ik al 3 keer meer in de stalling geweest en staat mijn fiets nu gewoon voor de deur. 
Als je de website bezoekt, moet je meteen inloggen. Ik had ergens nog de hoop dat ik een mooie data-visualisatie zou zien waar ik wanneer mijn fiets heb weggezet en voor hoelang. Maar niets van dat alles. Na inloggen kun je alleen een fiets inchecken en uitchecken. De site van de maker [geeft eveneens](https://www.ledspark.nl/) niet veel informatie. Het lijkt me dat deze oplossing vooral voor de beheerder van de fietsenstalling is bedacht en niet voor de fietsers. 

## Minimum Loveable Product
Het idee van deze dienst is niet slecht. Maar het mist de automatisering en het gemak die we inmiddels verwachten van zoiets. Als ik een QR code scan wil ik dat mijn fiets direct is opgeslagen op mijn account. Tevens wil ik dat het systeem zo slim is dat het op basis van locatie en tijd kan zien wanneer ik weer in de buurt van de stalling ben en me dan automatisch een signaal geeft waar mijn fiets staat. En als ik daarna weer ver genoeg weg ben van de stalling mijn fiets automatisch uitcheckt. De huidige generatie telefoons kunnen dit alles. Van locatiebepaling tot een inschatting maken of je loopt, fietst of rijdt, op basis van de gemiddelde bewegingsnelheid. 

Nu is het een dienst die nét niet af is. Je zou met wat goede wil kunnen zeggen dat het hier om een MVP gaat, een Minimum Viable Product. Het minimale wat een dergelijke dienst nodig heeft om van start te gaan. Maar voor de eindgebruiker is het geen *Minimum Loveable Product*. Het is niet een dienst die ik graag dagelijks zou gebruiken. Ik moet er nog teveel over nadenken en het in mijn dgelijkse routine houden om er goed gebruik van te maken. Het is niet _leuk_ om te gebruiken.

Het principe van het Minimum Loveable Product is dat je in je ontwerp- en bouwproces zo snel mogelijk iets maakt wat praktisch bruikbaar is voor je gebruikers én waar ze blij van worden. Henrik Kniberg, de bedenker van de term, [legt uit](https://blog.crisp.se/2016/01/25/henrikkniberg/making-sense-of-mvp) dat veel software-ontwikkelaars beginnen met een wiel, vervolgens een chassis, dan de carosserie en dan eindelijk een auto bouwen. Pas als het product helemaal af is, dán is het echt bruikbaar voor de eindgebruiker. Maar die is inmiddels al aardig gefrustreerd omdat de voorgaande stappen totaal onbruikbaar zijn voor hem of haar. 

![](/images/mvp-car.png)

Het betoog van Kniberg is dat je niet alleen naar het product moet kijken, maar naar de _onderliggende behoefte van de gebruiker_. In plaats van je te focussen op het bouwen van een auto, focus je op de vervoersbehoefte van je gebruiker. 

Als je stip de horizon is "mijn gebruiker wil sneller van A naar B" (of "makkelijker een herinnering krijgen waar zijn fiets staat"...) dan zal je ontwikkelproces meer als onderstaande verlopen.

![](/images/mvp-fiets.png)

Ga van een simpel eerste product naar een steeds meer geavanceerde versie. Maar zorg dat die eerste versie in elk geval al iets doet om het probleem op te lossen. Zoals Kniberg in zijn artikel betoogt, deze versies zijn vooral om van te leren. Om te snappen waar gebruikers op letten en waar ze eigenlijk naar op zoek zijn. Zo bouw je betere versies van je product. 

Ik hoop dat ze dat bij de QR-parkeerdienst doen. Ik zal ze deze blogpost sturen zodat ze weer wat hebben geleerd van een eindgebruiker "in het wild" en ze hopelijk een beter product gaan maken...

![<>](/images/foto-fiets.jpg)

Inmiddels maak ik gewoon een foto van de plek in de fietsenstalling. Ik werk nog aan een oplossing om die foto automatisch weer tevoorschijn te toveren als ik in de avond weer in de buurt van de fietsenstalling ben. Volgens mij moet dat mogelijk zijn. En het hoeft niet moeilijk te zijn.



