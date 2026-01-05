file_path = "_____________TASK_______________/DEC_15_task_01.py/dog_breeds.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

countrys = [c.get("Country of Origin") for c in data]

for country in countrys:

    if country not in new_dict:

        new_dict[country] = [b.get("Breed") for b in data if b.get("Country of Origin") == country]

for data in new_dict.items():

    print(data, "\n")


# countries = [row["Country of Origin"] for row in data]
# breeds = [row["Breed"] for row in data]

# new_dict = {}

# # Group using zip()
# for country, breed in zip(countries, breeds):
#     if country not in new_dict:
#         new_dict[country] = [breed]
#     else:
#         new_dict[country].append(breed)

# # Print result
# for item in new_dict.items():
#     print(item, "\n")


