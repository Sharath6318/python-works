file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"


fr = open(file_path)

for line in fr:

    line = line.rstrip("\n")

    print(line)

