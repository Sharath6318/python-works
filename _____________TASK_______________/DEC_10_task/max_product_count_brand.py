file_path = "_____________TASK_______________/DEC_10_task/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

brands = [b.get("Brand") for b in data]

brand_count  = {b : brands.count(b) for b in brands}

max_count = max(brand_count.values())

max_pro_brand = [b for b, c in brand_count.items() if c == max_count]

print(f"Max product brand {max_pro_brand} and product count is {max_count}")