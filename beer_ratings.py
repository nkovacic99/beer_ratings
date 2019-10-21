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

print(piva_v_seznam_slovarjev(stran_v_seznam('beer_ratings', 'spletni_html')))
#ne pozabi izbrisat teh st spremenljivk
#pivi, ki ju funkcija ne zajame, sta na 75. in 248. mestu
#print(piva_v_seznam_slovarjev(stran_v_seznam('beer_ratings', 'spletni_html')))

def slovar_v_csv(seznam_slovarjev, directory, filename):
    pot_do_datoteke = os.path.join(directory, filename)
    kategorije = list()
    print(seznam_slovarjev[0].keys())
    for kategorija in seznam_slovarjev[0].keys():
        if kategorija not in kategorije:
            kategorije.append(kategorija)
    print(kategorije)
    with open(pot_do_datoteke, 'w', encoding='utf-8') as f:
        csv_writer = csv.DictWriter(f, fieldnames=kategorije, delimiter=',')
        csv_writer.writeheader()
        for slovar in seznam_slovarjev():
            csv_writer.writerow(slovar)

slovar_v_csv(piva_v_seznam_slovarjev(stran_v_seznam('beer_ratings', 'spletni_html')), 'beer_ratings', 'csv_file')