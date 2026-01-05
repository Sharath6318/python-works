file_path = "_____________TASK_______________/DEC_16_task_02/Heart_Disease_Prediction.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

male_ages = []
female_ages = []

for row in data:

    if row["Sex"] == "1": 

        male_ages.append(int(row["Age"]))

    elif row["Sex"] == "0":   

        female_ages.append(int(row["Age"]))

avg_male_age = round(sum(male_ages) / len(male_ages), 2)
avg_female_age = round(sum(female_ages) / len(female_ages), 2)

print("Average Male Age:", avg_male_age)
print("Average Female Age:", avg_female_age)







