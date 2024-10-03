# Napiš skript v Pythonu, který otevře soubor alice.txt (Alice’s Adventures in Wonderland od Lewise Carrolla) - 
# ke stažení v [1] a spočítá četnost (počet výskytů) všech znaků.
kniha_cetnost_znaky = []
with open ('alice.txt', encoding='utf-8') as vystupni_soubor:
    text = vystupni_soubor.read()
print(len(text))

# Velká písmena převeď za malá a ignoruj mezery 
# a znaky nového řádku (ostatní znaky jako čárky nebo závorky zařaď do výsledku).
kniha_prevod_znaku = []
with open ('alice.txt', encoding='utf-8') as vystupni_soubor:
    for radek in vystupni_soubor:
        text = text.lower() and text.strip()
print(text)

import json

ukol1_output = []

with open ('ukol1_output.json', mode='w', encoding='utf-8') as file:
    json.dump(text, file, ensure_ascii=False, indent=4) 

