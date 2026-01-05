file_path = "PYTHON-WORKS\\_____________TASK_______________\\NOV_26_task\\process_move\\movies.txt"

move_import_file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/Higly_rated_movies.csv"

fr = open(file_path)

mov_w = open(move_import_file_path,"w")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

rating_list = [rat.get("Film") for rat in data if int(rat.get("Rotten Tomatoes %")) >  8.0]

for movies in rating_list:

    mov_w.write(movies + "\n")





