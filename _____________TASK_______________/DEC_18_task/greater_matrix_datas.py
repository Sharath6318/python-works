file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_18_task/amazon_sales_2025_INR_cleaned.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

filter_data = list(filter(lambda a : float(a.get("Metric1")) > 10000000, data))

for data in filter_data:

    print(data, "\n")

