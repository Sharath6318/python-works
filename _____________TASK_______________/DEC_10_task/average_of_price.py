file_path = "_____________TASK_______________/DEC_10_task/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

average = [float(p.get("Price(USD)")) for p in data]

len_of_average = len(average)

sum_of_average = sum(average)

average_of_price = round(sum_of_average / len_of_average, 2)

print(f"Average of Price - {average_of_price}")
