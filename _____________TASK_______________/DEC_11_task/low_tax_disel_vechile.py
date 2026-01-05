file_path = "_____________TASK_______________/DEC_11_task/toyota.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

diesel_vech_with_tax = {v.get("model") : v.get("tax") for v in data if v.get("fuelType") == "Diesel"}

low_tax = min(diesel_vech_with_tax.values())

low_tax_diesel_vech = [v for v, t in diesel_vech_with_tax.items() if t ==  low_tax]

print(f"low tax diesel vechiles : {low_tax_diesel_vech}")