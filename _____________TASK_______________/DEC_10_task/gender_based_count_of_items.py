file_path = "_____________TASK_______________/DEC_10_task/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

gender = [g.get("Gender") for g in data]

for g in gender:

    if g not in new_dict:

        new_dict[g] = 1

    else:

        new_dict[g] += 1

print(new_dict)