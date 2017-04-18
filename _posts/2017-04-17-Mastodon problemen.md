---
layout: post
title: De problemen met Mastodon
excerpt: Er is veel jubel over Mastodon. Maar er zijn natuurlijk problemen. Een eerste overzicht...
published: true
date: 2017-04-18 19:23
header: header-mastodonskeleton.jpg
---
Het lijkt soms of ik een grote fanboy ben voor Mastodon. Nu moet ik toegeven dat ik na twee weken nog geen genoeg krijg van het netwerk, met name omdat er steeds nieuwe ontwikkelingen zijn, er komen nieuwe instanties en er *gebeurt* iets. Er gebeurt iets substantieler dan een nieuw advertentieformaat op Facebook of een nieuwe CEO bij Twitter. 

Ja, vanuit een online-marketing-oogpunt zijn bovenstaande nieuwtjes van groot belang en ja ze interesseren me. Maar mijn intrinsieke motivatie waarom ik ooit zo dol ben geworden op dat internet, dat komt weer naar boven met Mastodon. 

Het is niet allemaal koek en ei en er is een hoop aan te merken op deze invasie van nieuwe servers. Zo kan er wel eens een server uitliggen door een typefout van de admin. Of worden de inschrijvingen tijdelijk stopgezet omdat het hobby-rackje van een amateur-devops de gangkast uit staat te roken. 

## Mastodon problemen.
Daarom vandaag een lijstje met wat problemen die nu (april 2017) op Mastodon en aanverwante diensten spelen. Mocht je hier terecht komen omdat je je inleest of je wel aan dat Mastodon moet beginnen, zeg niet dat we je niet hebben gewaarschuwd!

Ik ga proberen deze pagina up to date te houden maar ik heb een gewone baan en een leven dus word niet boos als er nog problemen staan die al opgelost zijn. Er zijn ergere dingen in de wereld.

