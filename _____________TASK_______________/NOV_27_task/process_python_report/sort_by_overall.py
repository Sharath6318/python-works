file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"
import_file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/sorted_overall.csv"

fr = open(file_path)

sorted_fw = open(import_file_path, "w")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sort_val = sorted(data, key= lambda d : d.get("OVERALL"), reverse=True)

for info in sort_val:

    sorted_fw.write(str(info) + "\n")




    