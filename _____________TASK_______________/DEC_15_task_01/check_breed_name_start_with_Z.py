file_path = "_____________TASK_______________/DEC_15_task_01.py/dog_breeds.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

check_start_z = any(i.get("Breed").startswith("Z") for i in data)

print(check_start_z)