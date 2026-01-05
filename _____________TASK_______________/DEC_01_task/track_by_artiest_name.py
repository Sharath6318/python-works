file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

artist_Name = input("Enter the artist name : ").lower()

reader = csv.DictReader(fr)

data = [data for data in reader]

data_by_artist_name = [a for a in data if a.get("artist_name").lower() == artist_Name]

print(data_by_artist_name)




