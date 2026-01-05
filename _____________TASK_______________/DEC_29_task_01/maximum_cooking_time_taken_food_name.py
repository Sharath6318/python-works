file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

max_cooking_time = max(time.get('prep_time') for time in data)

max_prep_food_name = [food.get('name') for food in data if food.get('prep_time') == max_cooking_time]

print(f'maximum cooking time food name : {max_prep_food_name}')