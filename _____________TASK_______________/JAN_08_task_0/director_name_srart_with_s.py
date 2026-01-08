from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

dir_name_start_with_S = [i.get('directors')[0] for i in data if i.get('directors')[0].startswith('S')]

print(dir_name_start_with_S)
