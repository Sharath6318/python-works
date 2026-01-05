file_path = "_____________TASK_______________/DEC_29_task_01/indian_food.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

main_courses = [course.get('name') for course in data if course.get('course') == "main course"]

for main_cour in main_courses:

    print(main_cour)