### Verwijderen account
Kan niet. [Nog niet](https://github.com/tootsuite/mastodon/issues/109). Als je eenmaal een account hebt op een instantie dan kun je deze niet verwijderen. Je kunt individuele toots verwijderen maar je account écht verwijderen inclusief alle data is nog niet mogelijk. Dit kan ook nog wel een probleem worden omdat al je toots over de federatie worden gekopieerd en opgeslagen. Al zou er een afspraak komen om bij een ```delete``` request de toots te verwijderen, een individuele admin kan zo maar besluiten dat niet te doen...

### Meerdere accounts
De essentie van Mastodon is dat je op één instantie één account hebt. Maar omdat elke slimmerik met een server en wat vrije tijd een instantie kan beginnen, is het mogelijk om op meerdere instanties aanwezig te zijn. Dat is echter wel met steeds een nieuw account. Vergelijk het met e-mail of met Slack. Steeds een nieuw mailadres, of een nieuwe Slack inlog. 
Daar is nog geen oplossing voor en ik denk niet dat die gaat komen. Er zal zeker een app komen om meerdere instanties gelijktijdig te beheren. [Rambox](http://rambox.pro) is al zo'n app die dat kan. Maar ik verwacht dat er voor de Kerstdagen wel een Hootsuite of Buffer-achtige oplossing is voor meerdere Mastodon-accounts. 

### Vindbaarheid toots
Op dit moment kun je nog niet zoeken in de toots van je eigen account, je lokale instantie of de federatie. Je kunt *wel* zoeken op hashtags en gebruikersnamen. Maar full-text search is er nog niet. Ik heb vooralsnog geen idee of dat gaat komen.

### Vindbaarheid en betrouwbaarheid van personen
Dit is gerelateerd aan de meerdere accounts over instanties. Je kunt zoeken op gebruikersnamen en profielnamen. Maar als iemand over meerdere instanties dezelfde naam gebruikt, hoe weet je dan welk account je moet hebben? En hoe weet je of het werkelijk díe persoon is. Net als op andere online netwerken is het vrij eenvoudig om een nep account aan te maken. Hoe Mastodon dit gaat oplossen, óf ze het gaan oplossen, dat is nog onduidelijk. Tot die tijd zijn er [diverse aanwijzingen](/Identiteit-op-Mastodon/) die je zelf kunt uitvoeren om er voor te zorgen dat anderen weten welk account jouw primaire account is. 

### Verschillende aantallen toots en volgers in profielen

Hier ga ik nog een aparte post aan wijden omdat ik dit nog eens goed wil uitzoeken. Maar er zit een vreemde manier van tellen en tonen van het aantal toots en het aantal volgers en vrienden in de gebruikersaccounts. Het kan verschillen per instantie, of je kijkt via de Mastodon pagina of via de profielpagina van een gebruiker én of er al mensen op jouw instantie anderen volgen op de instantie van de andere gebruiker. Al met al, don't trust the number.

Volgt u het nog? 

### Servers verdwijnen

Het kan gebeuren. Iemand maakt een Mastodon instantie rondom een thema of subcultuur die je ligt. Je besluit er een account te nemen en je eigen *community* op te bouwen. Maar de admin van de instantie is het na een periode beu. Te veel updatewerk, te veel moderatie, te hoge kosten en te weinig opbrengsten (financieel of sociaal) en hij gooit het bijltje er bij neer. Dat kan. Dat is zijn goed recht. Maar het is wel vervelend. Hou er rekening mee dat dit kan gebeuren, met name op kleinere instanties.

### Keuze van instantie
De stress! De keuzeparadox! Met meer dan 900 servers *and counting* is het moeilijk om te kiezen. Waar zet ik mijn Mastodon-tent op? Op welke instantie is het leuk en kan ik gelijkgestemden vinden? 
Natuurlijk zul je mensen volgen op andere instanties, maar als je vrienden of collega's op dezelfde instantie zitten geeft dat toch een gevoel van *je eigen clubje*. Hoe maak je die keuze? Daar is nog geen checklist voor. Maar ik verwacht dat een slimme contentmanager een dezer dagen wel met een fraaie infographic of listicle komt om de uitleg te geven. Tot die tijd zal ik je een beetje op weg helpen (Ik ben niet slim genoeg voor die contentvolksverlakkerij)

- Check op de [Instances lijst](https://instances.mastodon.xyz/) welke naam je aanspreekt
- Kijk hoe druk het er is
- Bekijk de uptime van de server
- Check de "More info" link op de instances lijst om wellicht iets meer te leren over de instantie en de regels
- Neem al een [preview](http://www.unmung.com/mastoview?url=mstdn.nl&view=local) als mogelijk
- Maak een account en kijk het een dag aan.
- Ben niet bang om te switchen.

### Export/import van users maar niet van data
Als je wilt switchen van instantie dan kan dat. Je kunt in de accountinstellingen een export maken van je vrienden-lijst. Deze kun je weer prima importeren op je nieuwe instantie en iedereen krijgt netjes een notificatie dat je ze weer volgt op een ander account. Helaas is het (nog?) niet mogelijk om je toots mee te verhuizen. Vanwege het federatie-karakter zijn je toots verspreid over meerdere instanties en staan ze niet centraal op één server waar alles wordt geregeld. Zal dit worden opgelost? Wellicht samen met het verwijderen van je account. Op welke termijn dat is, ik durf er geen geld op in te zetten...

### Blacklist van instanties is onduidelijk

Jouw instantie-admin heeft de mogelijkheid om andere instanties te *black-listen*. Dat betekent dat de toots van die instantie niet in de federatie-tijdlijn komen van jouw instantie én dat je mensen van die instantie niet kunt volgen of een bericht kunt sturen. Dat kan vervelend zijn, zeker als admins onderling ruzie krijgen of er andere ego-oorlogjes gaande zijn. 
Op dit moment kun je nog nergens zien wie er op de blacklist van je instantie staan. Ik vermoed dat dit op korte termijn transparanter zal worden, zeker als er meer en meer instanties komen. Dit kan eveneens een kwaliteitskeurmerk worden voor instanties zodat de keuze voor nieuwe gebruikers makkelijker wordt. Dat dit is te misbruiken staat buiten kijf. Hoe we dát weer gaan oplossen, dat zullen we dan wel zien.

Dit zijn zo een paar van de lopende problemen die Mastodon op dit moment plagen en een échte grote groei nog tegenhouden. Niet dat die groei er nu niet is, maar zoals met alles in marketing: Het gaat niet alleen om de acquisitie, het gaat net zo goed om de activatie en retentie!