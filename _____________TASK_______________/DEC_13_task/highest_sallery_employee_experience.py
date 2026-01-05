file_path = "_____________TASK_______________/DEC_13_task/employee_salary_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

highesy_Monthly_salary = max(int(i.get("Monthly_Salary")) for i in data)

emp_name_experience = {i.get("Name") : i.get("Experience_Years") for i in data if int(i.get("Monthly_Salary")) == highesy_Monthly_salary}

print(emp_name_experience)