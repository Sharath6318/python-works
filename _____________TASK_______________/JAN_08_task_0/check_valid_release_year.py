# Check whether all movies in the dataset have a valid release year (greater than 1900)

from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

invalid_release_year = [i.get('name') for i in data if i.get("released_year") is None or i.get("released_year") <= 1900]

if not invalid_release_year:

    print("There is not invalid release year")

else:

    print(invalid_release_year)