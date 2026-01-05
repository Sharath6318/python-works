set_a = {100, 200, 300, 400}

set_a.remove(2000) # get a key error 

print(set_a)


# using discard method:

set_a = {100, 200, 300, 400}

set_a.discard(2000) # not get an error print the set values

print(set_a)