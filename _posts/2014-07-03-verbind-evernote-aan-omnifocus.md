---
ID: 51
title: Verbind Evernote aan Omnifocus
author: Frank Meeuwsen
tags: evernote
post_date: 2014-07-03
layout: post
published: true
---
<strong>Een van de krachten van een goed productiviteits systeem is de mogelijkheid om je taken bij elkaar te zien én om relevante gegevens bij een taak bij de hand te hebben. De combinatie Omnifocus en Evernote is om die reden een interessante. Omnifocus is goed in het organiseren en weergeven van je taken, projecten en contexten. Evernote is uitstekend om al je referentiemateriaal te organiseren en te bewaren. Echter, er is tot op heden nog geen echt goede koppeling tussen de twee. Het zijn twee separate systemen die geen geautomatiseerde koppeling hadden. Tot nu.</strong>


Als je een notitie in Evernote hebt die relevant is voor een taak in Omnifocus, hoe koppel je die twee? Tot op heden moest je bij de taak in Omnifocus een link maken naar de Evernote notitie en deze meenemen in je wekelijkse review. Gebruik je Evernote intensief voor je referentiemateriaal, dan is dat een vervelende taak. Een uitstekend uitgangspunt om te automatiseren dus! Met een Applescript heb ik een koppeling tussen de beide programma’s gemaakt waarbij je eveneens de vrijheid hebt om de herinneringstijd van de Evernote notitie mee te nemen naar Omnifocus

<h2 id="samenvatting">Samenvatting</h2>

In het kort werkt het als volgt

<ul>
    <li>Je installeert het script op je Mac</li>
    <li>Je geeft de relevante notities in Evernote de tag “review”</li>
    <li>Via Lingon zorg je dat het script automatisch elke x minuten loopt</li>
    <li>Je notities komen in Omnifocus</li>
</ul>

<strong>Let op</strong>: Dit script en de bijbehorende opties werken <em>alleen</em> op Mac OSX. Dit werkt dus <strong><em>niet</em></strong> op Windows, <strong><em>niet</em></strong> op je iPad, iPhone, Samsung Galaxy Tablet, Pebble horloge, Google Glass of ander apparaat. Dit werkt <strong><em>alleen</em></strong> op een laptop of desktop waar Mac OSX op is geinstalleerd. En Evernote, Omnifocus en Lingon uiteraard.

De kern van het script is het koppelen van de notitielink van Evernote aan het notitieveld van Omnifocus. Hier zit de kracht van het script. Dit is ontstaan uit een blogpost van Asian Efficiency, die de eerste versie van dit script hebben gemaakt. Ik heb er een aantal functionaliteiten aan toegevoegd zoals de mogelijkheid om de herinnering in Evernote wel of niet over te zetten naar Omnifocus en de mogelijkheid om de originele herinnering in Evernote te verwijderen. Dit zijn individuele instellingen die je in het script maakt. Maar alle credit voor het originele script gaan naar Thanh Pham van Asian Efficiency en Nick Wild van 360 Degrees Media.

<h2 id="hoewerkthetscript">Hoe werkt het script?</h2>

Het script doet het volgende

<ul>
    <li>Het checkt of je een Evernote notitie hebt met de tag “review” (deze tag kun je in het script wijzigen naar een andere relevante tag voor je)</li>
    <li>Voor elke notitie met deze tag maakt het een nieuwe taak in Omnifocus in het formaat: “Review: NAAM_VAN_JE_NOTITIE” waarbij NAAM_VAN_JE_NOTITIE de originele naam van je Evernote notitie is. Tevens krijgt de taak een link naar de originele notitie in Evernote.</li>
    <li>Heb je bij de Evernote notitie een herinnering gezet? Dan krijgt de taak deze datum en tijd als startdatum.</li>
    <li>Bij de notitie in Evernote verwijdert het script de tag en het zet de herinnering op “gereed”</li>
</ul>

Steeds als je een Evernote notitie als taak wilt toevoegen in Omnifocus, geef hem dan de tag “review” en het script doet de rest van het werk.

<h2 id="installatie">Installatie</h2>

Je hebt het volgende nodig voor het script

<ol>
    <li>Download <a href="https://github.com/frankmeeuwsen/Evernote2Omnifocus/archive/master.zip">het Evernote2Omnifocus script</a> en unzip het</li>
    <li>Maak eventueel wijzigingen in het script</li>
    <li>Maak van het script een applicatie</li>
    <li>Zorg dat je <a href="http://www.peterborgapps.com/lingon">Lingon 3 of Lingon X</a> hebt geinstalleerd</li>
    <li>Gebruik Lingon om het script periodiek te lopen.</li>
</ol>

Ik zal elke stap in detail uitleggen. Het is niet heel moeilijk, maar het vereist wel even wat aandacht. Het is net iets meer zelf nadenken dan een paar keer op een knop drukken.

<h3 id="downloadhetscript">Download het script</h3>

Als je de zip file van Github hebt gedownload kun je deze op elke gewenste plek uitpakken en de inhoud bekijken. Het bestand <strong>Evernote2Omnifocus.scpt</strong> is het belangrijkste. Ik adviseer dat je een map “Applescripts” in je homedirectory maakt waar je dit bestand plaatst.

