file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding='utf-8')

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

country_recoveryrate = {r.get('Country/Region')  : float(r.get('Recovered / 100 Cases')) for r in data}

max_recovery_rate = max(Rr for Rr in country_recoveryrate.values())

HrrC = [c for c, r in country_recoveryrate.items() if r == max_recovery_rate]

print(HrrC)