sum = 5

def SumofNum(n):

    if n == 0:

        return 0
    
    return n + SumofNum(n - 1)

print(SumofNum(5))

# 5 + sum_n(4) =>15
# 4 + sum_n(3) =>10 
# 3 + sum_n(2) =>6 
# 2 + sum_n(1) =>3
# 1 + sum_n(0) =>1
# 0