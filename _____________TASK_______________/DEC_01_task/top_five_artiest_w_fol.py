file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

sorted_data = sorted(data, key=lambda d : d.get("artist_followers"), reverse=True)

top_five = sorted_data[:5]

top_five_aritst_name = [n.get("artist_name") for n in top_five]

print(f"top 5 artists with the highest artist_followers {top_five_aritst_name}")