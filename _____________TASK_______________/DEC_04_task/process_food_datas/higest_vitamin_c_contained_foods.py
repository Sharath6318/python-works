file_path = "_____________TASK_______________/DEC_04_task/process_food_datas/Food_Nutrition_Dataset.csv.xls"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

food_name_vitamin_c = {f.get("food_name") : float(f.get("vitamin_c") ) for f in data if len(f.get("vitamin_c")) > 0}

max_of_vitamin_c = max(food_name_vitamin_c.values())

max_vitamin_c_foods_name = {f for f, c in food_name_vitamin_c.items() if c == max_of_vitamin_c}

print(f"high leval vitamin_c contained food names : {max_vitamin_c_foods_name}")



