letters = ["A", "B", "C", "D"]
n = len(letters)

for i in range(1, 5):

    for j in range(1, 5):

        print(letters[(i + j) % n], end=" ")

    print(" ")