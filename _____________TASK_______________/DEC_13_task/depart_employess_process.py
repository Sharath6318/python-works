file_path = "_____________TASK_______________/DEC_13_task/employee_salary_dataset.csv"
updataed_file_path = "_____________TASK_______________/DEC_13_task/department_wise_employess.csv"

fr = open(file_path)
up_data_fw = open(updataed_file_path, "w")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

dept = [d.get("Department") for d in data]

for dep in dept:

    new_dict[dep] = [emp.get("Name") for emp in data if emp.get("Department") == dep]


for data in new_dict.items():

    up_data_fw.write(str(data) + "\n")
