file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

count = 0

for data in data:

    count += 1

print(count)

