file_path = "_____________TASK_______________/DEC_16_task_02/Heart_Disease_Prediction.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sorted_data = sorted(data, key=lambda d : d.get("Age"))

print(sorted_data)

