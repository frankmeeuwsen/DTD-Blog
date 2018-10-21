---
layout: post
title: Mastodon, een netwerk van netwerken. Met veel vragen en twijfels.
excerpt: Een netwerk van netwerken is wat anders dan een sociaal netwerk in een silo. Wederom wat ideeën en gedachten.
published: true
tags: mastodon internet
categories: 
    - indieweb
---
De afgelopen dagen is het Mastodon universum, de Fediverse, enorm gegroeid. Door een explosie aan gebruikers uit Japan is het totaal aantal gebruikers in een relatief korte tijd tot boven de 300.000 gestegen. Ik vind dat een indrukwekkend aantal voor een decentraal, gefederaliseerd netwerk waar niet één centraal management of centraal systeem is. Tijdens de Eerste Paasdag is eveneens een nieuwe Nederlandse server gestart: [mstdn.nl](mstdn.nl). Je vindt daar een Nederlandstalige installatie van de software en een Nederlandstalige community. Toen ik daar melding van maakte op Twitter kwam al snel een discussie op gang over federatie, meerdere accounts en je eigen netwerk. Aangezien Twitter te beperkt is in de mogelijkheden om een beetje zinnig antwoord te geven, zal ik hier wat gedachten en ideeën op een rij zetten. 

## Hoe werkt de federatie op Mastodon en GNU/Social?
Ik noem hier expres beide systemen omdat ze verbonden zijn met elkaar. Er is namelijk niet "een" Mastodon universum en "een" GNU/Social universum. Door het onderliggende [oStatus protocol](https://en.wikipedia.org/wiki/OStatus) zijn ze verbonden en kun je elkaar volgen en communiceren over de netwerken heen.
Ik begrijp nog niet alles van de federatie en er zijn nog wel haken en ogen, maar ik vind het fascinerend wat er gebeurt. Al tien jaar maak ik gebruik van Twitter en Facebook en daar is veel van het huidige denken over online netwerken op gebaseerd. Maar een federatie van servers is iets wezenlijks anders en dat brengt vragen met zich mee. Geïnspireerd door [dit artikel](https://robek.world/featured/what-is-gnu-social-and-is-mastodon-social-a-twitter-clone/) van RW over GNU/Social start ik met kenmerken van Twitter (en Facebook) en hoe een federatie hier verandering in *kan* brengen.

### Twitter is een gesloten, centraal netwerk

Als ik iets post op Twitter kunnen anderen vanaf Facebook niet antwoorden en vice versa. Alleen mensen met een Twitter account kunnen antwoorden. Hetzelfde is op Facebook. Natuurlijk zit je complete vriendenkring en de buurvrouw op Facebook dus ja, dan is het logisch om daar aanwezig te zijn. Maar beiden netwerken zijn inherent gesloten. Ze hebben wel een API wat mogelijkheden biedt voor cross-posting, maar daadwerkelijke interactie tússen deze netwerken is niet mogelijk. 

### Twitter is er op gericht geld te verdienen

Niets nieuws onder de zon toch? Twitter en vooral Facebook zijn op deze aardkloot om *Maximum Shareholder Value* te bewerkstelligen. Alles wat op het platform gebeurt heeft tot doel om meer geld te verdienen voor de eigenaar. Daar hoeft niets mis mee te zijn, maar je kunt je afvragen of dat de juiste weg is voor iedereen die op dat netwerk zit. Met de enorme wurggreep van Facebook op het internet kun je je afvragen of dat wel juist is. Zoals Clay Shirky opmerkt in [een lezing](http://blogg.forteller.net/2011/think-internet/) uit 2011: 

>Het publieke domein op internet is vervangen door een commercieel domein. Een commercieel domein waar publieke gesprekken zijn toegestaan, voor zover de eigenaren van het netwerk het toestaan. 

Wat de regels van deze publieke gesprekken zijn, ligt vastgelegd in de Terms of Service van elk netwerk. Maar hoe kan één bedrijf bepalen waar wereldwijd over gesproken mag worden?

Een federatie van netwerken kán hier een antwoord op geven. Door het onderliggende protocol kan een groeiende groep servers met elkaar communiceren en kunnen individuele gebruikers zelf bepalen wat ze op welk netwerk doen. Een netwerk van netwerken. Eigenlijk zoals het internet ooit is gestart. 

Het is dus interessant om te zien hoe Mastodon nu werkt. Er zijn nog een aantal beperkingen, zo is de zoekfunctionaliteit vrijwel onwerkbaar en weet je niet welke instantie echt interessant voor je is. 
Maar als je eenmaal ergens zit kun je rondkijken op andere instanties via de *Federated Timeline*. In Mastodon is dat de meest rechtse tijdlijn die op sommige dagen niet is bij te houden door de drukte. Dat is niet zo gek, vergelijk het met de publieke tijdlijn van Twitter als die nog zou bestaan. Of de publieke tijdlijn van Facebook. Heeft díe ooit bestaan eigenlijk? 
Maar die Federated Timeline geeft je dus een beeld wat er in het complete universum speelt van GNU/Social servers. En elke Local Timeline laat je zien wat er op de server gebeurt waar je op dat moment bent ingelogd. 

## Maar toch zie ik niet alles...hoe kan dat?

Ik ben daar nog niet helemaal achter. Laat ik weer met screenshots een voorbeeld geven. Zo volg ik [@Scarbir](https://mastodon.groningendigitalcity.com/@Scarbir) die op de instantie van Groningen Digital City zit. Zie hier [zijn publieke pagina](https://mastodon.groningendigitalcity.com/@Scarbir) met de openbare toots.

![<>](/images/scarbirweb.png "Scarbir")

Echter, als ik in Mastodon zelf kijk zie ik dit

![<>](/images/scarbirmst.png "scarbirmst")

Ik zie dus niet al zijn posts in de Mastodon instantie waar ik zit. Maar op zijn publieke pagina zie ik wel alles. Net als op [deze preview-pagina](http://www.unmung.com/mastoview?url=mastodon.groningendigitalcity.com&view=federated) van diverse instanties. Hoe dat nu exact zit is me nog niet precies duidelijk. Dat dit nu niet echt betrouwbaar overkomt is me wél duidelijk. Als je iemand op een andere instantie volgt en die persoon publiceert openbare toots (wat volgens mij uit het eerste screenshot blijkt), dan mag je er van uit gaan dat deze toots in je tijdlijn terugkomen. 


## Waarom heeft elke server een eigen tijdlijn? Ik wil een *xyz* tijdlijn 

Een terechte vervolgvraag is "Ik wil alleen een Nederlandse tijdlijn", die Japanners of Fransen kunnen me gestolen worden op de Federated Timeline. Helemaal gelijk! Wil ik ook! Spoiler alert: Dat kan (nog) niet in de huidige software van Mastodon. Wederom, vergelijk het met de publieke tijdlijn van Twitter. Hier zullen net zo hard meerdere talen voorbij schieten en moet je je een weg banen voor je gelijkgestemden vindt. Daar hebben Facebook en Twitter nu prima algoritmes voor om wél direct relevante accounts voor te schotelen. Zo ver is de software bij GNU/Social nog lang niet en ik vermoed dat dat nog wel eens héél lang kan gaan duren voor het er is. De mogelijkheid om een adresboek te uploaden en te kijken wie van je vrienden al op een instantie zit? Ik betwijfel of dat ooit in een open source omgeving mogelijk gaat worden. Niet in de minste plaats vanwege de mogelijke privacy-implicaties. 

Wat moet je dan doen? Er is in elk geval al [een pagina](https://mastodon-bridge.herokuapp.com/) waar je inlogt met je Twitter account en je krijgt te zien wie van je Twitter vrienden ook op Mastodon zitten. Daar kun je al beginnen om je netwerk op te bouwen. Kijk rond bij andere accounts in hun volgers lijst of daar interessante mensen zitten. Check de lokale tijdlijn van de instantie of er boeiende gesprekken zijn waar je een bijdrage aan kunt leveren. Zoek op hashtags of er gelijkgestemden zijn. Kijk op [deze site](http://www.unmung.com/mastoview?url=mstdn.nl&view=local) waar je (voor nu) op de tijdlijnen van meerdere instanties kunt bekijken zonder er een account te hebben. 

Wat je naar mijn mening in elk geval *niet* moet doen is inloggen, achterover leunen en maar denken dat alles op Mastodon vanzelf hetzelfde wordt als op Facebook en Twitter. Als je dat wil, dan moet je op die netwerken blijven. GNU/Social is er al jaren en het zal voorlopig niet verdwijnen verwacht ik. Er zit geen verdienmodel achter voor aandeelhouders of adverteerders dus het kan op zijn eigen tempo groeien en evolueren. Dat vind ik enorm fascinerend. Ik hoef geen kopie van Facebook en Twitter. Daar heb ik Facebook en Twitter al voor. Ik ben ook niet op zoek naar een exacte kopie van het netwerk wat ik op die sites heb. Dat is in elk geval niet mijn uitgangspunt om op Mastodon actief te zijn. Voor mij gaat het om de evolutie van sociale netwerken en hoe zich dat ontwikkeld over de komende tijd. Deze stap in Federated Instances vind ik een boeiende. Dus [duik ik er](/Mastodon) graag vol in...


## Een nieuwe instantie op Mastodon, heb ik een nieuw account nodig?
Er komen elke dag nieuwe instanties op Mastodon. Moet je dan steeds een nieuw account aanmaken? Ik zou het niet doen, aangezien dat een onbegonnen zaak is. Er zullen alleen maar meer instanties komen en het is onhoudbaar om overal accounts te maken. Dus nee, doe dat niet. Er is behoefte aan overzicht van instanties en een vorm van vertrouwen dat je bent wie je bent. Ik schreef al eerder over [je identiteit](/Identiteit-op-Mastodon/) op Mastodon, met een aantal tips om je eigen identiteit in elk geval een beetje veilig te stellen. Maar weet dat iedereen op elke instantie een account kan maken onder jouw naam. 

Er zijn verschillende reden om meerdere accounts aan te maken. Ze hebben vooral te maken met je eigen identiteit en wie je wilt zijn online. Een paar screenshots van de antwoorden die ik kreeg op Mastodon hierover.

![<>](/images/accountswitch.png "account")

![<>](/images/nolan.png "account")

![<>](/images/losseidentiteit.png "losseidentiteit")
(Lees zeker [de conversatie onder deze toot](https://toot.cafe/@nolan/23277)!)

![<>](/images/james.png "James")

Met een Mastodon account op een instantie kun je dus al anderen volgen op andere instanties en je kunt als je wilt meerdere identiteiten aannemen in de Fediverse. Het is niet iets waar *ik* nu direct behoefte aan heb. Aan de andere kant, er zijn een aantal Facebook groepen waar ik wat actief ben op gebied van muziek. Daar heb ik het over andere onderwerpen dan op een publieke tijdlijn. Een aparte instantie zou hier interessant voor kunnen zijn, maar de vraag is inderdaad of het opweegt tegen alle losse inlogaccounts. Het is de vraag of er a la Twitter een oplossing komt als Tweetdeck en Hootsuite om in één omgeving meerdere accounts te beheren. Dat kan het gebruik van Mastodon en federated instanties een nieuwe *boost* geven vermoed ik.

## Waarom kan ik niet één overkoepelend account hebben voor meerdere instanties?

Omdat het er nog niet is. De software is nu zo geschreven dat je voor elke nieuwe instantie een apart account nodig hebt. Ik denk dat dit voor het gros van de huidige gebruikers geen probleem is, wellicht dat ze 2 tot 3 identiteiten hebben. Uitzonderingen daargelaten...

![<>](/images/rw.png "RW")

Maar ik blijf bij mijn standpunt, als je gaat zoeken en rondklikken op het netwerk en de tijdlijnen kom je vast wat interessante mensen tegen. Meer en meer gebruikers doen een "[\#introduction](https://mastodon.social/tags/introduction)" post waarin ze via hashtags laten weten waar hun interesses liggen. Zoek op de hashtags van je eigen interesse en kijk wie je tegenkomt. Het maakt dan niet uit op welke instantie die ander zit. Ga ze volgen, ga de conversatie aan. Wellicht is het interessant en ontmoet je meer mensen. Op welke instantie dat ook mag zijn. Zo werkt het protocol en dat biedt mogelijkheden om buiten de silo van je eigen netwerk te kijken en te communiceren. En ja, er zal vast een Hootsuite-achtige oplossing komen om met een hoofdaccount andere accounts te volgen. Ik vraag me wel af of dit een top prioriteit is van de ontwikkelaars. Wederom, als je een kopie zoekt van je Facebook of Twitter netwerk dan kom je op Mastodon erg bedrogen uit. Je zult er zelf wat werk in moeten steken. Wie weet wat het oplevert. 

## Waarom is een federatie nu zoveel beter dan bijvoorbeeld Facebook of Twitter?

Clay Shirky sprak al in 2011 [zijn zorgen](http://blogg.forteller.net/2011/think-internet/) over de dominantie van Facebook. In het verleden zagen we hoe een steeds beter netwerk het oude overname. Van Friendster naar MySpace naar Facebook. Hyves heeft hier natuurlijk voor ons Nederlanders een speciale plaats. Maar sindsdien is er niet meer een nieuw netwerk waar al je vrienden weer een account maken en waar iedereen naar verhuisd. Niet in de mate zoals dat bij voorgaande netwerken gaat. De macht van Facebook is té groot. 

<iframe width="853" height="480" src="https://www.youtube.com/embed/UP7Fuo-0Xgk?rel=0" frameborder="0" allowfullscreen></iframe>

Er zullen altijd niche-netwerken zijn die kleinere groepen mensen bedienen. Maar die zullen het nooit winnen van Facebook vanwege de schaalgrootte. Sterker nog, Facebook wil die kleinere netwerken naar zich toe halen. Lees het manifesto ["Building Global Community"](https://www.facebook.com/notes/mark-zuckerberg/building-global-community/10103508221158471/?pnref=story) van Mark Zuckerberg en hou in je achterhoofd dat Facebook er is om veel geld te verdienen voor en met adverteerders. Facebook is er primair *niet* om een lokale community te ondersteunen en op te bouwen. Hoe kan één gecentraliseerd bedrijf met zoveel invloed en zoveel data (jouw social graph) de beste oplossing zijn voor elke community denkbaar op de wereld? Dat is niet alleen onmogelijk, het kan oprecht gevaarlijk zijn. Eén centraal westers bedrijf kan gewoonweg niet een "Global Community" bouwen waarin de stem van de adverteerder harder spreekt dan die van de gebruiker. [Een diepere analyse](https://stratechery.com/2017/manifestos-and-monopolies/) van het manifesto vind je bij Stratechery. Zeer de moeite waard als je hier meer over wilt weten.

Wordt Mastodon dan de grote opvolger van Facebook en Twitter? Nee. Daar geloof ik niet in. Maar waar ik wel in geloof is dat een vuurtje wat al jaren brandt (het GNU/Social netwerk en oStatus) wat groter is geworden. Als de omstandigheden goed zijn, als Twitter een flinke steek laat vallen naar haar gebruikers of als Facebook het middelpunt is van een groot beveiligingslek, dan denk ik dat de *federated instanties* een goede kans maken om de plaats in te nemen. Maar het zal niet vanzelf gaan en het zal niet makkelijk zijn. De huidige groep ontwikkelaars zal nog een flinke stap moeten zetten om Mastodon of de opvolger betrouwbaar, doorzoekbaar en benaderbaar te maken. 

Vragen?

Wil je meer weten over Mastodon? Lees dan mijn andere artikelen op deze blog:

* [Waarom is Mastodon zo leuk voor me?](/Mastodon/)
* [Identiteit op Mastodon](/Identiteit-op-Mastodon/)
* [Redesign de Mastodon federatie!](/Redesign-de-Mastodon-federatie/)
* [Hoe werkt het volgen in de GNU Social universe?](/RemoteFollow/)