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
def pivo_slovar(directory, filename):
    """
    Funkcija, ki:\n
        1. prebere shranjeno datoteko \n
        2. za vsako pivo naredi slovar s podatki o pivu \n
    """
    pot_do_datoteke = os.path.join(directory, filename)
    with open(pot_do_datoteke, 'r', encoding = 'utf-8') as f:
        string_spletne_strani = f.read()
    # iskalna_zahteva = re.compile()