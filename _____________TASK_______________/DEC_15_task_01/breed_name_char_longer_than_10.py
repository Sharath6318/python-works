file_path = "_____________TASK_______________/DEC_15_task_01.py/dog_breeds.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

breed_name = [n.get("Breed") for n in data if len(n.get("Breed")) > 10]

print(breed_name)