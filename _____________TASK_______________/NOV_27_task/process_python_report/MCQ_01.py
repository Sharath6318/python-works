file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

mcq_01 = {info.get("NAME") : info.get("MCQ1") for info  in data}

print(mcq_01)

