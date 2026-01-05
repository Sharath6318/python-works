file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

west_bengal_food_items = [foods.get("name") for foods in data if foods.get("region") == "West"]

print(west_bengal_food_items)