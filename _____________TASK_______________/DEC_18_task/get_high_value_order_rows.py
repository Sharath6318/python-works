file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_18_task/amazon_sales_2025_INR_cleaned.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

high_value_orders = [o for o in data if o.get("\ufeffReport_Section") == "HIGH_VALUE_ORDERS"]

print(high_value_orders)