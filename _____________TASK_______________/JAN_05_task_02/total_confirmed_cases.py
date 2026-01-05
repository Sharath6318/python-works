# Group data by WHO Region and calculate total confirmed cases per region.

file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

for row in data:

    region = row.get("WHO Region")

    confirmed_cases = int(row.get("Confirmed"))

    if region not in new_dict:

        new_dict[region] = confirmed_cases

    else:

        new_dict[region] += confirmed_cases

print(new_dict)