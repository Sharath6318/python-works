n = 5

for i in range(n): #01234

    for j in range(n): #01234

        if j == i or i == n - (j + 1):  

            print(1, end=" ")

        else:

            print(0, end=" ")

    print(" ")