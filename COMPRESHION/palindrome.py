words = ["cat", "act","madam","dam","malayalam"]

new_list = [w for w in words if(w == w[::-1])]

print(new_list)
