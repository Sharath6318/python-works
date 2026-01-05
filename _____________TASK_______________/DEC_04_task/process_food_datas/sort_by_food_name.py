# rearrange dataset based on the name sort

file_path = "_____________TASK_______________/DEC_04_task/process_food_datas/Food_Nutrition_Dataset.csv.xls"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sort_data = sorted(data, key=lambda d : d.get("food_name"))

print(sort_data)

# for data in sort_data:

#     print(data.get("food_name"))