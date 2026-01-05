file_path = "_____________TASK_______________/DEC_11_task/toyota.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

diesel_car_with_price = {v.get("model") : int(v.get("price")) for v in data if v.get("fuelType") == "Diesel"}
petrol_car_with_price = {v.get("model") : int(v.get("price")) for v in data if v.get("fuelType") == "Petrol"}

len_of_disel_car_price = len(diesel_car_with_price.values())
sum_of_disel_car_price = sum(diesel_car_with_price.values())

average_of_diesel_car_price = sum_of_disel_car_price/len_of_disel_car_price
print(f"Average of diesel car Price : {average_of_diesel_car_price}")

len_of_petrol_car_price = len(petrol_car_with_price.values())
sum_of_petrol_car_price = sum(petrol_car_with_price.values())

average_of_petrol_car_price = round(sum_of_petrol_car_price/len_of_petrol_car_price, 2)
print(f"Average of petrol car Price : {average_of_petrol_car_price}")