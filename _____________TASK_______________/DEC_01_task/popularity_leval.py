file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

aritst_popularity = [p for p in data if p.get("artist_popularity") > 60]

