file_path = "_____________TASK_______________/DEC_13_task/employee_salary_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

employee_education = [i.get("Education_Level") for i in data]

education_leval_count = {e : employee_education.count(e) for e in employee_education}

max_count = max(education_leval_count.values())

most_employee_education_leval = {d for d, c in education_leval_count.items() if c == max_count}

print(f"Most employee education level {most_employee_education_leval}")



