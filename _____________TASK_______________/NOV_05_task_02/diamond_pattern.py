for r in range(1, 6):

    for s in range(5, r, -1):

        print(" ", end="")

    for  c in range(r):

        print("*", end= " ")

    print()

for R in range(1, 6):

    for C in range(R):

        print(" ", end="")

    for C in range(5, R, -1):

        print("*", end=" ")

    print()