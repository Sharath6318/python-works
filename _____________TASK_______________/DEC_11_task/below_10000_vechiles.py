file_path = "_____________TASK_______________/DEC_11_task/toyota.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

budget_vechile = {v.get("model") for v in data if int(v.get('price') ) < 10000}

for vechiles in budget_vechile:

    print(vechiles)