file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, "r", encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

track_name = [info.get("track_name") for info in data]

print(f" first 5 track names : {track_name[:5]}")





