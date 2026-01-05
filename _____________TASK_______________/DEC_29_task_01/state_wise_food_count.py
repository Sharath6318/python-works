file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

state = [st.get('state') for st in data]

for st in state:

    if st not in new_dict :

        new_dict[st] = 1

    else:

        new_dict[st] += 1

print(new_dict)
