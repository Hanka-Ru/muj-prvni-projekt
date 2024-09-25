text = "Tento text bude zapsán do souboru."

# mode='r' -> čtení
# mode='w' -> zápis
# mode='a' -> zápis - append (přidávací)

with open('vystup.txt', mode='w', encoding='utf-8') as vystupni_soubor:
    # tady je otevreny
    print(text, file=vystupni_soubor)

# tady uz je zavreny

# tady uz je zavreny
# musím dát mód w - jinak hodí erorr

names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('uzivatele.txt', mode='w', encoding='utf-8') as output_file:
    for name in names:
        print(name, file=output_file)  # print se postara o nove radky sam

with open('uzivatele.txt', mode='w', encoding='utf-8') as output_file:
    for name in names:
        output_file.write(name + '\n')  # zapisuji primo, nove radky resim sama