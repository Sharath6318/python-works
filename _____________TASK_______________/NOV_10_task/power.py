def power(num, exp):

    power_val = num ** exp

    return power_val


number = int(input("Enter the number :"))
expersion = int(input("Enter the Expersion :"))

print(power(number, expersion))