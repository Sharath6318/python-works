num = int(input("Enter the number :"))

count = 0

while(num != 0):

    last_digit = num % 10

    count += 1 

    num //= 10

print(count)
