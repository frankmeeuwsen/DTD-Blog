---
layout: post
title: GDPR en het Indieweb (deel 3) - Webmentions
date: 2018-05-12T145101CEST
excerpt:
published: true
header:
syndication: indienews
---

Met de komst van de AVG (Algemene Verordening Gegevensbescherming) ofwel de GDPR zoek ik de afgelopen dagen uit wat dit nu eigenlijk betekent voor deze site. Bij Olisto zijn we druk bezig om zowel de app als site en andere diensten goed in te richten volgens de nieuwe wetgeving. Maar wat het betekent voor deze privé website, dat wist ik nog niet zo goed. In dit deel ga ik dieper (véél dieper) in op mijn bevindingen rondom de manier van reageren op deze site. Eerder maakte ik al [een overzicht](/GDPR-en-het-Indieweb/) wat er volgens mij moest gebeuren en hoe ik [mijn statistieken heb aangepast](/GDPR-en-het-Indieweb-deel-2/). 

## Reacties op een website

Zoals recent bij de [maandelijkse #blogpraat sessie](http://www.blogpraat.com/blogpraat/blogpraat-7-mei-2018-de-privacywet-avg-en-je-blog) op Twitter al naar voren kwam, hoe je na 25 mei met je reacties om moet gaan is nog wat onduidelijk voor velen. Je verwerkt in principe gebruikersgegevens met een reactieformulier, veelal een naam en emailadres. Dus ben je verplicht om hier melding van te maken door middel van een privacyverklaring. Maar als je gebruik maakt van een gratis dienst zoals Blogger of WordPress.com, hoe zit het dan? Of als je een zelf-geïnstalleerde dienst hebt? Voor met name WordPress zijn er inmiddels voldoende plugins en oplossingen die je verder helpen. 

Natuurlijk werkt het op deze blog weer nét iets anders. Ik maak gebruik van Webmentions. Een relatief nieuwe manier van het ontvangen, versturen en weergeven van reacties op blogposts. Het bijzondere is dat er eigenlijk niets wordt opgeslagen. Dus hoe zit het dan? 

## Webmentions

Ik zal eerst proberen uit te leggen wat webmentions zijn. Hierbij krijg ik hulp van Sebastiaan Andeweg, die eerder deze week [een prima overzicht](https://seblog.nl/2018/05/09/5/de-magie-van-webmentions) schreef over webmentions. Wat me toen duidelijk werd is dat het begrip _Webmention_ uit twee delen bestaat, het protocol en de weergave.

### Webmentions Protocol
Een webmention is een manier om een site op de hoogte te stellen dat er een nieuwe binnenkomende link is van een andere pagina ergens op het web. Ik schrijf bijvoorbeeld nu over webmentions en ik link hierboven naar de post van Sebastiaan. Ik weet dat Sebastiaan webmentions ondersteunt, dus bij publicatie zal zijn site een bericht krijgen van mijn site dat ik heb gelinkt naar hem. Mijn site, of eigenlijk mijn server, of eigenlijk een dienst genaamd [Webmention Endpoint](https://webmention.herokuapp.com/) stuurt nu naar de site van Sebastiaan een notificatie in de trant van "Hey server, check het uit, Frank heeft op deze link iets geschreven over een artikel van jou wat je op deze link hebt staan." Waarbij dus de twee links staan. Een link naar deze pagina en een link naar de pagina van Sebastiaan. Dat ziet er in code als volgt uit.

![](/images/webmention-src.png)

Vrees niet, als dagelijkse gebruiker of reguliere blogger zie je hier normaal niets van. Bovenstaande is een webmention die ik ontving van het weblog van Ton Zijlstra, die in [zijn blogpost verwijst](https://www.zylstra.org/blog/2018/05/re-learning-apple-script-to-automate-some-work/) naar een artikel van mij. 
Mijn [webmention dienst](https://webmention.herokuapp.com/) bekijkt de binnenkomende link en stuurt een akkoord terug naar de site van Ton. 
Vanaf dat moment zal de reactie onder het artikel staan, zoals je zelf kunt zien onderaan [dit artikel](/dogfood-2/) van me.
Dit is in de basis wat een webmention is. Er zijn nog specifieke parameters die je mee kunt geven, bijvoorbeeld of je een reactie stuurt of slechts een "like" of er een bookmark van maakt. Er zijn allerlei manieren om het webmention protocol in te vullen. Maar in de basis is het een protocol waarbij twee sites elkaar automatisch laten weten dat ze naar elkaar linken. 

![<>](https://media1.giphy.com/media/yODVOeMxWBwBO/giphy.gif?cid=e1bb72ff5af6eda76938354e415414c3)

Zijn webmentions dan [pingbacks](https://en.wikipedia.org/wiki/Pingback)? Voornamelijk oudere bloggers kennen de pingback nog wel. Het is een vergelijkbaar mechanisme met de webmention, maar omdat het gebruik maakte van XML-RPC requests en gevoelig was voor spam-aanvallen wordt de pingback niet veel meer gebruikt. Webmentions zijn voor ontwikkelaars [eenvoudiger te implementeren](https://indieweb.org/Webmention-faq#Why_webmention_instead_of_pingback) en beter te testen. Of ze minder gevoelig zijn voor spam-aanvallen is mij vooralsnog niet bekend. Er is een anti-spam extensie in de maak genaamd [Vouch](https://indieweb.org/Vouch), maar hier is mij verder nog weinig over bekend. 

### Webmentions en social media, de backfeed
Naast de reacties van andere blogposts is er eveneens een slimme manier gevonden om reacties van Twitter, Facebook en andere netwerken slim weer te geven. Omdat deze netwerken minder open zijn dan we zouden verwachten op het open internet, bieden ze standaard geen webmentions-functionaliteit aan. Dus als ik een tweet plaats met een link naar een artikel, en iemand reageert hier op of geeft het een like, dan zie ik daar niets van bij het artikel zelf. Daar komt [Bridgy](https://brid.gy/) om de hoek. Bridgy is een dienst die ik heb gekoppeld aan mijn Twitter account. Deze service houdt mijn account in de gaten en kijkt of er reacties komen op tweets van me die links hebben naar mijn artikelen. Als die reactie er is, dan stuurt Bridgy een webmention naar [Webmention Endpoint](https://webmention.herokuapp.com/), en zo komen reactie-tweets en likes eveneens onder mijn artikel te staan. Dit wordt wel _backfeed_ genoemd. 

![<>](https://media1.giphy.com/media/iAYupOdWXQy5a4nVGk/giphy.gif?cid=e1bb72ff5af6f0024d675572516ff93c)


### Webmentions weergave

Ja ik weet het...het duizelt mij ook nog steeds hoe dit allemaal werkt. Maar goed, bovenstaande gebeurt onder de motorkap en is wel goed om te begrijpen als we het over de AVG hebben. Nog even over het tonen van de reacties en likes onder een blogpost. De weergave van webmentions is iets heel anders dan het protocol wat ik hierboven beschrijf. De webmentions die ik ontvang worden weergegeven door middel van Javascript code wat weer zijn informatie haalt uit een bestand waar alle webmentions in staan. Onder elke blogpost staat deze code. Een onderdeel van deze code is een overzicht van de ontvangen reacties en likes op de post. Deze code staat niet op mijn server, maar staat bij het [Webmention Endpoint](https://webmention.herokuapp.com/). En bij Bridgy staan dus verwijzingen naar tweets van anderen die een reactie geven op mijn blogpost. Op Twitter. Maar deze komt uiteindelijk op mijn site. 

## Aanpassingen?
Dus moet ik nu iets doen aan deze situatie? Hoe ga ik dit logisch uitleggen in een privacy policy? Hoe leg ik bijvoorbeeld uit op Twitter dat als je een tweet leuk vindt waar een link naar mijn blog in is vermeld, je avatar, link en like wordt vermeld op mijn site? Moet ik daar toestemming voor vragen? Sebastian Greger stelt zichzelf deze vragen eveneens in zijn artikel [The Indieweb Privacy Challenge](https://sebastiangreger.net/2018/05/indieweb-privacy-challenge-webmentions-backfeeds-gdpr/). Twitter is van nature een behoorlijk publieke dienst, maar als je likes ineens op andere sites komen te staan zonder jouw expliciete goedkeuring, hoe zit dat dan? Ik ben er nog niet helemaal achter, maar ik vermoed/verwacht dat Twitter dit heeft afgetikt in zijn eigen voorwaarden. 

Tevens is in de GDPR wetgeving [artikel 9.2e](http://www.privacy-regulation.eu/nl/artikel-9-verwerking-van-bijzondere-categorieen-van-persoonsgegevens-EU-AVG.htm) te vinden. Deze geeft aan dat de data (de reactie) is vrijgesteld als "de verwerking betrekking heeft op persoonsgegevens die kennelijk door de betrokkene openbaar zijn gemaakt."
Al met al denk ik dat ik redelijk goed zit met het tonen van reacties onder mijn artikelen die bewust door de maker zijn gemaakt. Of dat nu een geschreven reactie is op een eigen blog, zoals Ton doet, of een reactie op Twitter. 

Maar hoe zit het met het *verwijderen* van webmentions? Stel dat iemand aangeeft dat hij/zij het niet op prijs stelt dat de like of tweet op mijn site staat. Is deze dan te verwijderen? Nadat ik onderzoek heb gedaan en wat andere Indieweb-ontwikkelaars heb uitgevraagd blijkt het met de dienst die ik gebruik, niet mogelijk om webmentions te verwijderen. Dat is dus wel vervelend. Ik heb de vraag in het verleden nog niet gekregen, maar ik vind het wel een prettig idee dat ik in de toekomst eenvoudig aan dit soort verzoeken kan voldoen. 

Ik wil gaan kijken of ik de webmentions-functionaliteit op mijn eigen server kan implementeren. Ik blijf het technologie-tovenarij vinden maar wellicht dat een eigen implementatie me helpt in het beter begrijpen wat er gebeurt. Met een eigen webmentions-functionaliteit heb ik beter beheer over wat er wordt getoond, op welke manier en kan ik op verzoek specifieke webmentions weghalen. De broncode van de Webmentions Endpoint staat [gewoon online](https://github.com/voxpelli/webpage-webmentions) en ik kan er misschien op doorbouwen. 

## Reguliere reacties?

Maar waarom sta ik geen reguliere reacties toe zoals elk ander weblog? Ik had hier voorheen een Disqus-plugin geïnstalleerd. Het aantal reacties wat direct op dit blog binnenkwam was zo klein dat ik het niet de moeite waard vond om de plugin te laten staan. Temeer omdat Disqus weer een dienst is waar de data wordt opgeslagen, met alle mogelijke gevolgen van dien. Ik wilde eveneens wat experimenteren met webmentions en het idee dat reacties van sociale netwerken hier verschijnen vind ik wel interessant. 
Ik ben niet van plan op korte termijn weer een regulier reactieformulier te plaatsen. Ik denk niet dat het veel meerwaarde heeft, voor mij is het extra beheer en onderhoud en ik denk dat het principe van webmentions een interessante toekomst heeft. Daarom ondersteun ik deze liever. In de woorden van Dave Winer, wil je reageren, [schrijf een blogpost](http://scripting.com/2014/10/07/20YearsOfBlogging.html#aITOCF).

## Webmentions en de AVG

Maar hoe vermeld ik dit nu in het licht van het AVG? Ik heb besloten om een versimpelde versie van de webmentions-uitleg in mijn privacy policy op te nemen. Ik maak hier melding van de diensten Bridgy en Webmention Endpoint (voor nu) die interactie tussen mijn artikelen en de lezer monitoren, opslaan en weergeven. In verwacht dat dit voldoende zal zijn voor nu. De wetgeving is in mijn ogen duidelijk over de toepasbaarheid bij persoonlijke websites en bij openbaar gemaakte data/reacties door de lezer. 

## Conclusie

Webmentions zijn nog lastig uit te leggen zoals je merkt. De werking en waar de links tussen lezer en schrijver worden opgeslagen is niet altijd  even duidelijk. Het [Indieweb principe](https://indieweb.org/different) "selfdogfood" vind ik een interessante stellingname. Bouw en gebruik wat je zelf nodig hebt. Dat is een ander uitgangspunt dan wat we veelal online vinden, waar iedereen zich organiseert op grote netwerken en afhankelijk is wat de dienst ter beschikking stelt voor jou om te gebruiken. 
In het licht van de AVG/GDPR neem ik deze principes mee in de privacy statement, waarbij ik aangeef dat ik veel experimenteer en probeer op deze site, maar wel vanuit een [privacy-first designprincipe](https://en.wikipedia.org/wiki/Privacy_by_design). 

## Meer weten?

Over webmentions wordt steeds meer geschreven en gediscussieerd. In de WordPress community zijn [al plugins te vinden](https://wordpress.org/plugins/indieweb/) die webmentions ondersteunen en [andere Indieweb principes](https://indieweb.org/WordPress/Plugins) (zoals een eigen oAuth server!). Andere relevante artikelen over webmentions:

* [Seblog - De magie van webmentions](https://seblog.nl/2018/05/09/5/de-magie-van-webmentions)
* [Sebastian Greger - The Indieweb privacy challenge (Webmentions, silo backfeeds, and the GDPR)](https://sebastiangreger.net/2018/05/indieweb-privacy-challenge-webmentions-backfeeds-gdpr/)
* [Webmentions on Indieweb Wiki](https://indieweb.org/Webmention)
* [Nicolas Hoizey - So long Disqus, hello Webmention](https://nicolas-hoizey.com/2017/07/so-long-disqus-hello-webmentions.html)