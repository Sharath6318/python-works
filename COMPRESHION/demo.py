# Easy way to creating list tuple set dict from a sequance......

# syntax:

#result = [return iteration condition] => list compreshion
#result = {return iteration condition} => set compreshion
#result = tuple(return iteration condition) => tuple compreshion
#result = {k : v iteration condition} => dict compreshion

arr = [3,4,5,6,7,8]

res = [n ** 2 for n in arr]

print(res)