from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

mrtg150 = [i.get('name') for i in data if int(i.get('duration')) > 150]

print(mrtg150)