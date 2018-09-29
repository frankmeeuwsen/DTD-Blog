---
layout: post
title: Hoe werken Webmentions? 
excerpt: Wat zijn Webmentions en waar zijn de comments en omekot wat nu?
published: true
header: webmentions.jpg
categories: indieweb
tags: webmentions indieweb jekyll
---

Er was ooit een tijd dat we geen sociale netwerken hadden. Ja lieve kinders, opa gaat weer vertellen....  
In de begindagen van het online publiceren, de blogosfeer, waren de gesprekken rondom blogposts en artikelen voornamelijk te vinden rondom de individuele sites in de reactiepanelen. Natuurlijk gebeurt dat nog steeds, maar we kunnen niet ontkennen dat een aanzienlijk deel van de conversaties is verplaatst naar sociale netwerken.

Je hoeft niet te kniezen om dat feit, het is nu eenmaal zo. En laten we eerlijk zijn, op andere sites als Reddit en Twitter ontstaan net zo goed geweldige _threads_ rondom een blogpost. Het is alleen jammer dat je er voor naar andere plaatsen moet gaan om ze te lezen. Je zorgvuldig geschreven artikel krijgt zeker wel aandacht en liefde van je fans, maar niet op de plek waar je het hebt gepubliceerd. De conversatie woedt hevig op andere plaatsen terwijl je eigen reactiepanelen stil blijven.

In het verleden is al eens getracht om met name de Twitter reacties onder te brengen in de standaard reactiepanelen van blogsoftware. Ik meen dat in de Wordpress community hier wat mee is geëxperimenteerd en er zijn wat start-ups die pogingen hebben gewaagd.

## Webmentions are coming!

Webmentions zijn een [W3C Recommendation][1] sinds begin 2017 en deze technologie probeert om reacties van andere online plaatsen onder te brengen bij jouw artikel. De blogveteranen kennen wellicht nog de Pingback en Trackback, die ooit door Movable Type is geïntroduceerd. In Wordpress zit de functie nog, maar het hele systeem van de Pingback is [nogal vervuild][2] door spammers.   
Webmentions trachten dit probleem te omzeilen. Het werkt in de basis als volgt. Sorry voor de fanboy uitleg, past wel een beetje bij de kop van deze paragraaf:

1. Arya post een blog
2. Sansa heeft een reactie en ze post een eigen blog die linkt naar Arya
3. De blogsoftware van Sansa ziet de link en haalt de post op bij Arya, waar in de broncode het _Webmention Endpoint_ van Arya staat
4. De blogsoftware van Sansa stuurt een notificatie naar het endpoint.
5. De blogsoftware van Arya pikt de blogpost op van Sansa om te verifiëren dat de link écht bestaat. Daarna zal de reactie van Sansa bij de post van Arya worden geplaatst

Doordat Arya als uitgever van de originele post een notificatie krijgt van een nieuwe post die naar haar linkt, kan ze alle reacties verzamelen en tonen bij de originele post. Of nog filteren op bepaalde kwaadwillende URL's of spam en die verwijderen en op een _blacklist_ zetten.

Welnu, in bovenstaande is het Sansa die een _blogpost_ schrijft als reactie op Arya. Maar Webmentions kunnen even zo goed om gaan met Likes, reposts en retweets. 

## De brug tussen blogs en social
Jazeker... zoals je al ziet op [eerdere blogposts][3] kunnen Webmentions de reacties opvangen van Twitter die komen op tweets waar de post in is gelinkt. Dat kan zijn omdat ik het zelf op Twitter heb gezet óf omdat iemand anders mijn blogpost linkt en daar weer likes en reacties op komen. 
Twitter, Facebook, Instagram, ze zouden in een weekend de webmentions kunnen ondersteunen verwacht ik. Helaas doen ze dat nog niet, maar dat deert niet. Het internet klust zelf wel wat in elkaar. Ik maak bijvoorbeeld nu gebruik van [Bridgy][4], een gratis dienst die als brug dient tussen de netwerken om de likes en retweets te verzamelen.

## De uitdaging
Het klinkt allemaal als halleluja als je dit hierboven leest. Fantastisch! Met een paar klikken heb je alle conversaties op het sociale web bijeen ge-sleepnet op je eigen site. Heerlijk!

Nou...

Dat valt nog vies tegen. Ik ben twee middagen bezig geweest om Webmentions te activeren op mijn site en nog is het niet helemaal lekker werkend. Ik had voorheen de gratis webdienst Disqus als reactiepaneel maar ik vond het toch allemaal wat _clunky_ en eronder gepropt. Gewoon niet zo netjes. Echter, voor Webmentions is er in mijn geval, een statische site in plaats van Wordpress, geen kant en klare plugin die ik even hoepsakee installeer en direct werkt. Ik ben met een aantal diensten in de weer geweest, waaronder al genoemde Bridgy, om ten eerste te snappen hoe het werkt en ten tweede het dan werkend te krijgen. 
Gisterenmiddag had ik de webmentions werkend. Ik zag ineens likes en reacties van Twitter onder [mijn Jim & Andy post][5] (dank je Twitter vrienden! Lobi!) Maar het ziet er niet uit. De code die ik van [de gebruikte dienst][6] kreeg is behoorlijk Spartaans. Mijn CSS en ontwerp_skills_ zijn eveneens roestig dus ik schiet op dat vlak nog niet echt op. Ik zou het liefste iets hebben als onderstaande afbeelding.

![][image-1]

