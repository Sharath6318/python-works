file_path = "_____________TASK_______________/DEC_10_task/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

for row in data:

    Gender = row.get("Gender")

    Category = row.get("Category")

    if Gender not in new_dict:

        new_dict[Gender] = {}

    if Category not in new_dict[Gender]:

        new_dict[Gender][Category] = []

    else:

        new_dict[Gender][Category].append(row)

for data in new_dict.items():

    print(data, "\n\n")


    







