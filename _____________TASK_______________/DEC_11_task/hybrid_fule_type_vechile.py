file_path = "_____________TASK_______________/DEC_11_task/toyota.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

Hybrid_fule_type_vech = {v.get("model") for v in data if v.get("fuelType") == "Hybrid"}

print(Hybrid_fule_type_vech)