venecky = [3, 5, 2, 1, 0, 5, 9]
venecky[6] = 12 # cislovani od nuly, neděle 6, upravuji jen jednu pozici
print(venecky)

venecky = [3, 5, 2, 1, 0, 5, 9]
# výpis hodnot za všední dny, od indexu 0 do indexu 0 1 2 3 4)
# na jakém indexu začínám : první index, který ve výběru nechci
print(venecky[:3])  # vypíše 3 čísla, pokud do první pozice nanapíšu nic, bere jako nulu

venecky = [3, 5, 2, 1, 0, 5, 9]
# výběr od soboty do neděle
print(venecky[5:])  
# pokud za dvojtečku nic nedám, tak to bere jako konec seznamu

# chci vypsat poslední 3 hodnoty a nevím, kolik hodnot mám v seznamu - UZITECNÉ POKUD JE HODNĚ DAT
# PODÍVÁM SE NA ZAČÁTEK NEBO NA KONEC
print(venecky[-3:])

# chci pondělí, páte a sobotu
venecky = [3, 5, 2, 1, 0, 5, 9]
print(venecky[:2] + venecky[4:6]) # + spojí seznamy dohromady, nesčítá
print(sum(venecky))  # jde ze závorke uvnitř ven
print(len(venecky)) 
print(sorted(venecky)) # seřadí
print(sorted(venecky, reverse=True)) # seřadí sestupně

# funguje i na textový seznam, počítá i mezery
lekce = "czechitas digitální akademie python"
print(lekce[-6:]) # posledních 6 znaků

inzerat = "Na této pozici budete využívat Python a SQL"
# Je v řetezci inzerát slovo Python
# if co hledam, in kde hledam
if "Python" in inzerat:  # Záleží na velikosti písmen
    print("Jdu se přihlásit")

# cvicení
pohyby = [1200, -250, -800, 540, 721, -613, -222]
# Vypište v pořadí třetí pohyb z uvedeného seznamu.
print(pohyby[2])
# Vypište všechny pohyby kromě prvních dvou.
print(pohyby[2:])
# Vypište kolik je všech pohybů dohromady.
print(len(pohyby))
# Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
print(min(pohyby))
print(max(pohyby))
# Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
print(sum(pohyby))
# Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. Sestavte v výraz (vzoreček), 
# který spočítá průměrnou hodnotu v takovém seznamu. Otestujte jej na seznamech různých délek.
s = [2, 5, 9, 11, 20]
v = sum(s) / len(s)
print(v)
# Postupujte obdobně jako v úložce Průměr, ale tentokrát sestavte výraz pro výpočet rozpětí, 
# tedy rozdílu mezi minimální a maximální hodnotou.
r = max(s) - min(s)
print(r)
# Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. 
# V takovém případě vyberte jako střed číslo blíže ke konci seznamu.
seznam = [2, 5, 9, 11, 20]
delka = len(seznam) 
print(seznam[2])
# sudý seznam
seznam = [2, 5, 11, 20]
delka = len(seznam) 
print(delka)
print(seznam[2])

inzerat = "Na této pozici budete využívat Python a SQL"
# chci převést všechna písmena na malá
# používám metodu: název_promenne.nazev_metody()
inzerat = inzerat.lower()
if "python" in inzerat:  # Záleží na velikosti písmen
    print("Jdu se přihlásit")

inzerat = "      Na této pozici budete používat Python a sql             "
# odstraníme zbytečné mezery strip - mezery před prvním písmenem a za posledním
# zjistim délku inzerátu
inzerat = inzerat.strip


dny_v_tydnu = "po,út,st,čt,pá,so,ne"
# chci převést řetězec na seznam
seznam_dny = dny_v_tydnu.split(",") # split může mít i více znaků nebo stri
print(seznam_dny)
print(len(seznam_dny))
# pro práci s daty, kde je nepořádek, někdo píše s čásrkou někdo se středníkem

# inzerat = "       Na této pozici budete využívat Python a sql       "
# Odstraníme zbytečné mezery - mezery před prvním a za posledním písmenem
# inzerat = inzerat.strip()
# Zjistíme délku inzerátu
# print(len(inzerat))
dny_v_tydnu = "po,   út, st, čt,pá,so, ne"
# Chci převést řetězec na seznam
seznam_dny = dny_v_tydnu.split(",")
# Prázdný seznam - do něj budu vkládat hodnoty
seznam_dny_bez_mezer = []
for den in seznam_dny:
    den_bez_mezery = den.strip()
    seznam_dny_bez_mezer.append(den_bez_mezery)
print(seznam_dny_bez_mezer)
print(dny_v_tydnu.split(", "))

cesta_k_souboru = ("dokumenty", "da_data", "python", "soubor.txt")
# dokumenty/da_data/projekt/soubor.txt
# chceme si vytvořit cestu, vložíme lomítko
# převádím seznam na řetězec
cesta_retezec = "/".join(cesta_k_souboru)
print(cesta_retezec)
# join spojí do seznamu s oddělovačem /

retezec_jako_prase = "  Ahoj,   já píšu  mezery děsně     nepravidelně   "
print(retezec_jako_prase)
seznam_fesak = " ".join(retezec_jako_prase.strip().split())
retezec_fesak = " ".join(seznam_fesak)
print(seznam_fesak)

# nahrazení dat - replace, můžeme nad jední řetežcem použít několikrát
text = "Lekci vede lektor Marek"
novy_retezec = text.replace("Marek", "Martin")
print(novy_retezec)

import math
# Napište program, který dostane na vstupu desetinné číslo a na výstup napíše toto číslo # zaokrouhlené 
# nejdříve nahoru, # potom dolů a potom běžným Pythonovským zaokrouhlováním.
cislo = 4.2
print(math.ceil(cislo))
print(math.floor(cislo))
print(round(cislo))

#Uložte si do proměnné jmeno svoje jméno. Pomocí volání vhodných metod jej převeďte 
#nejdříve na malá písmena a poté na velká písmena.
jmeno = "Hana Růžičková"
print(jmeno.lower())
print(jmeno.upper())

hodnoty = ['12', '1', '7', '-11']
cislo = hodnoty[2]
cislo = int(cislo) + 4
hodnoty[2] = str(cislo)
print(hodnoty)
# chyba type error -operaci mezi více hodnotami, operace není podporovaná

hodnoty = '12.1 1.68 7.45 -11.51'
hodnoty = hodnoty.split()
cislo = hodnoty[3]
cislo = float(cislo) + 0.25
print(cislo)
# rozdělím si splitem seznam, float nahradím string na float - des.číslo
hodnoty[3] = str(cislo)
hodnoty = " ".join(hodnoty)
# TypeError: sequence item 3: expected str instance, float found
# v seznamu se něco, co není řetežec







