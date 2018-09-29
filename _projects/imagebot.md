---
layout: post
title: Mijn eerste bot. In Node.js en met Twitter
excerpt:
published: false
tags: code cheatsheet
categories: webtech
---

Bron: [Make a Twitter bot that random tweets images](https://botwiki.org/tutorials/random-image-tweet/)

Uitgangspunt: Ik wil leren iets in node.js te maken. Ik heb er al eens wat mee geklooid en het lijkt een leercurve te hebben die me past.

Ik begin met ```npm init``` om de eerste informatie van de node.js app te beschrijven. Dan moet ik nu dus al bedenken wat ik wil...

Wat ik zo apart vind is dat ik voor elke node.js app weer de *dependencies* opnieuw moet installeren. Dat zou toch op een meer centrale plaats moeten kunnen staan?

Ik gebruik voor deze eerste bot mijn nieuwe Twitter account [Frank Droid](https://twitter.com/FrankdroidBot). Daar ga ik dus ook de API tokens mee ophalen. Hier een handige tutorial: [How to create a Twitter app](https://botwiki.org/tutorials/how-to-create-a-twitter-app/).

Argh! Na netjes copy paste van de authenticatie tokens krijg ik dit in de terminal

MBPFM:scripts frankmeeuwsen$ node 'imagebot/server.js'
{ errors: [ { code: 215, message: 'Bad Authentication data.' } ] }

En dat bleek één spatie teveel te zijn in de config.js variabelen. Argh!

## Afbeeldingen toevoegen

OK. De volgende stap. Zorg dat de bot iets boeiends post. Animated gifs zijn altijd boeiend, dus laten we dat eens proberen...

De handleiding geeft eigenlijk kant en klare code maar het is redelijk goed te lezen en te begrijpen. Ik doe wat kleine aanpassingen zoals de tijd tussen de tweets (milliseconden, altijd een ding).

Terwijl ik de bot zijn werk laat doen zie ik een foutmelding, de images moeten maximaal 5 Mb zijn. Dus even een viertal afbeeldingen uit de map images gehaald. 

## Bots laten lopen
OK, nu de bot zijn werk doet is het belangrijkste codewerk wel gedaan. Nu is het interessant om te zien waar ik het kan hosten zodat de bot zijn werk kan blijven doen. Ik heb een NAS, maar ik merk dat ik daar node niet echt aan de praat krijg. Ik kan zien of ik mijn Raspberry Pi als botmachine kan inrichten. Dan zou ik er meer bots op kunnen hosten. Een ***botfarm***! Op Botwiki staan [verschillende mogelijkheden](https://botwiki.org/tutorials/bot-hosting/) die ik later eens ga proberen.

Inmiddels dus bij DigitalOcean al zitten klooien. Met name het kopieren van de bestanden is altijd weer een dingetje. Dit is wel [een handige bron om scp](https://kb.iu.edu/d/agye) beter te snappen. En wederom, niets is zo belangrijk als exact de juiste spaties en paden aan te geven... Iets via scp sturen naar de server gebeurt dus met

```scp -r -i /Users/frankmeeuwsen/.ssh/digitalocean /Users/frankmeeuwsen/Resilio\ Sync/@Projecten/scripts/imagebot frank@95.85.33.39:~/imagebot```