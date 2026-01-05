file_path = "_____________TASK_______________/DEC_15_task_01.py/dog_breeds.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

bread_count = 0

for b in data:

    bread_count += 1


print(f"total number of dog breeds {bread_count}")

    