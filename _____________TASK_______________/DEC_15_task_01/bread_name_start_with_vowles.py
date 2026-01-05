file_path = "_____________TASK_______________/DEC_15_task_01.py/dog_breeds.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

vowles = "aeiouAEIOU"

filter_data = list(filter(lambda n : n.get("Breed")[0] in vowles, data))

for data in filter_data:

    print(data, "\n")