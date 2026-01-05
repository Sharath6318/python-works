file_path = "PYTHON-WORKS/File-operations/cart/cart_items_100.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

order_summary = {}

for o in data:

    user = o.get("user")
    quantity = int(o.get("quantity"))


    if user in order_summary:

        order_summary[user] += quantity

    else:

        order_summary[user] = quantity

max_quantity = max(order_summary.values())
min_quantity = min(order_summary.values())

max_product_pur_cus = []
min_product_pur_cus = []

for u, q in order_summary.items():

    if q == max_quantity:

        max_product_pur_cus.append(u)

    if q == min_quantity:

        min_product_pur_cus.append(u)

print(f"Most product purchase customer : {max_product_pur_cus}")
print(f"less product purchase customer : {min_product_pur_cus}")

