celkovy_pocet = 0

with open('praha.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        pocet_slov_na_radku = len(radek.split())
        celkovy_pocet += pocet_slov_na_radku

print(f'uloha ma celkem {celkovy_pocet} slov')

# .txt soubory se používá na jednoduché krátké soubory, xls a jiné se načítají jiným způsobem

# nejlepsi uzasne reseni
with open('praha.txt', encoding='utf-8') as soubor:
    celkovy_pocet = len(soubor.read().split())

print(f'uloha ma celkem {celkovy_pocet} slov')