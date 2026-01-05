# sort_datas_by_highest_time_moblie_users_to_low

file_path = "_____________TASK_______________/DEC_09_task/mental_health_social_media_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sorted_val = sorted(data, key=lambda s :s.get("social_media_time_min"), reverse=True)

print(sorted_val)