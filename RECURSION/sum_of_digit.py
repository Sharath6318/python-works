def sum_of_digit(num):

    if num == 0:

        return num
    
    return num % 10 + sum_of_digit(num // 10)
    

print(sum_of_digit(543))