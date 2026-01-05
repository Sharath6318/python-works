for r in range(1, 6):

    for s in range(r - 1):
         print(" ", end="")

    for c in range(6, r, -1):
         
         print("*", end=" ")

    print()