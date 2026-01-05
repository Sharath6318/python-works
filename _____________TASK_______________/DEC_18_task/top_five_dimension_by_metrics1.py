file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_18_task/amazon_sales_2025_INR_cleaned.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sorted_Data = sorted(data , key=lambda d : float(d.get("Metric1")), reverse=True)[:5]

top_five_dim = [data.get("Dimension") for data in sorted_Data]

print(top_five_dim)