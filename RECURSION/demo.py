# function call itself is called recursion

# def say_hi(limit):

#     if limit == 0:

#         return # exit the function ....................

#     print("hiiii")

#     return say_hi(limit - 1)

# say_hi(3)


# def display_num(limit):

#     if limit == 0:

#         return 1
    
#     print(limit)

#     return display_num(limit - 1)

# display_num(10)



# def sum_of(limit):

#     if limit == 1:

#         return 1
    
#     return limit + sum_of(limit -1)

# print(sum_of(5))

"""
sum_of(5)

5 + sum_of(4) 5 + 10 = 15
4 + sum_of(3) 4 + 6 = 10
3 + sum_of(2) 3 + 3 = 6
2 + sum_of(1) => 2 + 1 = 3
sum_of(1) => 1

"""
