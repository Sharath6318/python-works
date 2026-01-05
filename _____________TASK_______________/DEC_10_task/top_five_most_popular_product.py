file_path = "_____________TASK_______________/DEC_10_task/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]


sorted_data = sorted(data, key=lambda d : float(d.get("Popularity_Score")), reverse= True)[:5]

for i, data in enumerate(sorted_data, start=1):

    print(f"{i} -> {data}")


