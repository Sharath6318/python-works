num = 5

for r in range(num): #01234

    for s in range(num - r): #5 - 0, 5 - 1, 5 - 2.

        print(" ", end = "\t")

    for c in range(r + 1): # 0 + 1

        print("*", end= "\t")

    for n in range(r + 0): # 0 +0; 1 + 0; 2 + 0, 3 + 0, 

        print("*", end="\t")

    print()


