file_path = "_____________TASK_______________/DEC_15_task_01.py/dog_breeds.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

len_of_breed_in_england = list(map(lambda n : len(n.get("Breed")), list(filter(lambda v : v.get("Country of Origin") == "England", data))))

print(f"Length of breed in england {len_of_breed_in_england}")