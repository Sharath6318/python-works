file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/movies.txt"

import_file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/sorted_movies.csv"

fr = open(file_path)

fw = open(import_file_path, "w")

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

total_list = {info.get("Film") : info.get("Rotten Tomatoes %") for info in data}

sort_val = sorted(total_list, key=lambda n : n[1], reverse=True)

for movie in sort_val:

    fw.write(movie + "\n")







