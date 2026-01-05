num = int(input("Enter the number :"))

while(num != 0):

    last_digit = num % 10

    power_val = last_digit ** 2

    print(power_val)

    num //= 10