# Find all movies that were released after 2015 and won the Oscar.

from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

movie_aft_2015 = [i.get('name') for i in data if i.get('released_year') > 2015]

print(movie_aft_2015)