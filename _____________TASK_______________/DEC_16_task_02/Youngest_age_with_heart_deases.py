file_path = "_____________TASK_______________/DEC_16_task_02/Heart_Disease_Prediction.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

Age_with_heart_deases = [int(i.get("Age") )for i in data if i.get("Heart Disease") == "Presence"]


print(f"youngest patient age with heart disease {min(Age_with_heart_deases)}")