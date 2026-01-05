def Unique_values(items):

    set_val = set(items)
    duplicate_val = set()

    for ch in items:

        if(items.count(ch) > 1):

            duplicate_val.add(ch)

    unique_val = set_val.symmetric_difference(duplicate_val)
 
    print(unique_val)
    

items = [1, 2, 3, 3, 4, 5, 5, 7]

Unique_values(items)