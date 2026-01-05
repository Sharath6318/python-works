file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

veg_dish_from_south_reg = [dish.get('name') for dish in data if dish.get('diet') == 'vegetarian' and dish.get('region') == 'South']

print(veg_dish_from_south_reg)