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

	* država izvora ima zaradi števila glasov (in subjektivnega ocenjevanja) velik vpliv na skupno oceno piva
	* stopnja alkohola je premosorazmerna s kalorično vrednostjo piva
	* stopnja priljubljenosti (oz. skupna ocena) piva je odvisna od stila piva

## CSV datoteka

CSV datoteka vsebuje podatke o:

	* mestu, na katerem pivo je
	* imenu piva
	* izvorni pivnici
	* vrsti piva
	* stopnji alkohola
	* stevilu ljudi, ki so za to pivo glasovali
	* povprecni oceni oddanega glasu

Podatke, ki so shranjeni v .csv datoteki, sem dobil s pomočjo Python scripta beer_ratings.py, ki je prav tako shranjen v repozitoriju.