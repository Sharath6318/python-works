for r in range(1, 6):

    for  c in range(r):

        print(" ", end = "")

    for r in range(6, r, -1):

        print("*", end=" ")

    print()

for i in range(1,5):

    for j in range(5, i, - 1):

        print(" ", end= "")

    for j in range(i + 1):

        print("*", end=" ")

    print()