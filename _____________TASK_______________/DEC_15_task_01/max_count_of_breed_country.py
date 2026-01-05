file_path = "_____________TASK_______________/DEC_15_task_01.py/dog_breeds.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

countrys = [c.get("Country of Origin") for c in data]
breeds = [b.get("Breed") for b in data]

# Use zip() when you want to combine multiple related columns row-wise.....................

new_dict = {}

country_wise_breed_count = {}

for country, breed in zip(countrys, breeds):

    if country not in new_dict:

        new_dict[country] = [breed]

    else:

        new_dict[country].append(breed)

for c, b in new_dict.items():

    country_wise_breed_count[c] = len(b)

max_count = max(country_wise_breed_count.values())

max_count_country = [country for country, count in country_wise_breed_count.items() if count == max_count]

print(max_count_country)




