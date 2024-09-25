# Podíváme se na plánování dovolené. Protože vybráme na poslední chvíli, máme již k dispozici předpověď počasí. 
# Protože si během dovolené chceme užít turistiku po městech nebo v horách, preferujeme spíše teploty 
# do 30 stupňů. V seznamu teploty máme týdenní předpověď pro jednu potenciání lokalitu. 
# Kolik dní tam můžeme čekat teplotu do 30 stupňů?
teploty = [22, 32, 28, 30, 21, 33, 29]
ceny_ubytovani = [42000, 30000, 18000, 40000, 25000, 27000]
# definuju funkci, název můžu vymslet jakýkoliv, nutné odsazení pod ní
def najdi_hodnoty_mensi_nez(seznam, limit):
    pocet = 0 # musí se vždy udělat na zač.
    for hodnota in seznam:  # tepltoty jsme si přepsali na seznam a ten dopsali k def
        if hodnota <= limit:  # pro univezrální použití jsme si 30 přepsali na limit a limit s čárkou před dopsali do def
            pocet = pocet + 1
    return pocet  # !!!!! nutné pro fungování - funkce vrátí výsledek, pokud tam není, vrátí prázdnou hodnotu
chladnejsi_dny = najdi_hodnoty_mensi_nez(teploty, 30)
print(chladnejsi_dny)  # print mi to vypíše
if chladnejsi_dny < 2:
    print("Je tam vedro")
else:
    print("Je to ok")
# Dále uvažujeme, že nechceme utratit příliš mnoho peněz a chceme tedy v lokalitě mít několik možností 
# ubytování s cenou do 35 tisíc. V seznamu ceny_ubytovani máme ceny za několik hotelů, 
# kde mají volné místo. Kolik hotelů vyhovuje naší cenové podmínce?
# udělám funkci viz výše - definuju funkci viz výše
# JE MOŽNO POUŽÍT RETURN I PRINT, MOŽNO OBOJÍ, MUSÍ BÝT ALE PRINT NA SEBOU, RETURN UKONČUJE PŘÍKAZ, cokoli
# napíšeme pod return, nebude fungovat
levne_ubytovani = najdi_hodnoty_mensi_nez(ceny_ubytovani, 35000)
print(levne_ubytovani)

# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.
cislo_1 = int(10)
cislo_2 = int(4)
def mult(cislo_1, cislo_2):
    return cislo_1 * cislo_2
returned_value = mult(cislo_1, cislo_2)
print(returned_value)

# Převod kilometrů na míle a zpět
# Napište dvě funkce: kilometry_na_mile(kilometry) a mily_na_kilometry(mile), 
# které provedou převod mezi kilometry a mílemi.
kilometr = 3
def kilometry_na_mile(kilometry):
    return kilometr / 1.602
mile = kilometry_na_mile(kilometr)
print(mile)

# Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného 
# čísla určí měsíc narození, které vrátí jako výstup. Nezapomeň, že pro ženy je k měsíci připočtena 
# hodnota 50. 
# Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.
# fukce month_of_birth
def month_of_birth(birth_number):
        month = birth_number[2:4]
        month = int(month)
        return month % 50
print(month_of_birth("9555125899"))




def vynasob_cislo_deseti(cislo):
     cislo * 10
print(vynasob_cislo_deseti(5))

def kontrola_emailu(data):
     vystup = []
     for radek in data:
        if "@" in radek:
          vystup.append(radek)
     return vystup
emaily = [  "misa@czechitas.cz",
            "kuba@czechitas.cz",
            "soustruh@czechitas.cz",
            "jirkczechitas.cz"]
print(kontrola_emailu(emaily))


def kontrola_emailu(data):
     chyby = 0
     for radek in data:
        if "@" not in radek:
          chyby = chyby + 1
     return chyby
emaily = ["misa@czechitas.cz",
            "kuba@czechitas.cz",
            "soustruh@czechitas.cz",
            "jirkaczechitas.cz"]
print(kontrola_emailu(emaily))

     




    
