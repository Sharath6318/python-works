file_path = "_____________TASK_______________/DEC_09_task/mental_health_social_media_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

platforms_below_22_age = [i.get("platform") for i in data if int(i.get("age")) < 22]

most_used_count = {p : platforms_below_22_age.count(p) for p in platforms_below_22_age}

max_count = max(most_used_count.values())

most_used_platform = {p for p, c in most_used_count.items() if c == max_count}

print(most_used_platform)