file_path = "PYTHON-WORKS/File-operations/cart/cart_items_100.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

order_summary = {}

for o in data:

    title = o.get("title")
    qty = int(o.get("quantity"))


    if title in order_summary:

        order_summary[title] += qty

    else:

        order_summary[title] = qty

# print(order_summary)

max_value = max(order_summary.values())
min_value = min(order_summary.values())

max_order_item = []
min_order_item = []

for o, c in order_summary.items():

    if c == max_value:

        max_order_item.append(o)

    if c == min_value:

        min_order_item.append(o)


# print(f"Most order item : {max_order_item}")
# print(f"Min order item : {min_order_item}")