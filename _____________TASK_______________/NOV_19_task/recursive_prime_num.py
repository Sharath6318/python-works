numbers=[2,4,5,10,13,14,13,11,7,9,7]

def is_prime(n):

    for i in range(2, n):

        if(n % i == 0):

            return False
        
    return True

prime = [n for n in numbers if is_prime(n)]

print(prime)
            




