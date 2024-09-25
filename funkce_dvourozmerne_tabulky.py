book = {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018}
# tabulka jako v SQL, excel
# title 	sold 	price 	year
books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
# chci vypsat ceny knížek
total_sales = 0
for item in books:
    print(item["price"])
# chci vypsat tržby za knížky
for item in books:
    print(item["price"] * item["sold"])
    total_sales = total_sales + item["price"] + item["sold"]
print(total_sales)

data = ["Python", "SQl", "Datové modelování", "Tableau"]
with open("")

