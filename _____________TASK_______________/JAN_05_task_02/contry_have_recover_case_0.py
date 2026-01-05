# List countries where recovered cases are zero.
file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding='utf-8')

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

countrys = [r.get("Country/Region") for r in data if int(r.get('Recovered')) == 0]

print(countrys)