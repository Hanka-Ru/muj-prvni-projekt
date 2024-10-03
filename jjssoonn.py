import json

with open(r'zavod.json', encoding='utf-8') as file:
    runners = json.load(file)

for runner in runners:
    jmeno = runner['jmeno']
    casy = runner['casy']
    ofc = casy['oficialni']

    print(f'{jmeno}: jeho cas je: {ofc}')
    print(f"{runner['jmeno']}: jeho cas je: {runner['casy']['oficialni']}")

finishers = []
for runner in runners:
    jmeno = runner['jmeno']
    casy = runner['casy']
    ofc = casy['oficialni']
    if ofc != 'DNF':
        finishers.append([jmeno, ofc])
# Výpis stříbrného medailisty (druhý v pořadí je na indexu 1)
print(finishers)
print(finishers[1])

""""" Stáhněte si soubor words.txt a zpracujte z něj výstupní soubor ve formátu JSON obsahující slovník. 
Klíče budou písmena a hodnoty seznamy slov, které začínají písmenem v klíči. Pokud na nějaké písmeno žádná 
slova nezačínají, tak ve výstupu toto písmeno nebude. Seřaďte tyto seznamy podle abecedy. Zajistěte, 
aby i klíče ve výstupním JSON souboru byly seřazeny a data byla odsazena čtyřmi mezerami pro 
lepší čitelnost člověkem."""

# Vytvořím si prázdný slovník, do kterého budu vytvářet požadovaný výstup
# Otevřu si vstupní soubor a budu ho načítat v cyklu po řádcích
# Zbavím se znaku pro nový řádek v každém slově
# Zjistím si první písmeno slova
# Pokud písmeno není klíčem slovníku, tak tento záznam vytvořím a jako hodnotu vložím seznam s tímto slovem
# Jinak slovo připojím na konec existujícího seznamu slov
# Po zpracování celého vstupu seřadím seznamy slov na všech klíčích
# Výstupní slovník zapíšu do souboru ve formátu JSON
# V dokumentaci musím najít, jak zajistím, aby byl výstup hezky odsazovaný o 4 mezery a klíče slovníku byly seřazené

import json

result = {}

with open('words.txt', encoding='utf-8') as file:
    for row in file:
        word = row.strip()
        first_letter = word[0]

        if first_letter not in result:
            result[first_letter] = [word]
        else:
            result[first_letter].append(word)

# seradime slova
for letter, words in result.items():
    words.sort()

with open('sorted_words.json', mode='w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4, sort_keys=True)

import requests

response = requests.get('https://api.kodim.cz/python-data/people')
data = response.json()

print(len(data))
clovek = data[0]
print(clovek.keys())

num_genders = {}
for person in data:
    gender = person['gender']
    if gender not in num_genders:
        num_genders[gender] = 1
    else:
        num_genders[gender] += 1

print(num_genders)
  
    