file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"
python_file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/process_batch_wise/python_student_data.csv"
Data_science_file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/process_batch_wise/dataScience_student_data.csv"

fr = open(file_path)

python_fw = open(python_file_path, "w")
Data_Science_fw = open(Data_science_file_path, "w")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

for student in data:

    if student.get("BATCH ") == "Python":

        python_fw.write(student.get("NAME") + "\n")

    elif student.get("BATCH ") == "Data Science":

        Data_Science_fw.write(student.get("NAME") + '\n')






