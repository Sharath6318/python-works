# 4. Check whether any director has won the Oscar more than once.

from json import load

file_path = "_____________TASK_______________/JAN_08_task_0/oscar-best-picture-award-winners.json"

fr = open(file_path, encoding="utf-8")

data = load(fr)

name_and_oscar_cou = {}

for i in data:

    director_name = i.get("name")

    if director_name in name_and_oscar_cou:

        name_and_oscar_cou[director_name] += 1

    else:

        name_and_oscar_cou[director_name] = 1

director_won_Oscar_more_than_one = [n for n, c in name_and_oscar_cou.items() if c > 1]

if not director_won_Oscar_more_than_one:

    print("There is no directors won the oscar more than one")

else:

    print(director_won_Oscar_more_than_one)










