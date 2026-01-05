file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"

fr = open(file_path)

fr.readline()

total_count = 0

for line in fr:

    total_count += 1

print(total_count)



