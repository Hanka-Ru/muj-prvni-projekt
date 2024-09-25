import requests

"""""
Jak už jsme si ověřili v lekci, datové API na adrese https://api.kodim.cz/python-data/people obsahuje seznam lidí. Napište program, který tento seznam z API stáhne a převede z formátu JSON na Python slovníky. Proveďte následující úkoly.

    Zjistěte kolik lidí celkem seznam obsahuje.
    Zjistěte jaké všechny informace máme o jednotlivých osobách.
    Zjistěte, kolik je v souboru mužů a žen."""

response = requests.get("https://api.kodim.cz/python-data/people")
people = response.json()

# 1. Zjistíme, kolik lidí seznam obsahuje
total_people = len(people)
print(f"Celkový počet lidí v seznamu: {total_people}")

# 2. Zjistíme, jaké všechny informace máme o jednotlivých osobách
if total_people > 0:
    first_person = people[0]
    available_keys = first_person.keys()
    print("Informace o jednotlivých osobách:")
    for key in available_keys:
        print(f"- {key}")

# 3. Zjistíme, kolik je mužů a žen
men_count = 0
women_count = 0

for person in people:
    if person['gender'] == 'Male':
        men_count += 1
    elif person['gender'] == 'Female':
        women_count += 1

print(f"Počet mužů: {men_count}")
print(f"Počet žen: {women_count}")


# Na adrese https://svatky.adresa.info/json najdete API, které vám odpoví, kdo má dneska svátek.
response = requests.get("https://svatky.adresa.info/json")
svatky = response.json()
