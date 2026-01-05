file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)



data = [data for data in reader]

track_popularity = [p.get("track_popularity") for p in data]

sum_val = sum([int(num) for num in track_popularity])

len_val = len(track_popularity)

average = round((sum_val / len_val), 2)

print(average)



