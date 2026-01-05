factorials = {}

for i in range(1, 11):
    
    def factorial(num):

        fact = 1

        for i in range(num):

            fact += fact * i

        return fact

    factorials[i] = factorial(i)

# print(factorials)


# def fact(n):

#     if n == 1:

#         return 1
    
#     else:

#         return n * fact(n - 1)
    
# print(fact(5))


fact = lambda n : 1 if n == 1 else  n * fact(n - 1)

fact_dict = {i : fact(i) for i in range(1, 11)}

print(fact_dict)