Je ziet hoe de likes op deze afbeelding netjes bij elkaar staan. Dit schijnt trouwens een [_facepile_][7] te heten. Wist ik ook niet. Nu ben ik meer van het type "doe mij een plugin die de basis wegzet en ik tweak het wat" dan dat ik alles helemaal zelf moet gaan uitvogelen en met teveel proberen tot een acceptabel resultaat komt. Het moet wel leuk blijven he, dat zelf publiceren...
Ik wil nog overstappen naar een andere dienst, Webmention.io, voor het verzamelen en tonen van alle reacties en likes, maar die kreeg ik nog niet lekker aan de praat. Dus dat is voor later zorg. 

## Maar hoe reageer ik nu op deez' schrijfsels?
Ja, dat is nog wel een dingetje om uit te vogelen. Ben ik nog niet aan toegekomen. Want als je dus direct onder de blogpost een reactie wilt achterlaten, dan moet dat wel mogelijk zijn natuurlijk. Ik wil uiteindelijk wel van Disqus af. Het is een flinke brok Javascript met allerlei toeters en bellen die ik niet nodig vind.   
Ik leef echter niet in een wereld waar ik maar aanneem dat elke bezoeker op mijn site zijn eigen blog heeft en daar een reactie schrijft als eigen blog en die via Webmention naar mij stuurt. Ik word al moe van het opschrijven van die zin, laat staan dat het principe van Webmentions echt breed gedragen zal worden. Dus is het mooi als er wel een reguliere reactiemogelijkheid is. Ik heb Disqus nu nog even aan gezet. Tot ik een andere oplossing heb gevonden. 

## Hoe begin ik met Webmentions?
Om toekomstige knutselaars en web-hobbyisten al iets meer op weg te helpen, bij deze een extragratis *Digging The Digital DoorlinkLijst* met relevante documentatie en services voor Webmentions. Hij zal niet compleet zijn, vul aan waar nodig. Bijvoorbeeld door een webmention naar deze pagina te sturen...

### Webmentions linklijst
* [Wikipedia uitleg][8]
* [IndieWeb pagina][9] met veel voorbeelden en uitleg
* [W3C Recommendation][10] (serieus saaie kost, maar voor de volledigheid)
* Nicolas Hoizey legt het prima uit in de blogpost "[So long Disqus, hello Webmention][11]"
* Drew McLellan's [blogpost][12] is de inspiratie voor deze Nederlandse uitleg. Thanks Drew!
* Jeremy Keith geeft [een technische uitleg][13] over het parsen van Webmentions.
* [Bridgy][14], om de social reacties te verzamelen
* [Webmention Heroku][15] om ze op te halen en weer te geven op je eigen site.
* [Webmention.io][16] als alternatief voor de Heroku installatie
* [Wordpress][17] plugin!
* [Jekyll plugin][18] om Webmentions op je site te tonen. (Ik kreeg het niet aan de praat...)

PS: Waar ik nu echt in ben geinteresseerd is of een aantal links die hierboven staan, een webmention sturen naar hun moederschip en ik dáár weer automagisch wordt gelinkt. Zou mooi zijn als dat lukt....

Headerbeeld 
	<a style="background-color:black;color:white;text-decoration:none;padding:4px 6px;font-family:-apple-system, BlinkMacSystemFont, &quot;San Francisco&quot;, &quot;Helvetica Neue&quot;, Helvetica, Ubuntu, Roboto, Noto, &quot;Segoe UI&quot;, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:1.2;display:inline-block;border-radius:3px;" href="https://unsplash.com/@adamjang?utm_medium=referral&amp;utm_campaign=photographer-credit&amp;utm_content=creditBadge" target="_blank" rel="noopener noreferrer" title="Download free do whatever you want high-resolution photos from Adam Jang"><span style="display:inline-block;padding:2px 3px;"><svg xmlns="http://www.w3.org/2000/svg" style="height:12px;width:auto;position:relative;vertical-align:middle;top:-1px;fill:white;" viewBox="0 0 32 32"><title></title><path d="M20.8 18.1c0 2.7-2.2 4.8-4.8 4.8s-4.8-2.1-4.8-4.8c0-2.7 2.2-4.8 4.8-4.8 2.7.1 4.8 2.2 4.8 4.8zm11.2-7.4v14.9c0 2.3-1.9 4.3-4.3 4.3h-23.4c-2.4 0-4.3-1.9-4.3-4.3v-15c0-2.3 1.9-4.3 4.3-4.3h3.7l.8-2.3c.4-1.1 1.7-2 2.9-2h8.6c1.2 0 2.5.9 2.9 2l.8 2.4h3.7c2.4 0 4.3 1.9 4.3 4.3zm-8.6 7.5c0-4.1-3.3-7.5-7.5-7.5-4.1 0-7.5 3.4-7.5 7.5s3.3 7.5 7.5 7.5c4.2-.1 7.5-3.4 7.5-7.5z"></path></svg></span><span style="display:inline-block;padding:2px 3px;">Adam Jang</span></a>

[1]:	https://www.w3.org/TR/webmention/
[2]:	https://en.wikipedia.org/wiki/Pingback#Exploits
[3]:	/Jim-en-Andy/
[4]:	https://brid.gy/
[5]:	/Jim-en-Andy/
[6]:	https://webmention.herokuapp.com/
[7]:	https://indieweb.org/facepile
[8]:	https://en.wikipedia.org/wiki/Webmention
[9]:	https://indieweb.org/webmention
[10]:	https://www.w3.org/TR/2017/REC-webmention-20170112/
[11]:	https://nicolas-hoizey.com/2017/07/so-long-disqus-hello-webmentions.html
[12]:	https://allinthehead.com/retro/378/implementing-webmentions#comments
[13]:	https://adactio.com/journal/6495
[14]:	https://brid.gy/
[15]:	https://webmention.herokuapp.com/
[16]:	https://webmention.io/
[17]:	https://wordpress.org/plugins/webmention/
[18]:	https://github.com/aarongustafson/jekyll-webmention_io

[image-1]:	../images/webmentions-1.jpg