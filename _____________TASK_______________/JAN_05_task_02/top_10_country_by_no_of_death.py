file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

country_death = {c.get("Country/Region") : c.get('Deaths') for c in data}


top_10_records_by_death_count = sorted(country_death.items(), key = lambda dc : int(dc[1]), reverse=True)[ :10]

print(top_10_records_by_death_count)


