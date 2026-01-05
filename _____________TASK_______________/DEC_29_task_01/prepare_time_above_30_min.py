file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

food_items = [items.get('name') for items in data if int(items.get("prep_time")) > 30]

print(food_items)