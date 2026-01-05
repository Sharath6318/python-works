file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

country_recovery = {c.get("Country/Region") : c.get('Recovered') for c in data}


sorted_records= sorted(country_recovery.items(), key = lambda dc : int(dc[1]))

country_by_recover_rate = dict(sorted_records)

top_10_country_by_recover_rate = list(country_by_recover_rate.keys())[:10]

print(top_10_country_by_recover_rate)