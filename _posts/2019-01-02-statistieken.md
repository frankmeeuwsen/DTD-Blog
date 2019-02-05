---
layout: post
title: De eerste blogstatistieken van 2018
date: 2019-01-02 22:05:10 +1h
excerpt:
published: true
header:
category: bloggen
tags: 
- bloggen
- statistiek
---
Als je mijn blog wat vaker bezoekt zal het je niet zijn ontgaan dat ik in 2018 meer heb geschreven dan in de jaren voorafgaand. Als ik een volledig CMS zou hebben met allerlei plugins en extra's, dan kon ik waarschijnlijk in een minuut of wat de volledige statistieken van het afgelopen jaar opvragen. Maar omdat ik zo eigenwijs ben om alles zelf te willen doen met Jekyll en tekstbestanden, moest ik wederom zelf aan de slag om uit te vogelen hoeveel ik nu eigenlijk heb geschreven. 

## Shell scripts
Ik ben van nature geen programmeur, maar de afgelopen maanden heb ik me wel wat principes en werkwijzen eigen gemaakt die helpen bij elke programmeertaal. Het bepalen van een strategie hoe ik tot een bepaalde uitkomst wil komen (in dit geval, een lijstje met het aantal blogposts per jaar), het principe van het _loopen_ over een lijst met bestanden en het werken met variabelen. Elke programmeertaal heeft zijn unieke schrijfwijze en eigenaardigheden, maar veel principes en uitgangspunten zijn hetzelfde. Met wat basiskennis van de commandline en de juiste zoektermen kon ik in een korte tijd een eigen script schrijven wat me al direct inzicht geeft in mijn schrijfgedrag over de afgelopen jaren. 

Al mijn blogposts staan in één directory op mijn harde schijf als Markdown bestanden. Al deze bestanden hebben in de bestandsnaam hetzelfde patroon: yyyy-mm-dd-bestandsnaam.md. Elk bestand met een blogpost begint dus met het jaartal van publicatie. Daarmee is het al relatief eenvoudig om een lijstje met aantallen te krijgen.


        #!/bin/bash
        jaar=2009
        while [ "$jaar" -lt 2019 ]; do
                echo "$jaar had $(ls $jaar-*.m*d* | wc -l ) posts"
                jaar=$((jaar + 1))
        done

Ik loop over alle jaartallen tussen 2009 en 2019. De truc zit in het stukje `$(ls $jaar-*.m*d* | wc -l )`. Wat ik hier doe is eerst in de directory zoeken op bestanden die beginnen met het dan geldende jaartal, bijvoorbeeld 2017 en eindigen op .md of .markdown, de bestandsformaten voor Markdown bestanden. Vervolgens lees ik simpelweg het aantal regels wat uit die zoektocht komt en dat geef ik weer. `wc -l` staat voor WordCount met de optie het aantal regels (lines). Daar komt dan uit.

        2009 had       58 posts
        2010 had      178 posts
        2011 had       79 posts
        2012 had       81 posts
        2013 had      190 posts
        ls: 2014-*.m*d*: No such file or directory
        2014 had        0 posts
        ls: 2015-*.m*d*: No such file or directory
        2015 had        0 posts
        2016 had        3 posts
        2017 had       84 posts
        2018 had      237 posts

Het shell script is verre van perfect, het mist bijvoorbeeld foutafhandeling voor 2014 en 2015 en de uitlijning van de uitkomst is niet ideaal. Maar het doet zijn werk en dat is het belangrijkste voor nu. 

## Blogstem
Verder is het goed om te weten dat er nog veel blogposts missen uit het verleden. In 2009 startte ik met een blog als zelfstandig ondernemer maar dat eindigde in 2013. Dat is dus wel compleet. In 2014 en 2015 schreef ik op verschillende plekken, waar ik niet een volledig archief van heb. Of in elk geval niet goed ontsloten op deze plek. Dat geldt eveneens voor de jaren 2000 - 2008. Dat is zeker nog iets voor de toekomst, maar voor nu werkt bovenstaande prima om een beeld te krijgen. In 2018 heb ik duidelijk meer geschreven dan in de jaren er voor. Zo was 2013 nog wel productief, evenals 2010, maar vorig jaar schiet er wel uit. 

Ik vind het prettig om te zien dat ik ondanks drukke werkzaamheden en een gezin toch nog de tijd kan vrijmaken om voor mezelf te schrijven. Om mijn blog-stem weer terug te vinden en mijn eigen ideeën weer een plek te geven en verder te laten ontwikkelen. Ik heb eveneens [een eigen archief](https://twitter.frankmeeuwsen.com) van al mijn tweets. Ik vind het wel een leuk project om die eens langs de lat te leggen en te zien welke trends in getallen daar in is te vinden. Maar dat is een project voor een andere rustige vakantiedag.
