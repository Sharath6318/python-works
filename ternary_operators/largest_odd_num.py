import math


def largest_odd(n):

    odd = 0

    while(n != 0):

        if(n % 2 != 0):

            odd = n

            break
        
        else:

            n = math.floor(n / 10)

    return odd
    
number = int(input("Enter the number :"))

largest_Odd = largest_odd(number)

print(largest_Odd)
            



