file_path = "_____________TASK_______________/DEC_02_task/cart_items_100.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

products = [product.get("title") for product in data]

product_count = {p : products.count(p) for p in products}

print(product_count)        