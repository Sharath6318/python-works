file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"

import_file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/rank_list.csv"


fr = open(file_path)

rang_fw = open(import_file_path, "w")

sorted_fw = open(import_file_path, "w")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sort_val = sorted(data, key= lambda d : d.get("OVERALL"), reverse=True)

students_info = []

for info in sort_val:

    students_info.append(info.get("NAME"))

    rank = students_info[:3]

sorted_fw.write(str(rank))

