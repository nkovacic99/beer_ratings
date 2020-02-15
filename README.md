# beer_ratings
# Najbolj popularna piva na svetu
Projektna naloga pri predmetu Programiranje 1, z naslovom 'Najbolj popularna piva na svetu'.

V tej projektni nalogi bom ocenjeval piva s pomočjo podatkov, ki jih bom analiziral s strani https://www.beeradvocate.com/beer/top-rated/. Na tej spletni strani je 250 najbolj priljubljenih piv. Spletna stran je ameriška, kar pomeni, da bi bila lestvica piv v Evropi verjetno povsem drugačna. 

## Skupine, po katerih bom ločeval podatke

* ime piva
* skupna ocena (oceno lahko spreminjajo uporabniki, tako da bo zaradi velikega števila ocen navadno precej realna)
* stil piva
* število glasov
* povprečna ocena
* izvorna pivnica
* stopnja alkohola

## Hipoteze
* med 250 najbolj priljubljenimi pivi je največ piv tipa "IPA" in najmanj piv tipa "PALE ALE"
* več kot polovica piv ima več kot 7% vsebovanost alkohola
* svetlo pivo je bolj priljubljeno od temnega
* največ glasov je prejelo ameriško pivo

## CSV datoteka

CSV datoteka vsebuje podatke o:

* mestu, na katerem pivo je
* imenu piva
* izvorni pivnici
* vrsti piva
* stopnji alkohola
* številu ljudi, ki so za to pivo glasovali
* povprečni oceni oddanega glasu

Podatke, ki so shranjeni v .csv datoteki, sem dobil s pomočjo Python scripta beer_ratings.py, ki je prav tako shranjen v repozitoriju.