file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

song_duration = [s.get("track_duration_min") for s in data]

max_song_duration = max(song_duration)

track = [t.get("track_name") for t in data if t.get("track_duration_min") == max_song_duration]

print(f"Track with the maximum track_duration_min : {track}")



