file_path = "_____________TASK_______________/DEC_11_task/toyota.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

automatic_vech = [v.get("model") for v in data if v.get("transmission") == "Automatic"]

manual_vech = [v.get("model") for v in data if v.get("transmission") == "Manual"]

count_of_automatic_vech = {v : automatic_vech.count(v) for v in automatic_vech}

count_of_manual_vech = {v : automatic_vech.count(v) for v in manual_vech}

print(f"Automatic vehicles -> {count_of_automatic_vech}")

print(f"Manual vehicles -> {count_of_manual_vech}")

