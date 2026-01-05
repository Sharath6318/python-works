file_path = "_____________TASK_______________/DEC_09_task/mental_health_social_media_dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

male_snapchat_user_count = len([i.get("gender") for i in data if i.get("gender") == "Male" and i.get("platform") == "Snapchat"])
female_snapchat_user_count = len([i.get("gender") for i in data if i.get("gender") == "Female" and i.get("platform") == "Snapchat"])

max_snapchat_user_count = max(male_snapchat_user_count, female_snapchat_user_count)

if max_snapchat_user_count == male_snapchat_user_count:

    print("Male are most snapchat users")

else:

    print("femals are the most snapchat users")

