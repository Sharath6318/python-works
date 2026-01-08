#  Count the total number of Oscar-winning movies in the dataset.

from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding='utf-8')

data = load(fr)

total_movie = 0

for movie in data:

    total_movie += 1

print(f"Total number of Oscar-winning movies {total_movie}")