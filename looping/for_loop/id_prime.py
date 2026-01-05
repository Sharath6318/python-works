num = int(input("Enter the num :"))

is_prime = True

for i in range(2, num):

    if(num % i == 0):

        is_prime = False

        break

if(is_prime):

    print("Prime number")

else:

    print("not a prime")