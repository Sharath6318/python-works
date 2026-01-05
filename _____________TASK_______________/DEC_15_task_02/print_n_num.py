
def nNumbers(n):

    if n == 0:

        return
    
    nNumbers(n - 1)

    print(n)

nNumbers(5)



