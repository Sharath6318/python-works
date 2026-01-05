file_path = "_____________TASK_______________/DEC_04_task/process_food_datas/Food_Nutrition_Dataset.csv.xls"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

food_category = {f.get("food_name") : f.get("category") for f in data}

for f, c in food_category.items():

    if c not in new_dict:

        new_dict[c] = [f]

    else:

        new_dict[c].append(f)

len_of_foods = []

for c, f in new_dict.items():

    len_of_foods.append(len(f))

higest_food_count = max(len_of_foods)

highest_food_category = [c for c, f in new_dict.items() if len(f) == higest_food_count]

print(f"category have more food : {highest_food_category}")


    


    



