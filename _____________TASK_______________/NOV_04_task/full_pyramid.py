for r in range(1, 6):

    for c in range(5, r, -1):

        print(" ", end="")

    for c in range(r):

        print("*", end=" ")

    print()