file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sweet_item_count = len([items.get('flavor_profile') for items in data if items.get('flavor_profile') == 'sweet'])

print(sweet_item_count)