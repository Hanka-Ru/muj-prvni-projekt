#BUILT IN FUNCTION - VŠE FUKNCE, KTERÉ PYTHON MÁ
#1.1
cena_listku = 12
pocet_navstevniku = 174
predstaveni_za_mesic = 15
prijem_divadla = cena_listku * pocet_navstevniku * predstaveni_za_mesic
print(prijem_divadla)
print(f"Měsíční příjem divadla je {prijem_divadla} EUR")

#1.2
cena_listku = 12
cena_listku_student =cena_listku * 0.65
pocet_navstevniku = 174
predstaveni_za_mesic = 15
#vstupné student je 65%
prijem_divadla = (cena_listku * (pocet_navstevniku / 2) * predstaveni_za_mesic) +(cena_listku_student * (pocet_navstevniku / 2) * predstaveni_za_mesic)
print(prijem_divadla)
print(f"Měsíční příjem divadla je {prijem_divadla} EUR")

#2.1
jmeno_divadla = (" Národní" + " divadlo") * 3
print(jmeno_divadla)

cislo = "111111" * 256 + "000000" * 256 
print(cislo)

# Uložte do proměnné velikost_souboru celočíselnou hodnotu udávající počet herců a hereček, kteří hrají v divadle. 
# Do proměnné platy spočítejte celkové náklady divadla na platy, 
# víme-li, že průměrný plat v divadle je 22 392 Kč.
velikost_souboru = 30
prumerny_plat = 22392
platy = velikost_souboru * prumerny_plat
print(f"Celkové náklady divadla na platy je {platy} Kč")

zaokrouhlene_cislo = round(3.5)
print(zaokrouhlene_cislo)
zaokrouhlene_cislo = round(2.5)
print(zaokrouhlene_cislo)

cislo = 3.141592
zaokrouhlene_cislo = round(cislo, 2)
print(zaokrouhlene_cislo)

jmeno = 'Theodor Holohlávek'
delka_jmena = len(jmeno)
print(delka_jmena)

jmeno = input("Zadej své jméno: ")
prijmeni = input("Zadej své příjmení: ")
print(f"{jmeno} {prijmeni} ")
vek = input("Zadej svůj věk ")
vek = int(vek)
print(vek)