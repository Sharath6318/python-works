def GCD(num1, num2):

    min_val = min(num1, num2)

    Greatest_common_divisors = 0

    for i in range(1, min_val + 1):

        if(num1 % i == 0 and num2 % i == 0):

            Greatest_common_divisors = i

    return Greatest_common_divisors

number_1 = int(input("Enter the num1 value :"))

number_2 = int(input("Enter the num2 value :"))

print(GCD(number_1, number_2))

