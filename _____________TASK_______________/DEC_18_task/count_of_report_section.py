file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_18_task/amazon_sales_2025_INR_cleaned.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

print(data)

report_section = [info.get("\ufeffReport_Section") for info in data]


count_of_rs = {c : report_section.count(c) for c in report_section}

print(count_of_rs)