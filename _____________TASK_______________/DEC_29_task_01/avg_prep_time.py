file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

preparition = [prep.get('prep_time') for prep in data]

len_of_prep = len(preparition)
sum_of_prep = 0

for time in preparition:

    sum_of_prep += int(time)

avg_prep = round(sum_of_prep / len_of_prep, 2)

print(f'Average of prepare time : {avg_prep}')