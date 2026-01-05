file_path = "_____________TASK_______________/DEC_02_task/cart_items_100.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

cmr_using_users = [info.get("user") for info in data if info.get("title") == "Camera"]

print(f"Camera using users : {cmr_using_users}")