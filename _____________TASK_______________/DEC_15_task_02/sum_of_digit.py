def SumofNum(num):

    if num == 0:

        return num
    
    return (num % 10) + SumofNum(num // 10)

print(SumofNum(3456))

