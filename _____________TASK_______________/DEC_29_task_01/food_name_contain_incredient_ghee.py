file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

food_names = [names.get("name") for names in data if names.get('ingredients') and 'ghee' in names.get('ingredients').lower()]

print(food_names)