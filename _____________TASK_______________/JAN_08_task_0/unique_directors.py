from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

all_dir = {i.get('name') for i in data}

print(f"list of unique directors from the dataset {all_dir}")

