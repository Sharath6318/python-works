file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"
Attendance_report_file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/attendance_report.csv"


fr = open(file_path)
attendance_report_fw = open(Attendance_report_file_path, "w")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

attendance_report_below_80_per = [{"Name" : info.get("NAME"), "Present_count" : info.get("PRESENT_COUNT"), "Absent_count" : info.get("ABSENT_COUNT"), "Percentage" : info.get("PRESENT_%")}
                      for info in data if len(info.get("PRESENT_%")) > 1 and float(info.get("PRESENT_%")) < 80]


for report in attendance_report_below_80_per:

    attendance_report_fw.write(str(report) + "\n")