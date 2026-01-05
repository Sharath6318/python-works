file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_18_task/amazon_sales_2025_INR_cleaned.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

matrics_02 = [float(m.get("Metric2")) for m in data]


len_of_metric_02 = len(matrics_02)
sum_of_metric_02 = sum(matrics_02)

average_of_marrics_02 = round(sum_of_metric_02 / len_of_metric_02, 2)

print(f"Average of metric2 : {average_of_marrics_02}")



