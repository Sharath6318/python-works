from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

movie_titles = [i.get('name') for i in data]

for movie in movie_titles:

    print(movie)