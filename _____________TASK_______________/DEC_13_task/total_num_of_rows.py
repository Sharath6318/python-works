file_path = "_____________TASK_______________/DEC_13_task/employee_salary_dataset.csv"

fr = open(file_path, encoding="utf-8")

fr.readline()

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

count = 0

for c in data:

    count += 1


print(f"Total num of rows {count}")
