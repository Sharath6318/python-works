def fact(n):

    if n == 0:

        return 1
    
    return n * fact(n - 1)

print(fact(5))

# 5 => n * fact(5 - 1) => 5 * 24=120
# 4 => n * fact(4 - 1) => 4 * 6=24
# 3 => n * fact(3 - 1) => 3 * 2=6
# 2 => n * fact(2 - 1) => 2 * 1= 2
# 1 => n * fact(0)  => 1 
# 0 => 1