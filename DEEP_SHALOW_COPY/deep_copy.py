#A deep copy creates a new object and also copies all nested objects.

from copy import copy

from copy import deepcopy

king_fav_food = [
    ["dosa", "tea"],
    ["meals","lime juice"],
    ["chapthy","lime juice"]
]

Queen_fav_food = deepcopy(king_fav_food)

Queen_fav_food[0][0] = "idly"

print(Queen_fav_food)
print(king_fav_food)    