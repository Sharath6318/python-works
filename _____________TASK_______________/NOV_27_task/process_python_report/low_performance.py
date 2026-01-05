file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

low_percentage = [info.get("NAME") for info in data if info.get("OVERALL") != "-" and float(info.get("OVERALL")) < 30]

print(low_percentage)

