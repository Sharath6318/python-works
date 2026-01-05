file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/movies.txt"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

data = [data for data in reader]

Rating = [rat.get("Rotten Tomatoes %") for rat in data]

max_rating = max(Rating)

Hig_rate_movie = {h.get("Film") : h.get("Rotten Tomatoes %")  for h in data if h.get("Rotten Tomatoes %") == max_rating}

print(f"Highest Rated Movie: {Hig_rate_movie}")
























# movies = []

# rating = []

# for line in fr:

#     line = line.rstrip("\n").split(",")

#     movies.append(line)

# movies.remove(movies[0])

# for i in range(1, len(movies)):

#     rating.append(movies[i][5])

# max_rating = max(rating)

# for L in movies:

#     if L[5] == max_rating:

#         print(f"Highest Rated Movie : {L[0]} -- Rating {L[5]}")





    





    












    

    















    

