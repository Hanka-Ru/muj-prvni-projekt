from statistics import mean
import math

# Uvažujme vysvědčení, které máme zapsané jako slovník.
# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

znamky = 0
for key, value in school_report.items():
    znamky = znamky + value
print(sum(school_report.values())/ len(school_report))

# použiju funkci mean z modulu statitics, viz nahoře import
prumer = mean(school_report.values())
print(f'prumerna znamka je {prumer}')

for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)

# mel cestinu?
print('Český jazyk' in school_report)

# dostal ctyrku?? (z cehokoliv)
print(4 in school_report.values())

# jak prochazet
# for key in book.keys(): ...  # to samé jako "for key in book:" 
# for value in book.values(): ...
# for key, value in book.items(): ...


# lze použít import statistics
# pak je zápis 
# prumer = statistics.mean(school_report.values())

# Gustav je vášnivým čtenářem detektivek z našeho nakladatelství a navíc si zapisuje knihy, které přečetl. 
# Níže ve slovníku vidíme, jaké informace si eviduje - název knihy, počet stran a hodnocení od 0 do 10.
# Napiš program, který spočte celkový počet stran, které Gustav přečetl. 
# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
lits_of_books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
total_pages = 0
for book in lits_of_books: # tady je book slovník
    total_pages += book["pages"]

    if book["rating"] >=8:
        print(book["title"])
print(f"Celkem přečetl {total_pages} ")

# klíče: název, náročnost, doba, ingrediednce - v těch je další seznam položka, množství, cena
# cena je napsaná slovy
# abychom mohli sečít, nejdřív se potřebujeme dostat k hodnotám
recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}
celkova_cena = 0
# chceme projít všechny ingredience - for
for potravina in recept["ingredience"]:
    # ['batát', '1', '15 kč'], to je ta potravina
    # musím na to jít odzadu
    cena_text = potravina[2]
    # 15 kč
    cena_cislo = float(cena_text[:-3]) # úplně vše imo posldeních 3 čísel, float des. číslo
    print(cena_cislo)
    celkova_cena += cena_cislo

print(math.ceil(celkova_cena))  # zaookrouhlíme nahoru až na konci
# dá se použít i split

celkova_cena = 0
for potravina in recept['ingredience']:
    # ['batát', '1', '15 kč'],
    cena_text = potravina[2]
    # '15 kč'
    # '1012 kč'
    cena, mena = cena_text.split()  # pripravime si rovnou dve promenne
    cena_cislo = float(cena)
    celkova_cena += cena_cislo

zaokrouhlena_cena = math.ceil(celkova_cena)
print(f'Celkem zaplatime {zaokrouhlena_cena}')



