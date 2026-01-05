def reverse_num(num):


    if num == 0:

        return "" 
    
    return str(num % 10)  + str(reverse_num(num // 10))

print(reverse_num(345))