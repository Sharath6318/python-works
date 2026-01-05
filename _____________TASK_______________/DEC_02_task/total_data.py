file_path = "_____________TASK_______________/DEC_02_task/cart_items_100.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

count = 0

for info in data:

    count += 1

print(f"total datas : {count}")

