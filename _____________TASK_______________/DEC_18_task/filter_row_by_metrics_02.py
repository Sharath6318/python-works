file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_18_task/amazon_sales_2025_INR_cleaned.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]


filtered_data = [d for d in data if float(d.get("Metric2")) > 1000 and float(d.get("Metric2")) < 3000]

# using_filter = list(filter(lambda a : float(a.get("Metric2")) > 1000 and float(a.get("Metric2")) < 3000, data))

for data in filtered_data:

    print(data, "\n")
