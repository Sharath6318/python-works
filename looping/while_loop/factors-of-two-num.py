num1 = int(input("Enter the num1 val :"))
num2 = int(input("Enter the num2 val :"))

small = 0

i = 1

if(num1 < num2):

    small = num1
else:
    
    small = num2

while(i <= small):

    if(num1 % i == 0 and num2 % i == 0):

        print(i)

    i += 1