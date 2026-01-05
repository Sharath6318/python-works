file_path = "_____________TASK_______________/DEC_04_task/process_food_datas/Food_Nutrition_Dataset.csv.xls"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

food_with_0_fat = {f.get("food_name") for f in data if float(f.get("fat")) == 0}

for foods in food_with_0_fat:

    print(foods)

