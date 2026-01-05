#  define multiple methods with the same name but different parameter signatures.

def add(*args):

    print(sum(args))

add(10, 20)
add(10, 20, 30)
add(10, 20, 50)

# def sum_numbers(a, b, c):

#     return a + b + c

# my_list = [1, 2, 3]
# result = sum_numbers(*my_list)
# print(result)