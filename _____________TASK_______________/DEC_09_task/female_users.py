file_path = "_____________TASK_______________/DEC_09_task/mental_health_social_media_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv 

reader = csv.DictReader(fr)

data = [data for data in reader]

female_user_detail = [d for d in data if d.get("gender") == "Female"]

print(female_user_detail)