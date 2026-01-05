num1 = int(input("Enter the num1 value :"))
num2 = int(input("Enter the num2 value :"))


def last_num_max(n1, n2):

    return n1 if(n1 % 10) > (n2 % 10) else n2

print(last_num_max(num1, num2))