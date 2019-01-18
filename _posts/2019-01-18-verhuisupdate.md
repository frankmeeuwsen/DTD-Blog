---
layout: post
title: Verhuisupdate
date: 2019-01-18 16:21:46 +1h
excerpt: We zijn er nog niet...
published: true
header:
categories: 
tags: 
---
Een korte update na een dagje werken met allerlei commando's, Stack Overflow lezen en Digital Ocean handleidingen volgen:

* Ik heb in elk geval een subdomein van dit domein naar een server bij [Digital Ocean](https://m.do.co/c/c3654dd40a00) weten te wijzen.
* Op die server is [Ruby](https://www.ruby-lang.org/en/) al voorgeïnstalleerd, zodat de blogsoftware [Jekyll](http://jekyllrb.com/) zijn werk kan doen.
* Tevens heb ik op de server [git](https://git-scm.com/) geïnstalleerd, de versiebeheer software om nieuwe posts en andere updates te doen en te administreren.
* Ik kan met een account via SSH inloggen op de server vanaf mijn laptop. 
* Ik heb lokaal een test repository gemaakt waarmee ik updates kan sturen naar de server via git. Ik kan dus zonder gebruik te maken van diensten als Github of Gitlab direct updates sturen naar de server. 

Dat laatste is wel een behoorlijke overwinning voor me. In het afgelopen jaar heb ik veel geleerd over git en ik was me al langer bewust dat ik niet per se iets als Github hoef te gebruiken. Er is niets mis mee, maar het is een extra stap als ik nieuwe artikelen wil plaatsen. Als backup voor de code is het een prima oplossing natuurlijk. 
De manier om dit mogelijk te maken is door op de server git te activeren en een kale git-repository te maken. Op mijn laptop verander ik de `git-remote` URL's naar het adres van de git repository op mijn server. De hobbel die ik hier nog tegenkwam is het gebruik van SSH keys. Hiermee kun je zonder wachtwoorden en op een veilige(r) manier communiceren met servers. Maar het vereist wel een nauwkeurige installatie en configuratie. 

### Vastlopers
Er zijn echter een paar zaken waar ik steeds hopeloos vastloop. 

* De webserver nginx en apache zijn beiden geïnstalleerd. Ik wil het liefste nginx gebruiken, maar als ik de server herstart is apache weer actief. Dat moet ik nog uitzoeken.
* Zoals gezegd, ik kan updates van de lokale repo naar de server sturen. Daarna moet de site echter wel worden gebouwd door Jekyll. Dit lukt nog niet.
* Dit komt omdat ik ergens iets fout doe in het toewijzen van lees- en schrijfrechten van gebruikers op de server. Hoe ik dit moet oplossen, dat weet ik nog niet.
* Jekyll draait op Ruby. Voor Ruby heb je een zogenaamde versie-manager, [RVM](http://rvm.io/). Daarnaast is er nog een programma genaamd [Bundler](http://bundler.io/) om allerlei plugins voor Jekyll te installeren. Zowel Bundler als RVM krijg ik niet goed aan de praat om netjes alles te installeren en te updaten. Hier lijk ik eveneens vast te lopen in een conflict tussen gebruikersrechten. Kort gezegd, als ik bijvoorbeeld `bundle -v` doe, krijg ik een ander resultaat dan `sudo bundle -v` (1.16.1 versus 2.0.1). Maar om die twee gelijk te trekken, dat lukt me dus niet.
* Veelal zijn er problemen in het $PATH op de server. Dit is eveneens een concept wat ik nog onvoldoende in de smiezen heb om zelf veranderingen in aan te brengen en te _snappen_ wat ik doe. 

Ik ben op weg, maar het is nog een hobbelig pad, zonder duidelijke richtingsaanwijzers en de lokale inwoners spreken een taal die ik niet helemaal snap. Zo voelt het sinds een paar uur. Het begon goed, maar sinds ik op het punt ben om Ruby en Jekyll aan de praat te krijgen, loopt het krakend vast.

Ik hoop dit weekend nog wat tijd er aan te kunnen besteden. Al zal die tijd eerst zitten in nieuwe handleidingen en uitleg over gebruikers, groepen en rechten op Linux systemen. 
