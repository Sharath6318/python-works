from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

oscar_wining_movie_title_year = {i.get('name') : i.get("released_year") for i in data}

for k, v in oscar_wining_movie_title_year.items():

    print(k, v)