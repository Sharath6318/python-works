file_path = "_____________TASK_______________/DEC_09_task/mental_health_social_media_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

platforms = [p.get("platform") for p in data] 

platforms_count = {c : platforms.count(c) for c in platforms}

highely_used_platform_count = max(platforms_count.values())

highely_used_platform = {p for p, c in platforms_count.items() if c == highely_used_platform_count}

print(highely_used_platform)