import csv
import os
import re
import requests
#necessary libraries

SPLETNA_STRAN_PIV = 'https://www.beeradvocate.com/beer/top-rated/'
DIRECTORY = 'beer_ratings'
HTML_SCRIPT_FILENAME = 'spletni_html'
CSV_FILENAME = 'csv_file.csv'

def v_datoteko(url, directory, filename):
    """
    Funkcija, ki prebere spletno stran in jo shrani v datoteko
    """
    html_tekst = requests.get(url).text
    pot_do_datoteke = os.path.join(directory, filename)
    with open(pot_do_datoteke, 'w', encoding = 'utf-8') as f:
        f.write(html_tekst)

#should a function be simpler?
def stran_v_seznam(directory, filename):
    """
    Funkcija, ki:\n
        1. prebere shranjeno datoteko \n
        2. datoteko "razkosa" na več delov
    """
    pot_do_datoteke = os.path.join(directory, filename)
    with open(pot_do_datoteke, 'r', encoding = 'utf-8') as f:
        string_spletne_strani = f.read()
    iskalna_zahteva = re.compile(
    r'<tr><td align="center" valign="top" class="hr_bottom_light" bgcolor=".*?'
    r'"><span style=".*?>.*?</span></td><td align=".*?"'
    r' valign="top" class="hr_bottom_light"><a href=".*?"><b>.*?</b>'
    r'</a><span class="muted"><br><a href=".*?">.*?</a><br><a href=".*?">'
    r'.*?</a>.*?</span></td><td align="left" valign="top" class="hr_bottom_light"><b>.*?'
    r'</b></td><td align="left" valign="top" class="hr_bottom_light"><b>.*?'
    r'</b></td><td align="left" valign="top" class="hr_bottom_light">.</td></tr>', re.DOTALL)
    return(re.findall(iskalna_zahteva, string_spletne_strani))

#dve pivi preskoci --> vrne None
def piva_v_seznam_slovarjev(seznam_piv):
    """
    Funkcija, ki vzame seznam html podatkov in za vsako pivo naredi slovar. \n
    Na koncu vrne seznam vseh slovarjev piv.
    """
    seznam_slovarjev = list()
    for pivo in seznam_piv:
        iskalna_zahteva = re.compile(
        r'<tr><td align="center" valign="top" class="hr_bottom_light" bgcolor=".*?"><span style=".*?">(?P<MESTO>.*?)'
        r'</span></td><td align=".*?" class=".*?"><a href=".*?"><b>(?P<IME_PIVA>.*?)'
        r'</b></a><span class="muted"><br><a href=".*?">(?P<PIVNICA>.*?)'
        r'</a><br><a href=".*?">(?P<VRSTA_PIVA>.*?)'
        r'</a> . (?P<STOPNJA_ALKOHOLA>.*?)%' #dve pivi nimata zabeležene stopne alkohola => ju ne najde
        r'</span></td><td align="left" valign="top" class=".*?"><b>(?P<ST_GLASOV>.*?)'
        r'</b></td><td align="left" valign="top" class=".*?"><b>(?P<AVG_OCENA>.*?)'
        r'</b></td><td align="left" valign="top" class=".*?">.</td></tr>', re.DOTALL)
        beer = re.search(iskalna_zahteva, str(pivo))
        if beer == None:
            iskalna_zahteva2 = re.compile(
            r'<tr><td align="center" valign="top" class="hr_bottom_light" bgcolor=".*?"><span style=".*?">(?P<MESTO>.*?)'
            r'</span></td><td align=".*?" class=".*?"><a href=".*?"><b>(?P<IME_PIVA>.*?)'
            r'</b></a><span class="muted"><br><a href=".*?">(?P<PIVNICA>.*?)'
            r'</a><br><a href=".*?">(?P<VRSTA_PIVA>.*?)'
            r'</a>.*?'
            r'</span></td><td align="left" valign="top" class=".*?"><b>(?P<ST_GLASOV>.*?)'
            r'</b></td><td align="left" valign="top" class=".*?"><b>(?P<AVG_OCENA>.*?)'
            r'</b></td><td align="left" valign="top" class=".*?">.</td></tr>', re.DOTALL)
            beer2 = re.search(iskalna_zahteva2, str(pivo))
            slovar_pivo = beer2.groupdict()
            seznam_slovarjev.append(slovar_pivo)
        else:
            slovar_pivo = beer.groupdict()
            seznam_slovarjev.append(slovar_pivo)
    return(seznam_slovarjev)

def popravi_st_glasov(seznam_slovarjev):
    """
    Popravi vnos ST_GLASOV, da vrne število brez decimalne vejice.
    """
    for pivo in seznam_slovarjev:
        glasovi = pivo['ST_GLASOV']
        glasovi = int(glasovi.replace(',', ''))
        pivo['ST_GLASOV'] = glasovi
    return seznam_slovarjev
        
def slovar_v_csv(seznam_slovarjev, directory, filename):
    pot_do_datoteke = os.path.join(directory, filename)
    kategorije = list()
    for kategorija in seznam_slovarjev[0].keys():
        if kategorija not in kategorije:
            kategorije.append(kategorija)
    with open(pot_do_datoteke, 'w', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=kategorije, delimiter=',')
        csv_writer.writeheader()
        for slovar in seznam_slovarjev:
            csv_writer.writerow(slovar)

def main():
    v_datoteko(SPLETNA_STRAN_PIV, DIRECTORY, HTML_SCRIPT_FILENAME)
    slovar_v_csv(popravi_st_glasov(piva_v_seznam_slovarjev(stran_v_seznam(DIRECTORY, HTML_SCRIPT_FILENAME))), DIRECTORY, CSV_FILENAME)

main()