# List countries where active cases are greater than recovered cases.

file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

countrys = {i.get("Country/Region") for i in data if i.get('Active') > i.get('Recovered')}

print(countrys)