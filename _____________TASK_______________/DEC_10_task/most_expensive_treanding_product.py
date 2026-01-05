file_path = "_____________TASK_______________/DEC_10_task/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv 

reader = csv.DictReader(fr)

data = [data for data in reader]

max_trending_item_price = max([float(p.get("Price(USD)")) for p in data if p.get("Trend_Status") == "Trending"])

category_price_treanding = {float(c.get("Price(USD)")) : c.get("Category")  for c in data if c.get("Trend_Status") == "Trending"}

max_price_trending_item = [c for p, c in category_price_treanding.items() if p == max_trending_item_price]

print(f"Highest rate trending product {max_price_trending_item} Rate {round(max_trending_item_price)}")

