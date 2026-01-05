def perfect_number(n):

    sum = 0

    for i in range(1, n):

        if(n % i == 0):

            sum += i
        
    if(n == sum):

        print("perfect number")

    else:

        print("not a perfect number")


num = int(input("Enter a number :"))

perfect_number(num)

