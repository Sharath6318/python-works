file_path = "_____________TASK_______________/DEC_16_task_02/Heart_Disease_Prediction.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

chest_pain_type_four = [int(c.get("Chest pain type")) for c in data if c.get("Chest pain type") == "4"]

chest_pain_type_four_count = 0

for i in chest_pain_type_four:

    chest_pain_type_four_count += 1

print(f"Count patients with chest pain type four {chest_pain_type_four_count}")