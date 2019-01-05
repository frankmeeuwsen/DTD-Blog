---
ID: 151
title: >
  Importeer automatisch documenten in
  Evernote (OSX)
author: Frank Meeuwsen
post_date: 2014-07-31 09:15:00
layout: post
published: true
---
<strong>Evernote is redelijk onverschillig hóe je er iets instopt. Je kunt het zelf intypen, er in slepen, naar mailen, automatiseren of via foto’s en scans importeren. Een mooie functionaliteit op Evernote voor Windows is de mogelijkheid om een specifieke folder op je computer te monitoren en nieuwe bestanden die je er in zet automatisch in Evernote te importeren. Helaas mist dat voor de Mac. Dat moest toch op te lossen zijn…</strong>

<!--more-->

Sinds ik in 2012 ben overgestapt van Windows op de Mac heb ik nooit meer teruggekeken naar Windows. Alles wat ik de afgelopen 18 jaar op een Windows machine heb gedaan, of met name de laatste 5 jaar, kan ik prima op een Mac doen. Ik ben een tevreden Mac gebruiker, ondanks de manier waarop Apple omgaat met het idee van open software en vrije keuze.
Maar er was één probleem wat me maar bleef dwarszitten. Evernote op Windows heeft een hele mooie functionaliteit, namelijk de Watchfolder. Je geeft een specifieke folder op die Evernote in de gaten blijft houden voor nieuwe bestanden. Als er nieuwe bestanden in deze folder komen dan worden ze automatisch een nieuwe Evernote notitie en optioneel wordt het bestand uit de map verwijderd. In mijn eigen workflow op Windows werkte dat erg prettig. In mijn favorietenlijst in de Windows Explorer had ik deze map staan zodat ik er direct een bestand in kon slepen om het in Evernote te zetten, evenals een flatbed scanner die ik naar deze map liet scannen. Zo kon ik in korte tijd veel bestanden automatisch naar Evernote sturen voor latere verwerking.

Helaas is deze functionaliteit niet standaard aanwezig in Evernote voor OSX. Je kunt de bestanden wel vanaf de Finder in Evernote slepen, maar daarmee verwijder je het originele bestand niet van je Mac. Dat is iets wat ik wél graag wil. Maar gelukkig zijn er oplossingen beschikbaar die gratis in OSX zitten. Je hebt er niets extra’s voor nodig behalve wat tijd en nauwkeurigheid. Ik heb een script gevonden waarmee je in OSX bestanden automatisch aan Evernote kunt toevoegen. In dit script zit een switch waarmee je twee kanten op kunt:
<ol>
	<li>Je kunt de flow volledig automatiseren. Je plaats een bestand in een folder, het wordt in een vooraf vastgesteld notitieboek geplaatst met één of meer vooraf vastgestelde tags en verwijderd uit de folder.</li>
	<li>Je hebt meer keuzevrijheid, je kunt (nieuwe) tags toevoegen aan de notitie en eventueel kiezen in welk (nieuw) notitieboek het terechtkomt.</li>
</ol>
Aan jou de keuze welke van de scripts je wilt gebruiken. Mijn ervaring is dat een erg persoonlijke voorkeur is en afhankelijk van je favoriete <em>workflow</em>. Door de switch in het script aan te passen kun je experimenteren met jouw favoriete flow.

<em>Disclaimer: Dit script heb ik elders op het web gevonden. Ik claim dus geenszins dat het intellectuele eigendom van dit script bij mij ligt. Alle credits gaan naar Justin Lancy van <a href="http://veritrope.com/">Veritrope.com</a>!</em>

Stroop je mouwen op, want we gaan spelen met Applescript!
<h2 id="importeerbestandeninevernoteviaapplescript">Importeer bestanden in Evernote via Applescript</h2>
Het originele script om de Watchfolder functionaliteit in OSX na te bootsen komt van de website <a href="http://veritrope.com/tech/evernote-desktop-folder/">Veritrope</a>. Dat is sowieso een schatkist als je met Evernote en Applescript wilt spelen, kijk er eens rond! Hoe kun je dit script installeren en gebruiken?
<ol>
	<li>Download <a href="http://allesonthouden.nl/wp-content/uploads/2014/07/Evernote_Folder_Action_Files.zip">dit zip bestand</a>, unzip het en sla op een logische plek op.</li>
	<li>Open het bestand in de Applescript editor en je ziet bovenin een aantal switches staan die je in kunt stellen. Dit zijn de volgende opties
