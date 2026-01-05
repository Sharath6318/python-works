file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/movies.txt"

import_movie_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/genre_count.txt"

fr = open(file_path)

fw = open(import_movie_path, "w")

import csv

reader = csv.DictReader(fr)

new_dict = {}

data = [data for data in reader]

genre_list = [genre.get("Genre") for genre in data]

for gen in genre_list:

    if gen in new_dict:

        new_dict[gen] += 1

    else:

        new_dict[gen] = 1

for k, v in new_dict.items():

    fw.write(f"{k} : {v}\n")

