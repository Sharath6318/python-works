def expo(base, pow):

    return base ** pow

assert expo(1, 5) == 1, "test case 1 faild with the arg (1, 5)"
assert expo(4, 2) == 16 , "test case 2 faild with the arg (1, 5)"
assert expo(2, 3) == 8, "test case 3 faild with the arg (1, 5)"
assert expo(3, 3) == 27, "test case 4 faild with the arg (1, 5)"
assert expo(4, 3) == 64, "test case 5 faild with the arg (1, 5)"
assert expo(5, 1) == 25, "test case 6 faild with the arg (1, 5)"

print("ok")