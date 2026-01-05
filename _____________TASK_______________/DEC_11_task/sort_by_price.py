file_path = "_____________TASK_______________/DEC_11_task/toyota.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]


sorted_data_price = sorted(data, key=lambda d : int(d.get("price")), reverse=True)

print(sorted_data_price)

