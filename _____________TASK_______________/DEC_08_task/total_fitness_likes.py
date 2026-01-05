# total likes in fitness.....................

file_path = "_____________TASK_______________/DEC_08_task/Instagram_Analytics.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

total_fitness_likes = 0

for val in data:

    if val.get("content_category") == "Fitness":

        total_fitness_likes += int(val.get("likes"))

print(total_fitness_likes)