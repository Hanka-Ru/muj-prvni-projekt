item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
key = "weight"  # vytvořím si proměnou, vložím si klíč, brání překlepům
item["price"] = 829 # úprava existující hodnoty
item["weight"] = 22 # přidání nové hodnoty
print(item["weight"])  # vypíše jednu hodnotu
# přidám do slovníku nový klíč - weight - přepíšu item a tím to přidám, mezi přidáním a úpravou není rozdíl
print(item) # vypíše všechny hodnoty
print(f"Vybraný předmět je {item["title"]}")

# chceme ověřit, že známe hmotnost - zda je klíč "weight"
if key in item:   # když vložím proměnu key, "weight" si přepíšu na key
    print(f"Hmotnost je {item[key]}")
else:
    print("Hmotnost neznáme.")

# Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka
#  z daného předmětu. Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, 
# matematiku a dějepis). Vypiš obsah slovníku pomocí funkce print().
vysvedceni = {"česky jazyk": 1, "matematika": 3, "dějepis": 2}
print(vysvedceni)

# Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. V následujícím slovníku najdeš
# tři knihy a u každé z nich je počet prodaných kusů.
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
    }
sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] += 100 # zvýšení o 100
# nebo sales["Vrah zavolá v deset"] = sales["Vrah zavolá v deset"] + 100
print(sales)

# chci vypsat názvy knih
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
    }
for key, value in sales.items(): # ve slovníku jsou dvojice, jedna proměnná nestačí. za sales .items() - musím
# dopsat, pokud procházím slovník
    print(f"Knihy {key} bylo prodáno {value} kusů.")
# sečtu počet prodaných kusů
total_sales = 0 # nesmím zapomenout
for key, value in sales.items():  # nezapomenout na .items()
    total_sales = total_sales + value
print(total_sales)
print(sum(sales.values()))  # jiná forma zápisu, musím brát values jako hodnoty
print(len(sales))  # délka slovníku


# V následujícím slovníku jsou uložena čísla lístků tomboly a příslušné výhry.
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

cislo_listu = int(input("Zadej číslo lístku: "))
if cislo_listu in tombola:
    print(f"Vyhráváš {tombola[cislo_listu]}")
else:
    print("Nevyhráváš nic")



