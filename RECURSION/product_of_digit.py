def product_of_digit(num):

    if num == 0:

        return 1
    
    return num % 10 * product_of_digit(num // 10)
    
print(product_of_digit(534))