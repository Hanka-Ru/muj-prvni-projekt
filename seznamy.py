jmena = ["Míša", "Eli", "Pavel", "Soustruh"]
# vypišu jméno na začátku seznamu
print(jmena[0])

jmena = ["Míša", "Eli", "Pavel", "Soustruh"]
# Zkontroluju, zda je v seznamu Pavel
if "Jirka" in jmena:
    print("Jméno je v seznamu.")
else:
    print("Jméno chybí.")

vysvedceni = [
    ["Chováni", 1],
    ["Český jazyk", 2],
    ["Anglický jazyk", 1],
    ["Matematika", 4]
    ]
# Známka z chování
print(vysvedceni[0][1])

vysvedceni = [
    ["Chování", 1], 
    ["Český jazyk", 2],
    ["Anglický jazyk", 1],
    ["Matematika", 4]
    ]
# Název předposledního předmětu
print(vysvedceni[-2][0])

# Chceme spočítat průměr známek
soucet_znamek = 0
# U pomocné proměnné si můžu zvolit jakýkoliv název
# Já si vybral řádek
for radek in vysvedceni:
    soucet_znamek = soucet_znamek + radek[1]
print(soucet_znamek/len(vysvedceni))

# Chceme vypsaat předměty, kde bychom se měli polepšit
vysvedceni = [
    ["Chování", 1], 
    ["Český jazyk", 2],
    ["Anglický jazyk", 1],
    ["Matematika", 4]
    ]
# Chceme vypsat předměty, kde bychom se měli polepšit
for radek in vysvedceni:
    # Vypiš název, pokud je známka horší než 3
    if radek[1] > 3:
        print(radek[0])
    