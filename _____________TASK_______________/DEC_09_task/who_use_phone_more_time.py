file_path = "_____________TASK_______________/DEC_09_task/mental_health_social_media_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

username_mobileusage = {i.get("person_name") : i.get("daily_screen_time_min") for i in data}

max_usage = max(username_mobileusage.values())

user_use_mobile_more_time = {u : t for u, t in username_mobileusage.items() if t == max_usage}

print(f"long duration mobile use person {user_use_mobile_more_time}")