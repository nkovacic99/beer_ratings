import csv
import os
import re
import requests
#necessary libraries

def v_datoteko(url, directory, filename):
    """
    Funkcija, ki prebere spletno stran in jo shrani v datoteko
    """
    html_tekst = requests.get(url).text
    pot_do_datoteke = os.path.join(directory, filename)
    with open(pot_do_datoteke, 'w', encoding = 'utf-8') as f:
        f.write(html_tekst)

#figure out if a function should be more simple
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


#preverimo, da sploh lahko kličem po v bistvu .findall seznamu
#for pivo in stran_v_seznam('beer_ratings', 'spletni_html'):
#    print(pivo)

def pivo_v_seznam_slovarjev(seznam_piv):
    """
    Funkcija, ki vzame seznam html podatkov in za vsako pivo naredi slovar. \n
    Na koncu vrne seznam vseh slovarjev piv.
    """
    seznam_slovarjev = list()
    for pivo in stran_v_seznam('beer_ratings', 'spletni_html'):
        iskalna_zahteva = re.compile(
        r'<tr><td align="center" valign="top" class="hr_bottom_light" bgcolor=".*?"><span style=".*?">(?P<MESTO>.*?)'
        r'</span></td><td align=".*?" class=".*?"><a href=".*?"><b>(?P<IME_PIVA>.*?)'
        r'</b></a><span class="muted"><br><a href=".*?">(?P<PIVNICA>.*?)'
        r'</a><br><a href=".*?">(?P<VRSTA_PIVA>.*?)'
        r'</a> . (?P<STOPNJA_ALKOHOLA>.*?)'
        r'</span></td><td align="left" valign="top" class=".*?"><b>(?P<ST_GLASOV>.*?)'
        r'</b></td><td align="left" valign="top" class=".*?"><b>(?P<AVG_OCENA>.*?)'
        r'</b></td><td align="left" valign="top" class=".*?">.</td></tr>', re.DOTALL)
        beer = re.search(iskalna_zahteva, str(pivo))
        if beer == None:
            pass
        else:
            slovar_pivo = beer.groupdict()
            seznam_slovarjev.append(slovar_pivo)
    return(seznam_slovarjev)