file_path = "_____________TASK_______________/DEC_16_task_02/Heart_Disease_Prediction.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

male= [d.get("Sex") for d in data if d.get("Sex") == "1"]
female= [d.get("Sex") for d in data if d.get("Sex") == "0"]

male_count = {"Male" : male.count(mc) for mc in male}
female_count = {"female": female.count(fc) for fc in female}

print(male_count)
print(female_count)