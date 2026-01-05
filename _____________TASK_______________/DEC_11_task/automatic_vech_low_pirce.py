file_path = "_____________TASK_______________/DEC_11_task/toyota.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

low_price = min([p.get("price") for p in data if p.get("transmission") == "Automatic"])

automatic_vech = {v.get("model") for v in data if v.get("transmission") == "Automatic" and v.get("price") == low_price}

print(f"Automatic vehicles with low price -> {automatic_vech}")