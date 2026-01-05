file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

album_name = [a.get("album_name") for a in data]

new_dict = {}

for album in album_name:

    if album in new_dict:

        new_dict[album] += 1

    else:

        new_dict[album] = 1


for res in new_dict.items():

    print(res)





