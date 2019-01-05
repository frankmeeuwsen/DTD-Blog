---
ID: 53
title: Geavanceerde zoekopdrachten in Evernote
author: Frank Meeuwsen
tags: evernote
post_date: 2014-07-13 22:38:31
layout: post
published: true
---
<strong>Het zoekvenster in Evernote is een kleine krachtpatser die je misschien wat meer kunt uitdagen dan je zou denken. Je hebt inmiddels genoeg notities in Evernote zitten, nu is het tijd om de juiste kennis op het juiste moment er weer uit te krijgen. Natuurlijk kun je zoeken op trefwoorden, maar de zoekmogelijkheden zijn robuuster dan dat. Hier zijn een paar zoekmogelijkheden die je echt eens moet proberen.</strong> <!--more--> Je kunt in Evernote zoeken in:

<ul>
    <li>Alle notities binnen heel Evernote met Win+Shift+F (Windows) of Cmd+Ctrl+E (Mac). Met deze sneltoetsen activeer je de zoekfunctie van Evernote ook als je in een ander programma aan het werken bent.</li>
    <li>De notitie die je nu open hebt met Ctrl+F (Windows) of Cmd+F (Mac).</li>
</ul>

Tips:

<ul>
    <li>Plak deze tips als notitie in Evernote, zodat je de zoekopties altijd bij de hand hebt.</li>
    <li>Zoekopdrachten zijn <em>niet</em> hoofdlettergevoelig, dus <em>archief</em> is hetzelfde als <em>Archief</em>.</li>
    <li>De operatoren voer je, ook in de Nederlandse versie van Evernote, Engelstalig in.</li>
    <li>Sommige operatoren kunnen wel met een spatie achter de dubbele punt terecht, de meeste niet. Dus je kunt het beste geen spatie achter de operators plaatsen.</li>
    <li>De webversie van Evernote helpt je met het samenstellen van gerichte zoekopdrachten, bijvoorbeeld op het type notitie of de datum.</li>
    <li>In Evernote voor Windows kun je de opbouw van een zoekopdracht al wel overzichtelijk opvragen en verfijnen via de sneltoets Ctrl+F10.</li>
</ul>

<h2 id="geavanceerdezoekoperatoren">Geavanceerde zoekoperatoren</h2>

Om alle notities te laten zien waarin één van de trefwoorden voorkomt (dus óf offerte óf advies óf jansen), gebruik je operator <em>any:</em>

<blockquote><em>any:</em>offerte advies jansen</blockquote>

Let op: als je <em>any:</em> gebruikt moet deze operator altijd aan het begin van de zoekopdracht staan. Je kunt in één specifiek notitieboek zoeken. Zo kun je bijvoorbeeld in een notitieboek met de naam “Archief” zoeken naar notities met de tekst offerte óf advies:

<blockquote>notebook:Archief any:offerte advies</blockquote>

Let op: je kunt de operator <em>notebook:</em> maximaal éénmaal toepassen. Deze operator moet helemaal voorin staan - zélfs voor <em>any:</em>. Als je toch meerdere notitieboeken noemt dan zoekt Evernote in het laatstgenoemde notitieboek. Als je geen enkel notitieboek meegeeft dan doorzoekt Evernote het actieve notitieboek. Om alle notitieboeken te doorzoeken klik je bovenaan je lijst met notitieboeken op “Alle notitieboeken” voordat je de zoekopdracht intypt. Notitieboeken kun je verzamelen in een stapel. Een stapel <em>Administratie</em> met daarin diverse notitieboeken doorzoek je als volgt:

<blockquote>stack:Administratie</blockquote>

De <em>tag:</em> operator laat je je notities filteren op specifieke labels. Bijvoorbeeld notities met het label “offerte”:

<blockquote>tag:offerte</blockquote>

Je kunt ook zoeken op notities die juist níet voorzien zijn van het label “offerte”:

<blockquote>-tag:offerte</blockquote>

Als een notitie of label spaties bevat dan omsluit je deze met aanhalingstekens. Bijvoorbeeld:

