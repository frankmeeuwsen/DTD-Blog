Overstappen met Youtube naar een ander account

Voorgeschiedenis

* Google Apps account, gratis. Was tot 2012 te doen, daarna is het betaald geworden. Wel altijd blijven gebruiken. Was op eigen domein
* Dochter heeft mailadres op dat domein. Heeft een YT account op dat adres. Hier heeft ze flink wat abonnementen op kanalen, playlists en een Watch Later playlist

Wens

* Gapps verwijderen. Niet meer nodig om te gebruiken. Dus wil ik er van af. Echter, mijn dohcter wil wel graag de YT account houden.

Probleem
* Geprbeerd om het account op een ander (non-Google) mailaccount te zetten. Dat is nergens mogelijk. Vanuit YT kom je op een Aboutme.google adres terecht. Hier is het mailadres alleen te wijzigen via de admin van het domein (dat ben ik) maar in het admin deel van Google Apps kan ik nergens het mailadres wijzigen.
Het is best veel om handmatig om te zetten, met name alle playslists en de lijst van videos in haar Watch Later lijst. Handmatig dit werk doen is sowieso geen optie. 

Het idee is om via de YT API te kijken hoever ik kan komen om de abonnementen en playlists om te zetten. Het idee om via de API de lijsten en abonnementen binnen te halen als JSON bestand. Daarna wil ik deze JSON bestanden weer inlezen in het nieuwe Youtube account. Dit vereist wat tussenstappen en schakelen tussen twee accounts. 

De werkwijze is nog verre van ideaal. Bij voorkeur zou ik eerst in de twee accounts inloggen toestemming krijgen om te lezen en te schrijven. Vervolgens via een webinterface zou ik alles op kunnen halen en om kunnen zetten na een definitieve OK. Dat heb ik nu niet gedaan. Alles is via de commandline gedaan in NodeJS. Ik heb hier veel geleend van de NodeJS Quickstart die de Youtube API aanbiedt. Met name de authenticatie is vrij uitgebreid beschreven en dat helpt heel erg om van start te gaan.  

YT heeft een vrij uitgebreide API waar veel in mogelijk is, maar helaas niet alles. Zo is het bijvoorbeeld niet meer mogelijk om de Watch Later (Later Kijken) playlist te exporteren via de API. Om onduidelijke reden heeft Youtube dit in september 2017 afgesloten. Hier moet ik dus een omweg voor gebruiken. 	
Voorwerk - Youtube key en accounts klaarmaken


