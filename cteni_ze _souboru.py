# otevírání souborů
lines = []

with open('mereni.txt', encoding='utf-8') as file:  # VELMI DŮLEŽITÝ PŘÍKAZ, PŘÍKAZ POD - CHCI HO V DATOVÉ ANALÝZE PROCHÁZET
    for line in file: # for "něco" na soubor - dostávám řádky, nezáleží na pojmenování "něco"
        lines.append(line)

print(lines)

output = []

with open('mereni.txt', encoding='utf-8') as file:
    for line in file:
        day, temp = line.split('\t')
        output.append([day, float(temp)])  # float sežral znak nového řádku - žere znaky, které se u nehodí

print(output)
# Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin, 
# což není příliš realistické. Stáhněte si textový soubor vykaz.txt, který obsahuje 12 řádků a na 
# každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.
# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz. 
# Vytiskněte tento seznam do terminálu funkcí print() abyste si ověřili, že jste soubor načetli správně.

# nejdřív si vyzkoušet vlastní seznam

# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. Spočítejte a na výstup vytiskněte 
# celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.

# tady jsem si nejdrive overil funkcnost na kratkem seznamu a pak nacetl ze souboru:
# seznam napsany natvrdo
hodiny_za_rok = ['10', '20']

# seznam nacteny ze souboru
hodiny_za_rok = []
with open('vykaz.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        hodiny_za_rok.append(radek)

# tady jsem si nejdrive overil funkcnost na kratkem seznamu a pak nacetl ze souboru:
# --- tahle cast dole se vubec nemusi menit ----

hodinovka = int(input('Zadej hodinovku: '))

celkovy_plat = 0
for hodiny in hodiny_za_rok:
    plat_za_mesic = hodinovka * int(hodiny)
    celkovy_plat += plat_za_mesic

print(celkovy_plat)

hodinovka = int(input('Zadej hodinovku: '))

celkovy_plat = 0
pocet_mesicu = 0

with open('vykaz.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        # vypocti plat za mesic
        plat_za_mesic = hodinovka * int(radek)
        celkovy_plat += plat_za_mesic

        # pocitej mesice
        pocet_mesicu += 1

print(f'celkovy plat  = {celkovy_plat}')
print(f'prumerny plat = {celkovy_plat / pocet_mesicu}')

# ukončením odsazením se uzavře soubor
# ukol 2
#Počet slov
seznam_radku = []

with open('praha.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        seznam_radku.append(radek)

radky_po_slovech = []
for radek in seznam_radku:
    list_slov = radek.split()
    radky_po_slovech.append(list_slov)

# pocty slov
for radek in radky_po_slovech:
    print(len(radek))

celkovy_pocet = 0
for radek in radky_po_slovech:
    celkovy_pocet += len(radek)

print(f'uloha ma celkem {celkovy_pocet} slov')

