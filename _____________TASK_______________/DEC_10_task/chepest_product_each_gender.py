file_path = "_____________TASK_______________/DEC_10_task/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

Men_product_and_price = {float(c.get("Price(USD)")): c.get("Category")  for c in data if c.get("Gender") == "Men"}

Women_product_and_price = {float(c.get("Price(USD)")) : c.get("Category") for c in data if c.get("Gender") == "Women"}


min_price_of_men_products = min(Men_product_and_price.keys())
min_price_of_Women_products = min(Women_product_and_price.keys())

cheapest_men_product = [c for p, c in Men_product_and_price.items() if p == min_price_of_men_products]
cheapest_women_product = [c for p, c in Women_product_and_price.items() if p == min_price_of_Women_products]

print(f"Cheapest Men product {cheapest_men_product}")
print(f"Cheapest Women Product {cheapest_women_product}")