file_path = "_____________TASK_______________/DEC_10_task/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

Classic_categorys_items = {items.get("Category") for items in data if items.get("Trend_Status") == "Classic"}

print(f"Classic categories {Classic_categorys_items}")