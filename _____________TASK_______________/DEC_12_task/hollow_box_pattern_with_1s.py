"""
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
"""
n = 5 

for i in range(1, n + 1):

    for j in range(1, n + 1):

        if i == n or i == 1 or j == 1 or j == 5:

            print(1, end=" ")

        else:

            print(0, end=" ")

    print(" ")