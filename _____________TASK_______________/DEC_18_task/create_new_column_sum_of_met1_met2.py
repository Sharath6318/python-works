file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_18_task/amazon_sales_2025_INR_cleaned.csv"

fr = open(file_path, encoding="utf-8")


import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

douple_val = list(map(lambda row : {**row, "Metric2": float(row["Metric2"]) * 2}, data))

for data in douple_val:

    print(data, "\n")
