# Find the total number of deaths per WHO Region.

file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

for row in data:

    region = row.get("WHO Region")

    death = int(row.get("Deaths"))

    if region not in new_dict:

        new_dict[region] = death

    else:

        new_dict[region] += death

print(new_dict)