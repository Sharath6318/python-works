# find the average sleep_hours of all users

file_path = "_____________TASK_______________/DEC_09_task/mental_health_social_media_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sleep_hours = [float(s.get("sleep_hours") )for s in data]

len_of_sleep_hrs = len(sleep_hours)

sum_of_sleep_hrs = sum(sleep_hours)

average_of_sleep_hrs = sum_of_sleep_hrs / len_of_sleep_hrs

print(f"Average of sleep_hours of all users : {average_of_sleep_hrs}")

