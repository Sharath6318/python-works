file_path = "_____________TASK_______________/DEC_04_task/process_food_datas/Food_Nutrition_Dataset.csv.xls"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

food_cal = [float(v.get("calories")) for v in data]

average_of_calories = round((sum(food_cal)/ len(food_cal)), 2)

print(f"Average of all calories : {average_of_calories}")

