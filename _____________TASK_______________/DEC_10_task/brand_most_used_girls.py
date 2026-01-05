file_path = "_____________TASK_______________/DEC_10_task/Winter_Fashion_Trends_Dataset.csv"

fr = open(file_path, encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

brand_used_women = [c.get("Brand") for c in data if c.get("Gender") == "Women"]

brand_with_count = {b : brand_used_women.count(b) for b in brand_used_women}

max_count = max(brand_with_count.values())

brand_most_used_women = [b for b, c in brand_with_count.items() if c ==  max_count]

print(f"Womens Most used Brand - {brand_most_used_women}")






