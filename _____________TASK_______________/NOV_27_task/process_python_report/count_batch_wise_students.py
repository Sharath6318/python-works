file_path = "_____________TASK_______________/NOV_27_task/process_python_report/student_data.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

python_student_count = 0
data_science_student_count = 0

data = [data for data in reader]

for batch in data:

    if batch["BATCH "] == "Python":

        python_student_count += 1

    elif batch["BATCH "] == "Data Science":

        data_science_student_count += 1

print(f"Total Python students : {python_student_count}")
print(f"Total Data Science students : {data_science_student_count}")







