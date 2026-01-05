file_path = "_____________TASK_______________/DEC_16_task_02/Heart_Disease_Prediction.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

age = [int(a.get("Age")) for a in data]

print(f"Minimum age : {min(age)}")
print(f"Maximun age : {max(age)}")