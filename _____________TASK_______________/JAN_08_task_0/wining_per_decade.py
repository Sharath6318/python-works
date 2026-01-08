from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, "r", encoding="utf-8")

movies = load(fr)

decade_count = {}

for movie in movies:
    year = movie["released_year"]
    decade = f"{(year // 10) * 10}s"   
    
    decade_count[decade] = decade_count.get(decade, 0) + 1

print(decade_count)



