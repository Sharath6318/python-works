treasure = {
    "box1" : "gold",
    "box2" : "diamond",
    "box3" : "silver",
    "box4" : "paltinum"
}

# val = treasure["box5"] # if key not exist get key error

# print(val)


value = treasure.get("box4", "empty box") # if key not exist not get an error, return the default value user pass

print(value)
