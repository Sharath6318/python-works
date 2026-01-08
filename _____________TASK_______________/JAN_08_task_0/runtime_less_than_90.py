from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)


for movie in data:

    move_duration = int(str(movie.get('duration')).split(' ')[0])

    if move_duration < 90:

        print(movie.get('name'))