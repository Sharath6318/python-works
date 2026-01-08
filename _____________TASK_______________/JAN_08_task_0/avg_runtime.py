from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

runtime = []

for movie in data:

    runtime.append(int(str(movie.get('duration')).split(' ')[0]))

length_of_runtime = len(runtime)

sum_of_runtime = sum(runtime)

average_runtime = round(sum_of_runtime / length_of_runtime, 2)

print(average_runtime)

    