<h3 id="wijzigingeninhetscript">Wijzigingen in het script</h3>

Open het script in de Applescript Editor om nog eventuele wijzigingen te maken. Je ziet dan iets als onderstaande venster

<img class="aligncenter wp-image-135" src="/images/2014/07/20140601AO_En2OFSCPT-1024x703.jpg" alt="20140601AO_En2OFSCPT" width="700" height="481" />

In het onderdeel Settings kun je desgewenst wijzigingen aanbrengen.
<strong>todoTag</strong> : De gebruikte tag in Evernote om aan Omnifocus te koppelen. Deze staat standaard op “review” maar hier kun je elke andere tag van maken.
<strong>taskPrefix</strong> : Dit is de tekst die in Omnifocus voor de titel van de Evernote notitie komt. Hij staat standaard op “Review: ” maar deze kun je aanpassen naar een andere tekst. Wil je geen prefix, maak er dan "“ van.
<strong>transferReminder</strong> : Wil je de originele herinnering uit Evernote meenemen naar Omnifocus? Deze staat standaard op ”true“. Zet hem op ”false“ om de herinnering niet mee te nemen naar Omnifocus
<strong>deleteReminder</strong> : Wil je de originele herinnering in Evernote verwijderen? Standaard is ”true“ maar zet hem op ”false" om de herinnering in Evernote te bewaren.

<h3 id="maakvanhetscripteenapplicatie">Maak van het script een applicatie</h3>

Nu maak je van dit script een applicatie. Je maakt er dan een losstaand programma van wat je als elk ander programma op je Mac kunt starten. Dit doe je als volgt in Applescript-editor

&nbsp;

<img class="aligncenter wp-image-132" src="/images/2014/07/20140601AO_En2OFSCPT_export.jpg" alt="20140601AO_En2OFSCPT_export" width="700" height="453" />

<ul>
    <li>Kies Archief &gt; Exporteer</li>
    <li>Ga naar de map waar je je Applescripts opslaat, bv Home/USERNAME/Applescript</li>
    <li>Sla het script op met Structuur: Programma</li>
    <li>Bewaar</li>
</ul>

<h3 id="lingoninstellen">Lingon instellen</h3>

Nu kun je het programma al testen. Maak een notitie in Evernote met de tag “review” en dubbelklik op Evernote2Omnifocus.app in je script directory. Je zult zien dat in Omnifocus een taak in je Inbox komt met de naam van je notitie.

Echter, je wilt niet constant zelf er aan denken om deze applicatie te starten. Hiervoor kun je het uitstekende programma <a href="http://www.peterborgapps.com/lingon/">Lingon</a> gebruiken. Het kost € 7,40 als je het op de site zelf koopt (Lingon X) en € 4,99 in de <a href="http://clkuk.tradedoubler.com/click?p=24371&amp;a=2064103&amp;uo=4&amp;partnerId=2003&amp;url=https://itunes.apple.com/nl/app/lingon-3/id450201424?mt=12?ls=1&amp;mt=8">Mac Appstore</a> (affiliate link). Het verschil zit hem in de de mogelijheden van de applicaties. Lingon X is net iets geavanceerder dan Lingon 3. Met Lingon kun je de interval instellen wanneer het script zijn werk moet doen. Dit kan op de Mac eveneens handmatig via launchd. Heb je daar geen ervaring mee, gebruik dan Lingon.
Start Lingon en je ziet iets als onderstaande scherm. Ik gebruik Lingon X. In Lingon 3 kan de weergave net iets anders zijn maar de werking is veelal gelijk.

<img class="aligncenter size-full wp-image-133" src="/images/2014/07/20140601AO_En2OFSCPT_lingon1.jpg" alt="20140601AO_En2OFSCPT_lingon1" width="491" height="369" />

Klik op de plus-knop bovenin om een nieuwe job aan te maken.
Je krijgt nu een venster waarin je wat informatie moet opgeven. Geef de job de naam Evernote2Omnifocus. Kies bij “Voer uit” het pad naar je applicatie die je in de vorige stap hebt opgeslagen.
Bij “Datum” vink je aan “Altijd” en “Tijd” &gt; Elk uur op 0 minuut. Nu zal op elk heel uur het script lopen als je je Mac aan hebt staan.
<strong>Let op</strong>: Zet de interval waarop het script loopt altijd hoger dan de synchronisatie interval van Evernote. Evernote moet een notitie namelijk eenmaal synchroniseren om een notitielink te krijgen.
Klik op “Bewaar”

<img class="aligncenter size-full wp-image-134" src="/images/2014/07/20140601AO_En2OFSCPT_lingon2.jpg" alt="20140601AO_En2OFSCPT_lingon2" width="487" height="445" />

Dit zijn alle stappen. Vanaf nu zal elke notitie met de tag “review” automatisch na elk uur in je Inbox van Omnifocus staan waarna je het verder kunt verwerken. Zo verlies je nooit meer een Evernote notitie bij een relevante taak in Omnifocus door de notitielink bij de taak.

Vragen, opmerkingen en bugs zijn welkom in de reacties. Wil je het script verbeteren? Maak dan een <a href="https://github.com/frankmeeuwsen/Evernote2Omnifocus">branch in Github aan</a> zodat anderen er direct van kunnen profiteren.
