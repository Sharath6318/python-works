# Calculate the average likes per post


file_path = "_____________TASK_______________/DEC_08_task/Instagram_Analytics.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

count = 0
sum_of_likes = 0

for row in data:

    sum_of_likes += int(row.get("likes"))
    count += 1

average = round(sum_of_likes / count, 2)

print(f"Average like per post : {average}")
