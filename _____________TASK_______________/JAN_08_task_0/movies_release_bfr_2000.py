from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

movies_bfr_2000 = [i.get("name") for i in data if i.get("released_year") < 2000]

print(movies_bfr_2000)