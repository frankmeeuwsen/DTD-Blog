---
layout: post
title: Een blog om Webmentions te testen
date: 2018-10-21 12:55:10 +2h
excerpt: Je kunt dit gerust negeren
published: true
header:
categories: 
tags: 
---

## Doel

Ik wil in mijn lokale omgeving zoveel mogelijk testen met het automatisch versturen van webmentions bij nieuwe blogposts. Als het lokaal werkt, kan ik het online zetten en er verder mee werken

## Uitdaging

- Lokale server: Hiervoor zet ik ngrok aan voor mijn jekyll site. Ik krijg dan een URL die via het web is te benaderen
- Test tool: Met de site [Webmention Rocks](https://webmention.rocks/) kan ik allerlei scenario's testen met mijn lokale installatie en lokale posts die niet per se online hoeven te staan
- Automatisch verzenden: Ik heb nu op Heroku een script geinstalleerd wat automatisch gaat lopen als de site opnieuw is gepubliceerd, ofwel als de pagina bij Github Pages opnieuw is opgebouwd. Dan worden namelijk nieuwe posts gecheckt en eventueel webmentions verzonden. Nog niet mijn ideale oplossing maar het werkt. Hoop ik.

## Test URL's

Nu staan [hier](https://webmention.rocks/test/1) [links](https://webmention.rocks/test/2) naar [webmention.rocks](https://webmention.rocks/test/3) die de [webmentions](https://webmention.rocks/test/4) kunnen [ontvangen](https://webmention.rocks/test/5) die ik [verstuur](https://webmention.rocks/test/6). Ik pak alleen de eerste tests. Als die werken, werkt de rest van de 23 tests ook wel. Het gaat tenslotte om verzenden. Eens zien wat er nu gaat gebeuren....

Laat ik voor alle zekerheid ook nog even [naar Ton linken](https://www.zylstra.org/blog/2018/10/solvingwebmentions/), zodat hij weer een webmention krijgt die hij mooi kan weergeven in zijn nog te ontwikkelen CSS-code :-)

## Eerste resultaten

Helaas werkte de eerste test niet. Door een probleem met de versienummers bij het originele script. Dat moest dus eerst worden gefixt. Laten we het daarom nog eens proberen nu.
