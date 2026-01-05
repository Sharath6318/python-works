lst = [10,20,30,40]

res = {n : n ** index for index,n in enumerate(lst, 1)}

print(res)