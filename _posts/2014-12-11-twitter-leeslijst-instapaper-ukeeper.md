---
ID: 774
title: >
  Hoe maak je een Twitter leeslijst in
  Evernote?
author: Frank Meeuwsen
tags: evernote
post_date: 2014-12-11 10:00:16
layout: post
published: true
---
<strong>Er zijn meer wegen die naar Rome leiden. Zo is het met het maken van een leeslijst. Op je dagelijkse bezoeken aan websites, social media en mogelijk een RSS-lezer kom je zeker boeiende artikelen tegen die je op een later moment nog eens wilt herlezen of geconcentreerder wilt lezen. Ik kom dagelijks boeiende links tegen op Twitter als ik onderweg ben en op mijn telefoon kijk. Ik heb niet altijd de tijd of de energie om me te focussen op een artikel, speciaal als het een wat langer stuk is. Daarom heb ik een eigen routine gemaakt waarmee ik met één actie een compleet artikel in Evernote kan plaatsen</strong>
<!--more-->
<h2>Waarom geen Pocket, Instapaper of een andere dienst?</h2>
De eerste vraag die ik veelal krijg is waarom ik voor mijn leesmap geen aparte service gebruik zoals het uitmuntende Pocket of Instapaper. Op de achtergrond gebruik ik deze wel. Ik merk echter aan mijn eigen gedrag door de jaren heen dat “een extra plek voor spullen” bij mij averechts werkt. Mijn Pocket map zit bomvol met ongelezen artikelen, evenzo met Pinboard of eender elke andere dienst. Voor mij werkt het prettigst om één plaats te hebben waar al mijn spullen terecht komen en waar ik kan beslissen wat er mee te doen. In de realiteit kan ik vanalles in een andere app dan Evernote opslaan om er vervolgens niet meer naar te kijken
<h2>Opslaan in Evernote via Instapaper, IFTTT en uKeeper</h2>
Wat ik je nu ga uitleggen is een heel specifiek gebruikerscenario. Het gaat hier om het opslaan van artikelen die ik tegenkom op de officiële Twitterclient voor iOS. Als iemand een tweet plaatst met een link waarvan ik vermoed dat ik deze later nog wil lezen, dan gebruik ik deze routine.
Een van de voordelen van de officiële iOS Twitter client is dat je kunt opgeven welke “Read Later” app je wilt gebruiken. Je kunt hier kiezen voor Instapaper, Pocket of de ingebouwde iOS leeslijst. Ik kies voor Instapaper, maar je kunt net zo makkelijk voor Pocket kiezen.

De routine heeft de volgende stappen:
<ul>
	<li>Ik druk in de iOS Twitter client lang op een link waardoor het contextmenu tevoorschijn komt</li>
	<li>Ik kies voor “Opslaan in Instapaper”</li>
	<li>In If This Then That (IFTTT) activeert een recept waarmee voor elk geplaatst item in Instapaper een mail verstuurt</li>
	<li>Deze mail gaat naar <a href="http://www.ukeeper.com/">uKeeper</a>. Dit is een speciale dienst die op basis van links een webpagina ophaalt en de platte tekst verstuurt naar een opgegeven mailadres</li>
	<li>Ik stuur deze tekst naar mijn <a href="http://allesonthouden.nl/evernote-en-email/">eigen Evernote mailadres</a>.</li>
</ul>
<h3>Koppeling met uKeeper</h3>
Het speciale sausje zit in het laatste deel, van IFTTT naar uKeeper en naar Evernote. Dit werkt op basis van onderstaand IFTTT recept.

