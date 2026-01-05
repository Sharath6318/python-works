for i in range(4):

    for j in range(4):

        if (i == 1 and  j == 1 or i == 1 and j == 2)  or (i == 2 and  j == 1 or i == 2 and j == 2) :

            print("S", end=" ")

        else:

            print("R", end=" ")

    print("")