
# same method name but differnent number of parameters 

# python do not support method overloading

# class Calculator:

#     def add(self, num1, num2):

#         print(num1 + num2)

#     def add(self, num1, num2, num3):

#         print(num1 + num2 + num3)

#     def add(self, num1, num2, num3, num4): # only the last method work in the same name case

#         print(num1 + num2 + num3 + num4)

# cal_instance = Calculator()
# cal_instance.add(10, 20)
# cal_instance.add(10, 20, 30)
# cal_instance.add(10, 20, 40, 50)


# so solve the problem *args and **kwargs

# args -> return the tupel formate
# kwargs ->  return the dict formate

# def add(*args):

#     print(sum(args))

# add(10, 20)
# add(10, 20, 30)
# add(10, 20, 50)


# 

# class Numbercount:

#     def solution(*args, **kargss):

#         if kargss.get("value") in args:

#             count_val = args.count(kargss.get("value"))

#             return(count_val)

# num_const_instance = Numbercount()

# print(num_const_instance.solution(10, 10, 20, 30, 40, 50, value = 10))