<a id="embed_recipe-228439" class="embed_recipe embed_recipe-l_35" href="https://ifttt.com/view_embed_recipe/228439-fulltxt-to-evernote-through-ukeeper" target="_blank"><img style="max-width: 100%;" src="https://ifttt.com/recipe_embed_img/228439" alt="IFTTT Recipe: Fulltxt to Evernote through uKeeper connects instapaper to gmail" width="370px" /></a><script src="//ifttt.com/assets/embed_recipe.js" async="" type="text/javascript"></script>Wat je als eerste doet is op <a href="http://www.ukeeper.com/">uKeeper</a> een verbinding maken tussen je eigen mailadres en je Evernote mailadres. Of je deze service vertrouwt met je mailadressen laat ik aan je eigen inschattingsvermogen. Maar zonder deze koppeling kun je niet verder. Je vult bij uKeeper je eigen mailadres in via waar de links binnenkomen en bij uitgaand je Evernote mailadres. Je kunt nu een test sturen door bv de URL van dit artikel te mailen naar uKeeper. Mail de link in het onderwerp naar drops@ukeeper.com en bekijk na een paar minuten of het volledige artikel in Evernote staat. Het kan zijn dat je Evernote handmatig moet synchroniseren om hem eerder binnen te krijgen. Als dat werkt kun je verder gaan verfijnen met IFTTT.

<h3>IFTTT recept als de pijpleiding</h3>

In IFTTT kun je <a href="https://ifttt.com/recipes/228439-fulltxt-to-evernote-through-ukeeper">dit recept</a> gebruiken als uitgangspunt voor je eigen koppeling. Hier ga ik er wel van uit dat je Gmail gebruikt. Doe je dat niet, kijk dan onderaan dit artikel voor een alternatief. Je stuurt de mail altijd naar <em>drop@ukeeper.com</em>. Je hebt nu de mailactie geautomatiseerd die je zojuist handmatig uitvoerde. Test het nog eens door een URL in Instapaper in te voeren. Wacht zo’n 15 minuten, omdat IFTTT maar eens per kwartier draait. Mijn routine is om de artikelen in mijn standaard notitieboek te laten binnenkomen. Zo kan ik in mijn dagelijkse routine zelf beslissen of het artikel inderdaad de moeite waard is om te lezen en de gepaste actie ondernemen: Opslaan in mijn leeslijst-notitieboek voor later, verwijderen of opslaan in een specifiek project-notitieboek en een actie aanmaken om het binnenkort te lezen.

<h3>Labels en notitieboeken</h3>

Je kunt je recept in IFTTT nog verder configureren door bestaande labels en notitieboeken in het onderwerp te zetten. De onderwerpregel wordt dan iets als <em>{{URL}} @leesmap #lezen</em>. Let wel op dat je hier een bestaand notitieboek en label gebruikt.

<h3>Overal opslaan in Instapaper</h3>

Het mooie is dat deze routine niet alleen werkt op Twitter maar altijd als ik iets opsla in Instapaper. Of ik nu Twitter gebruik, de Chrome extensie of een willekeurige andere wijze, alles wat ik in Instapaper opsla gaat automatisch naar Evernote met het volledige artikel.

<h3>Alternatief voor non-Gmail</h3>

Gebruik je geen Gmail? Dan is er een alternatief. Namelijk het recept om tweets die een ster geeft, automatisch te mailen naar uKeeper. <a id="embed_recipe-228446" class="embed_recipe embed_recipe-l_72" href="https://ifttt.com/view_embed_recipe/228446-send-interesting-articles-from-twitter-to-evernote-via-ukeeper-fulltxt" target="_blank"><img style="max-width: 100%;" src="https://ifttt.com/recipe_embed_img/228446" alt="IFTTT Recipe: Send interesting articles from Twitter to Evernote via uKeeper (fulltxt) connects twitter to gmail" width="370px" /></a><script src="//ifttt.com/assets/embed_recipe.js" async="" type="text/javascript"></script>

Misschien is deze manier nog sneller voor je, omdat dit weer overal in Twitter werkt. Maar het nadeel is dat je dan geen Instapaper koppeling hebt die je overal kunt gebruiken. Of doe net als ik en gebruik ze beiden!
<h2>Maar het kan toch ook anders?</h2>
Natuurlijk. Je kunt deze actie doen via Pocket, je kunt Zapier gebruiken, je zou een Yahoo Pipes kunnen maken, Pinboard als opslagmedium gebruiken of een eigen script schrijven en periodiek laten lopen. Mijn artikel begint niet voor niets met “Er zijn meer wegen die naar Rome leiden” en ik weet dat jullie je eigen routine hebben om dit mogelijk te maken. Ik ben er wel benieuwd naar dus laat van je horen in de reacties of op Twitter.

(Foto: <a href="http://startupstockphotos.com/">Startupstockphoto</a>)
