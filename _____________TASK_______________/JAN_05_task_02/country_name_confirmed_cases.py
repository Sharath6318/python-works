# Display country name and confirmed cases for countries belonging to the WHO Region "Europe".

file_path = "_____________TASK_______________/JAN_05_task_02/country_wise_latest_covid.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

country_name_confirmed_cases = {i.get("Country/Region") : i.get('Confirmed') for i in data if i.get('WHO Region') == "Europe"}

print(country_name_confirmed_cases)