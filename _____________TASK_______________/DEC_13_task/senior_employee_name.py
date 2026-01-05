file_path = "_____________TASK_______________/DEC_13_task/employee_salary_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

employee_name_experience_year = {i.get("Name") : i.get("Experience_Years") for i in data}

max_experience_year = max(employee_name_experience_year.values())

senior_employee = {n for n, y in employee_name_experience_year.items() if y == max_experience_year}

print(f"senior Employees {senior_employee} year of experience {max_experience_year}")