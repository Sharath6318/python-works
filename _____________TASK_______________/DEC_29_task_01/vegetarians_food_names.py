file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

vegetarians_peoples = [pep.get('name') for pep in data if pep.get('diet') == 'vegetarian']

print(vegetarians_peoples)