file_path = "_____________TASK_______________/DEC_13_task/employee_salary_dataset.csv"

fr = open(file_path, encoding = "utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

count_of_gender = {}

gender = [g.get("Gender") for g in data]

for gen in gender:

    if gen not in count_of_gender:

        count_of_gender[gen] = 1

    else:

        count_of_gender[gen] += 1

print(count_of_gender)



