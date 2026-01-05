def is_even(num):

    num_even = True

    if(num % 2 != 0):

        num_even = False


    return num_even

user_input = int(input("Enter the number :"))

print(is_even(user_input))

    