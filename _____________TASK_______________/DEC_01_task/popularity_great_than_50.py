file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

required_popularity = [info.get("track_name") for info in data if int(info.get("track_popularity")) > 50]

for name in required_popularity:

    print(name)

