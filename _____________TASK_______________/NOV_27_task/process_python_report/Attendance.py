file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

full_attendance= [batch.get("NAME") for batch in data if batch.get("PRESENT_%") == "100"]

print(f" 100 % Attendance Students : {full_attendance}")

