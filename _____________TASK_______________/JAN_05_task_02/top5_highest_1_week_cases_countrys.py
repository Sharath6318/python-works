# Display top 5 countries with highest weekly case increase (1 week change).

file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding='utf-8')

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

country_cases = {r.get('Country/Region') : r.get('1 week change') for r in data}

sorted_records = sorted(country_cases.items(), key=lambda r : int(r[1]), reverse=True)[:5]

top_five_records = dict(sorted_records)

print(f"top 5 countries with highest weekly case increase : {top_five_records.keys()}")