# top 5 users with highest anxiety_level

file_path = "_____________TASK_______________/DEC_09_task/mental_health_social_media_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sorted_val = sorted(data, key=lambda s : s.get("anxiety_level"), reverse=True)

anxiety_leval_high_to_low = [v.get("person_name") for v in sorted_val]

print(f"Top five users with highest anxiety level : {anxiety_leval_high_to_low[:5]}")