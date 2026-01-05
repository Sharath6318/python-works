file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

confirmed_cases = {r.get("Country/Region") : int(r.get('Confirmed')) for r in data}

max_confirmed_case = max(c for c in confirmed_cases.values())

hcc = [cou for cou, cas in confirmed_cases.items() if cas == max_confirmed_case]

print(f'Highest number of confirmed cases country {hcc}')