# A shallow copy creates a new object, but nested objects are shared with the original

from copy import copy

king_fav_colors = ["red", "green", "purple"]

queen_fav_colors = copy(king_fav_colors)

queen_fav_colors.append("blue")

print(queen_fav_colors)
print(king_fav_colors)
