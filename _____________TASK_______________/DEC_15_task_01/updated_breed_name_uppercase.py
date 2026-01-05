file_path = "_____________TASK_______________/DEC_15_task_01.py/dog_breeds.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

def breed_name_update(data):

    data["Breed"] = data["Breed"].upper()

    return data

updata_data = list(map(breed_name_update, data))

for data in updata_data:

    print(data)