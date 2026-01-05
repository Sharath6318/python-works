file_path = "PYTHON-WORKS/_____________TASK_______________/DEC_01_task/spotify_data_clean.csv"

fr = open(file_path, encoding="utf-8", errors="replace")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

artist_genres = [a.get("artist_genres") for a in data]

new_dict = {}

for genrec in artist_genres:

    if genrec in new_dict:

        new_dict[genrec] += 1

    else:

        new_dict[genrec] = 1

for info in new_dict.items():

    print(info)




