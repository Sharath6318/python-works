file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]



explicit_true = [info.get("track_name") for info in data if info.get("explicit") == "TRUE"]

print(f"total_tracks_have_explicit = True : {len(explicit_true)}")
