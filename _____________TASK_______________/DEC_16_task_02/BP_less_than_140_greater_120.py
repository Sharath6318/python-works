file_path = "_____________TASK_______________/DEC_16_task_02/Heart_Disease_Prediction.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

Normal_Bp = [b.get("Age") for b in data if int(b.get("BP")) > 120 and int(b.get("BP")) < 140]

print(f"patients age with BP between 120 and 140 {Normal_Bp}")