from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

yearlist_year = min(i.get("released_year") for i in data)

yearlist_realese_move = [i.get('name') for i in data if int(i.get("released_year")) == yearlist_year]

print(yearlist_realese_move)