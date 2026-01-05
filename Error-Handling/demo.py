# syntax Error
# logic Error
# Runtime Error -- filenotfoundError, keyerror  , ZeroDivisionerrors, NameError, typeError, indexError

# BLOCK

# try

    # Expect error code

# catch

    # handle error

# finnaly

    # clean up process

# keyword.............

# raise - throw custom error -- raise Exception("Invalid age")

# assert - dubug 



# num_1 = int(input("num1 : "))
# num_2 = int(input("num2 : "))

# try:

#     result = num_1 / num_2

#     print(result)

# except Exception as ex: # Error name

#     print(ex)

# print("file operation")
# print("completed")



# lst = [10, 20, 30, 40, 50, 60]


# try:

#     user_input = int(input("Enter the index_value in the list of numbers : "))

#     lst.pop(user_input)

#     print(lst)

# except ValueError:

#     print("Your are enter the wrong value")

# except IndexError:

#     print("Out of index")


# finally.....................


num_1 = int(input("Enter the number 1 : "))
num_2 = int(input("Enter the number 2 : "))


try:

    res = num_1 / num_2

    print(res)

except Exception as e:

    num_2 = int(input("Enter the number 2 again : "))

    res = num_1 / num_2

    print(res)

finally:

    print("if any error occur the finnaly block will work")





