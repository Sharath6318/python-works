#  Verify whether all movies in the dataset contain both director and runtime information.

from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

verify_data = [i.get('name') for i in data if i.get('duration') is None or i.get('name') is None]

if not verify_data:

    print('All movies in the dataset contain both director and runtime')

else:

    print(verify_data)

