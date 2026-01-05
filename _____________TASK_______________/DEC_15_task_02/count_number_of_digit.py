def count(num):

    if num == 0:

        return num

    return 1 + count(num // 10) 
    
print(count(12345))


number = 12345

# 1 => 1 + 1234
#2 => 1 + 1 + 123
#3 => 1 + 1 + 1 + 12
#4 => 1 + 1 + 1 + 1
#5 => 1 + 1 + 1 + 1 + 1