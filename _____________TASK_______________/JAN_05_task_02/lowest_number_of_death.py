file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding= "utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

country_death = {c.get("Country/Region") : c.get('Deaths') for c in data}

lowest_death_count = min(dc for dc in country_death.values())

ldcC = [c for c, d in country_death.items() if d == lowest_death_count]

print(ldcC)