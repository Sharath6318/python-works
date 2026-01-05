file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

Emty_col = {line.get("NAME") for line in data for k, v in line.items() if v == '-'}

print(Emty_col)