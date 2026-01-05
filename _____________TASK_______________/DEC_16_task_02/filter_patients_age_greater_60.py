file_path = "_____________TASK_______________/DEC_16_task_02/Heart_Disease_Prediction.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

filter_data = list(filter(lambda d : int(d.get("Age")) > 60, data))

for data in filter_data:

    print(data, "\n")