# Napiš kód, který zpracuje seznam čísel a vypíše jejich součet (bez použití funkce sum())
seznam_cisel = [3, 2, 9, 2]
soucet_cisel = 0
for cislo in seznam_cisel:
    soucet_cisel = soucet_cisel + cislo
print(soucet_cisel)

# Napiš kód, který zpracuje seznam čísel a vypíše největší prvek v tomto seznamu (bez použití funkce max()).
seznam_cisel = [3, 2, 9, 2]
nejvyssi_cislo = 0
for cislo in seznam_cisel:
# je aktuální číslo větší než zatím největší číslo?
    if cislo > nejvyssi_cislo:
        nejvyssi_cislo = cislo
print(nejvyssi_cislo)

# Napiš kód, který zpracuje seznam čísel a vypíše pouze sudá čísla z tohoto seznamu.
seznam_cisel = [3, 2, 9, 2]
for cislo in seznam_cisel:
    if cislo % 2 == 0:
            print(cislo)