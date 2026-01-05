file_path = "_____________TASK_______________/DEC_11_task/toyota.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

max_milages = max([m.get("mileage") for m in data])

vech_millage = {v.get("model") : v.get("year") for v in data if v.get("mileage") == max_milages}

print(vech_millage)