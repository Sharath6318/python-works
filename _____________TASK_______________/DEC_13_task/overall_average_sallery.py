file_path = "_____________TASK_______________/DEC_13_task/employee_salary_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sallery = [int(s.get("Monthly_Salary")) for s in data]

len_of_sallery = len(sallery)

sum_of_sallery = sum(sallery)

average_of_sallery = sum_of_sallery / len_of_sallery

print(f"overall average salary {average_of_sallery}")



