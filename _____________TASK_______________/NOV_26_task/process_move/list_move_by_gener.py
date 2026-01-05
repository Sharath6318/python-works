file_path = "PYTHON-WORKS/_____________TASK_______________/NOV_26_task/process_move/movies.txt"

fr = open(file_path)

import csv

reader = csv.DictReader(fr)

user_input = input("Enter the genre : ").title()

data = [data for data in reader]


user_request_movies = [genre.get("Film") for genre in data if user_input == genre.get("Genre")] 

for Movies in user_request_movies:

    print(Movies)