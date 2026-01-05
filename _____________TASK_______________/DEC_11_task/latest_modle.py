file_path = "_____________TASK_______________/DEC_11_task/toyota.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

latest_year = max([y.get("year") for y in data])

latest_model_vechile = {v.get("model") for v in data if v.get("year") == latest_year}

for vechiles in latest_model_vechile:

    print(vechiles)