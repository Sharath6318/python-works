arr = [3,4,12,13,14,20,22]


even_arr = []
odd_arr = []

for ch in arr:

    if(ch % 2 == 0):
        
        even_arr.append(ch)

    else:

        odd_arr.append(ch)

print(even_arr)
print(odd_arr)