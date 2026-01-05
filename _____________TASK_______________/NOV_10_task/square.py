def square_list(num):

    square = []
    
    for i in range(0, len(num)):

        square_val = num[i] ** 2

        square.append(square_val)

    return square

list_val = [5, 10, 15, 20, 25]

print(square_list(list_val))

        


