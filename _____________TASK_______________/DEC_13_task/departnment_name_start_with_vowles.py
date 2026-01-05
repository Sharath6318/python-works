file_path = "_____________TASK_______________/DEC_13_task/employee_salary_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

vowles = "aeiouAEIOU"

name_start_vowles = list(filter(lambda n : n.get("Department")[0] in vowles, data))

for data in name_start_vowles:

    print(data, "\n")