file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

max_overall = max([info.get("OVERALL") for info in data if info.get("OVERALL") != "-"])

high_performance = [info.get("NAME") for info in data if info.get("OVERALL") != "-" and info.get("OVERALL") ==  max_overall]

print(high_performance)

