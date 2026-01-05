file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

regions = [reg.get('region') for reg in data]


for reg in regions:

    if reg.isalpha():

        if reg not in new_dict:

            new_dict[reg] = 1

        else:

            new_dict[reg] += 1

max_items = max(new_dict.values())

max_food_count_region_name = [r for r, c in new_dict.items() if c == max_items]

print(max_food_count_region_name)
