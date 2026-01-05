file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

countrys = [C.get('Country/Region') for C in data]

print(f"Total no of countr/Religion : {len(countrys)}")