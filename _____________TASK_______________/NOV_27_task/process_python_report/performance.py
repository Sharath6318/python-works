file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"
performance_report_file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/performance_category.csv"

fr = open(file_path)

performance_fw = open(performance_report_file_path, "w")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

performance_report = [{"Name" : info.get("NAME"), 
                       "Overall" : info.get("OVERALL"), "Category" : ("Excellent" if len(info.get("OVERALL")) > 1 and float((info.get("OVERALL"))) >= 70 
                        else "Good" if len(info.get("OVERALL")) > 1 and float(info.get("OVERALL")) > 40 and float(info.get("OVERALL")) < 69 
                        else "Need Improvement")} for info in data]

for performance in performance_report:

    performance_fw.write(str(performance) + '\n')

