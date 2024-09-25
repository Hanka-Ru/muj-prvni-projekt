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

result = {}

with open('words.txt', encoding='utf-8') as file:
    words_text = file.read()

words = words_text.split()

s


  
    