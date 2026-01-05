file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_18_task/amazon_sales_2025_INR_cleaned.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

count = 0

for data in data:

    count += 1

print(count)