<blockquote>tag:“offerte advies”</blockquote>

Om op meerdere labels te zoeken herhaal je de operator <em>tag:</em>, je ziet dan bijvoorbeeld alle notities met het label “offerte advies” én het label “MKB”:

<blockquote>tag:“offerte advies” tag: MKB</blockquote>

Wil je zowel alle MKB notities als alle adviesoffertes vinden? Dan combineer je met de operator <em>any:</em>

<blockquote>any: tag:“offerte advies” tag:MKB</blockquote>

Met de <em>wildcard</em> * kun je ook alleen de eerste letters van een woord opgeven. Dit werkt ook met labels. Zo kun je notities vinden met <em>vergadering</em> of <em>vergaderen</em>:

<blockquote>vergader*</blockquote>

Tip: notities met <em>minimaal één label</em> kun je vinden met tag:* en notities <em>zonder label</em> met -tag:* Als je een trefwoord zoekt waarvan je zeker weet dat het in de titel staat dan kun je daarin zoeken met <em>intitle:</em>.

<blockquote>intitle:offerte</blockquote>

Per notitie houdt Evernote bij wanneer deze is <em>aangemaakt (created)</em> en voor het laatst <em>gewijzigd (updated)</em>. Andere tijdregistraties zijn <em>gedeeld (sharedate)</em>, <em>herinneringsdatum (reminderTime)</em> en <em>gereedgemeld (reminderDoneTime)</em>. Bij het aanmaken van een notitie zijn beide data aan elkaar gelijken. De operatoren op te zoeken op data zitten iets gecompliceerder in elkaar door de manier waarop je de datum moet samenstellen. Je kunt zoeken op een absolute datum in de vorm JJJJMMDD (jaar, maand, dag). Om bijvoorbeeld te zoeken op een notitie die is aangemaakt <em>op óf na</em> 21 april 2011 zoek je op:

<blockquote>created:20110421</blockquote>

Als je wilt zoeken op een notities die <em>precies op</em> 21 april 2011 zijn aangemaakt, dan zoek je met een kleine omweg op:

<blockquote>created:20110421 -created:20110422</blockquote>

Het is zelfs mogelijk om het tijdstip bij de zoekopdracht te betrekken, bijvoorbeeld notities vanaf 21 april 2011 09:00u (lokale tijd):

<blockquote>20110421T090000</blockquote>

Om in de tijdzone GMT te zoeken plaats je er een hoofdletter <em>T</em> achter. Je kunt ook op een relatieve datum zoeken en zo notities sinds <em>gisteren (day)</em>, twee <em>weken (week)</em> geleden, afgelopen <em>maand (month)</em> of vorig <em>jaar (year)</em> zijn gewijzigd. Notities die gisteren of vandaag zijn aangepast kun je terugvinden met:

<blockquote>updated:day–1</blockquote>

Tip: Je kunt de datum van aanmaak en wijziging handmatig in een notitie aanpassen. Weet je de bestandsnaam? Met de operator <em>filename:</em> kun je daarop zoeken:

<blockquote>filename:factuur–1221712.pdf</blockquote>

Of, als je maar een deel van de bestandsnaam weet:

<blockquote>filename:factuur*</blockquote>

Notities met een herinnering kun je vinden met deze zoekopdracht:

<blockquote>reminderOrder:*</blockquote>

Om notities te vinden waarin je selectievakjes hebt gebruikt zoek je op:

<blockquote>todo:*</blockquote>

Je kunt specificeren of je notities zoekt die todo’s bevatten die je nog moet doen met <em>false</em> (of die juist al zijn gedaan met <em>true</em>):

<blockquote>todo:true</blockquote>

Je ziet dat er veel meer mogelijkheden zijn om te zoeken in Evernote dan alleen op trefwoorden. Een volledige lijst van de zoekoperatoren vind je bij de <a href="https://dev.evernote.com/doc/articles/search_grammar.php">Evernote Search Grammar</a>. In de meest recente <em>engelstalige</em> versie van Evernote Mac is de zoekfunctionaliteit nog sterker verbeterd.
