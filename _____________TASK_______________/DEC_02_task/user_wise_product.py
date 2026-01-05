file_path = "_____________TASK_______________/DEC_02_task/cart_items_100.csv"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

new_dict = {}

users = [u.get("user") for u in data]

for user in users:

    if user not in new_dict:

        new_dict[user] = {pro.get("title") for pro in data if pro.get("user") == user}

for updata in new_dict.items():

    print(updata, "\n")


