file_path = "_____________TASK_______________/DEC_10_task/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sort_data = sorted(data, key=lambda d : d.get("Customer_Rating"), reverse=True) # sort by decending order

print(sort_data)