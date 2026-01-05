
fruits = ["apple", "banana", "cherry", "apple"]

dup = []

for ch in fruits:

    if(fruits.count(ch) > 1):

        dup.append(ch)

    for d in dup:

        if(d in fruits):

            fruits.remove(d)

print(fruits)
        













# rmv_duplicates = set(fruits)

# updated_list = list(rmv_duplicates)

# print(updated_list)


