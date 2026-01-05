file_path = "_____________TASK_______________/DEC_11_task/toyota.csv"

diesel_vech_file_path = "_____________TASK_______________/DEC_11_task/diesel_vech.csv"

fr = open(file_path, encoding="utf-8")
fw = open(diesel_vech_file_path, "w")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

diesel_vech = {v.get("model") for v in data if v.get("fuelType") == "Petrol"}

for vech in diesel_vech:

    fw.write(vech + "\n")