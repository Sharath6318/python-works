file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_18_task/amazon_sales_2025_INR_cleaned.csv"

fr = open(file_path, encoding="utf-8")


import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

for info in data:

    info["Metric2"] = float(info["Metric2"]) * 2

    print(info)