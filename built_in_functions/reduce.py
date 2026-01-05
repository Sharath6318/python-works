from functools import reduce

lst = [10,20,30,40]

max_num = reduce(lambda num1,num2 : num1 if num1 > num2 else num2,lst)

print(max_num)

min_num = reduce(lambda num1, num2 : num1 if num1 < num2 else num2, lst)
print(min_num)