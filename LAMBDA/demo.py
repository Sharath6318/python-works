# Anonymous function  with single expression.............................

square = lambda n : n ** 2

print(square(3))

is_odd = lambda n : True if n % 2 != 0 else False

print(is_odd(3))

is_positive = lambda n :True if n > 0 else False

print(is_positive(-1))

is_nagtive = lambda n : True if n < 0 else False

print(is_nagtive(-1))

is_century_year = lambda n : True if  n % 100 == 0 else False

print(is_century_year(2000))