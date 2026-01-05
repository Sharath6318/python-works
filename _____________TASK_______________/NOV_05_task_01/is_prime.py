def is_prime(n):

    for i in range(2, n):

        if(n % i == 0):

            return False
        
        return True


number = int(input("Enter the number :"))

print(is_prime(number))
