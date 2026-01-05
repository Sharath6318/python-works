numbers = [1, 2, 3, 2, 4, 5, 1, 6] 

val = set()
duplicate_val = set()

for num in numbers:

    if(num in val):

        duplicate_val.add(num)

    else:

        val.add(num)

print(duplicate_val)





    
    