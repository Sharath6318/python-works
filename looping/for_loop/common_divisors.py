num1 = int(input("Enter the num1 val :"))
num2 = int(input("Enter the num2 val :"))
num3 = int(input("Enter the num3 val :"))

small = min(num1, num2, num3)

for num in range(1, small+1):

    if(num1 % num == 0 and num2 % num == 0 and num3 % num == 0):

        print(num)