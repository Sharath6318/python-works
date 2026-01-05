file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

more_absent_students = [info for info in data if float(info.get("ABSENT_%")) > 20]

print(more_absent_students)