<em>property taggingSwitch : “OFF”</em> - Hiermee zet je de mogelijkheid aan of uit om voor het importeren nog tags en een notitieboek aan het bestand te koppelen. Wil je de flow volledig automatiseren, dan zet je deze op OFF. Zet hem anders op ON
<em>property defaultTag : “@verwerk”</em> - Hiermee geef je een standaard tag mee die al vooraf is ingevuld als de Tagging_switch op ON staat.
<em>property theDelims : {“,”}</em> - Het scheidingsteken waarmee je in het keuzemenu de tags wilt scheiden. Dit is standaard de komma
<em>property deleteFiles : “ON”</em> - Als je de originele bestanden wilt verwijderen van je Mac na import in Evernote, dan zet je deze op ON.Onderstaande twee variabelen zijn noodzakelijk als je Tagging_Switch op OFF hebt staan. Je geeft dan een standaard notitieboek en tag(s) mee aan het bestand wat je importeert. Ik gebruik mijn standaard notitieboek “!Inbox” en de tag “@verwerk” zodat ik weet dat ik hier nog iets mee moet doen
<em>property EVnotebook : “!Inbox”
</em><em>property EVTag : {“@verwerk”}</em></li>
	<li>Sla dit bestand op in de map <strong><em>Folder Action Scripts</em></strong>. Deze is te vinden in <strong><em>/Library/Scripts/Folder Action Scripts</em></strong> (Je kunt de Library openen door in de Finder naar het Menu “Ga” te gaan en de Option (⌥) toets ingedrukt te houden. Je ziet nu de map Bibliotheek of Library verschijnen. Klik er op en in Finder zit je in de map. Het kan zijn dat je eenmalig je Administrator wachtwoord moet invoeren.</li>
	<li>Nu heb je het bestand opgeslagen in een plek die voor de Mac makkelijk bereikbaar is. Volgende stap: we maken een Watchfolder waar je bestanden in kunt zetten en aan het script verbinden.</li>
	<li>Maak in de Finder een map aan op een logische plek. Ik heb bv in de map /frank/documenten/ een map gemaakt “@Evernote”.</li>
	<li>Na het aanmaken sleep ik de map naar mijn Favorietenbalk zodat ik er altijd snel iets in kan slepen.</li>
	<li>In de Finder rechtsklik op de map en kies Voorzieningen &gt; Mapacties-configuratie<img class="aligncenter size-full wp-image-368" src="/images/2014/07/ApplescriptImport_voorzieningen.jpg" alt="ApplescriptImport_voorzieningen" width="573" height="105" /></li>
	<li>In het volgende scherm kies je het script wat je zojuist hebt opgeslagen en klik op “Wijs toe”<img class="aligncenter size-full wp-image-367" src="/images/2014/07/ApplescriptImport_kiesscript.jpg" alt="ApplescriptImport_kiesscript" width="360" height="400" /></li>
	<li>Nu zie je in het scherm links je geselecteerde map en rechts het script wat je zojuist hebt toegewezen. Zorg dat voor beide namen een vink staat. Sluit dit scherm met ⌘-W<img class="aligncenter size-full wp-image-364" src="/images/2014/07/ApplescriptImport_MapConfiguratie.jpg" alt="ApplescriptImport_MapConfiguratie" width="480" height="382" /></li>
	<li>Nu kun je een bestand in de map slepen en kijken wat er gebeurt. Afhankelijk van de switch die je hebt ingesteld bovenin het script wordt het bestand automatisch geïmporteerd of krijg je eerst een keuzemenu met tags en notitieboeken.<img class="aligncenter size-full wp-image-366" src="/images/2014/07/ApplescriptImport_KeuzeTag.jpg" alt="ApplescriptImport_KeuzeTag" width="615" height="178" /></li>
</ol>
<h2 id="extratips">Extra tips</h2>
Het script geeft je géén keuze uit je bestaande tags. Je krijgt dus geen keuzemenu met tags of automatisch aanvullen van tags te zien in het script. Je zult dus zelf de tags in moeten typen. Daarom kies ik voor een standaard tag en notitieboek en verwerk de bestanden in Evernote zelf.

Wil je wijzigen van verwerken met tags naar verwerken zonder tags of vice versa? Dan kun je het originele script openen in de map <strong><em>/Library/Scripts/Folder Action Scripts</em></strong> en weer opslaan. Het script werkt dan direct met de nieuwe instellingen. Je hoeft dus niet opnieuw het script aan je Watchfolder te koppelen.

Hou het zo simpel mogelijk voor jezelf. Mijn ervaring is dat ik liever de ondersteuning van Evernote heb via autocomplete om tags toe te voegen, dan dat ik per te importeren bestand ga nadenken welke tags er bij horen. Verzamelen gebeurt bij mij heel snel, verwerken neem ik de tijd voor en doe ik op de meest ideale plaats. Dat is in dit geval Evernote.
<h2 id="evernoteimportviaautomator">Evernote import via Automator</h2>
Vind je bovenstaande stappen te omslachtig, dan kun je het wat simpeler maken met een <a href="http://nineboxes.net/2009/09/using-mac-os-x-services-to-import-files-into-evernote/">Automator Voorziening</a>. Hier zit echter niet de mogelijkheid om tags of een notitieboek te kennen, evenmin het verwijderen van het originele bestand. Met wat extra scripting en ellebogenwerk kun je bovenstaande script hier vast in krijgen. Mocht je dit voor elkaar krijgen, dan hoor ik dat graag!
<h2>Evernote import via IFTTT en Dropbox</h2>
Op Evernotepro.nl vind je <a href="http://www.evernotepro.nl/2014/09/import-mappen-voor-de-mac/">een handige manier</a> om je bestanden automatisch in Evernote te krijgen door ze eerst in Dropbox te zetten. Handig!

(Foto: <a href="https://www.flickr.com/photos/lorenkerns/9618877636/in/photolist-5T9VRB-4hCs7F-545f2X-9TdxYo-Hqtp1-8ghssu-wz8aM-fgXPpD-7vqZJG-8cxhmn-2R97kJ-4oFqyU-fgXPyg-Ehcf-iSBg3-fDZgcS-3vWSv-6zQju-3EV35j-ruw73-fgXPHe-fgXPCH-naEdnG-jbDX2-8rmyoZ-j8juf-nAPfgP-4wpGFf-3gwa-6YnSX2-35fHr-6vCqjd-4yaASg-4LSFmf-6zQjt-6UBifF-5Wjjhs-5M1kD8-5f11nK-kS8azR-foLooV-kS88og-kS8TTM-7JUacL-2mkc9-mmmuQ-2PzNbc-5KcYps-aUsVW-w5WHZ/">Loren Kerns via Flickr</a>)
