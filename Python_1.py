#CTRL F5 - klavesova zkratka pro RUN
cislo = 20
print(cislo)
cena_listku = 250
pocet_osob = 3
celkova_cena = cena_listku * pocet_osob
# pokud je cena vice než 1000, dáváme slevu 10%
if celkova_cena > 1000:   # musí být dvojtečka
    celkova_cena = celkova_cena * 0.9
    print("Získáváte slevu 10%.") # f není nutný, není tam proměnná. podmínky vždy odsazené
elif celkova_cena > 500:
      celkova_cena * 0,95
      print("Získáváte slevu 5%.")
else:
        print("Bohužel nezískáváte slevu :-(")
print(f"celkova cena všech lístků je {celkova_cena} Kč.")
# formátovaný řetežec - přidat f (fstring)


