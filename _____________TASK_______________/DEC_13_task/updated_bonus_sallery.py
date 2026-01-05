file_path = "_____________TASK_______________/DEC_13_task/employee_salary_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

def increase_salary(data):

    data["Monthly_Salary"] = int(data["Monthly_Salary"]) + 10000

    return data
        
updated_employees = list(map(increase_salary, data))

for data in updated_employees:

    print(data)