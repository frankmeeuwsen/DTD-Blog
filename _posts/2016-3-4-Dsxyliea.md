---
layout: post
category : Programming
tags : [dyslexia, typoglycemia, Javascript]
title: Dsxyliea
---

Ik kwam [deze site](http://geon.github.io/programming/2016/03/03/dsxyliea) tegen waar haarfijn wordt uitgelegd hoe dyslexie werkt. Via Twitter kwam de vraag om een Nederlandse tekst. Bij deze de vertaling van de originele site.

Een dyslectische vriend beschreef me eens hoe zij het lezen van een tekst ervaart. Ze *kan* wel lezen, maar het kost veel concentratie en de letters lijken rond te springen.

Ik bedacht me of het mogelijk zou zijn dat gevoel in Javascript na te bootsen voor een website. Ja dus.

Wil je je eigen versie maken? Maak dan op Github een [Fork it](https://github.com/geon/geon.github.com/blob/master/_posts/2016-03-03-dsxyliea.md) van het origineel.

> Dyslexie (uit het Grieks dys- ("beperkt") en lexis ("woord"), dus beperkt lezen; ook wel (onterecht) als woordblindheid aangeduid) is een term die in de wetenschap gebruikt wordt voor ernstige problemen met het kunnen lezen van woorden.

> Onderzoek vanuit de neuropsychologie heeft aangetoond dat er verschillende vormen van dyslexie bestaan. Deze hangen samen met specifieke problemen die men kan ondervinden bij het lezen van woorden. Dyslexie kan optreden bij kinderen als ontwikkelingsstoornis, of als gevolg van hersenbeschadiging. Kinderen die het predicaat 'dyslexie' krijgen, blijken een heterogene groep te vormen. Er kunnen problemen zijn in het herkennen van het visuele woordbeeld, of problemen in de sfeer van begrijpen van taal en klanken. De meeste dyslectische kinderen (85%) blijken daarbij niet zozeer moeite te hebben met het herkennen van het visuele woordbeeld, maar met het verbinden van een letter met een klank.

*Bron: [Wikipedia](https://nl.wikipedia.org/wiki/Dyslexie)*




<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
<script type="text/javascript">

"use strict";

$(function(){

	var getTextNodesIn = function(el) {
	    return $(el).find(":not(iframe)").addBack().contents().filter(function() {
	        return this.nodeType == 3;
	    });
	};

	// var textNodes = getTextNodesIn($("p, h1, h2, h3"));
	var textNodes = getTextNodesIn($("*"));



	function isLetter(char) {
		return /^[\d]$/.test(char);
	}


	var wordsInTextNodes = [];
	for (var i = 0; i < textNodes.length; i++) {
		var node = textNodes[i];

		var words = []

		var re = /\w+/g;
		var match;
		while ((match = re.exec(node.nodeValue)) != null) {

			var word = match[0];
			var position = match.index;

			words.push({
				length: word.length,
				position: position
			});
		}

		wordsInTextNodes[i] = words;
	};


	function messUpWords () {

		for (var i = 0; i < textNodes.length; i++) {

			var node = textNodes[i];

			for (var j = 0; j < wordsInTextNodes[i].length; j++) {

				// Only change a tenth of the words each round.
				if (Math.random() > 1/10) {

					continue;
				}

				var wordMeta = wordsInTextNodes[i][j];

				var word = node.nodeValue.slice(wordMeta.position, wordMeta.position + wordMeta.length);
				var before = node.nodeValue.slice(0, wordMeta.position);
				var after  = node.nodeValue.slice(wordMeta.position + wordMeta.length);

				node.nodeValue = before + messUpWord(word) + after;
			};
		};
	}

	function messUpWord (word) {

		if (word.length < 3) {

			return word;
		}

		return word[0] + messUpMessyPart(word.slice(1, -1)) + word[word.length - 1];
	}

	function messUpMessyPart (messyPart) {

		if (messyPart.length < 2) {

			return messyPart;
		}

		var a, b;
		while (!(a < b)) {

			a = getRandomInt(0, messyPart.length - 1);
			b = getRandomInt(0, messyPart.length - 1);
		}

		return messyPart.slice(0, a) + messyPart[b] + messyPart.slice(a+1, b) + messyPart[a] + messyPart.slice(b+1);
	}

	// From https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
	function getRandomInt(min, max) {

		return Math.floor(Math.random() * (max - min + 1) + min);
	}


	setInterval(messUpWords, 50);
});


</script>
