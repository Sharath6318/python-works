# words = ["program", "problem", "perfect", "apple"]

# words_start_with = [w.startswith("pro") for w in words]

# print(any(words_start_with)) 


num = 17

check_prime = not any([num % i == 0 for i in range(2, num)])

# print(check_prime)


print(chr(65))
print(ord('z'))