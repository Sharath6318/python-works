# group the data by gender and find average stress_level

file_path = "_____________TASK_______________/DEC_09_task/mental_health_social_media_dataset.csv"


fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

female_user_stress_leval = [float(d.get("stress_level")) for d in data if d.get("gender") == "Female"]
male_user_stress_leval = [float(d.get("stress_level")) for d in data if d.get("gender") == "Male"]

len_of_female_user_stress_leval, sum_of_female_user_stress_leval = len(female_user_stress_leval), sum(female_user_stress_leval)
len_of_male_user_stress_leval, sum_of_male_user_stress_leval = len(male_user_stress_leval), sum(male_user_stress_leval)

Average_stress_leval_of_male = round(sum_of_male_user_stress_leval / len_of_male_user_stress_leval, 2)
Average_stress_leval_of_female = round(sum_of_female_user_stress_leval / len_of_female_user_stress_leval, 2)

print(f"Average stress leval of male : {Average_stress_leval_of_male}")
print(f"Average stress leval of female : {Average_stress_leval_of_female}")



