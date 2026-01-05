file_path = "_____________TASK_______________/DEC_13_task/employee_salary_dataset.csv"

updated_experience_file_path = "_____________TASK_______________/DEC_13_task/updated_experience_data.csv"

fr = open(file_path, encoding="utf-8")

experience_upd_fw = open(updated_experience_file_path, "w")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sorted_data = sorted(data, key=lambda i : int(i.get("Experience_Years")), reverse=True)

for data in sorted_data:

    experience_upd_fw.write(str(data) + "\n")